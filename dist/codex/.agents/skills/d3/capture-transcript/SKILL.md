---
description: Capture and structure a meeting transcript. Extracts key decisions, action items, and open questions from raw conversation text. Stores as a referenceable transcript artifact. Use when you have a meeting recording/transcript to process, or when user asks to capture/save/process a transcript.
name: capture-transcript
---
<!-- DO NOT EDIT - Generated from canonical/ by generate.py -->

## Core Principle

**Extract only what was said. Never invent decisions or actions not in the transcript.**

Transcripts are standalone artifacts. Their relationship to specs is established at usage time (when you run `refine-spec` or `create-spec` and provide the transcript as input), not at capture time.

---

## Workflow

### 1. Detect Provider and Template
- Read AGENTS.md for D3 config
- Search for `### Transcript Provider` section
- If no Transcript Provider configured, guide user to add one to AGENTS.md:
  ```markdown
  ### Transcript Provider
  **Skill:** d3-markdown:markdown-transcript-provider
  **Configuration:**
  - Transcripts Directory: ./transcripts
  - Default Location: .
  ```
- Load meeting transcript template from d3-templates skill (or custom path if configured)
- Store provider and template for later steps

### 2. Get Transcript Input
Ask user:
```
Please paste your meeting transcript below.

This can be:
- A raw transcript from a recording tool
- Meeting notes copied from a document
- A chat log or conversation export
```

Wait for user to paste the transcript content.

### 3. Ask Meeting Type
Ask user:
```
What type of meeting was this?
A) Planning (sprint planning, feature planning, kickoff)
B) Technical (architecture, design review, tech discussion)
C) Standup (daily sync, status update)
D) Retro (retrospective, post-mortem)
E) Other
```

### 4. Determine Meeting Date
- Look for an explicit date in the transcript (e.g., timestamps, "January 15th meeting", date headers)
- If a date is found, confirm with user: `I found the meeting date: YYYY-MM-DD. Is that correct?`
- If no date is found, ask the user: `I couldn't find a date in the transcript. When did this meeting take place? (default: today, YYYY-MM-DD)`
- Use today's date if the user confirms the default

### 5. Generate Structured Summary

Analyze the transcript in a single pass and extract:
- **Summary:** 2-3 sentence overview of what was discussed
- **Key Decisions:** Numbered decisions with bold titles — only include decisions explicitly stated or clearly agreed upon in the transcript
- **Action Items:** Numbered items with Owner and Due fields — only include items explicitly assigned or volunteered for
- **Open Questions:** Numbered questions with context — include questions raised but not answered during the meeting

**CRITICAL RULES:**

1. **Extract ONLY what was said:**
   - A decision must be explicitly stated or clearly agreed upon
   - An action item must be explicitly assigned or volunteered for
   - An open question must be explicitly raised and left unresolved

2. **NEVER invent:**
   - Decisions that weren't made
   - Action items that weren't assigned
   - Questions that weren't asked
   - Participants that weren't mentioned

3. **Preserve context:**
   - Include enough context for each item to be understood without re-reading the full transcript
   - Use participants' actual names/roles as mentioned

4. **Handle sparse transcripts:**
   - If no decisions were made, the Key Decisions section should state: _No decisions were made during this meeting._
   - If no action items were assigned, the Action Items section should state: _No action items were assigned during this meeting._
   - If no open questions remain, the Open Questions section should state: _No open questions were raised._

### 6. Propose Title
- Generate a descriptive slug from the transcript content (e.g., "search-feature-kickoff", "database-migration-review")
- Format: lowercase, hyphens, no special characters
- Present to user for confirmation:
```
Proposed title: "Search Feature Kickoff"
File will be saved as: transcripts/2026-02/planning-search-feature-kickoff.md

Is this title good, or would you like to change it?
```

### 7. Show Summary for Review
Present the full structured summary to the user before storing:
```
Here's the structured transcript:

Summary: [2-3 sentences]

Key Decisions: [N]
1. ...

Action Items: [N]
1. ...

Open Questions: [N]
1. ...

The raw transcript will be preserved in full.

Ready to save? Or would you like to adjust anything?
```

### 8. Store via Provider

Use provider:
```
$[provider-name] store_transcript title=\"[Title]\" meeting_type=\"[type]\" meeting_date=\"[YYYY-MM-DD]\" participants=\"[comma-separated list]\" body=\"[FULL_CONTENT]\"
```

The body includes:
- Template header (title, date, type, participants)
- Summary section
- Key Decisions section
- Action Items section
- Open Questions section
- Raw Transcript section (full unedited transcript)

### 9. Provide Summary & Next Steps

```
✅ Transcript captured: [Title] - [path]

Extracted:
- Decisions: [N]
- Action Items: [N]
- Open Questions: [N]

Next steps:
- Create a spec from this transcript: /d3:create-spec (paste the transcript path when asked)
- Refine an existing spec: /d3:refine-spec PAGE-ID (reference this transcript)
- View transcript: [path]
```

---

## Error Handling

| Issue | Action |
|-------|--------|
| No provider configured | Guide user to add Transcript Provider to AGENTS.md |
| Empty transcript | Ask user to paste the transcript content |
| No date in transcript | Ask user for the meeting date, default to today |
| Very short transcript (<100 words) | Warn that the transcript is very short and extracted content may be minimal. Confirm before proceeding |
| No decisions extractable | Normal — set Key Decisions section to "No decisions were made during this meeting." |
| No action items found | Normal — set Action Items section to "No action items were assigned during this meeting." |
| Storage fails | Provide full structured transcript text for manual saving |
| Location not found | List available locations |

---

## Key Principles

1. **Extraction, not generation** — Every item in the summary must trace back to the transcript
2. **Standalone artifacts** — Transcripts exist independently; specs reference them, not the other way around
3. **Raw preservation** — The full unedited transcript is always preserved in the Raw Transcript section
4. **One pass** — Generate the entire structured summary in a single analysis pass
5. **User confirmation** — Always show the summary and get confirmation before storing
