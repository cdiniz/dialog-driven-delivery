---
description: Compare a feature specification against the actual codebase to detect drift. Identifies missing implementations, extra code, behaviour mismatches, schema drift, and story drift. Produces a structured deviation report. Use when implementation may have diverged from spec, after a development phase completes, or when user asks to align/compare/check spec against code.
---

## Core Principle

**Specs describe intent. Code describes reality. Surface the gaps honestly.**

Systematically compare what the specification says should exist against what the codebase actually contains. Report deviations without judgement — don't attempt to fix anything. Bounded exploration over exhaustive analysis: it's better to report confidently on what was found than to guess about what wasn't.

---

## Workflow

### 1. Detect Providers, Templates, and Settings
- Read `d3.config.md` for D3 config
- Search for ### D3 Config  ### Templates
- Detect spec mode from provider configuration:
  - If `### Product Spec Provider` AND `### Tech Spec Provider` both exist → **separated mode**. Store each provider's skill and configuration independently.
  - If only `### Spec Provider` exists → **combined mode**. Store single provider config.
- Store for later steps

### 2. Fetch Specification
Command accepts spec identifier, URL, or title in `$ARGUMENTS`.

Determine which provider owns the spec:
- **Combined mode:** Use the single spec provider's `get_spec`
- **Separated mode:** Detect whether the identifier refers to a product or tech spec (from title suffix, filename, or content). Use the matching provider's `get_spec`.

**If separated mode:**
After fetching, derive the companion title by swapping the suffix ("Product Spec" ↔ "Tech Spec") and fetch it from the other provider via `search_specs` or `get_spec`.
Alignment always needs both product and technical context.

Display:
```
**Specification:** [Title] - [URL]
**Product Spec:** [✅ Found / ⏳ Minimal / ❌ Not found]
**Technical Spec:** [✅ Found / ⏳ Minimal / ❌ Not found]
```

If either spec is missing or minimal: Warn but continue with available content.

### 3. Detect Existing Stories
Find the epic matching the spec title and list all its children (stories, tasks, or any issue type).
- Store epic key and child list for later story drift analysis
- If no epic or no children found, skip story drift in Step 6

### 4. Extract Search Anchors
Parse the specification for concrete, searchable implementation clues:

**From Technical Spec sections:**
- API Contracts → route paths, HTTP methods, endpoint names
- Data Models → model/table/schema names, field names
- System Changes → service names, module names, integration points
- Infrastructure → queue names, cache keys, environment variables

**From Product Spec sections:**
- User Interface → component names, page names, form names
- User Journey → workflow names, feature flags

**Output:** A list of search anchors, each with a type (route, model, component, service, test) and search terms.

If few anchors extracted: Warn that the spec may lack technical detail, limiting alignment accuracy.

### 5. Explore Codebase
Use search anchors to systematically find relevant code files. Multi-pass approach:

1. **Routes/Endpoints** — Search for API paths, controller/handler definitions
2. **Models/Schemas** — Search for data model definitions, migration files, type definitions
3. **Components/Pages** — Search for UI component files matching spec references
4. **Services/Modules** — Search for business logic matching service names
5. **Tests** — Search for test files covering the above

**Bounded exploration:**
- Cap at ~10 files per anchor to stay manageable
- Prefer exact matches over fuzzy matches
- Read key files to understand actual behaviour (not just filenames)
- Note which anchors found no matches — these become candidates for "Missing Implementation"

**Output:** A map of anchor → relevant files with brief summaries of what each file does.

### 6. Identify Deviations
Compare spec vs code section by section. Classify each deviation into one of five categories:

**Deviation Categories:**

| Category | Meaning |
|----------|---------|
| Missing Implementation | Spec describes it, code doesn't have it |
| Extra Implementation | Code has it, spec doesn't mention it |
| Behaviour Mismatch | Both exist, but logic differs |
| Schema Drift | Data models or API contracts differ from spec |
| Story Drift | Story ACs match neither the current spec nor the actual code |

**Process:**
1. For each spec section with search anchors, compare stated behaviour against discovered code
2. For API contracts: compare routes, methods, request/response shapes, status codes
3. For data models: compare fields, types, constraints, relationships
4. For user workflows: compare described flows against implemented UI/logic
5. For stories (if found in Step 3): compare story ACs against both spec and code
6. Note any implemented functionality not described in the spec (Extra Implementation)

**Story Drift detection:**
For each story found in Step 3, check:
- Do the ACs still match what the spec says? (spec drift)
- Do the ACs still match what the code does? (implementation drift)
- Flag stories where ACs match neither

### 7. Generate Deviation Report

```
## Deviation Report: [Spec Title]

**Analysed:** [N] search anchors across [M] files
**Exploration gaps:** [Any anchors with no matches, if applicable]

---

### Critical Deviations

[DEV-1] **[Category]:** [Brief title]
- **Spec says:** [What the specification describes]
- **Code does:** [What the implementation actually does]
- **Severity:** Critical
- **Recommendation:** [Update Spec / Update Code / Discuss]

### Moderate Deviations

[DEV-2] ...

### Minor Deviations

[DEV-3] ...

### Story Drift

[STORY-KEY]: [Story Title]
- **AC says:** [What the acceptance criteria state]
- **Spec says:** [What the current spec states]
- **Code does:** [What the implementation does]
- **Recommendation:** [Update Story / Update Spec / Update Code / Discuss]

---

**Summary:**
- Critical: [N] deviations
- Moderate: [N] deviations
- Minor: [N] deviations
- Story Drift: [N] stories affected
- Well-Aligned: [Sections/areas where spec and code agree]
```

### 8. Provide Summary

```
✅ Specification alignment complete!

**Specification:** [Title] - [URL]

Deviation Summary:
- Critical: [N] deviations
- Moderate: [N] deviations
- Minor: [N] deviations
- Story Drift: [N] stories affected

Well-Aligned Areas:
- [List sections/areas where spec and code agree]

Exploration Gaps:
- [Any anchors that found no code matches — may indicate missing implementation or incorrect search terms]

Next: /d3:refine-spec (update spec) → /d3:decompose (new stories)
```

---

## Error Handling

| Issue | Action |
|-------|--------|
| Spec not found | Verify identifier/URL, suggest search |
| Spec lacks technical detail | Warn about limited alignment accuracy, proceed with available anchors |
| No search anchors extracted | Inform user the spec may be too high-level for code alignment, suggest refining tech spec first |
| Codebase too large / too many matches | Tighten search to exact matches, increase specificity, note gaps |
| No code found for anchor | Report as potential "Missing Implementation" with caveat that search may have missed it |
| Epic/stories not found | Skip story drift analysis, proceed with spec-vs-code only |
| Story provider unavailable | Skip story drift analysis, proceed with spec-vs-code only |

---

## Key Principles

1. **Honest reporting** — Report what was found and what wasn't; never hide exploration gaps
2. **Bounded exploration** — Cap file reads per anchor, note what wasn't searched
3. **Five deviation categories** — Missing, Extra, Mismatch, Schema Drift, Story Drift cover all cases
4. **Severity-driven** — Critical deviations surface first, minor ones don't distract
5. **Report only** — Present findings with recommendations, but don't take action or ask what to do next
6. **Spec and code are equal** — Neither is automatically "right"; deviations go both ways
