from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mcp.server.fastmcp import FastMCP

from d3_config import load_config
from adapters import create_adapter

mcp = FastMCP("d3")


def _get_adapter(artifact_type: str):
    cfg = load_config()
    if artifact_type not in cfg.artifacts:
        raise ValueError(
            f"Unknown artifact type: {artifact_type}. "
            f"Available: {list(cfg.artifacts)}"
        )
    art = cfg.artifacts[artifact_type]
    return create_adapter(art.adapter, art.config)


@mcp.tool()
def create_artifact(
    artifact_type: str,
    title: str,
    body: str,
    location_id: str = ".",
) -> dict:
    """Create a new artifact (spec, story, or transcript)."""
    adapter = _get_adapter(artifact_type)
    return adapter.create_artifact(
        title=title,
        body=body,
        location_id=location_id,
    )


@mcp.tool()
def read_artifact(artifact_type: str, artifact_id: str) -> dict:
    """Read an existing artifact by ID or path."""
    adapter = _get_adapter(artifact_type)
    return adapter.read_artifact(artifact_id)


@mcp.tool()
def update_artifact(
    artifact_type: str,
    artifact_id: str,
    body: str,
) -> dict:
    """Update an existing artifact's body content."""
    adapter = _get_adapter(artifact_type)
    return adapter.update_artifact(
        artifact_id=artifact_id,
        body=body,
    )


@mcp.tool()
def search_artifacts(
    artifact_type: str,
    title: str,
) -> dict:
    """Search artifacts by title."""
    adapter = _get_adapter(artifact_type)
    return adapter.search_artifacts(title=title)


if __name__ == "__main__":
    mcp.run()
