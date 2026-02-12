import glob
import os

import pytest

from .claude_runner import run_claude
from .validators import (
    extract_frontmatter,
    has_placeholder,
    heading_texts_lower,
    total_markers,
)

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")

PRODUCT_HEADINGS = ["overview", "user journey", "requirements", "open questions"]
TECH_HEADINGS = ["technical approach", "system changes", "testing requirements"]
STORY_FRONTMATTER_FIELDS = ["type", "id", "spec", "title", "status"]


def _read_fixture(name: str) -> str:
    with open(os.path.join(FIXTURES_DIR, name)) as f:
        return f.read()


class TestD3Workflow:

    @pytest.mark.timeout(360)
    def test_01_create_spec(self, test_workspace, spec_state):
        transcript = _read_fixture("sample_transcript.txt")

        prompt = f"""\
/d3:create-spec

Follow every step in the create-spec workflow. Read the templates before generating.

I want to provide a meeting transcript.

Here is the transcript:
---
{transcript}
---

Use the default root location.
For the title, use "Task Dashboard".
The spec looks good, please create it.
Do not ask any questions. Use the information provided to make all decisions.
"""
        output = run_claude(prompt, cwd=test_workspace)

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

        assert "task-dashboard.md" == spec_state["name"], (
            f"Unexpected spec filename: {spec_state['name']}"
        )
        assert "product specification" in content.lower(), (
            "Missing top-level Product Specification section"
        )
        assert "technical specification" in content.lower(), (
            "Missing top-level Technical Specification section"
        )

    @pytest.mark.timeout(360)
    def test_02_refine_spec(self, test_workspace, spec_state):
        refinement = _read_fixture("refinement_input.txt")
        spec_name = spec_state["name"]
        original_content = open(spec_state["path"]).read()

        prompt = f"""\
/d3:refine-spec {spec_name}

I want to describe changes (option C - describe changes).

Here are the updates from our follow-up meeting:
---
{refinement}
---

These decisions resolve open questions in the spec. Apply all changes immediately.
The proposed changes look correct, please apply them now using the update_spec operation.
Do not ask any questions. Do not show me a preview. Just update the spec file directly.
"""
        run_claude(prompt, cwd=test_workspace, timeout=600)

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

    @pytest.mark.timeout(360)
    def test_03_decompose(self, test_workspace, spec_state):
        spec_name = spec_state["name"]

        prompt = f"""\
/d3:decompose {spec_name}

Project key: LOCAL

I did not have a decomposition meeting. Please decompose conversationally.

The proposed stories look good. Please create them all.
Confirm all INVEST checks pass. Proceed with creation.
Do not ask any questions. Use the information provided to make all decisions.
"""
        output = run_claude(prompt, cwd=test_workspace)

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

        for path, content, fm in stories:
            for field in STORY_FRONTMATTER_FIELDS:
                assert field in fm, f"Missing frontmatter '{field}' in {path}"

            assert "task-dashboard" in str(fm.get("spec", "")), (
                f"Story doesn't reference parent spec in {path}"
            )

            lower = content.lower()
            assert "given" in lower and "when" in lower and "then" in lower, (
                f"Missing Given-When-Then ACs in {path}"
            )
