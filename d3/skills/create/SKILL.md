---
name: create
description: Create a new D3 artifact — feature specifications, ADRs, user stories, structured meeting transcripts or custom artifact — from any input (a pasted meeting transcript, an existing document, or a conversational description). Reads d3.config.md to figure out the artifact type, template, and storage destination, then fills in ONLY what was actually discussed and marks everything else with uncertainty markers. Use whenever the user wants to write up a spec from meeting notes, document a decision as an ADR, capture a discussion as a transcript, draft a story, or says things like "turn this transcript into a spec", "write this up", "create a spec/ADR/story for X", "document this meeting". The hallmark is an artifact that doesn't exist yet and needs to be drafted from some raw context.
---

# D3 — Create Artifact

This skill drafts a new D3 artifact (spec, ADR, story, transcript, or other custom type) from raw input context. Its single most important rule: **fill only what is actually known, and mark everything else explicitly as uncertain**.

## Why this matters

When AI drafts a spec from a sparse conversation, the tempting failure mode is to invent plausible-sounding details to flesh it out — OAuth2 providers that were never discussed, rate limits nobody mentioned, error messages someone wrote once in a similar project. Those hallucinations look authoritative and get implemented as if they were decisions. This skill exists to prevent that: empty sections are better than imagined content, and surfaced uncertainties are better than hidden assumptions.

**Core principle: fill only what you know. Empty sections are better than hallucinated content.**

## Workflow

### 1. Load configuration and sibling skills

- Read `d3.config.md` at the repo root. If it doesn't exist, stop and tell the user to run the **d3:init** skill first.
- Invoke the sibling **d3:uncertainty-markers** skill to load marker standards. These are used in step 5.
- Read the Quiet Mode setting from the `### Settings` section.
- Read the Brain Source setting from the `### Settings` section. If set to anything other than `_none_` (empty), option D in step 3 is enabled.

### 2. Determine the artifact type

Read the Storage table from `d3.config.md`. Each row in the Artifact column is a supported type (Product Specs, Tech Specs, Stories, ADRs, Transcripts — or whatever the team has customized).

- **If the user's request already names the type** (e.g. "create an ADR for...", "draft a tech spec", "capture this meeting as a transcript"): match it to a row and proceed.
- **Otherwise:** present the available artifact types from the Storage table and let the user pick.

Once the type is chosen, load the template file referenced in the matching row's Template column. That template's section headings become the structure of the artifact. The same row's Location and Instructions columns control where and how to write.

### 3. Get input context

Ask how the user wants to provide the source material — unless they already pasted it or linked to a file, in which case skip the question and use what they gave you.

```
How would you like to provide the information?
A) Paste a meeting transcript
B) Paste an existing document
C) Describe it conversationally
D) Pull context from the team brain  (only shown if Brain Source is set)
```

**Quiet mode:** if the user's message already contains enough context (pasted text, a file reference, or a `brain:<topic>` reference), use it directly and skip the prompt.

**If the user picks D (or the request already names a brain topic, e.g. "create a product spec for catalog-browse from the brain"):**

1. Treat the Brain Source value as a readable location (filesystem path, relative or absolute). Find its entry-point index file — by convention `index.md` at the Brain Source root, or under a `wiki/` subfolder (try `<Brain Source>/index.md` first, then `<Brain Source>/wiki/index.md`). If neither exists, warn the user the brain has no readable index and fall back to options A/B/C.
2. Read the index. Assume nothing about its internal structure — it may group entries into sections (People, Projects, Decisions, Concepts, Summaries, etc.) but D3 does not rely on specific section names. Each entry is a title plus a link.
3. **Match the user's topic against entry titles using judgment, not strict string matching.** You are an LLM — recognise that `catalog-browse`, "Catalog browse: grid + pagination", and "Book grid layout" are the same concept. Consider synonyms, acronyms, rephrasings, and obviously-related concepts. Collect matching entries across all sections. Skip obviously irrelevant sections like "People" unless a person is the explicit subject. Err toward a broader candidate set — the user confirmation step below is cheap.
4. **Follow hub pages.** If any matched entry is a hub (a project overview, a concept page, a topic overview — anything that aggregates links to other files), read it and merge its linked files into the candidate set. This is the main safety net against title drift between related files. Always follow hubs when their title matches the topic; follow them even when you only suspect they might aggregate relevant links.
5. Show the user the full candidate set (paths + titles from the index) and ask for confirmation before reading. Err on the side of showing too many — it's cheaper for the user to prune one extra than to silently miss a relevant file. This step catches topic mismatches (e.g. "product recs" vs "recommendation engine") and over-reach.
6. **Quiet mode:** skip confirmation only if there is a single unambiguous match. If multiple matches, always confirm.
7. Read the confirmed files and use their concatenated content as the input context for step 4 of this workflow.
8. If no entries match, tell the user and fall back to options A/B/C.

The brain is read-only from this skill's perspective. Never write back to the Brain Source. Supersession / conflict resolution is the brain's responsibility — if two files conflict (e.g. a dated decision overrides an earlier one), read both and trust the later-dated file.

### 4. Analyze input and propose a title

Extract the relevant information from the input, guided by the sections defined in the matching template. Propose a title for the artifact.

- **Non-quiet mode:** present the proposed title and wait for confirmation.
- **Quiet mode:** accept the proposed title immediately.

### 5. Generate the artifact

Generate the full artifact following the template's structure. This step is where most of the work happens, and where most mistakes happen. Four rules:

1. **Create the full structure.** Every section heading from the template appears in the output. Never skip a section just because it wasn't discussed — the heading stays, the body is a placeholder.
2. **Fill only what was discussed.** For each section: if the input covered it, write real content. If it didn't, write `_To be defined - not yet discussed_`.
3. **Never invent.** Template examples are structural guides, not content prompts. If you find yourself typing plausible-sounding details that weren't in the input, stop and use a placeholder or an uncertainty marker instead.
4. **Mark uncertainties explicitly.** Use the four markers from the d3:uncertainty-markers skill:
   - `[OPEN QUESTION: text]` — user decision needed
   - `[DECISION PENDING: options]` — valid options exist, choice deferred
   - `[ASSUMPTION: statement]` — inference from context, needs validation
   - `[CLARIFICATION NEEDED: aspect]` — vague requirement

   If the template has an Open Questions / Assumptions section, list each inline marker there with context so stakeholders can scan what needs resolution.

The test for "did I hallucinate?" is: could I cite the exact sentence from the input that supports this line? If not, it's a placeholder or a marker.

### 6. Validate before creating

Run through this checklist before writing anything:

- [ ] All template headings present, none skipped
- [ ] Each section that was discussed has real content
- [ ] Each section that wasn't discussed has a placeholder
- [ ] No template examples copied as if they were real content
- [ ] Uncertainty markers tracked in the Open Questions / Assumptions section (if the template has one)

**Non-quiet mode:** show the user a summary — title, section coverage (e.g. "5 of 8 sections have content"), uncertainty marker count — and ask for confirmation before writing.

**Quiet mode:** skip the review and proceed.

### 7. Write the artifact

Follow the Instructions column from the matching Storage row. The Instructions column is the source of truth for *how* to write — treat it literally. If it says "Create a Confluence page using mcp__atlassian__createConfluencePage", use that exact tool with the parameters it specifies. Don't fall back to writing a local file unless the Instructions tell you to.

Write to the Location specified in the same row.

### 8. Report what was created

Tell the user:
- The title and path/URL of the new artifact
- Coverage stats relevant to the artifact type (e.g. "4 of 8 sections filled, 3 open questions")
- Suggested next steps — but only when they're actionable:
  - **d3:refine** — suggest only if the artifact has uncertainty markers or placeholder sections. If all sections are filled and there are no markers, don't suggest refine; the artifact is complete until new information arrives.
  - **d3:decompose** — suggest only for feature specs when the user wants to break them into stories.
  - If no next step is actionable, say so. A complete artifact with no open questions doesn't need a follow-up skill.

## Error handling

| Issue | Action |
|-------|--------|
| `d3.config.md` missing | Stop. Tell the user to run **d3:init** first. |
| Ambiguous scope | Ask clarifying questions before drafting |
| Minimal concrete info | Warn that the artifact will be mostly placeholders; confirm before drafting |
| Conflicting info from different speakers | Mark `[DECISION PENDING]` rather than picking one |
| Write fails (MCP error, permissions, etc.) | Provide the full artifact text inline so the user can save it manually |

## Related skills

- **d3:init** — must run before this skill to create `d3.config.md`
- **d3:uncertainty-markers** — loaded inline; defines the four marker types
- **d3:refine** — natural next step to update the artifact as more information arrives
- **d3:decompose** — natural next step for feature specs, to break them into user stories
- **d3:distill** — pre-processes messy multi-topic transcripts before feeding them into this skill
