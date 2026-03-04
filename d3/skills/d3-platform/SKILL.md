---
name: d3-platform
description: D3 platform-specific tool and configuration mappings for Claude Code. Read this before executing D3 commands or skills.
---
# D3 Platform Reference

## Tool Mapping
| Reference | Tool |
|---|---|
| read tool | `Read` |
| write tool | `Write` |
| search tool | `Grep` |
| glob tool | `Glob` |
| shell tool | `Bash` |

## MCP Tools (D3 Server)

All artifact I/O goes through the D3 MCP server. Use these tools directly — no skill invocation needed for artifact operations.

| MCP Tool | Purpose |
|---|---|
| `create_artifact` | Create a new artifact (spec, story, transcript) |
| `read_artifact` | Read an existing artifact by ID or path |
| `update_artifact` | Update an existing artifact's body content |
| `search_artifacts` | Search artifacts by content |
| `list_locations` | List available locations for an artifact type |
| `list_projects` | List available projects (story-specific) |
| `get_issue_types` | Get available issue types (story-specific) |
| `link_issues` | Link two issues together (story-specific) |

All MCP tools take `artifact_type` as the first parameter (e.g. `product_spec`, `tech_spec`, `user_story`, `meeting_transcript`).

## Skill Invocation
To invoke a skill, use this syntax:
```
Skill(skill="<skill-name>", args="<arguments>")
```

## Template References
D3 template files are located at:
```
d3/skills/d3-templates/references
```
