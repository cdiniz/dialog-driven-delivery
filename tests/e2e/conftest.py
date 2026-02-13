import os
import shutil
import subprocess

import pytest

from .claude_runner import REPO_ROOT

FIXTURES_DIR = REPO_ROOT / "tests" / "e2e" / "fixtures"
TEMPLATES_DIR = REPO_ROOT / "d3" / "skills" / "d3-templates" / "references"


def _init_workspace(tmpdir, claude_md_name="CLAUDE.md"):
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)
    os.makedirs(tmpdir)
    shutil.copy(FIXTURES_DIR / claude_md_name, os.path.join(tmpdir, "CLAUDE.md"))
    subprocess.run(["git", "init"], cwd=tmpdir, capture_output=True)
    subprocess.run(["git", "add", "."], cwd=tmpdir, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "init"], cwd=tmpdir, capture_output=True
    )
    return tmpdir


@pytest.fixture(scope="session")
def test_workspace():
    yield _init_workspace("/tmp/d3_e2e_debug")


@pytest.fixture(scope="session")
def custom_template_workspace():
    tmpdir = _init_workspace(
        "/tmp/d3_e2e_custom_templates",
        claude_md_name="CLAUDE-custom-templates.md",
    )
    templates_dest = os.path.join(tmpdir, "templates")
    os.makedirs(templates_dest)
    shutil.copy(
        FIXTURES_DIR / "custom-product-spec.md",
        os.path.join(templates_dest, "custom-product-spec.md"),
    )
    shutil.copy(
        TEMPLATES_DIR / "feature-tech-spec.md",
        os.path.join(templates_dest, "feature-tech-spec.md"),
    )
    shutil.copy(
        TEMPLATES_DIR / "user-story.md",
        os.path.join(templates_dest, "user-story.md"),
    )
    subprocess.run(["git", "add", "."], cwd=tmpdir, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "add templates"], cwd=tmpdir, capture_output=True
    )
    yield tmpdir


@pytest.fixture(scope="session")
def spec_state():
    return {}


@pytest.fixture(scope="session")
def sample_transcript():
    return (FIXTURES_DIR / "sample_transcript.txt").read_text()


@pytest.fixture(scope="session")
def refinement_input():
    return (FIXTURES_DIR / "refinement_input.txt").read_text()
