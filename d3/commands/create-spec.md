---
description: Create comprehensive feature specification from any input context (meeting transcripts, documents, or conversational discussion). Creates a unified specification containing both Product and Technical specifications. Use when starting a new feature, documenting a planning meeting, or when user asks to create/write a spec, specification, or feature documentation. Fills only known information and marks uncertainties.
---
## Core Principle

**Fill only what you know. Empty sections are better than hallucinated content.**

Create a single unified spec with BOTH Product and Technical sections. Specs grow progressively through refinement.

---

## Workflow

### 1. Detect Provider and Templates
- Read CLAUDE.md for D3 config
- Search for ### D3 Config  ### Templates
- If templates (tech and product spec templates) are not configure use skill d3-templates 
- Store for later steps

### 2. Get Input Context
Ask user:
```
How would you like to provide the feature information?
A) Paste meeting transcript
B) Paste existing document
C) Describe conversationally
```

### 3. Get Location
Ask where to create spec. If needed, use provider's `list_locations`.

### 4. Analyze & Propose Title
Extract from context:
- Product: Users, workflows, requirements, business value
- Technical: Architecture, APIs, data models, integrations
- Uncertainties: Questions, decisions, assumptions

Propose title, wait for confirmation.

### 5. Generate Specification

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

### 6. Validate Before Creation

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

**Present to user:**
```
Specification ready with [N] uncertainty markers:
- Open Questions: [X]
- Clarifications: [Y]
- Assumptions: [Z]

Resolve now, leave marked, or review first?
```

### 7. Create Specification

Use provider:
```
Skill(skill="[provider-name]", args="create_spec location_id=\"[LOCATION]\" title=\"[Title]\" body=\"[FULL_SPEC]\"")
```

### 8. Provide Summary

```
✅ Specification created: [Title] - [URL]

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
| Location not found | List available locations |
