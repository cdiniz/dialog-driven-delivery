---
name: atlassian-spec-provider
description: Create and manage specifications in Confluence using Atlassian MCP tools.
---
## What This Does

Handles all Confluence operations for D3 specifications. Uses Atlassian MCP server to create, read, update, and search Confluence pages.

## Operations

When invoked with operation in `$ARGUMENTS`:

### list_locations
Lists available Confluence spaces.

**MCP:** `mcp__atlassian__getConfluenceSpaces`
**Returns:** List of spaces with id, key, name, url

### create_spec
Creates a Confluence page.

**Parse args:** location_id, title, body, parent_id (optional)
**Preprocessing:**
- Remove empty checkbox markers `[ ]` from task lists (Confluence doesn't support them)
- **CRITICAL:** Preserve uncertainty markers: `[OPEN QUESTION: ...]`, `[DECISION PENDING: ...]`, `[ASSUMPTION: ...]`, `[CLARIFICATION NEEDED: ...]`
- Only strip: `- [ ]` -> `- ` and `- [x]` -> `- ` in list contexts
**MCP:** `mcp__atlassian__createConfluencePage` with contentFormat: "markdown"
**Returns:** id, url, title, version

### get_spec
Retrieves a Confluence page.

**Parse args:** page_id
**MCP:** `mcp__atlassian__getConfluencePage` with contentFormat: "markdown"
**Returns:** id, title, body, url, last_modified, version, location_id, parent_id

### update_spec
Updates a Confluence page.

**Parse args:** page_id, body, version_message (optional)
**Preprocessing:**
- Remove empty checkbox markers `[ ]` from task lists (Confluence doesn't support them)
- **CRITICAL:** Preserve uncertainty markers: `[OPEN QUESTION: ...]`, `[DECISION PENDING: ...]`, `[ASSUMPTION: ...]`, `[CLARIFICATION NEEDED: ...]`
- Only strip: `- [ ]` -> `- ` and `- [x]` -> `- ` in list contexts
**MCP:** `mcp__atlassian__updateConfluencePage` with contentFormat: "markdown"
**Returns:** id, url, version, last_modified

### search_specs
Searches Confluence pages.

**Parse args:** query, location_id (optional)
**MCP:** `mcp__atlassian__searchConfluenceUsingCql` with CQL query
**Returns:** List of matching pages with id, title, url, excerpt, location_id

## Configuration

Reads from CLAUDE.md:
- Cloud ID
- Default Location (space key)

## Notes

- Confluence uses "spaces" = D3 uses "locations" (generic term)
- Content format is always Markdown (MCP handles ADF conversion)
- Space keys (like "BOOT") may need conversion to numerical IDs
