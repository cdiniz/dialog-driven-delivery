from __future__ import annotations

import re
import subprocess
from datetime import date, datetime
from pathlib import Path

import yaml

from d3_config import _project_root

from .base import BaseAdapter


def _slugify(text: str) -> str:
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def _extract_title(content: str) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _parse_frontmatter(content: str) -> tuple[dict, str]:
    if not content.startswith("---"):
        return {}, content
    end = content.index("---", 3)
    fm_text = content[3:end].strip()
    body = content[end + 3:].lstrip("\n")
    fm = yaml.safe_load(fm_text) or {}
    return fm, body


def _build_frontmatter(data: dict) -> str:
    return "---\n" + yaml.dump(data, default_flow_style=False).strip() + "\n---"


class MarkdownAdapter(BaseAdapter):

    @property
    def directory(self) -> Path:
        raw = Path(self.config.get("directory", "./specs"))
        if raw.is_absolute():
            return raw
        return _project_root() / raw

    @property
    def mode(self) -> str:
        return self.config.get("mode", "spec")

    def create_artifact(
        self,
        title: str,
        body: str,
        location_id: str = ".",
        parent_id: str | None = None,
        metadata: dict | None = None,
    ) -> dict:
        if self.mode == "story":
            return self._create_story(title, body, location_id, parent_id, metadata)
        if self.mode == "transcript":
            return self._create_transcript(title, body, metadata)
        return self._create_spec(title, body, location_id)

    def read_artifact(self, artifact_id: str) -> dict:
        path = self._resolve_path(artifact_id)
        if path is None:
            raise FileNotFoundError(f"Artifact not found: {artifact_id}")
        content = path.read_text(encoding="utf-8")
        fm, body = _parse_frontmatter(content)
        title = fm.get("title") or _extract_title(content)
        stat = path.stat()
        result = {
            "id": str(path),
            "title": title,
            "body": body if fm else content,
            "url": path.as_uri(),
            "last_modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
            "location_id": str(path.parent.relative_to(self.directory)) if self.directory in path.parents else ".",
        }
        if fm:
            result["frontmatter"] = fm
        return result

    def update_artifact(
        self,
        artifact_id: str,
        body: str,
        version_message: str | None = None,
    ) -> dict:
        path = self._resolve_path(artifact_id)
        if path is None:
            raise FileNotFoundError(f"Artifact not found: {artifact_id}")

        existing = path.read_text(encoding="utf-8")
        fm, _ = _parse_frontmatter(existing)

        if fm:
            content = _build_frontmatter(fm) + "\n\n" + body
        else:
            content = body

        path.write_text(content, encoding="utf-8")

        version = None
        if version_message:
            version = self._git_commit(path, version_message)

        return {
            "id": str(path),
            "url": path.as_uri(),
            "version": version,
            "last_modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    def search_artifacts(
        self,
        query: str,
        location_id: str | None = None,
    ) -> dict:
        search_dir = self.directory
        if location_id and location_id != ".":
            search_dir = self.directory / location_id

        if not search_dir.exists():
            return {"results": []}

        results = []
        for md_file in sorted(search_dir.rglob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            if query.lower() in content.lower():
                fm, _ = _parse_frontmatter(content)
                title = fm.get("title") or _extract_title(content)
                excerpt = self._extract_excerpt(content, query)
                results.append({
                    "id": str(md_file),
                    "title": title,
                    "excerpt": excerpt,
                    "url": md_file.as_uri(),
                    "location_id": str(md_file.parent.relative_to(self.directory))
                    if self.directory in md_file.parents else ".",
                })

        return {"results": results}

    def list_locations(self) -> dict:
        locations = [{"id": ".", "name": "Root", "path": str(self.directory)}]

        if self.directory.exists():
            for item in sorted(self.directory.iterdir()):
                if item.is_dir() and not item.name.startswith("."):
                    locations.append({
                        "id": item.name,
                        "name": item.name,
                        "path": str(item),
                    })

        return {"locations": locations}

    def list_projects(self) -> dict:
        return {
            "projects": [{
                "id": "local",
                "key": "LOCAL",
                "name": "Local Project",
                "url": Path(self.directory).resolve().as_uri(),
            }],
        }

    def get_issue_types(self, project_key: str | None = None) -> dict:
        return {"issue_types": [{"id": "story", "name": "Story"}]}

    def link_issues(self, from_key: str, to_key: str, link_type: str) -> dict:
        from_path = self._find_story_by_key(from_key)
        to_path = self._find_story_by_key(to_key)

        if from_path is None:
            raise FileNotFoundError(f"Story not found: {from_key}")
        if to_path is None:
            raise FileNotFoundError(f"Story not found: {to_key}")

        content = from_path.read_text(encoding="utf-8")
        fm, body = _parse_frontmatter(content)

        if link_type == "blocks":
            fm.setdefault("blocks", []).append(to_key)
        elif link_type == "is_blocked_by":
            fm.setdefault("dependencies", []).append(to_key)
        else:
            fm.setdefault("dependencies", []).append(to_key)

        from_path.write_text(_build_frontmatter(fm) + "\n\n" + body, encoding="utf-8")

        return {"success": True, "link_type": link_type}

    # --- Spec mode ---

    def _create_spec(self, title: str, body: str, location_id: str) -> dict:
        filename = _slugify(title) + ".md"
        if location_id and location_id != ".":
            filepath = self.directory / location_id / filename
        else:
            filepath = self.directory / filename

        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(body, encoding="utf-8")

        return {
            "id": str(filepath),
            "title": title,
            "url": filepath.as_uri(),
            "path": str(filepath),
        }

    # --- Story mode ---

    def _create_story(
        self,
        title: str,
        body: str,
        location_id: str = ".",
        parent_id: str | None = None,
        metadata: dict | None = None,
    ) -> dict:
        metadata = metadata or {}
        spec_id = metadata.get("spec_id", parent_id or "")

        spec_dir_name = _slugify(Path(spec_id).stem) if spec_id else "unlinked"
        story_dir = self.directory / spec_dir_name
        story_dir.mkdir(parents=True, exist_ok=True)

        next_id = self._next_story_id(story_dir)
        story_id = f"story-{next_id}"
        filename = f"{story_id}-{_slugify(title)}.md"

        fm = {
            "type": "story",
            "id": story_id,
            "spec": spec_id,
            "title": title,
            "status": "todo",
            "size": metadata.get("size", "medium"),
            "created": date.today().isoformat(),
            "dependencies": [],
            "blocks": [],
            "labels": metadata.get("labels", []),
        }

        content = _build_frontmatter(fm) + "\n\n" + body
        filepath = story_dir / filename
        filepath.write_text(content, encoding="utf-8")

        return {
            "id": story_id,
            "key": story_id,
            "url": filepath.as_uri(),
            "summary": title,
            "spec_link": spec_id,
            "path": str(filepath),
        }

    def _next_story_id(self, story_dir: Path) -> int:
        existing = list(story_dir.glob("story-*.md"))
        if not existing:
            return 1
        ids = []
        for f in existing:
            match = re.match(r"story-(\d+)", f.stem)
            if match:
                ids.append(int(match.group(1)))
        return max(ids, default=0) + 1

    def _find_story_by_key(self, key: str) -> Path | None:
        for md_file in self.directory.rglob(f"{key}-*.md"):
            return md_file
        for md_file in self.directory.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            fm, _ = _parse_frontmatter(content)
            if fm.get("id") == key:
                return md_file
        return None

    # --- Transcript mode ---

    def _create_transcript(
        self,
        title: str,
        body: str,
        metadata: dict | None = None,
    ) -> dict:
        metadata = metadata or {}
        meeting_type = metadata.get("meeting_type", "other")
        meeting_date_str = metadata.get("meeting_date", date.today().isoformat())
        participants = metadata.get("participants", [])

        meeting_date = date.fromisoformat(meeting_date_str)
        year_month = meeting_date.strftime("%Y-%m")
        date_prefix = meeting_date.isoformat()

        slug = _slugify(title)
        filename = f"{date_prefix}-{meeting_type}-{slug}.md"
        month_dir = self.directory / year_month
        month_dir.mkdir(parents=True, exist_ok=True)

        filepath = month_dir / filename
        artifact_id = str(Path(self.directory.name) / year_month / filename)

        fm = {
            "type": "transcript",
            "id": artifact_id,
            "title": title,
            "meeting_type": meeting_type,
            "meeting_date": meeting_date_str,
            "participants": participants,
            "created": datetime.now().isoformat(),
            "labels": ["transcript", meeting_type, year_month],
        }

        content = _build_frontmatter(fm) + "\n\n" + body
        filepath.write_text(content, encoding="utf-8")

        return {
            "id": artifact_id,
            "title": title,
            "url": filepath.as_uri(),
            "path": str(filepath),
        }

    # --- Helpers ---

    def _resolve_path(self, artifact_id: str) -> Path | None:
        candidates = [
            Path(artifact_id),
            self.directory / artifact_id,
            self.directory / (artifact_id + ".md"),
        ]

        for candidate in candidates:
            if candidate.exists() and candidate.is_file():
                return candidate

        for match in self.directory.rglob(f"*{artifact_id}*.md"):
            return match

        return None

    def _extract_excerpt(self, content: str, query: str, context_chars: int = 80) -> str:
        lower = content.lower()
        idx = lower.find(query.lower())
        if idx == -1:
            return content[:context_chars * 2] + "..."
        start = max(0, idx - context_chars)
        end = min(len(content), idx + len(query) + context_chars)
        excerpt = content[start:end]
        if start > 0:
            excerpt = "..." + excerpt
        if end < len(content):
            excerpt = excerpt + "..."
        return excerpt

    def _git_commit(self, path: Path, message: str) -> str | None:
        try:
            subprocess.run(
                ["git", "add", str(path)],
                capture_output=True,
                check=True,
                cwd=path.parent,
            )
            subprocess.run(
                ["git", "commit", "-m", message],
                capture_output=True,
                check=True,
                cwd=path.parent,
            )
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True,
                check=True,
                text=True,
                cwd=path.parent,
            )
            return result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None
