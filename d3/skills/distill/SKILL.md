---
name: distill
description: Sanitise a raw meeting transcript by removing noise (greetings, small talk, filler, "you're on mute" tangents) and splitting it by subject into separate, focused files. Related topics within the same subject stay together. If a template is configured for the Transcripts artifact type in d3.config.md, structure each output with the template; otherwise emit clean transcript text only. Use for meetings covering unrelated subjects, or whenever the user wants to tidy up a raw transcript before feeding it into a spec, or says things like "clean this transcript", "split this meeting by subject", "distill these notes", "this meeting covered three things, can you separate them", "prep this transcript for the create skill". The hallmark is a raw meeting transcript that needs cleaning and/or subject separation before it becomes useful input to another D3 skill.
---

# D3 — Distill Transcript

This skill takes a raw meeting transcript — the kind that contains greetings, screen-sharing banter, and multiple subjects mashed together — and produces clean, focused files that can feed independently into **d3:create**.

## Core principle

**Remove noise, preserve signal. Split only when subjects are genuinely unrelated.**

A meeting often weaves through several related topics around a single subject — a feature's UI, API, and data model, for example. Those belong together in one file. Only split when the meeting jumps to a genuinely unrelated subject that would naturally live in a different artifact.

**Default bias: keep together. Splitting is the exception, not the rule.**

## Workflow

### 1. Load configuration

- Read `d3.config.md`. If missing, stop and tell the user to run **d3:init** first.
- Read Quiet Mode from `### Settings`.
- Read the Transcripts row from the Storage table for Location, Instructions, and Template.
- If the Template column has a value, load that template file — it will be used to structure each output.

### 2. Get the raw transcript

If the user's message already contains the transcript (pasted inline or as a file reference), use it directly. Otherwise ask them to paste it.

### 3. Identify subjects

Scan the full transcript and identify distinct **subjects** — not topics. A subject is a self-contained area of discussion that would naturally become its own artifact (a feature, an incident, a hiring decision, a retro theme). Within one subject, the conversation may move through many related topics: that is still one subject.

**The splitting test:** Ask "would these two portions reasonably live in the same document if I were writing notes by hand?" If yes, keep them together. Only split when the answer is clearly no.

**Strong signals of a genuinely new subject:**
- The meeting has an explicit agenda with unrelated items and moves between them
- A hard pivot to something that shares no entities, goals, or stakeholders with what came before ("okay, unrelated, about the hiring pipeline...")
- The participants, systems, or domain language change substantially

**NOT a new subject — keep together:**
- Discussing different aspects, layers, or components of the same feature/system (UI, API, data model, edge cases, rollout)
- Moving between requirements, decisions, concerns, and trade-offs on the same thing
- Revisiting an earlier point from a new angle
- Brief digressions that return to the main thread
- A decision followed by discussion of its implications
- Meta-discussion about the meeting itself ("can you hear me?", "let's timebox this")

When in doubt, do not split. Merging later is harder than splitting later.

### 4. Propose the split

**If the whole transcript is one subject (the common case):** State that it is a single-subject discussion and propose one output file. Do not enumerate internal topics.

**If multiple genuinely unrelated subjects are found:** Present them as a numbered list with a brief label for each (3–6 words) and the approximate share of the transcript each covers. Briefly justify *why* they are separate subjects rather than related topics, so the user can push back.

- **Quiet mode:** skip presenting and proceed with the detected split.
- **Otherwise:** ask the user to confirm, merge, rename, or drop subjects before proceeding. Merging should be easy — if the user says "those are the same thing," collapse them.

### 5. Distill each subject

For each confirmed subject, extract the relevant portions of the transcript.

**Remove:**
- Greetings, goodbyes, pleasantries ("how was your weekend", "hi everyone")
- Filler and verbal tics ("um", "you know", "like", "so basically")
- Tangents unrelated to the subject being extracted
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

Generate a title for each subject from its label.

**Format:** `YYYY-MM-DD Subject Label` — use today's date if no date is mentioned in the transcript, otherwise use the meeting date.

When writing to local files, convert the title to lowercase kebab-case with a `.md` extension. When writing to external tools (Confluence, Linear, etc.), use the title as-is.

- **Quiet mode:** accept the generated names and proceed.
- **Otherwise:** present proposed names and let the user adjust.

### 7. Generate output

**If a template was loaded in step 1:**

Generate each output following the template's structure. Apply the same rules as **d3:create**:
- All template headings must be present
- Fill sections with content extracted from the distilled transcript for that subject
- Sections not covered by the transcript get `_To be defined - not yet discussed_`
- Invoke the **d3:uncertainty-markers** skill for any ambiguous content

**If no template is configured:**

Each output contains only the cleaned transcript text — no metadata, no headings, no structure. This is the normal case when Transcripts has no Template in the Storage table.

### 8. Write output

Follow the Instructions column from the Transcripts row exactly. The Instructions define how and where to write — don't assume local markdown files. If the Instructions reference an MCP tool, use it; if they reference a CLI, use it; if they describe writing to a directory, do that.

### 9. Provide a summary

Tell the user:
- Number of subjects found and files created (usually one)
- Filenames / URLs and paths
- Approximate percentage of the original transcript that was noise (removed)
- If no template was used, suggest **d3:create** as the natural next step for each file

## Error handling

| Issue | Action |
|-------|--------|
| `d3.config.md` missing | Stop. Ask the user to run **d3:init** first. |
| Transcript too short or unclear | Warn that subject detection may be unreliable; ask to proceed or provide more context |
| Cannot distinguish subjects | Produce a single cleaned file and tell the user |
| No substantive content found | Warn the user — the transcript may be entirely small talk |
| Write fails | Provide the distilled text inline for manual saving |

## Related skills

- **d3:init** — prerequisite (creates `d3.config.md`)
- **d3:create** — natural next step: feed each distilled subject into create to produce an artifact
- **d3:refine** — alternative next step if the topic is an update to an existing artifact
- **d3:uncertainty-markers** — invoked when generating template-structured output with ambiguous content
