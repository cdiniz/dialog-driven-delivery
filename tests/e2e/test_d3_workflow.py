import glob
import os

import pytest

from .claude_runner import run_claude_conversation
from .validators import (
    extract_frontmatter,
    extract_sections,
    has_placeholder,
    heading_texts_lower,
    markers_tracked_in_open_questions,
    total_markers,
)

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")

PRODUCT_HEADINGS = ["overview", "user journey", "requirements", "open questions"]
TECH_HEADINGS = ["technical approach", "system changes", "testing requirements"]
STORY_FRONTMATTER_FIELDS = ["type", "id", "spec", "title", "status"]


def _read_fixture(name: str) -> str:
    with open(os.path.join(FIXTURES_DIR, name)) as f:
        return f.read()


def _create_spec_messages(transcript: str) -> list[str]:
    return [
        "/d3:create-spec\n\nI want to provide a meeting transcript.",
        f"Here is the transcript:\n---\n{transcript}\n---\n\n"
        f"Use the default root location.\n"
        f'For the title, use "Task Dashboard".',
        "The spec looks good, please create it.",
    ]


def _refine_spec_messages(spec_name: str, refinement: str) -> list[str]:
    return [
        f"/d3:refine-spec {spec_name}\n\nI want to describe changes.",
        f"Here are the updates from our follow-up meeting:\n---\n{refinement}\n---",
        "The proposed changes look correct, please apply them.",
    ]


def _decompose_messages(spec_name: str) -> list[str]:
    return [
        f"/d3:decompose {spec_name}\n\nProject key: LOCAL",
        "I did not have a decomposition meeting. Please decompose conversationally.",
        "The proposed stories look good. Please create them all. Make assumptions where needed and document them in the stories.",
    ]


class TestD3Workflow:

    @pytest.mark.timeout(600)
    def test_01_create_spec(self, test_workspace, spec_state):
        transcript = _read_fixture("sample_transcript.txt")
        output = run_claude_conversation(
            _create_spec_messages(transcript), cwd=test_workspace
        )

        spec_files = glob.glob(os.path.join(test_workspace, "specs", "*.md"))
        assert len(spec_files) >= 1, f"No spec files created. Output:\n{output[:1000]}"

        spec_path = spec_files[0]
        spec_state["path"] = spec_path
        spec_state["name"] = os.path.basename(spec_path)

        content = open(spec_path).read()
        headings = heading_texts_lower(content)

        for h in PRODUCT_HEADINGS:
            assert h in headings, f"Missing product heading: {h}"
        for h in TECH_HEADINGS:
            assert h in headings, f"Missing tech heading: {h}"

        assert has_placeholder(content), "No placeholder text for undiscussed sections"
        assert total_markers(content) > 0, "No uncertainty markers found"

        assert spec_state["name"].startswith("task-dashboard"), (
            f"Unexpected spec filename: {spec_state['name']}"
        )
        assert "product specification" in content.lower(), (
            "Missing top-level Product Specification section"
        )
        assert "technical specification" in content.lower(), (
            "Missing top-level Technical Specification section"
        )
        assert markers_tracked_in_open_questions(content), (
            "Uncertainty markers exist but no Open Questions section found"
        )

    @pytest.mark.timeout(600)
    def test_02_refine_spec(self, test_workspace, spec_state):
        refinement = _read_fixture("refinement_input.txt")
        spec_name = spec_state["name"]
        original_content = open(spec_state["path"]).read()
        original_sections = extract_sections(original_content)

        run_claude_conversation(
            _refine_spec_messages(spec_name, refinement), cwd=test_workspace
        )

        spec_files = [
            f
            for f in glob.glob(os.path.join(test_workspace, "specs", "*.md"))
            if not f.endswith(".backup")
        ]
        assert len(spec_files) == 1, f"Spec duplicated or missing: {spec_files}"

        updated_content = open(spec_state["path"]).read()
        assert updated_content != original_content, "Spec unchanged after refinement"

        lower = updated_content.lower()
        assert "postgresql" in lower or "priority" in lower, (
            "Refinement content not found in updated spec"
        )

        updated_sections = extract_sections(updated_content)
        for heading in ["overview", "user journey"]:
            orig = original_sections.get(heading)
            if orig is not None:
                assert heading in updated_sections, (
                    f"Section '{heading}' removed during refinement"
                )

    @pytest.mark.timeout(600)
    def test_03_decompose(self, test_workspace, spec_state):
        output = run_claude_conversation(
            _decompose_messages(spec_state["name"]), cwd=test_workspace
        )

        stories_dir = os.path.join(test_workspace, "stories")
        assert os.path.isdir(stories_dir), (
            f"Stories dir not created. Output:\n{output[:1000]}"
        )

        all_files = glob.glob(
            os.path.join(stories_dir, "**", "*.md"), recursive=True
        )

        stories = []
        for path in all_files:
            content = open(path).read()
            fm = extract_frontmatter(content)
            if fm is None or fm.get("type") != "story":
                continue
            stories.append((path, content, fm))

        assert len(stories) >= 1, (
            f"No story files found. Files: {all_files}. Output:\n{output[:1000]}"
        )

        spec_stem = os.path.splitext(spec_state["name"])[0]
        spec_subdir = os.path.join(stories_dir, spec_stem)
        assert os.path.isdir(spec_subdir), (
            f"Stories not in spec-named subdirectory. Found: {all_files}"
        )

        for path, content, fm in stories:
            for field in STORY_FRONTMATTER_FIELDS:
                assert field in fm, f"Missing frontmatter '{field}' in {path}"

            assert spec_stem in str(fm.get("spec", "")), (
                f"Story doesn't reference parent spec in {path}"
            )

            lower = content.lower()
            assert "given" in lower and "when" in lower and "then" in lower, (
                f"Missing Given-When-Then ACs in {path}"
            )


class TestCustomTemplates:

    @pytest.mark.timeout(600)
    def test_create_spec_uses_custom_template(self, custom_template_workspace):
        transcript = _read_fixture("sample_transcript.txt")
        output = run_claude_conversation(
            _create_spec_messages(transcript), cwd=custom_template_workspace
        )

        spec_files = glob.glob(
            os.path.join(custom_template_workspace, "specs", "*.md")
        )
        assert len(spec_files) >= 1, (
            f"No spec files created. Output:\n{output[:1000]}"
        )

        content = open(spec_files[0]).read()
        headings = heading_texts_lower(content)

        assert "operational readiness" in headings, (
            f"Custom template heading not found. Headings: {headings}"
        )
