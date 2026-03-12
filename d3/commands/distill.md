---
description: Sanitise a raw meeting transcript by removing noise (small talk, greetings, filler) and splitting it by topic into separate, focused files. If a template is configured for the Transcripts artifact type, use it to structure each output. Otherwise, output clean transcript text only. Use for multi-topic meetings or when you want to clean and split before further processing.
---

## Core Principle

**Remove noise, preserve signal. Split by topic, never merge.**

A single meeting often covers multiple subjects. Each topic deserves its own clean file so it can feed independently into `/d3:create`.

---

## Workflow

### 1. Load Configuration
- Read `d3.config.md`
- Read Quiet Mode from Settings
- Read the Transcripts row from the Storage table for Location, Instructions, and Template
- If the Template column has a value, load the template file — it will be used to structure each output

### 2. Get Raw Transcript

**If input text provided in `$ARGUMENTS`:** Use it directly. Skip the question below.

**Otherwise:** Ask the user to paste the raw meeting transcript.

### 3. Identify Topics

Scan the full transcript and identify distinct topics discussed. A topic is a sustained thread of conversation around a single subject — not every brief mention or aside.

**Topic detection signals:**
- Explicit transitions ("let's move on to...", "next item", "about the...")
- Shifts in subject matter between speakers
- Agenda items if mentioned

**What counts as a single topic:**
- A feature, system, or problem being discussed at length
- A decision-making thread with back-and-forth
- A planning or estimation discussion for one item

**What does NOT count as a separate topic:**
- Brief asides that return to the main subject within a few exchanges
- Meta-discussion about the meeting itself ("can you hear me?", "let's timebox this")

### 4. Propose Split

Present the identified topics as a numbered list with a brief label for each (3-6 words) and an indication of how much of the transcript each covers.

**If only one topic is found:** Say so and propose a single output file.

**If quiet mode:** Skip presenting and proceed with the detected topics.

**Otherwise:** Ask the user to confirm, merge, rename, or drop topics before proceeding.

### 5. Distill Each Topic

For each confirmed topic, extract the relevant portions of the transcript.

**REMOVE:**
- Greetings, goodbyes, pleasantries ("how was your weekend", "hi everyone")
- Filler and verbal tics ("um", "you know", "like", "so basically")
- Off-topic tangents unrelated to the topic being extracted
- Meta-discussion about the meeting ("you're on mute", "can you share your screen")
- Repeated or restated points — keep the clearest version only

**PRESERVE:**
- Speaker labels and timestamps (if present in the original)
- All substantive dialogue: requirements, decisions, concerns, questions, trade-offs
- Exact phrasing when someone states a decision or commitment
- Disagreements and alternative viewpoints
- Context that explains why something was said

**NEVER:**
- Summarise or paraphrase — keep the conversational format
- Add structure, headings, or formatting not in the original
- Reorder the conversation — maintain chronological flow
- Invent speaker attributions if not in the original

### 6. Name Outputs

Generate a title for each topic derived from the topic label.

**Format:** `YYYY-MM-DD Topic Label` (use today's date if no date is mentioned in the transcript)

When writing local files, convert the title to lowercase kebab-case with `.md` extension. When writing to external tools (Confluence, Linear, etc.), use the title as-is.

**If quiet mode:** Accept generated names. Skip the question below.

**Otherwise:** Present proposed names and let the user adjust.

### 7. Generate Output

**If a template was loaded in Step 1:**
Generate each output following the template structure. Apply the same rules as `/d3:create`:
- ALL template headings must be present
- Fill sections with content extracted from the distilled transcript for that topic
- Sections not covered by the transcript get `_To be defined - not yet discussed_`
- Invoke the uncertainty-markers skill for ambiguous content

**If no template:**
Each output contains only the cleaned transcript text — no metadata, no structure.

### 8. Write Output

Follow the Instructions column from the Storage table's Transcripts row exactly. The Instructions define how and where to write — do not assume local markdown files.

### 9. Provide Summary

Report:
- Number of topics found and files created
- Filenames and paths
- Approximate percentage of original transcript that was noise (removed)
- If no template was used, suggest `/d3:create` as next step for each file

---

## Error Handling

| Issue | Action |
|-------|--------|
| Transcript too short or unclear | Warn that topic detection may be unreliable, ask to proceed or provide more context |
| Cannot distinguish topics | Produce a single cleaned file, inform the user |
| No substantive content found | Warn the user — the transcript may be entirely small talk |
| Write fails | Provide the distilled text inline for manual saving |
