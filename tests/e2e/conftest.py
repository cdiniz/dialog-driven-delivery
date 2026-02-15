import os
import shutil

import pytest

from .claude_runner import REPO_ROOT

FIXTURES_DIR = REPO_ROOT / "tests" / "e2e" / "fixtures"
PLUGIN_DIRS = [REPO_ROOT / "d3", REPO_ROOT / "d3-markdown"]
TEMPLATES_DIR = FIXTURES_DIR / "templates"
FILE_SWAPS = {
    "skills/d3-templates/references/feature-product-spec.md": "product-spec.md",
    "skills/d3-templates/references/feature-tech-spec.md": "tech-spec.md",
    "skills/d3-templates/references/user-story.md": "user-story.md",
    "skills/d3-templates/SKILL.md": "SKILL.md",
}
CUSTOM_TEMPLATE_FILES = [
    "custom-product-spec.md",
    "custom-tech-spec.md",
    "custom-user-story.md",
]

E2E_TMP = REPO_ROOT / "tests" / "e2e" / ".workspaces"


def _init_plugins(worker_id: str):
    base = E2E_TMP / f"plugin-fixtures_{worker_id}"
    if base.exists():
        shutil.rmtree(base)
    base.mkdir(parents=True)
    plugin_paths = []
    for plugin_dir in PLUGIN_DIRS:
        dest = base / plugin_dir.name
        shutil.copytree(plugin_dir, dest)
        for rel_path, fixture_name in FILE_SWAPS.items():
            template_dest = dest / rel_path
            if template_dest.exists():
                shutil.copy(TEMPLATES_DIR / fixture_name, template_dest)
        plugin_paths.append(str(dest))
    return plugin_paths


def _init_workspace(tmpdir, claude_md_name="CLAUDE.md"):
    os.makedirs(tmpdir, exist_ok=True)
    claude_md_dest = os.path.join(tmpdir, "CLAUDE.md")
    if not os.path.exists(claude_md_dest):
        shutil.copy(FIXTURES_DIR / "workspace" / claude_md_name, claude_md_dest)
    return tmpdir


@pytest.fixture(scope="session")
def plugin_dirs(worker_id):
    return _init_plugins(worker_id)


@pytest.fixture(scope="session")
def test_workspace(worker_id):
    yield _init_workspace(str(E2E_TMP / f"spec-workflow_{worker_id}"))


@pytest.fixture(scope="session")
def custom_template_workspace(worker_id):
    tmpdir = _init_workspace(
        str(E2E_TMP / f"template-customisation_{worker_id}"),
        claude_md_name="CLAUDE-custom-templates.md",
    )
    templates_dest = os.path.join(tmpdir, "templates")
    os.makedirs(templates_dest, exist_ok=True)
    custom_dir = FIXTURES_DIR / "custom-templates"
    for name in CUSTOM_TEMPLATE_FILES:
        shutil.copy(custom_dir / name, os.path.join(templates_dest, name))
    yield tmpdir
