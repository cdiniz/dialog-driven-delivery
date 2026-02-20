---
description: Store and manage meeting transcripts as local markdown files. Stores transcripts in ./transcripts/ directory organized by month as markdown files tracked by git.
alwaysApply: false
---
## What This Does

Manages meeting transcripts as markdown files in the filesystem. Transcripts are stored in `./transcripts/` directory organized by year-month subdirectories with git version control.

---

## Configuration

Reads from `d3.config.md`:
```markdown
### Transcript Provider
**Skill:** d3-markdown:markdown-transcript-provider
**Configuration:**
- Transcripts Directory: ./transcripts
```

**Defaults if not found:**
- Transcripts Directory: `./transcripts`

---

## Operations

When invoked with operation in `$ARGUMENTS`:

### list_locations

Lists available directories for transcripts.

**Implementation:**
Use the glob tool to find subdirectories in transcripts/ (typically YYYY-MM directories), or return root location.

**Returns:**
```json
{
  "locations": [
    {"id": ".", "name": "Root", "path": "./transcripts"},
    {"id": "2026-01", "name": "2026-01", "path": "./transcripts/2026-01"},
    {"id": "2026-02", "name": "2026-02", "path": "./transcripts/2026-02"}
  ]
}
```

---

### store_transcript

Creates a transcript markdown file.

**Parse args:** title, body, meeting_type, meeting_date, participants

**Implementation:**
1. Determine year-month from meeting_date (YYYY-MM)
2. Sanitize title to slug: lowercase, spaces to hyphens, remove special chars
3. Construct filename: `{YYYY-MM-DD}-{meeting_type}-{slug}.md`
4. Determine filepath: `transcripts/{YYYY-MM}/{filename}`
5. Create directory if needed
6. Generate YAML frontmatter:
   ```yaml
   ---
   type: transcript
   id: transcripts/{YYYY-MM}/{filename}
   title: "{title}"
   meeting_type: "{meeting_type}"
   meeting_date: "{YYYY-MM-DD}"
   participants:
     - "{participant1}"
     - "{participant2}"
   created: "{ISO 8601 timestamp}"
   labels:
     - "transcript"
     - "{meeting_type}"
     - "{YYYY-MM}"
   ---
   ```
7. Write frontmatter + body to file using the write tool
8. Return metadata

**Returns:**
```json
{
  "id": "transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md",
  "title": "Sprint Kickoff",
  "url": "file:///absolute/path/to/transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md",
  "path": "./transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md"
}
```

---

### get_transcript

Retrieves a transcript markdown file.

**Parse args:** transcript_id (can be full path, partial path, or filename)

**Implementation:**
1. Find file using the read tool:
   - Try exact path
   - Try `transcripts/{transcript_id}`
   - Try `transcripts/{transcript_id}.md`
   - Use the glob tool with pattern `transcripts/**/*{transcript_id}*.md` as fallback
2. Read file content
3. Parse YAML frontmatter (between `---` markers)
4. Extract body (content after frontmatter)
5. Return metadata + parsed content

**Returns:**
```json
{
  "id": "transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md",
  "title": "Sprint Kickoff",
  "body": "[full markdown content after frontmatter]",
  "frontmatter": {
    "type": "transcript",
    "meeting_type": "planning",
    "meeting_date": "2026-02-05",
    "participants": ["Alice", "Bob"],
    "labels": ["transcript", "planning", "2026-02"]
  },
  "url": "file:///absolute/path",
  "last_modified": "2026-02-05 10:30:00"
}
```

---

### list_transcripts

Lists all transcripts, optionally filtered.

**Parse args:** meeting_type (optional), month (optional, format YYYY-MM)

**Implementation:**
1. Use the glob tool to find all markdown files: `transcripts/**/*.md`
2. For each file, parse YAML frontmatter
3. Filter by meeting_type if provided (match frontmatter `meeting_type` field)
4. Filter by month if provided (match directory name or frontmatter `meeting_date`)
5. Sort by meeting_date descending (most recent first)
6. Return list of transcript summaries

**Returns:**
```json
{
  "transcripts": [
    {
      "id": "transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md",
      "title": "Sprint Kickoff",
      "meeting_type": "planning",
      "meeting_date": "2026-02-05",
      "participants": ["Alice", "Bob"],
      "path": "./transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md"
    }
  ]
}
```

---

### search_transcripts

Searches transcript content.

**Parse args:** query, meeting_type (optional)

**Implementation:**
1. Use the search tool to search markdown files in transcripts/ for the query
2. For each match, parse frontmatter to extract title and meeting_type
3. Filter by meeting_type if provided
4. Return list of results with excerpts

**Returns:**
```json
{
  "results": [
    {
      "id": "transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md",
      "title": "Sprint Kickoff",
      "meeting_type": "planning",
      "excerpt": "...discussed the authentication approach...",
      "url": "file:///absolute/path",
      "path": "./transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md"
    }
  ]
}
```

---

## File Naming

- Date prefix: `YYYY-MM-DD-` (from meeting_date)
- Meeting type: `planning-`, `technical-`, `standup-`, `retro-`, `other-`
- Title converted to slug: "Sprint Kickoff" -> `sprint-kickoff`
- Full filename: `{YYYY-MM-DD}-{meeting_type}-{slug}.md`
- Lowercase with hyphens
- Remove special characters (except hyphens)
- All files have `.md` extension
- Files sort chronologically within each month directory

---

## Directory Structure

```
transcripts/
  2026-01/
    2026-01-15-planning-sprint-review.md
    2026-01-20-technical-database-migration.md
  2026-02/
    2026-02-03-planning-sprint-kickoff.md
    2026-02-04-standup-monday-sync.md
    2026-02-07-retro-sprint-retrospective.md
```

---

## YAML Frontmatter

Every transcript file includes YAML frontmatter for metadata:

```yaml
---
type: transcript
id: transcripts/2026-02/2026-02-05-planning-sprint-kickoff.md
title: "Sprint Kickoff"
meeting_type: "planning"
meeting_date: "2026-02-05"
participants:
  - "Alice"
  - "Bob"
created: "2026-02-05T10:00:00Z"
labels:
  - "transcript"
  - "planning"
  - "2026-02"
---
```

---

## Notes

- Use the read/write tools for file operations
- Use the glob tool for finding files
- Use the search tool for searching content
- Always create parent directories as needed (including YYYY-MM directories)
- Frontmatter is parsed by splitting on `---` markers
- Body content starts after the closing `---` of frontmatter
- Transcripts are standalone artifacts — relationship to specs is established at usage time
