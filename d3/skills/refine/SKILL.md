---
name: refine
description: Update an existing D3 artifact (spec, ADR, story, transcript, or a custom artifact) with new information — meeting notes, technical decisions, review feedback, or answers to previously-open questions. Detects which artifact type it is from d3.config.md, updates ONLY the sections the new information explicitly addresses, preserves everything else, and propagates changes to related artifacts (e.g. stories for a spec). Use whenever the user wants to update/refine/revise/iterate on an existing artifact, incorporate new meeting notes into a spec, resolve open questions, add review feedback, or says things like "update the spec with these notes", "refine the ADR", "the team decided X, update the story", "we got answers to the open questions, can you apply them". The hallmark is an artifact that already exists and needs to evolve.
---

# D3 — Refine Artifact

This skill updates an existing D3 artifact in place based on new information. It exists to prevent two equally-bad failure modes: **greedy updates** (rewriting unrelated sections because "while we're here") and **hallucinated elaboration** (filling empty sections just because they're empty).

## Core principle

**Update only what has new information. Preserve everything else.**

The new input is a delta, not a replacement. Detect which sections it actually addresses, update those, and leave the rest strictly alone — including empty placeholders that still aren't discussed.

## Workflow

### 1. Load configuration

- Read `d3.config.md`. If missing, stop and tell the user to run **d3:init** first.
- Read Quiet Mode from `### Settings`.
- Read Brain Source from `### Settings`. If set to anything other than `_none_` (empty), option F in step 5 is enabled.

### 2. Locate and fetch the artifact

The user will identify the artifact by path, title, or description. Match it to a row in the Storage table by checking:

1. Does the path fall under a Storage row's Location?
2. If ambiguous, does the artifact's structure match the referenced template for one row better than the others?

If it still can't be determined, ask the user which artifact type this is, presenting options from the Storage table.

Once identified, load the template for that row and read the current content of the artifact from its Location, following the row's Instructions.

### 3. Detect related artifacts

Some artifacts have downstream dependents. The most common case: a feature spec has user stories that reference it. Scan the Storage table for related types and note any that could be affected by changes to this artifact. Store the list for step 8.

### 4. Analyze current state

Briefly show the user the artifact's current state: title, location, which sections have real content vs placeholders, and how many uncertainty markers are present. This grounds the refinement conversation.

### 5. Request refinement input

Ask the user how they want to provide the new information:

```
How would you like to provide new information?
A) Paste a meeting transcript
B) Paste updated documentation
C) Describe the changes
D) Paste review feedback
E) Resolve open questions & assumptions (walk through them one at a time)
F) Pull new information from the team brain  (only shown if Brain Source is set)
```

**Quiet mode:** if the user's message already contains the new content, use it directly and skip the question.

### 5c. Option F — pull new information from the team brain

If the user picks F (or their request already names a brain topic, e.g. "refine the spec with the latest from the brain on product-recommendation"):

1. Read `<Brain Source>/INDEX.md`. If missing, warn and fall back to options A–E.
2. Match the requested topic against INDEX.md entries. If the user didn't give a topic, default to the current artifact's title and propose matches.
3. Show the user the matched entries and ask for confirmation. In quiet mode, only auto-confirm a single unambiguous match.
4. Read the confirmed files and use their concatenated content as the new information for step 6.
5. The brain is read-only for this skill — never write back to Brain Source.

### 5b. Option E — walk through open questions one at a time

If the user picks E, this is a special interactive flow:

1. Scan the artifact for uncertainty markers (`[OPEN QUESTION]`, `[DECISION PENDING]`, `[ASSUMPTION]`, `[CLARIFICATION NEEDED]`, and `_To be defined_` placeholders), plus any Open Questions or Assumptions tracking sections the template has.
2. Present them one at a time — don't dump the whole list.
3. For each item, ask the user for a resolution, to confirm the assumption, or to keep it open.
4. Collect all resolutions, then continue to step 6 treating the collected answers as the new information.

This flow is valuable because the questions were written at a specific point in time and may have grown stale. Walking through them one at a time gives the user a chance to think about each one, rather than dropping a wall of text on them.

### 6. Analyze new information (non-greedy)

For each section of the artifact, ask: _does the new input explicitly address this section?_

- **Yes** → prepare an update using only information explicitly stated in the input.
- **No** → leave the section completely alone. Do not fill empty placeholders just because they're empty. Do not elaborate on existing content. Do not rewrite for style.

Things to avoid — these are the recurring failure modes:

- Inventing details that weren't in the input
- Elaborating beyond what was stated
- Filling empty sections because they look lonely
- Removing `_To be defined_` without actual replacement content
- Treating template example text as a prompt to fill

Things to do:

- Add only explicitly stated information
- Replace placeholders when they're now discussed
- Add new uncertainty markers if the input introduces new ambiguity
- Preserve empty sections if the input didn't touch them
- Remove resolved uncertainty markers once the answer is in

### 7. Show proposed changes

Present the changes section-by-section: for each updated section, show the current content, the proposed content, and a one-line rationale. This gives the user a chance to catch greedy updates before they land.

**Quiet mode:** skip the review and accept all proposed changes.

### 8. Analyze related-artifact impact

For each change proposed in step 7, check whether it affects the related artifacts identified in step 3. Common cases:

- A new acceptance criterion in a spec might require updates to a story's ACs
- A removed requirement might invalidate a story altogether
- A resolved open question might unblock a story that had a "needs-clarification" label

Present the impact analysis and the proposed updates to related artifacts.

**Quiet mode:** proceed with the updates without presenting.

Skip this step entirely if no related artifacts were identified in step 3.

### 9. Validate changes

Quick checklist before writing:

- [ ] Every change has a clear rationale tied to specific input content
- [ ] Resolved uncertainty markers have been removed; new ones have been added where appropriate
- [ ] Nothing was invented — every update traces back to the input
- [ ] The artifact is still internally consistent (a change in section 2 doesn't contradict section 5)
- [ ] Template structure is intact
- [ ] Related-artifact updates match the main changes — no drift

### 10. Apply the updates

Write the updated artifact back to its Location, following the Storage row's Instructions literally. If related artifacts are affected, update them using their own Storage row's Instructions — which may target a different tool (e.g. the spec lives in Confluence but the stories live in Jira).

### 11. Report what changed

Tell the user:

- Which sections were updated
- Which open questions / assumptions were resolved
- Any new uncertainties introduced
- Which related artifacts were updated (and with what)
- Suggested next steps — but only when they're actionable:
  - **d3:refine** — suggest only if the artifact still has uncertainty markers or placeholder sections after this pass. If everything resolved and no new uncertainties were introduced, don't suggest another refine; the artifact is settled until new information arrives.
  - **d3:decompose** — suggest only for feature specs that are now complete enough to break into stories.
  - If no next step is actionable, say so. A fully-resolved artifact doesn't need a follow-up skill.

## Error handling

| Issue                                         | Action                                                          |
| --------------------------------------------- | --------------------------------------------------------------- |
| `d3.config.md` missing                        | Stop. Ask the user to run **d3:init** first.                    |
| No changes detected in input                  | Tell the user; ask for clarification or a different angle       |
| Conflicting info (input contradicts existing) | Show the conflict, ask how to resolve — don't silently pick one |
| Major scope change                            | Warn about downstream impact and confirm before proceeding      |
| Write fails                                   | Provide the full updated text inline for manual update          |
| Artifact can't be found                       | Verify the identifier; suggest a search                         |
| Can't detect artifact type                    | Ask the user to specify                                         |

## Related skills

- **d3:init** — prerequisite (creates `d3.config.md`)
- **d3:uncertainty-markers** — standards for the markers this skill resolves and adds
- **d3:create** — use that instead for brand-new artifacts; this skill only updates existing ones
- **d3:decompose** — natural next step once a spec is refined enough to break into stories
- **d3:align-spec** — complementary: compares a spec against code to find drift that this skill can then apply
- **d3:distill** — preprocess messy transcripts before feeding them in as new information
