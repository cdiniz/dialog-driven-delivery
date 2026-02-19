import os
import shutil
import subprocess

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


def pytest_configure(config):
    if not hasattr(config, "workerinput"):
        if E2E_TMP.exists():
            shutil.rmtree(E2E_TMP)
        E2E_TMP.mkdir(parents=True)


def _init_plugins(worker_id):
    base = E2E_TMP / "plugin-fixtures" / worker_id
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


def _init_workspace(workspace_dir, claude_md_name="CLAUDE.md"):
    if os.path.exists(workspace_dir):
        shutil.rmtree(workspace_dir)
    os.makedirs(workspace_dir)
    shutil.copy(
        FIXTURES_DIR / "workspace" / claude_md_name,
        os.path.join(workspace_dir, "CLAUDE.md"),
    )
    subprocess.run(["git", "init"], cwd=workspace_dir, capture_output=True)
    return workspace_dir


@pytest.fixture(scope="session")
def plugin_dirs(worker_id):
    return _init_plugins(worker_id)


@pytest.fixture
def markdown_workflow_workspace(request):
    yield _init_workspace(str(E2E_TMP / request.node.name))


@pytest.fixture
def markdown_custom_template_workspace(request):
    workspace = _init_workspace(
        str(E2E_TMP / request.node.name),
        claude_md_name="CLAUDE-custom-templates.md",
    )
    templates_dest = os.path.join(workspace, "templates")
    os.makedirs(templates_dest, exist_ok=True)
    custom_dir = FIXTURES_DIR / "custom-templates"
    for name in CUSTOM_TEMPLATE_FILES:
        shutil.copy(custom_dir / name, os.path.join(templates_dest, name))
    yield workspace


@pytest.fixture
def markdown_workspace_with_spec(request):
    workspace = _init_workspace(str(E2E_TMP / request.node.name))
    specs_dir = os.path.join(workspace, "specs")
    os.makedirs(specs_dir, exist_ok=True)
    shutil.copy(
        FIXTURES_DIR / "specs" / "about-page-base.md",
        os.path.join(specs_dir, "about-page.md")
    )
    yield workspace


@pytest.fixture
def markdown_workspace_with_refined_spec(request):
    workspace = _init_workspace(str(E2E_TMP / request.node.name))
    specs_dir = os.path.join(workspace, "specs")
    os.makedirs(specs_dir, exist_ok=True)
    shutil.copy(
        FIXTURES_DIR / "specs" / "about-page-refined-base.md",
        os.path.join(specs_dir, "about-page.md")
    )
    yield workspace
