---
description: Create a D3 artifact from any input context (meeting transcripts, documents, or conversational discussion). Detects artifact type from the Storage table in d3.config.md or asks the user. Fills only known information and marks uncertainties. Use when creating any new artifact.
---

## Core Principle

**Fill only what you know. Empty sections are better than hallucinated content.**

Create artifacts using the appropriate template. Artifacts grow progressively through refinement.

---

## Workflow

### 1. Load Configuration
- Read `d3.config.md`
- Read Quiet Mode from Settings

### 2. Determine Artifact Type

Read the Storage table from `d3.config.md`. Each row in the Artifact column is a supported artifact type.

**If the artifact type is clear from `$ARGUMENTS` or context:** Match it to a Storage table row and skip the question below.

**Otherwise:** Present the available artifact types from the Storage table and ask the user to pick one.

Once determined, load the template from the matching row's Template column. Use the row's Location and Instructions for storage.

### 3. Get Input Context

**If quiet mode and input text provided in `$ARGUMENTS`:** Use the provided text directly as input context. Skip the question below.

**Otherwise:**
Ask user:
```
How would you like to provide the information?
A) Paste meeting transcript
B) Paste existing document
C) Describe conversationally
```

### 4. Analyze Input & Propose Title

Extract relevant information from the input, guided by the sections defined in the matching template.

**If quiet mode:** Propose title and accept it immediately.

**Otherwise:** Propose title, wait for confirmation.

### 5. Generate Artifact

Generate the artifact following the matching template structure.

**CRITICAL RULES:**

1. **Create FULL structure** — ALL section headings from the template. Never skip sections.
2. **Fill ONLY what was discussed** — Discussed → real content. NOT discussed → `_To be defined - not yet discussed_`
3. **NEVER invent** — Template examples are structure guides, NOT content. When in doubt: placeholder, not guess.
4. **Mark uncertainties** — Invoke the uncertainty-markers skill for detailed guidance.

### 6. Validate Before Creation

**Validation checklist:**
- [ ] ALL template headings present
- [ ] No sections skipped
- [ ] Each discussed section has real content
- [ ] Each non-discussed section has placeholder text
- [ ] No template examples treated as real content
- [ ] Uncertainty markers tracked in Open Questions section (if template has one)

**If quiet mode:** Skip presenting to user. Proceed to creation.

**Otherwise:** Present a summary of the generated artifact (key stats, uncertainty count) and ask for confirmation before creating.

### 7. Create Artifact

Follow the Instructions column from the Storage table for the matching artifact type.
Write the artifact to the Location specified.

### 8. Provide Summary

Report what was created: title, path, coverage stats relevant to the artifact type, uncertainty marker count, and suggest next steps appropriate to the artifact type (e.g. `/d3:refine` to iterate).

---

## Error Handling

| Issue | Action |
|-------|--------|
| Ambiguous scope | Ask clarifying questions |
| Minimal concrete info | Warn artifact will be mostly empty, confirm |
| Conflicting info | Mark `[DECISION PENDING]` |
| Creation fails | Provide full artifact text for manual creation |
