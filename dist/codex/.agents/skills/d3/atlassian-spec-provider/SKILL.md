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

**Implementation:**
1. Extract parent page ID from configured Default parent page URL
2. Create page as child of parent using spaceId
3. Content format: markdown (MCP handles ADF conversion)

**Preprocessing:**
- Remove empty checkbox markers `[ ]` from task lists (Confluence doesn't support them)
- **CRITICAL:** Preserve uncertainty markers: `[OPEN QUESTION: ...]`, `[DECISION PENDING: ...]`, `[ASSUMPTION: ...]`, `[CLARIFICATION NEEDED: ...]`
- Only strip: `- [ ]` -> `- ` and `- [x]` -> `- ` in list contexts
**MCP:** `mcp__atlassian__createConfluencePage` with contentFormat: "markdown", parentPageId from config
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

Reads from `d3.config.md`:
```markdown
### Spec Provider
**Skill:** d3-atlassian:atlassian-spec-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Specs
- Spec Mode: combined
```

## Notes

- Confluence uses "spaces" = D3 uses "locations" (generic term)
- Content format is always Markdown (MCP handles ADF conversion)
- Space keys (like "PROJ") may need conversion to numerical IDs
