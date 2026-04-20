---
name: brain-pull
description: Pull context from a team knowledge repo ("team brain" / "llm-wiki") by reading its entry-point index, matching entries to a topic using LLM judgment (not strict keyword search), following hub pages, confirming the selection, and returning the concatenated content of the matched files. Use whenever the user wants D3 or any other skill to read from the brain, look up a topic in the brain, check the wiki, or pull context from the team knowledge repo — e.g. "check the brain for catalog-browse", "pull the latest on checkout from the brain", "look up product recs in the wiki", "create a spec for X from the team brain", "refine the spec using the brain". The hallmark is any request that references the team brain, team wiki, or llm-wiki as a source of context. Read-only — never writes to the brain.
---

# D3 — Pull Context from the Team Brain

This skill finds and reads the right files in a team brain (a separate knowledge repo, sometimes called an "llm-wiki") and returns their content as input context for whatever the user is doing next — usually a `d3:create` or `d3:refine` invocation, but it can feed any other skill too.

## Why this matters

Teams accumulate raw context (transcripts, slack threads, docs) in a knowledge repo that's been distilled into a navigable wiki. When Claude needs that context, it can't just grep — file titles, synonyms, and hub pages all get in the way of a naive match. This skill exists to do that lookup well: match by meaning, follow hubs so related files aren't missed, and confirm with the user before reading.

**Core principle: read-only, judgment-based matching, confirm before reading.**

## Workflow

### 1. Load configuration

- Read `d3.config.md` at the repo root. If it doesn't exist, stop and tell the user to run `d3:init` first.
- Read the Brain Source setting from the `### Settings` section. If it's `_none_` or missing, stop and tell the user to set Brain Source in `d3.config.md` (or run `d3:init` again).
- Read the Quiet Mode setting. Used in step 5.

### 2. Locate the entry-point index

Treat the Brain Source value as a readable location (filesystem path, relative or absolute). Find its entry-point index file:

1. Try `<Brain Source>/index.md` first.
2. If absent, try `<Brain Source>/wiki/index.md`.
3. If neither exists, stop and tell the user the brain has no readable index at that location. Do not guess a different path. Do not silently fall back to reading random files.

### 3. Read the index

Read the index. Assume nothing about its internal structure — it may group entries into sections (People, Projects, Decisions, Concepts, Summaries, etc.) but this skill does not rely on specific section names. Each entry is a title plus a link to a markdown file.

### 4. Match the topic against entries — by judgment, not strict string match

The user gave (or implied) a topic. Match it against entry titles using LLM judgment.

- Recognise that `catalog-browse`, "Catalog browse: grid + pagination", and "Book grid layout" are the same concept.
- Consider synonyms, acronyms, rephrasings, and obviously-related concepts.
- Collect matching entries across all sections.
- Skip obviously irrelevant sections like "People" unless a person is the explicit subject.
- Err toward a broader candidate set — the confirmation step below is cheap; missing a relevant file is expensive.

If the user didn't give an explicit topic (e.g. "refine this spec using the brain"), default to the subject of their current task — the spec's title, the feature name, whatever context Claude already has.

### 5. Follow hub pages

If any matched entry is a hub (a project overview, a concept page, a topic overview — anything that aggregates links to other files), read it and merge its linked files into the candidate set. This is the main safety net against title drift between related files.

- Always follow hubs when their title matches the topic.
- Follow them even when you only suspect they might aggregate relevant links.

### 6. Confirm the candidate set

Show the user the full candidate set (paths + titles from the index) and ask for confirmation before reading the full contents.

- Err on the side of showing too many — it's cheaper for the user to prune one extra than to silently miss a relevant file.
- This step catches topic mismatches (e.g. "product recs" vs "recommendation engine") and over-reach.

**Quiet mode:** skip confirmation only if there is a single unambiguous match. If multiple matches, always confirm.

### 7. Read the confirmed files

Read every confirmed file. Concatenate their content.

- **Supersession / conflicts are the brain's concern, not yours.** If two files conflict (e.g. a dated decision overrides an earlier one), read both and let the consuming skill or the user reason about which takes precedence. When the file titles or contents clearly indicate chronology (e.g. `2026-04-13-...` supersedes `2026-03-23-...`), surface that so the consumer can trust the later-dated content.
- Do not edit or annotate the brain files — you only read.

### 8. Report

Tell the user:

- The list of files that were read (paths + titles).
- A one-line summary of what the content covers (e.g. "catalog-browse decisions from March and April, plus the epic hub").
- That the content is now available in the conversation for the next step — whatever skill the user invokes next (`d3:create`, `d3:refine`, or something else) can use it as input context.

If no entries matched, tell the user that and stop. Do not invent content. Do not silently write anywhere.

### 9. Never write to the brain

The brain is strictly read-only from this skill's perspective. Any "publish back to the brain" workflow is the brain repo's own concern, triggered by the brain's own tooling.

## Error handling

| Issue                                  | Action                                                                            |
| -------------------------------------- | --------------------------------------------------------------------------------- |
| `d3.config.md` missing                 | Stop. Tell the user to run `d3:init` first.                                       |
| Brain Source is `_none_`               | Stop. Tell the user to set Brain Source in `d3.config.md`.                        |
| Index not found at either path         | Stop. Report the paths tried. Do not guess other paths.                           |
| No entries match the topic             | Tell the user. Do not invent, do not read random files.                           |
| Confirmed file can't be read           | Report which file, continue with the ones that could be read, flag the gap.       |
| User references brain but no topic     | Default to the current task's subject; if still ambiguous, ask for a topic.       |

## Related skills

- **d3:init** — creates `d3.config.md` with the `Brain Source` setting this skill reads.
- **d3:create** — common next step: create an artifact from the content this skill pulled.
- **d3:refine** — common next step: refine an existing artifact with new content from the brain.

## How this skill composes with create / refine

Most of the time you don't invoke this skill by itself — you invoke it as part of a larger request. Examples:

- *"Create a product spec for catalog-browse, pull from the team brain."* → Claude invokes `d3:brain-pull` first, then `d3:create` with the pulled content as input.
- *"Refine this spec using the brain."* → Claude invokes `d3:brain-pull` (topic defaults to the spec's subject), then `d3:refine` with the pulled content as the refinement input.
- *"Look up checkout mechanics in the brain."* → Claude invokes this skill standalone; the content lands in the conversation and the user decides what to do with it.

The consuming skill (create/refine/whatever) does not need to know anything about the brain — it just sees content in the conversation, exactly as if the user had pasted it.
