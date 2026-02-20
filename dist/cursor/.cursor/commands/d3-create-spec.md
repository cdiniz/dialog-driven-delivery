## Core Principle

**Fill only what you know. Empty sections are better than hallucinated content.**

Create a specification with BOTH Product and Technical sections. In `combined` mode (default), creates a single unified document. In `separated` mode, creates two linked documents — one for product, one for technical. Specs grow progressively through refinement.

---

## Workflow

### 1. Detect Provider, Templates, and Spec Mode
- Read `d3.config.md` for D3 config
- Search for ### D3 Config  ### Templates
- Read `Spec Mode` from Spec Provider configuration (default: `combined` when absent)
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

**If Spec Mode is `combined` (default):**

Invoke the [provider-name] skill (see platform reference for invocation syntax):
```
create_spec location_id="[LOCATION]" title="[Title]" body="[FULL_SPEC]"
```

**If Spec Mode is `separated`:**

Split the generated specification into two documents:

1. **Product Spec** — contains only the Product Specification sections from the product template
2. **Tech Spec** — contains only the Technical Specification sections from the tech template

Add a cross-reference header to each document linking to its companion:
```markdown
**Companion Spec:** [companion title] - [companion path/URL]
```

Invoke the [provider-name] skill twice:
```
create_spec location_id="[LOCATION]" title="[Title] - Product Spec" body="[PRODUCT_SPEC]"
create_spec location_id="[LOCATION]" title="[Title] - Tech Spec" body="[TECH_SPEC]"
```

The companion spec path is determined by the provider's response — update the first spec's cross-reference header after both are created if needed.

### 8. Provide Summary

**If Spec Mode is `combined`:**
```
✅ Specification created: [Title] - [URL]

Coverage:
- Product Spec: [40-70% typical]
- Technical Spec: [10-30% typical]
- Uncertainties: [N] markers

Next: Review → /d3:refine-spec → /d3:decompose
```

**If Spec Mode is `separated`:**
```
✅ Specification created:
- Product Spec: [Title] - Product Spec - [URL]
- Tech Spec: [Title] - Tech Spec - [URL]

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
