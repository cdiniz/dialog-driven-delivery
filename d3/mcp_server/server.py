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
    parent_id: str | None = None,
    metadata: dict | None = None,
) -> dict:
    """Create a new artifact (spec, story, or transcript)."""
    adapter = _get_adapter(artifact_type)
    return adapter.create_artifact(
        title=title,
        body=body,
        location_id=location_id,
        parent_id=parent_id,
        metadata=metadata,
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
    version_message: str | None = None,
) -> dict:
    """Update an existing artifact's body content."""
    adapter = _get_adapter(artifact_type)
    return adapter.update_artifact(
        artifact_id=artifact_id,
        body=body,
        version_message=version_message,
    )


@mcp.tool()
def search_artifacts(
    artifact_type: str,
    query: str,
    location_id: str | None = None,
) -> dict:
    """Search artifacts by content."""
    adapter = _get_adapter(artifact_type)
    return adapter.search_artifacts(query=query, location_id=location_id)


@mcp.tool()
def list_locations(artifact_type: str) -> dict:
    """List available locations for an artifact type."""
    adapter = _get_adapter(artifact_type)
    return adapter.list_locations()


@mcp.tool()
def list_projects(artifact_type: str) -> dict:
    """List available projects (story-specific)."""
    adapter = _get_adapter(artifact_type)
    return adapter.list_projects()


@mcp.tool()
def get_issue_types(artifact_type: str, project_key: str | None = None) -> dict:
    """Get available issue types for a project (story-specific)."""
    adapter = _get_adapter(artifact_type)
    return adapter.get_issue_types(project_key=project_key)


@mcp.tool()
def link_issues(
    artifact_type: str,
    from_key: str,
    to_key: str,
    link_type: str,
) -> dict:
    """Link two issues together (story-specific)."""
    adapter = _get_adapter(artifact_type)
    return adapter.link_issues(from_key=from_key, to_key=to_key, link_type=link_type)


if __name__ == "__main__":
    mcp.run()
