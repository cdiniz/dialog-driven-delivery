---
name: create-spec
description: Create comprehensive feature specification from any input context (meeting transcripts, documents, or conversational discussion). Creates a unified specification containing both Product and Technical specifications. Use when starting a new feature, documenting a planning meeting, or when user asks to create/write a spec, specification, or feature documentation. Fills only known information and marks uncertainties explicitly.
---

## Philosophy

Create a **single specification** containing BOTH Product and Technical specs. Fill only what you know from context - empty sections are better than hallucinated content. Specs grow progressively through `/refine-spec`.

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
- [ ] Step 7: Create specification in provider
- [ ] Step 8: Provide summary
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

Before filling templates, explicitly identify:

1. **What WAS discussed:**
   - List specific topics mentioned in transcript
   - Note which template sections these map to

2. **What was NOT discussed:**
   - List template sections with no corresponding information
   - These will use `_To be defined - not yet discussed_` placeholder

**Example analysis:**
```markdown
Discussed:
- Business goal/value proposition → Overview section
- User actions/workflows → Requirements section
- Success metrics → Success Metrics section

NOT discussed:
- API endpoints → API Contracts section (use placeholder)
- Architecture → Architecture section (use placeholder)
- Data schemas → Data Models section (use placeholder)
- Error handling → Error Handling section (use placeholder)
```

**Section-by-Section Filling Process:**

For EACH section in the templates:

1. **Ask:** "Was this specific topic explicitly discussed in the transcript?"
2. **If YES:** Fill with actual content from transcript
3. **If NO:** Use `_To be defined - not yet discussed_` for the ENTIRE section

**CRITICAL - Template Placeholders Are NOT Content:**

Templates show EXAMPLES like `[New API endpoint]` or `POST /api/path` or architecture diagrams.

**These are STRUCTURE GUIDES showing what COULD go there, NOT content to fill in.**

❌ **WRONG:** See `[New API endpoint]` → invent endpoint name
✅ **CORRECT:** See `[New API endpoint]` → if not discussed, replace ENTIRE section with `_To be defined - not yet discussed_`

**If a section wasn't discussed:**
```markdown
## API Contracts
_To be defined - not yet discussed_

## Architecture
_To be defined - not yet discussed_

## Data Models
_To be defined - not yet discussed_
```

**Load Templates:**

1. Use template paths from provider detection (Step 0):
   - `feature_spec_template` (default: `d3/templates/feature-spec.md`)
   - `technical_spec_template` (default: `d3/templates/technical-spec.md`)
2. Use Read tool to load template content from these paths
3. Use template structure to organize spec content

**Structure:**
```markdown
# Feature: [Feature Name]

## 📋 Product Specification
[Use feature-spec.md structure - fill only available information]

---

## 🔧 Technical Specification
[Use technical-spec.md structure - fill only available information]
```

**Filling Guidelines:**

1. **Map extracted information** to appropriate template sections
2. **Fill ONLY what you know** - don't invent content
3. **Use explicit placeholders** for empty sections: `_To be defined - not yet discussed_`
4. **Preserve template section numbering**

**CRITICAL - What NOT to Fill In:**

❌ **DO NOT invent technical details that weren't discussed:**
- API endpoint names (e.g., `/api/resource/{id}/action`)
- Architecture diagrams or component names
- Database schemas or table structures
- Technology choices (unless explicitly mentioned)
- Specific error codes or status codes
- Authentication/authorization details
- Deployment strategies
- Performance metrics or SLAs

❌ **DO NOT elaborate beyond what was said:**
- If transcript says "display items", don't specify carousel, grid, list, or card layout
- If transcript says "track actions", don't invent analytics event schemas
- If transcript says "filter by type", don't define the taxonomy or filtering logic

✅ **DO fill in ONLY what was explicitly discussed:**
- Business goals mentioned in transcript
- User workflows described
- Requirements stated by stakeholders
- Metrics or success criteria defined
- Constraints or edge cases discussed

**Example from typical product-focused transcript:**

✅ **Correct filling:**
```markdown
## Requirements
- [Specific requirements mentioned in transcript]
- [User actions described]
- [Business rules stated]

## Success Metrics
- [Metrics explicitly mentioned]

## API Contracts
_To be defined - not yet discussed_

## Architecture
_To be defined - not yet discussed_

## Data Models
_To be defined - not yet discussed_
```

❌ **Incorrect filling (hallucination):**
```markdown
## API Contracts
GET /api/resource/{id}/action
Response: { data: Object[] }
[Invented endpoint structure]

## Architecture
[Detailed diagram with invented components]

## Data Models
[Invented schema and table structure]
```

**Uncertainty Markers:**

For detailed guidance, see `uncertainty-markers` skill or invoke it when needed.

**Rules:**
- If user didn't answer → `[OPEN QUESTION: specific question]`
- If vague requirement → `[CLARIFICATION NEEDED: what needs defining]`
- If reasonable inference → `[ASSUMPTION: statement]`
- If multiple approaches → `[DECISION PENDING: option A vs B]`
- **Never make silent assumptions**
- **When in doubt, use `_To be defined - not yet discussed_` instead of guessing**
- Link all markers to Section 4 (Open Questions & Assumptions)

---

### Step 6: Validate Uncertainty Markers

**CRITICAL - Run before creation:**

```
Uncertainty Validation Checklist:
- [ ] Count all markers: [OPEN QUESTION], [ASSUMPTION], [CLARIFICATION NEEDED], [DECISION PENDING]
- [ ] Verify each marker has entry in Section 4
- [ ] If validation fails: Add missing entries and re-validate
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

**If Option A:** Ask questions for each marker, update spec, remove resolved markers.

**Quality Gates:**
- ⚠️ Warning if >10 `[OPEN QUESTION]` markers (spec may be too incomplete)
- ⚠️ Warning if critical requirements have `[OPEN QUESTION]` (blocks implementation)

---

### Step 7: Create Specification

Use Skill tool to invoke spec provider:

```
Skill(
  skill="[provider-name]",
  args="create_spec location_id=\"[LOCATION]\" title=\"[Title]\" body=\"[Full Spec]\" parent_id=\"[Optional]\""
)
```

Provider returns: `{id, url, title, version}`

---

### Step 8: Provide Summary

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

---

## Key Principles

### Non-Greedy Filling

**Core Philosophy:** D3 prevents AI hallucination by being radically honest about what is unknown.

1. **Empty is honest:** Better to show gaps than hallucinate
2. **Partial is fine:** Can have complete Product Spec with empty Technical Spec
3. **Progressive:** Specs grow through refinement cycles
4. **Explicit gaps:** Team knows what to discuss next
5. **Default to placeholder:** When in doubt, use `_To be defined - not yet discussed_`

**Common Pattern in Initial Specs:**

Most feature discussions focus on product/business aspects. Technical details come later.

**Typical Coverage After First Meeting:**
- Product Spec: 40-70% filled
- Technical Spec: 10-30% filled (often just high-level approach)

This is EXPECTED and CORRECT. Don't try to "complete" the technical spec by inventing details.

**Example - Typical product discussion:**

When transcript focuses on business/product aspects only:

✅ **Fill these sections:**
- Overview: Business goals, value proposition
- Requirements: User-facing features, workflows
- Success Metrics: Business metrics mentioned

❌ **Leave empty (use `_To be defined_`):**
- API Contracts (no endpoints discussed)
- Data Models (entity names mentioned but no schema)
- Architecture (no components discussed)
- Error Handling (not discussed)
- Security (not discussed)
- Performance SLAs (not discussed)

### Smart Context Detection

Don't force categorization - analyze what's present:
- **Product indicators:** User stories, personas, workflows, business value, UI/UX
- **Technical indicators:** Architecture, technologies, APIs, data models, performance

**Fill ONLY what's there - don't elaborate or invent!**

---

## Error Handling

- **Ambiguous scope:** Ask clarifying questions about purpose
- **No concrete info:** Warn spec will be mostly empty, confirm creation
- **Minimal technical discussion:** This is NORMAL - don't try to fill technical sections with invented details
- **Conflicting info:** Mark with `[DECISION PENDING]` in Open Questions
- **Creation fails:** Provide full spec text for manual creation
- **Location not found:** List available locations
- **Provider fails:** Fall back to providing spec content

**When Technical Spec is Mostly Empty:**

If technical sections are >70% empty placeholders, this is EXPECTED and CORRECT for initial specs.

Show message:
```markdown
Note: Technical specification is mostly empty - this is expected for initial specs.
Technical details are typically defined in subsequent refinement sessions.
Use `/d3:refine-spec` when technical decisions are made.
```

---

## Example

**Quick reference** (see [examples.md](references/examples.md) for detailed scenarios):

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

## Important Notes

- **Always creates both specs** in single document
- **Progressive filling:** Start with what you have
- **Honest gaps:** Empty sections clearly marked
- **Uncertainty markers:** Prevent hallucination
- **Single source of truth:** Everything in one place
- **Provider-agnostic:** Uses Markdown, works with any platform

See [templates.md](references/templates.md) for template details and [examples.md](references/examples.md) for comprehensive examples.
