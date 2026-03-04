from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class ArtifactConfig:
    adapter: str = "markdown"
    config: dict = field(default_factory=dict)


@dataclass
class D3Config:
    artifacts: dict[str, ArtifactConfig] = field(default_factory=dict)
    templates: dict[str, str] = field(default_factory=dict)
    settings: dict[str, object] = field(default_factory=dict)


def _normalise_key(name: str) -> str:
    return name.lower().replace(" ", "_")


def _project_root() -> Path:
    root = os.environ.get("D3_PROJECT_ROOT")
    if root:
        return Path(root)
    return Path.cwd()


def load_config(config_path: Path | None = None) -> D3Config:
    if config_path is None:
        config_path = _project_root() / "d3.config.yaml"

    if not config_path.exists():
        return D3Config()

    with open(config_path) as f:
        raw = yaml.safe_load(f)

    if not raw:
        return D3Config()

    artifacts = {}
    for name, entry in raw.get("artifacts", {}).items():
        key = _normalise_key(name)
        artifacts[key] = ArtifactConfig(
            adapter=entry.get("adapter", "markdown"),
            config=entry.get("config", {}),
        )

    templates = {
        _normalise_key(k): v
        for k, v in raw.get("templates", {}).items()
    }

    settings = raw.get("settings", {}) or {}

    return D3Config(artifacts=artifacts, templates=templates, settings=settings)
