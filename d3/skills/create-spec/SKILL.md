---
name: create-spec
description: Create comprehensive feature specification from any input context (meeting transcripts, documents, or conversational discussion). Creates a unified specification containing both Product and Technical specifications. Use when starting a new feature, documenting a planning meeting, or when user asks to create/write a spec, specification, or feature documentation. Fills only known information and marks uncertainties 
---

## Philosophy

Create a **single specification** containing BOTH Product and Technical specs. Fill only what you know from context - empty sections are better than hallucinated content. Specs grow progressively through refinenement.

---

## Workflow Checklist

Copy this and track progress:

```
Specification Creation Progress:
- [ ] Step 1: Detect provider configuration
- [ ] Step 2: Request and analyze input context
- [ ] Step 3: Get specification location
- [ ] Step 4: Propose specification title
- [ ] Step 5: Generate specification content
- [ ] Step 6: Validate uncertainty markers
- [ ] Step 7: Validate content and template
- [ ] Step 8: Create specification in provider
- [ ] Step 9: Provide summary
```

---

## Steps

### Step 1: Detect Provider

Detect provider configuration from CLAUDE.md. See [provider-detection.md](../../shared/provider-detection.md) for details.

Store provider name for Steps 3 and 7.

---

### Step 2: Request Input Context

Ask user for context:

```markdown
I'll help you create a comprehensive feature specification.

How would you like to provide the feature information?

**Option A: Meeting Transcript** - Paste a transcript from any planning or design meeting
**Option B: Document** - Paste an existing document or specification
**Option C: Describe Conversationally** - We'll discuss the feature together
```

---

### Step 3: Get Specification Location

**If user needs list:** Use provider's `list_locations` operation via Skill tool.

```markdown
Where would you like to create this specification?

**Location:** [Location key or name]
**Parent (optional):** [Parent container/location if applicable]
```

---

### Step 4: Analyze Input & Propose Title

**Extract information:**
- Product aspects: Users, workflows, requirements, business value, metrics
- Technical aspects: Architecture, technologies, APIs, data models, integrations
- Uncertainties: Questions, pending decisions, assumptions

**Propose title:**

```markdown
Based on your input, I found information about [brief summary].

I propose creating a specification named: **"[Proposed Name]"**

Should I create this specification in [LOCATION]?
```

Wait for confirmation.

---

### Step 5: Generate Specification

**Pre-Filling Analysis:**

List what WAS discussed vs. what was NOT discussed:

```markdown
Discussed:
- Business goals → Overview section
- User workflows → Requirements section
- Success metrics → Metrics section

NOT discussed:
- API endpoints → API Contracts (use placeholder)
- Architecture → Architecture (use placeholder)
- Data schemas → Data Models (use placeholder)
```

**Load Templates:**

1. Use paths from Step 1:
   - `feature_spec_template` (default: `d3/templates/feature-spec.md`)
   - `technical_spec_template` (default: `d3/templates/technical-spec.md`)
2. Read template content using Read tool
3. Use template structure to organize spec content

**Filling Process:**

**CRITICAL - ALWAYS Create Full Structure:**
1. Create BOTH Product and Technical Specification sections
2. Create ALL section headings from templates (with numbering)
3. Never skip sections - use placeholders for empty content

**For EACH section:**
1. **Explicitly discussed?** → Fill with actual content from transcript
2. **Not discussed?** → Keep heading, use `_To be defined - not yet discussed_`

**CRITICAL - No Hallucination:**

Template examples like `[New API endpoint]` or `POST /api/path` are **structure guides**, NOT content to fill.

- Never invent: endpoints, schemas, architectures, error codes, technology choices
- Never elaborate beyond what was said
- When in doubt: placeholder, not guess

**For complete anti-hallucination rules and examples:** See [FILLING-GUIDE.md](FILLING-GUIDE.md)

**Uncertainty Markers:**

Use when needed:
- User didn't answer → `[OPEN QUESTION: specific question]`
- Vague requirement → `[CLARIFICATION NEEDED: what needs defining]`
- Reasonable inference → `[ASSUMPTION: statement]`
- Multiple approaches → `[DECISION PENDING: option A vs B]`

Link all markers to Open Questions & Assumptions section.

See `uncertainty-markers` skill for detailed guidance.

---

### Step 6: Validate Uncertainty Markers

**Run before creation:**

```
Uncertainty Validation Checklist:
- [ ] Count all markers: [OPEN QUESTION], [ASSUMPTION], [CLARIFICATION NEEDED], [DECISION PENDING]
- [ ] Verify each marker has entry in Open Questions & Assumptions section
- [ ] Only proceed when all markers are tracked
```

**Present to user:**

```markdown
I've generated the specification with [N] uncertainty markers:

**Open Questions:** [X] items requiring decisions
**Clarifications:** [Y] items needing specifics
**Assumptions:** [Z] items inferred from context

Would you like to:
**Option A:** Resolve them now - I'll ask follow-up questions
**Option B:** Leave them marked for later
**Option C:** Review the spec first, then resolve
```

**Quality Gates:**
- ⚠️ Warning if >10 `[OPEN QUESTION]` markers (spec may be too incomplete)
- ⚠️ Warning if critical requirements have `[OPEN QUESTION]` (blocks implementation)

---

### Step 7: Validate content and template

Use a subtask to review the specification against the following checklist:
- [ ] ALL Headers from the spec templates are present
- [ ] Verify if each section was discussed, if it was not, make sure it's `_To be defined - not yet discussed_`
- [ ] Only proceed when all sections are or verified


### Step 8: Create Specification

Use Skill tool to invoke spec provider:

```
Skill(
  skill="[provider-name]",
  args="create_spec location_id=\"[LOCATION]\" title=\"[Title]\" body=\"[Full Spec]\" parent_id=\"[Optional]\""
)
```

Provider returns: `{id, url, title, version}`

---

### Step 9: Provide Summary

```markdown
✅ Feature specification created successfully!

**Specification:** [Title] - [URL]
**Location:** [LOCATION]

## Coverage Summary

**📋 Product Specification:**
- Overview: [Filled/Partial/Empty]
- User Journey: [X workflows / Empty]
- Requirements: [Y requirements / Empty]
- Open Questions: [Z unresolved]

**🔧 Technical Specification:**
- Technical Approach: [Filled/Partial/Empty]
- Architecture: [X diagrams / Empty]
- API Contracts: [Y endpoints / Empty]
- Data Models: [Z models / Empty]
- Open Questions: [W unresolved]

## Uncertainties

**Total markers:** [N]
- Product questions: [X]
- Technical questions: [Y]
- Assumptions to validate: [Z]

## Next Steps

1. Review: [URL]
2. [If gaps] Schedule discussions for missing sections
3. Use `/d3:refine-spec [spec-identifier]` to add information
4. Once complete, use `/d3:decompose [spec-identifier]` for user stories
```

**When Technical Spec is Mostly Empty:**

If technical sections are >70% empty placeholders, show this message:

```markdown
Note: Technical specification is mostly empty - this is expected for initial specs.
Technical details are typically defined in subsequent refinement sessions.
Use `/d3:refine-spec` when technical decisions are made.
```

---

## Key Principles

### Non-Greedy Filling

D3 prevents AI hallucination by being radically honest about what is unknown:

1. **Empty is honest** - Better to show gaps than hallucinate
2. **Structure always present** - Create ALL section headings, even with placeholder content
3. **Partial is fine** - Can have complete Product Spec with mostly-placeholder Technical Spec
4. **Progressive** - Specs grow through refinement cycles
5. **Default to placeholder** - When in doubt, use `_To be defined - not yet discussed_`

**Typical coverage after initial meeting:**
- Product Spec: 40-70% filled
- Technical Spec: 10-30% filled

This is EXPECTED and CORRECT. Don't try to "complete" the technical spec by inventing details.

---

## Error Handling

- **Ambiguous scope:** Ask clarifying questions about purpose
- **No concrete info:** Warn spec will be mostly empty, confirm creation
- **Minimal technical discussion:** Normal - don't fill technical sections with invented details
- **Conflicting info:** Mark with `[DECISION PENDING]` in Open Questions
- **Creation fails:** Provide full spec text for manual creation
- **Location not found:** List available locations
- **Provider fails:** Fall back to providing spec content

---

## Example

```
User: /d3:create-spec

Agent: How would you like to provide the feature information?

User: Option A [pastes transcript]

Agent: Where should I create this?

User: PROJ

Agent: I propose: "Advanced Search with Filters". Create it?

User: Yes

Agent: ✅ Created! Product Spec: 70% filled, Technical: 30% filled
       5 open questions remain. Use /d3:refine-spec to continue.
```

---

## Resources

**Detailed guidance:**
- [FILLING-GUIDE.md](FILLING-GUIDE.md) - Complete anti-hallucination rules and examples
- [examples.md](references/examples.md) - Full workflow examples
- [templates.md](references/templates.md) - Template structure details

**Related skills:**
- `uncertainty-markers` - Standards for marking unknowns
- `refine-spec` - Update existing specifications
- `decompose` - Break specs into user stories
