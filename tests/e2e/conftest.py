import os
import shutil
import subprocess

import pytest

from .claude_runner import REPO_ROOT

FIXTURES_DIR = REPO_ROOT / "tests" / "e2e" / "fixtures"

@pytest.fixture(scope="session")
def test_workspace():
    tmpdir = "/tmp/d3_e2e_debug"
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)
    os.makedirs(tmpdir)
    shutil.copy(FIXTURES_DIR / "CLAUDE.md", os.path.join(tmpdir, "CLAUDE.md"))
    subprocess.run(["git", "init"], cwd=tmpdir, capture_output=True)
    subprocess.run(
        ["git", "add", "."],
        cwd=tmpdir,
        capture_output=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "init"],
        cwd=tmpdir,
        capture_output=True,
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
