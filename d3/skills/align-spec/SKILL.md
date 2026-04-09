---
name: align-spec
description: Compare a feature specification against the actual codebase to detect drift. Reads the spec from d3.config.md, extracts concrete implementation anchors (routes, models, components, services), systematically searches the codebase for them, and produces a deviation report classifying findings as Missing Implementation, Extra Implementation, Behaviour Mismatch, Schema Drift, or Story Drift. Report only — does not fix anything. Use whenever the user wants to check whether a spec still matches the code, audit implementation against spec, detect drift after a development phase, compare stories against reality, or says things like "does the spec still match the code", "align this spec", "what's drifted", "audit the implementation against the spec", "check the stories against what we actually built". The hallmark is an existing spec + existing code, and a question about whether they agree.
---

# D3 — Align Spec with Code

This skill compares a feature specification against the actual codebase and reports where they disagree. It is a **reporting** skill — it does not modify code or specs. The goal is an honest map of the gaps so a human can decide what to fix.

## Core principle

**Specs describe intent. Code describes reality. Surface the gaps honestly.**

Neither is automatically right. A deviation might mean the code is behind the spec, or the spec is behind the code, or both are now wrong. This skill doesn't judge — it just reports, and leaves decisions to the user.

**Bounded exploration over exhaustive analysis:** it is better to report confidently on what was found than to guess about what wasn't. Cap exploration, note the gaps, and move on.

## Workflow

### 1. Load configuration

- Read `d3.config.md`. If missing, stop and ask the user to run **d3:init**.
- From the Storage table, find **all** rows whose Artifact name contains "Spec" (Product Specs and Tech Specs are separate rows by default) and the row matching "Stories".

### 2. Fetch the specification

The user will identify the spec by path, title, or description. Read each matched spec row's content.

Show the user what was found:

```
**Feature:** [Title]
**Product Spec:** [Found / Minimal / Not found] — [path]
**Tech Spec:**    [Found / Minimal / Not found] — [path]
```

If any spec is missing or minimal, warn but continue with whatever content is available. Note the limitation in the final report.

### 3. Detect existing stories

Search the Storage Location for "Stories" for items matching the spec title. Match by relationship (parent, epic, folder) rather than by item type — different backends use different type names. Store the list for step 6 (story drift analysis). If no stories are found, skip story drift.

### 4. Extract search anchors

Parse the spec for concrete, searchable implementation clues. The more specific the anchor, the more useful the search.

**From the Technical Spec:**
- API Contracts → route paths, HTTP methods, endpoint names
- Data Models → model/table/schema names, field names
- System Changes → service names, module names, integration points
- Infrastructure → queue names, cache keys, environment variable names

**From the Product Spec:**
- User Interface → component names, page names, form names
- User Journey → workflow names, feature flag names

Output: a list of search anchors, each labelled with a type (route, model, component, service, test) and one or more search terms.

If very few anchors come out, warn the user that the spec may be too high-level for meaningful code alignment — the report accuracy will be limited.

### 5. Explore the codebase

Use the anchors to find relevant code. Multi-pass:

1. **Routes / Endpoints** — search for API paths and controller/handler definitions
2. **Models / Schemas** — data model definitions, migration files, type definitions
3. **Components / Pages** — UI component files matching spec references
4. **Services / Modules** — business logic matching service names
5. **Tests** — test files covering the above

**Bounded exploration:**
- Cap at ~10 files per anchor so the analysis stays manageable
- Prefer exact matches over fuzzy matches
- Read key files to understand actual behaviour — filenames alone are not enough
- Note which anchors found no matches — these become candidates for "Missing Implementation"

Output: a map of anchor → relevant files, with brief summaries of what each file does.

### 6. Identify deviations

Compare spec against code section by section. Classify each deviation into one of five categories:

| Category | Meaning |
|----------|---------|
| Missing Implementation | Spec describes it, code doesn't have it |
| Extra Implementation | Code has it, spec doesn't mention it |
| Behaviour Mismatch | Both exist, but the logic differs |
| Schema Drift | Data models or API contracts differ from the spec |
| Story Drift | Story ACs match neither the current spec nor the actual code |

**For each spec section with search anchors:** compare the stated behaviour against the discovered code.

- API contracts: compare routes, methods, request/response shapes, status codes
- Data models: compare fields, types, constraints, relationships
- User workflows: compare described flows against the implemented UI/logic
- Stories (if found in step 3): compare story ACs against both the current spec and the current code
- Note any implemented functionality not described in the spec (Extra Implementation)

**Story drift detection** — for each story from step 3, check both:
- Do the ACs still match what the spec says? (spec drift)
- Do the ACs still match what the code does? (implementation drift)

Flag stories where the ACs match neither.

### 7. Generate the deviation report

```
## Deviation Report: [Spec Title]

**Analysed:** [N] search anchors across [M] files
**Exploration gaps:** [any anchors with no matches]

---

### Critical Deviations

[DEV-1] **[Category]:** [Brief title]
- **Spec says:** [what the specification describes]
- **Code does:** [what the implementation actually does]
- **Severity:** Critical
- **Recommendation:** [Update Spec / Update Code / Discuss]

### Moderate Deviations

[DEV-2] ...

### Minor Deviations

[DEV-3] ...

### Story Drift

[STORY-KEY]: [Story Title]
- **AC says:** [what the acceptance criteria state]
- **Spec says:** [what the current spec states]
- **Code does:** [what the implementation does]
- **Recommendation:** [Update Story / Update Spec / Update Code / Discuss]

---

**Summary:**
- Critical: [N]
- Moderate: [N]
- Minor: [N]
- Story Drift: [N] stories affected
- Well-Aligned: [sections/areas where spec and code agree]
```

### 8. Provide a final summary

```
Specification alignment complete!

**Specification:** [Title] — [path]

Deviation Summary:
- Critical: [N]
- Moderate: [N]
- Minor: [N]
- Story Drift: [N] stories affected

Well-Aligned Areas:
- [sections/areas where spec and code agree]

Exploration Gaps:
- [anchors that found no code matches — may indicate missing implementation OR limits of the search]

Suggested next steps (based on findings):
- Spec outdated? → d3:refine to update the spec to match reality
- Missing implementation? → d3:decompose to create stories for the gaps
- Behaviour mismatch? → discuss with the team, then either fix the code or d3:refine the spec
```

## Error handling

| Issue | Action |
|-------|--------|
| `d3.config.md` missing | Stop. Ask the user to run **d3:init** first. |
| Spec not found | Verify identifier/path, suggest a search |
| Spec lacks technical detail | Warn about limited alignment accuracy, proceed with available anchors |
| No search anchors extracted | Tell the user the spec is too high-level for code alignment; suggest refining the tech spec first |
| Codebase too large / too many matches | Tighten searches to exact matches, increase specificity, note the gaps |
| No code found for an anchor | Report as potential "Missing Implementation" with a caveat that the search may have missed it |
| No stories found | Skip story drift analysis, proceed with spec-vs-code only |

## Key principles

1. **Honest reporting** — report what was found *and* what wasn't; never hide exploration gaps
2. **Bounded exploration** — cap file reads per anchor; note what wasn't searched
3. **Five deviation categories** — Missing, Extra, Mismatch, Schema Drift, Story Drift cover all cases
4. **Severity-driven** — surface critical deviations first, don't let minor ones bury them
5. **Report only** — present findings with recommendations; do not modify code, specs, or stories
6. **Spec and code are equal** — neither is automatically "right"; deviations go both ways

## Related skills

- **d3:init** — prerequisite (creates `d3.config.md`)
- **d3:refine** — natural follow-up when the report shows the spec is behind the code
- **d3:decompose** — natural follow-up when the report shows missing implementation that needs stories
- **d3:create** — if the spec is so far gone that a rewrite is easier than a refine
