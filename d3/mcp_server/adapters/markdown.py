from __future__ import annotations

import re
from pathlib import Path

from d3_config import _project_root

from .base import BaseAdapter


def _normalise(text: str) -> str:
    return re.sub(r"[\s_-]+", " ", text.lower())


def _slugify(text: str) -> str:
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


class MarkdownAdapter(BaseAdapter):

    @property
    def directory(self) -> Path:
        if "directory" not in self.config:
            raise ValueError("MarkdownAdapter requires 'directory' in config")
        raw = Path(self.config["directory"])
        if raw.is_absolute():
            return raw
        return _project_root() / raw

    def create_artifact(
        self,
        title: str,
        body: str,
        location_id: str = ".",
    ) -> dict:
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
        }

    def read_artifact(self, artifact_id: str) -> dict:
        path = self._resolve_path(artifact_id)
        if path is None:
            raise FileNotFoundError(f"Artifact not found: {artifact_id}")

        content = path.read_text(encoding="utf-8")

        return {
            "id": str(path),
            "title": path.stem,
            "body": content,
            "url": path.as_uri(),
        }

    def update_artifact(
        self,
        artifact_id: str,
        body: str,
    ) -> dict:
        path = self._resolve_path(artifact_id)
        if path is None:
            raise FileNotFoundError(f"Artifact not found: {artifact_id}")

        path.write_text(body, encoding="utf-8")

        return {
            "id": str(path),
            "url": path.as_uri(),
        }

    def search_artifacts(
        self,
        title: str,
    ) -> dict:
        if not self.directory.exists():
            return {"results": []}

        results = []
        for md_file in sorted(self.directory.rglob("*.md")):
            if _normalise(title) in _normalise(md_file.stem):
                results.append({
                    "id": str(md_file),
                    "title": md_file.stem,
                    "url": md_file.as_uri(),
                })

        return {"results": results}

    def _resolve_path(self, artifact_id: str) -> Path | None:
        path = Path(artifact_id)
        if path.exists() and path.is_file():
            return path
        return None


