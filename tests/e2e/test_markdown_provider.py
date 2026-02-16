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

INPUTS_DIR = os.path.join(os.path.dirname(__file__), "fixtures", "inputs")

PRODUCT_HEADINGS = ["overview", "requirements", "open questions"]
TECH_HEADINGS = ["technical approach", "testing requirements"]
STORY_FRONTMATTER_FIELDS = ["type", "id", "spec", "title", "status"]


def _read_fixture(name: str) -> str:
    with open(os.path.join(INPUTS_DIR, name)) as f:
        return f.read()


def _find_specs(workspace):
    return glob.glob(os.path.join(workspace, "specs", "*.md"))


def _create_spec_messages(transcript: str) -> list[str]:
    return [
        "/d3:create-spec\n\nI want to provide a meeting transcript.",
        f"Here is the transcript:\n---\n{transcript}\n---\n\n"
        f"Use the default root location.\n"
        f'For the title, use "About Page".',
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
        f"/d3:decompose {spec_name}",
        "LOCAL",
        "I did not have a decomposition meeting. Please decompose conversationally.",
        "The proposed stories look good. Please create them all. Make assumptions where needed and document them in the stories.",
    ]


class TestMarkdownWorkflow:
    """
    Sequential E2E workflow tests for markdown provider.
    Tests complete lifecycle: create → refine → decompose.
    """

    @pytest.mark.timeout(600)
    def test_create_spec_from_transcript(self, markdown_workflow_workspace, plugin_dirs):
        transcript = _read_fixture("sample_transcript.txt")
        run_claude_conversation(
            _create_spec_messages(transcript),
            cwd=markdown_workflow_workspace,
            plugin_dirs=plugin_dirs,
        )

        spec_files = _find_specs(markdown_workflow_workspace)
        assert len(spec_files) >= 1, "No spec files found"
        assert len(spec_files) == 1, f"Multiple spec files found: {spec_files}"
        spec_path = spec_files[0]
        spec_name = os.path.basename(spec_path)

        content = open(spec_path).read()
        headings = heading_texts_lower(content)

        for h in PRODUCT_HEADINGS:
            assert h in headings, f"Missing product heading: {h}"
        for h in TECH_HEADINGS:
            assert h in headings, f"Missing tech heading: {h}"

        assert has_placeholder(content), "No placeholder text for undiscussed sections"
        assert total_markers(content) > 0, "No uncertainty markers found"

        assert spec_name.startswith("about-page"), (
            f"Unexpected spec filename: {spec_name}"
        )
        assert markers_tracked_in_open_questions(content), (
            "Uncertainty markers exist but no Open Questions section found"
        )

    @pytest.mark.timeout(600)
    def test_refine_existing_spec(self, markdown_workspace_with_spec, plugin_dirs):
        spec_files = _find_specs(markdown_workspace_with_spec)
        assert len(spec_files) >= 1, "No spec files found"
        assert len(spec_files) == 1, f"Multiple spec files found: {spec_files}"
        spec_path = spec_files[0]
        spec_name = os.path.basename(spec_path)
        refinement = _read_fixture("refinement_input.txt")
        original_content = open(spec_path).read()
        original_sections = extract_sections(original_content)

        run_claude_conversation(
            _refine_spec_messages(spec_name, refinement),
            cwd=markdown_workspace_with_spec,
            plugin_dirs=plugin_dirs,
        )

        post_refine_specs = _find_specs(markdown_workspace_with_spec)
        assert len(post_refine_specs) >= 1, "Spec file missing after refinement"
        assert len(post_refine_specs) == 1, f"Spec duplicated after refinement: {post_refine_specs}"
        assert os.path.exists(spec_path + ".backup"), "Backup file not created during refinement"

        updated_content = open(spec_path).read()
        assert updated_content != original_content, "Spec unchanged after refinement"

        lower = updated_content.lower()
        assert "acme" in lower, (
            "Refinement content not found in updated spec"
        )

        updated_sections = extract_sections(updated_content)
        for heading in ["overview"]:
            orig = original_sections.get(heading)
            if orig is not None:
                assert heading in updated_sections, (
                    f"Section '{heading}' removed during refinement"
                )

    @pytest.mark.timeout(600)
    def test_decompose_spec_into_stories(self, markdown_workspace_with_refined_spec, plugin_dirs):
        spec_files = _find_specs(markdown_workspace_with_refined_spec)
        assert len(spec_files) >= 1, "No spec files found"
        assert len(spec_files) == 1, f"Multiple spec files found: {spec_files}"
        spec_path = spec_files[0]
        spec_name = os.path.basename(spec_path)
        output = run_claude_conversation(
            _decompose_messages(spec_name),
            cwd=markdown_workspace_with_refined_spec,
            plugin_dirs=plugin_dirs,
        )

        stories_dir = os.path.join(markdown_workspace_with_refined_spec, "stories")
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

        spec_stem = os.path.splitext(spec_name)[0]
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


class TestMarkdownConfiguration:
    """
    Configuration and customisation tests for markdown provider.
    Tests run independently.
    """

    @pytest.mark.timeout(600)
    def test_create_spec_uses_custom_template(self, markdown_custom_template_workspace, plugin_dirs):
        transcript = _read_fixture("sample_transcript.txt")
        output = run_claude_conversation(
            _create_spec_messages(transcript),
            cwd=markdown_custom_template_workspace,
            plugin_dirs=plugin_dirs,
        )

        spec_files = glob.glob(
            os.path.join(markdown_custom_template_workspace, "custom-specs", "*.md")
        )
        assert len(spec_files) >= 1, (
            f"No spec files created. Output:\n{output[:1000]}"
        )

        content = open(spec_files[0]).read()
        headings = heading_texts_lower(content)

        assert "operational readiness" in headings, (
            f"Custom template heading not found. Headings: {headings}"
        )
