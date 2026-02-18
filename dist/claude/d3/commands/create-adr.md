---
description: Create an Architectural Decision Record (ADR) from any input context (meeting transcripts, documents, or conversational discussion). Captures architectural decisions — framework choices, database selections, event-driven vs synchronous, etc. — as immutable records following MADR v4 format. Use when a technical or architectural decision has been made or is being proposed. If a decision changes, create a new ADR that supersedes the old one.
---
## Core Principle

**Capture the decision AND the reasoning. An ADR without rationale is just a changelog entry.**

ADRs are immutable records following [MADR v4](https://adr.github.io/madr/) format. If a decision changes, create a new ADR that supersedes the old one. Decisions feed into specifications via `/d3:refine-spec`.

---

## Workflow

### 1. Detect Provider and Templates
- Read CLAUDE.md for D3 config
- Search for `### ADR Provider` section first
- If no ADR Provider configured, fall back to `### Spec Provider`
- Load ADR template from d3-templates skill (or custom path if configured)
- Store provider and template for later steps

### 2. Get Input Context
Ask user:
```
How would you like to provide the architectural decision information?
A) Paste meeting transcript
B) Paste existing document
C) Describe conversationally
```

### 3. Get Location
Ask where to create the ADR. If needed, use provider's `list_locations`.

Use the location from ADR Provider config if available, otherwise Spec Provider's location.

### 4. Auto-Number
Search existing ADRs using provider's `search_specs` to determine the next number:
- Search for "ADR-" prefix in the configured location
- Parse existing numbers and determine the next sequential number
- If no existing ADRs found, start with ADR-001

### 5. Analyze Input & Extract Decision

Extract from context (following MADR v4 structure):
- **Context and Problem Statement:** The situation and problem driving the decision
- **Decision Drivers:** Forces, concerns, and constraints influencing the decision
- **Considered Options:** All options that were evaluated
- **Decision Outcome:** Which option was chosen and why
- **Consequences:** Good, bad, and neutral impacts of the decision
- **Confirmation:** How compliance with the decision will be verified
- **Pros and Cons of each Option:** Detailed analysis per option

Propose title (short, representative of solved problem and found solution), wait for confirmation.

### 6. Determine Status & Metadata

- If a clear decision was made → Status: **Accepted**
- If still under discussion or pending approval → Status: **Proposed** with `[DECISION PENDING: ...]` markers
- Ask user to confirm the status
- Identify decision-makers, consulted, and informed parties from context

### 7. Handle Superseding

Ask: "Does this ADR supersede an existing one?"

If yes:
- Fetch the old ADR using provider's `get_spec`
- Update old ADR status to "Superseded by ADR-[NEW_NUMBER]" using provider's `update_spec`
- Add `Supersedes: ADR-[OLD_NUMBER]` metadata to new ADR

If no: Continue without cross-references.

### 8. Generate ADR

**CRITICAL RULES:**

1. **Follow MADR v4 template structure:**
   - ALL section headings from template
   - Never skip sections
   - Use "Good, because..." / "Bad, because..." / "Neutral, because..." format for consequences and pros/cons

2. **Fill ONLY what was discussed:**
   - Discussed → Real content
   - NOT discussed → `_To be defined - not yet discussed_`

3. **NEVER invent:**
   - Technical details, alternatives, or consequences not mentioned
   - When in doubt: placeholder, not guess

4. **Decision Outcome format:**
   - Always state: `Chosen option: "[option]", because [justification]`
   - For proposed decisions: `[DECISION PENDING: option A vs option B vs ...]`

5. **Mark uncertainties:**
   - `[OPEN QUESTION: ...]` - Needs answer
   - `[DECISION PENDING: ...]` - Multiple approaches, not yet decided
   - `[ASSUMPTION: ...]` - Reasonable inference
   - `[CLARIFICATION NEEDED: ...]` - Vague aspect

Invoke uncertainty-markers skill for detailed guidance.

### 9. Validate Before Creation

**Structure validation (MADR v4):**
- [ ] ALL template headings present (Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Consequences, Confirmation, Pros and Cons of the Options, More Information)
- [ ] Context and Problem Statement explains the situation clearly
- [ ] Decision Drivers lists the forces/concerns
- [ ] Decision Outcome uses "Chosen option: X, because Y" format
- [ ] At least 2 options in Considered Options
- [ ] Pros and Cons section has detailed analysis per option using "Good/Bad/Neutral, because..." format
- [ ] No invented details — only what was discussed

**Uncertainty validation:**
- [ ] Count all markers: `[OPEN QUESTION]`, `[ASSUMPTION]`, `[CLARIFICATION NEEDED]`, `[DECISION PENDING]`
- [ ] If status is "Accepted", no `[DECISION PENDING]` markers should remain in Decision Outcome section
- [ ] If status is "Proposed", `[DECISION PENDING]` markers are expected

**Present to user:**
```
ADR-[NUMBER]: [Title]
Status: [Proposed/Accepted]
Options analyzed: [N]
Uncertainty markers: [N]

Ready to create? Or would you like to adjust anything?
```

### 10. Create ADR

Use provider:
```
Skill(skill="[provider-name]", args="create_spec location_id=\"[LOCATION]\" title=\"ADR-[NUMBER]: [Title]\" body=\"[FULL_ADR]\"")
```

### 11. Provide Summary & Next Steps

```
✅ ADR created: ADR-[NUMBER]: [Title] - [URL]

Status: [Proposed/Accepted]
Decision: [Chosen option summary]
Options analyzed: [N]
Uncertainty markers: [N]

Next: Use /d3:refine-spec to incorporate this decision
into relevant specifications' "Architectural Context > Relevant ADRs" section.
```

---

## Error Handling

| Issue | Action |
|-------|--------|
| No provider configured | Guide user to add ADR Provider or Spec Provider to CLAUDE.md |
| No decision found in input | Ask clarifying questions to identify the decision |
| Minimal context | Warn ADR will be sparse, confirm before creating |
| Conflicting information | Mark `[DECISION PENDING]` with conflicting options listed |
| Old ADR not found for superseding | Warn, create new ADR without cross-reference |
| Creation fails | Provide full ADR text for manual creation |
| Location not found | List available locations |

---

## Key Principles

1. **MADR v4 format** — Follow the standard for interoperability and familiarity
2. **Immutable records** — Don't edit ADRs, supersede them
3. **Decision Drivers + Outcome** — Separate the forces from the decision
4. **"Good/Bad/Neutral, because..."** — Structured pros/cons format for every option
5. **Confirmation** — Document how to verify the decision was implemented
6. **Feed into specs** — ADRs connect to specifications via refinement
7. **Transcript-first** — Meeting discussions are the primary input
8. **Uncertainty is explicit** — Proposed decisions use `[DECISION PENDING]` markers
