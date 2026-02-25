## Core Principle

**Fill only what you know. Empty sections are better than hallucinated content.**

Create a specification with BOTH Product and Technical sections. When a single `### Spec Provider` is configured, creates a single unified document. When `### Product Spec Provider` and `### Tech Spec Provider` are both configured, creates two separate documents — one for product, one for technical — using their respective providers. Specs grow progressively through refinement.

---

## Workflow

### 1. Detect Providers, Templates, and Settings
Read and execute `d3/shared/detect-config.md`.
If spec templates (tech and product spec) are not configured, use skill `d3-templates`.

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

### 3. Get Location

**If quiet mode:** Use Default Location from provider configuration in `d3.config.md`. If no default is configured, use the provider's root location (`.`).

**Otherwise:**
Ask where to create spec. If needed, use provider's `list_locations`.

### 4. Analyze & Propose Title
Extract from context:
- Product: Users, workflows, requirements, business value
- Technical: Architecture, APIs, data models, integrations
- Uncertainties: Questions, decisions, assumptions

**If quiet mode:** Propose title and accept it immediately.

**Otherwise:** Propose title, wait for confirmation.

### 5. Generate Specification

**CRITICAL RULES:**

1. **Create FULL structure — NEVER omit a section:**
   - ALL section headings from both templates MUST appear in the output
   - BOTH Product and Technical sections, every heading, every time
   - A section with placeholder text is correct. A missing section is ALWAYS wrong.
   - Adding something to Open Questions does NOT replace the section heading + placeholder

2. **Fill ONLY what was discussed:**
   - Discussed → Real content
   - NOT discussed → `_To be defined - not yet discussed_`
   - Template examples (like `POST /api/path`) are structure guides, NOT content

   **Example of a correctly handled undiscussed section:**
   ```
   ## User Journey
   _To be defined - not yet discussed_
   ```

3. **NEVER invent:**
   - Endpoints, schemas, architectures, error codes, technology choices
   - When in doubt: placeholder, not guess

4. **Mark uncertainties with inline markers (separate from placeholder text):**
   - `[OPEN QUESTION: ...]` - Something discussed but not resolved
   - `[CLARIFICATION NEEDED: ...]` - Vague requirement that was raised
   - `[ASSUMPTION: ...]` - Reasonable inference you are making
   - `[DECISION PENDING: ...]` - Multiple approaches in play
   - These markers go in sections that HAVE content — not as a substitute for placeholder text in empty sections

Invoke uncertainty-markers skill for detailed guidance.

### 6. Validate Before Creation

**Structure validation:**
- [ ] ALL template headings present — count them against the template
- [ ] No sections skipped or merged — every heading appears individually
- [ ] Each discussed section has real content
- [ ] Each non-discussed section has `_To be defined - not yet discussed_` (not just an Open Questions entry)
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

### 7. Create Specification

Follow provider dispatch conventions (`d3/shared/provider-dispatch.md`):

**If combined mode:**
```
create_spec location_id="[LOCATION]" title="[Title]" body="[FULL_SPEC]"
```

**If separated mode** — split into product sections and technical sections, then:
```
[product-spec-provider] create_spec location_id="[LOCATION]" title="[Title] - Product Spec" body="[PRODUCT_SPEC]"
[tech-spec-provider] create_spec location_id="[LOCATION]" title="[Title] - Tech Spec" body="[TECH_SPEC]"
```

### 8. Provide Summary

**If combined mode:**
```
✅ Specification created: [Title] - [URL]

Coverage:
- Product Spec: [40-70% typical]
- Technical Spec: [10-30% typical]
- Uncertainties: [N] markers

Next: Review → /d3:refine-spec → /d3:decompose
```

**If separated mode:**
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
