---
name: distill
description: Clean a raw meeting transcript by removing noise (greetings, small talk, filler, "you're on mute" tangents) and split it by topic into separate focused files — one topic per file, never merged. If a template is configured for the Transcripts artifact type in d3.config.md, structure each output with the template; otherwise emit clean transcript text only. Use for multi-topic meetings or whenever the user wants to tidy up a raw transcript before feeding it into a spec, or says things like "clean this transcript", "split this meeting by topic", "distill these notes", "this meeting covered three things, can you separate them", "prep this transcript for the create skill". The hallmark is a raw meeting transcript that needs cleaning and/or topic separation before it becomes useful input to another D3 skill.
---

# D3 — Distill Transcript

This skill takes a raw meeting transcript — the kind that contains greetings, screen-sharing banter, and three topics mashed together — and produces clean, single-topic files that can feed independently into **d3:create**.

## Core principle

**Remove noise, preserve signal. Split by topic, never merge.**

A single meeting often covers multiple subjects. Each topic deserves its own clean file so it can become its own spec, ADR, or story without dragging in unrelated context.

## Workflow

### 1. Load configuration

- Read `d3.config.md`. If missing, stop and tell the user to run **d3:init** first.
- Read Quiet Mode from `### Settings`.
- Read the Transcripts row from the Storage table for Location, Instructions, and Template.
- If the Template column has a value, load that template file — it will be used to structure each output.

### 2. Get the raw transcript

If the user's message already contains the transcript (pasted inline or as a file reference), use it directly. Otherwise ask them to paste it.

### 3. Identify topics

Scan the full transcript and identify distinct topics. A topic is a **sustained thread of conversation around a single subject** — not every brief mention or aside.

Signals that mark a topic transition:
- Explicit cues: "let's move on to...", "next item", "about the..."
- Shifts in subject matter that stick for more than a couple of exchanges
- Agenda items mentioned at the start or in a chair's interjection

What counts as one topic:
- A feature, system, or problem discussed at length
- A decision-making thread with back-and-forth
- A planning or estimation discussion for a single item

What does **not** count as a separate topic:
- Brief asides that return to the main subject within a few exchanges
- Meta-discussion about the meeting itself ("can you hear me?", "let's timebox this")
- One-off questions that are answered and then abandoned

### 4. Propose the split

Present the identified topics as a numbered list with a short label (3–6 words) for each and an indication of how much of the transcript each covers.

- **If only one topic:** say so and propose a single output file — don't force a split.
- **Quiet mode:** skip presenting and proceed with the detected topics.
- **Otherwise:** ask the user to confirm, merge, rename, or drop topics before proceeding.

### 5. Distill each topic

For each confirmed topic, extract the relevant portions of the transcript.

**Remove:**
- Greetings, goodbyes, pleasantries ("how was your weekend", "hi everyone")
- Filler and verbal tics ("um", "you know", "like", "so basically")
- Off-topic tangents unrelated to the topic being extracted
- Meta-discussion about the meeting ("you're on mute", "can you share your screen")
- Repeated or restated points — keep the clearest version only

**Preserve:**
- Speaker labels and timestamps (if present in the original)
- All substantive dialogue: requirements, decisions, concerns, questions, trade-offs
- Exact phrasing when someone states a decision or commitment
- Disagreements and alternative viewpoints
- Context that explains *why* something was said

**Never:**
- Summarise or paraphrase — keep the conversational format
- Add structure, headings, or formatting not in the original
- Reorder the conversation — maintain chronological flow
- Invent speaker attributions if the original doesn't have them

The downstream skill (usually d3:create) is going to re-read this transcript and make structural decisions from it. The more the distilled output looks like the original conversation, the better that downstream step works.

### 6. Name the outputs

Generate a title for each topic from its label.

**Format:** `YYYY-MM-DD Topic Label` — use today's date if no date is mentioned in the transcript, otherwise use the meeting date.

When writing to local files, convert the title to lowercase kebab-case with a `.md` extension. When writing to external tools (Confluence, Linear, etc.), use the title as-is.

- **Quiet mode:** accept the generated names and proceed.
- **Otherwise:** present proposed names and let the user adjust.

### 7. Generate output

**If a template was loaded in step 1:**

Generate each output following the template's structure. Apply the same rules as **d3:create**:
- All template headings must be present
- Fill sections with content extracted from the distilled transcript for that topic
- Sections not covered by the transcript get `_To be defined - not yet discussed_`
- Invoke the **d3:uncertainty-markers** skill for any ambiguous content

**If no template is configured:**

Each output contains only the cleaned transcript text — no metadata, no headings, no structure. This is the normal case when Transcripts has no Template in the Storage table.

### 8. Write output

Follow the Instructions column from the Transcripts row exactly. The Instructions define how and where to write — don't assume local markdown files. If the Instructions reference an MCP tool, use it; if they reference a CLI, use it; if they describe writing to a directory, do that.

### 9. Provide a summary

Tell the user:
- Number of topics found and files created
- Filenames / URLs and paths
- Approximate percentage of the original transcript that was noise (removed)
- If no template was used, suggest **d3:create** as the natural next step for each file

## Error handling

| Issue | Action |
|-------|--------|
| `d3.config.md` missing | Stop. Ask the user to run **d3:init** first. |
| Transcript too short or unclear | Warn that topic detection may be unreliable; ask to proceed or provide more context |
| Cannot distinguish topics | Produce a single cleaned file and tell the user |
| No substantive content found | Warn the user — the transcript may be entirely small talk |
| Write fails | Provide the distilled text inline for manual saving |

## Related skills

- **d3:init** — prerequisite (creates `d3.config.md`)
- **d3:create** — natural next step: feed each distilled topic into create to produce an artifact
- **d3:refine** — alternative next step if the topic is an update to an existing artifact
- **d3:uncertainty-markers** — invoked when generating template-structured output with ambiguous content
