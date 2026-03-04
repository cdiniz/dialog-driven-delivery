from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml

_RESERVED_ARTIFACT_KEYS = {"adapter", "template"}


@dataclass
class ArtifactConfig:
    adapter: str = "markdown"
    template: str | None = None
    config: dict = field(default_factory=dict)


@dataclass
class D3Config:
    adapters: dict[str, dict] = field(default_factory=dict)
    artifacts: dict[str, ArtifactConfig] = field(default_factory=dict)
    settings: dict[str, object] = field(default_factory=dict)


def _normalise_key(name: str) -> str:
    return name.lower().replace(" ", "_")


def _project_root() -> Path:
    root = os.environ.get("D3_PROJECT_ROOT")
    if root:
        return Path(root)
    return Path.cwd()


def _merge_artifact_config(adapter_name: str, artifact_fields: dict, adapters: dict) -> dict:
    shared = dict(adapters.get(adapter_name, {}))
    shared.update(artifact_fields)
    return shared


def load_config(config_path: Path | None = None) -> D3Config:
    if config_path is None:
        config_path = _project_root() / "d3.config.yaml"

    if not config_path.exists():
        return D3Config()

    with open(config_path) as f:
        raw = yaml.safe_load(f)

    if not raw:
        return D3Config()

    adapters = raw.get("adapters", {}) or {}

    artifacts = {}
    for name, entry in raw.get("artifacts", {}).items():
        key = _normalise_key(name)
        adapter_name = entry.get("adapter", "markdown")
        template = entry.get("template")
        artifact_fields = {
            k: v for k, v in entry.items()
            if k not in _RESERVED_ARTIFACT_KEYS
        }
        merged = _merge_artifact_config(adapter_name, artifact_fields, adapters)
        artifacts[key] = ArtifactConfig(
            adapter=adapter_name,
            template=template,
            config=merged,
        )

    settings = raw.get("settings", {}) or {}

    return D3Config(adapters=adapters, artifacts=artifacts, settings=settings)
