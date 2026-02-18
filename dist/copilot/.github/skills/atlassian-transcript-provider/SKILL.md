---
name: atlassian-transcript-provider
description: Store and manage meeting transcripts in Confluence using Atlassian MCP tools. Stores transcripts as child pages under a designated Transcripts parent page with labels for filtering.
---
## What This Does

Manages meeting transcripts as Confluence child pages under a designated "Transcripts" parent page. Uses Atlassian MCP server to create, read, and search transcript pages. Transcripts are organized by labels for month and meeting type filtering.

## Configuration

Reads from .github/copilot-instructions.md:
```markdown
### Transcript Provider
**Skill:** d3-atlassian:atlassian-transcript-provider
**Configuration:**
- Cloud ID: your-cloud-id
- Default Location: PROJ
- spaceId: 1234567
- Default parent page: https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789/Transcripts
```

## Operations

When invoked with operation in `$ARGUMENTS`:

### list_locations
Lists available Confluence spaces for transcript storage.

**MCP:** `mcp__atlassian__getConfluenceSpaces`
**Returns:** List of spaces with id, key, name, url

### store_transcript
Creates a Confluence child page under the Transcripts parent page.

**Parse args:** title, body, meeting_type, meeting_date, participants

**Implementation:**
1. Create page title: `[YYYY-MM-DD] [Meeting Type] - [Title]`
   - Capitalize meeting type (e.g., "planning" -> "Planning")
2. Extract parent page ID from configured Default parent page URL
3. Create page as child of parent using spaceId
4. Apply labels: `transcript`, `{meeting_type}`, `{YYYY-MM}`
5. Content format: markdown (MCP handles ADF conversion)

**Preprocessing:**
- Remove empty checkbox markers `[ ]` from task lists (Confluence doesn't support them)
- Only strip: `- [ ]` -> `- ` and `- [x]` -> `- ` in list contexts

**MCP:** `mcp__atlassian__createConfluencePage` with contentFormat: "markdown", parentPageId from config
**Post-create:** Apply labels using `mcp__atlassian__addConfluencePageLabel` for each label: `transcript`, `{meeting_type}`, `{YYYY-MM}`
**Returns:** id, url, title, version

### get_transcript
Retrieves a Confluence transcript page.

**Parse args:** page_id
**MCP:** `mcp__atlassian__getConfluencePage` with contentFormat: "markdown"
**Returns:** id, title, body, url, last_modified, version, labels

### list_transcripts
Lists transcript pages using CQL label filtering.

**Parse args:** meeting_type (optional), month (optional, format YYYY-MM)

**Implementation:**
1. Build CQL query: `type = page AND label = "transcript"`
2. If meeting_type provided: add `AND label = "{meeting_type}"`
3. If month provided: add `AND label = "{YYYY-MM}"`
4. Sort by created date descending

**MCP:** `mcp__atlassian__searchConfluenceUsingCql`
**Returns:** List of transcript pages with id, title, url, labels

### search_transcripts
Searches transcript content using CQL.

**Parse args:** query, meeting_type (optional)

**Implementation:**
1. Build CQL query: `type = page AND label = "transcript" AND text ~ "{query}"`
2. If meeting_type provided: add `AND label = "{meeting_type}"`

**MCP:** `mcp__atlassian__searchConfluenceUsingCql`
**Returns:** List of matching pages with id, title, url, excerpt

## Page Structure

```
Transcripts (parent page)
  [2026-02-03] Planning - Search Feature Kickoff
  [2026-02-04] Technical - Database Migration Review
  [2026-02-05] Standup - Monday Sync
  [2026-02-07] Retro - Sprint Retrospective
```

**Labels per page:**
- `transcript` (always present)
- Meeting type: `planning`, `technical`, `standup`, `retro`, `other`
- Month: `2026-02`, `2026-01`, etc.

## Notes

- Follows the same operation interface as `markdown-transcript-provider`
- Confluence uses "spaces" = D3 uses "locations" (generic term)
- Uses Confluence labels for filtering instead of directory structure
- Uses CQL for search instead of grep
- Content format is always Markdown (MCP handles ADF conversion)
- Space keys (like "PROJ") may need conversion to numerical IDs
- Labels are created automatically if they don't exist
