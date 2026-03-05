---
description: Create comprehensive feature specification from any input context (meeting transcripts, documents, or conversational discussion). Creates a unified specification containing both Product and Technical sections. Use when starting a new feature, documenting a planning meeting, or when user asks to create/write a spec, specification, or feature documentation. Fills only known information and marks uncertainties.
---

## Core Principle

**Fill only what you know. Empty sections are better than hallucinated content.**

Create a single unified specification with BOTH Product and Technical sections. Specs grow progressively through refinement.

---

## Workflow

### 1. Load Configuration and Templates
- Read `d3.config.md`
- From the Storage table, find the row matching "Specs"
- Read Quiet Mode from Settings
- Load templates from d3-templates skill (or custom paths if configured in Templates section)

### 2. Get Input Context

**If quiet mode and input text provided in `$ARGUMENTS`:** Use the provided text directly as input context. Skip the question below.

**Otherwise:**
Ask user:
```
How would you like to provide the feature information?
A) Paste meeting transcript
B) Paste existing document
C) Describe conversationally
```

### 3. Analyze & Propose Title
Extract from context:
- Product: Users, workflows, requirements, business value
- Technical: Architecture, APIs, data models, integrations
- Uncertainties: Questions, decisions, assumptions

**If quiet mode:** Propose title and accept it immediately.

**Otherwise:** Propose title, wait for confirmation.

### 4. Generate Specification

**CRITICAL RULES:**

1. **Create FULL structure:**
   - ALL section headings from both templates
   - BOTH Product and Technical sections
   - Never skip sections

3. **Fill ONLY what was discussed:**
   - Discussed → Real content
   - NOT discussed → `_To be defined - not yet discussed_`
   - Template examples (like `POST /api/path`) are structure guides, NOT content

4. **NEVER invent:**
   - Endpoints, schemas, architectures, error codes, technology choices
   - When in doubt: placeholder, not guess

5. **Mark uncertainties:**
   - `[OPEN QUESTION: ...]` - User didn't answer
   - `[CLARIFICATION NEEDED: ...]` - Vague requirement
   - `[ASSUMPTION: ...]` - Reasonable inference
   - `[DECISION PENDING: ...]` - Multiple approaches

Invoke uncertainty-markers skill for detailed guidance.

### 5. Validate Before Creation

**Structure validation:**
- [ ] ALL template headings present (with numbering)
- [ ] No sections skipped
- [ ] Each discussed section has real content
- [ ] Each non-discussed section has placeholder text
- [ ] No template examples treated as real content

**Uncertainty validation:**
- [ ] Count all markers: `[OPEN QUESTION]`, `[ASSUMPTION]`, `[CLARIFICATION NEEDED]`, `[DECISION PENDING]`
- [ ] Each marker has entry in Open Questions & Assumptions section
- [ ] Warn if >10 open questions or critical requirements blocked

**If quiet mode:** Skip presenting to user. Leave all markers in place and proceed to creation.

**Otherwise — present to user:**
```
Specification ready with [N] uncertainty markers:
- Open Questions: [X]
- Clarifications: [Y]
- Assumptions: [Z]

Resolve now, leave marked, or review first?
```

### 6. Create Specification

Follow the Instructions column from the Storage table for "Specs".
Write the artifact to the Location specified.

### 7. Provide Summary

```
Specification created: [Title] - [path]

Coverage:
- Product Spec: [40-70% typical]
- Technical Spec: [10-30% typical]
- Uncertainties: [N] markers

Next: Review → /d3:refine-spec → /d3:decompose
```

If Technical >70% empty: Note this is expected for initial specs.

---

## Expected Outcomes

**After initial meeting:**
- Product Spec: 40-70% filled (workflows, requirements, business goals)
- Technical Spec: 10-30% filled (architecture details come later)

This is CORRECT. Don't try to complete sections by guessing.

---

## Error Handling

| Issue | Action |
|-------|--------|
| Ambiguous scope | Ask clarifying questions |
| Minimal concrete info | Warn spec will be mostly empty, confirm |
| Minimal technical discussion | Normal - use placeholders, don't invent |
| Conflicting info | Mark `[DECISION PENDING]` |
| Creation fails | Provide full spec text for manual creation |
