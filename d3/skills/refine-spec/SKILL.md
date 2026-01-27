---
name: refine-spec
description: Refine existing feature specifications based on new information (meeting transcripts, technical decisions, feedback, or discussions). Automatically detects whether changes are product-focused, technical, or both. Updates only affected sections while preserving existing content. Use when updating specs, adding details to existing documentation, incorporating meeting notes into specs, or when user mentions refining/updating/improving an existing specification.
---

## Philosophy

Update ANY part of existing specifications based on new input. Automatically detect which sections need updating - Product, Technical, or both. **Update only what has new information, preserve everything else.**

---

## Workflow Checklist

Copy this and track progress:

```
Specification Refinement Progress:
- [ ] Step 1: Detect provider configuration
- [ ] Step 2: Fetch current specification
- [ ] Step 3: Analyze current coverage
- [ ] Step 4: Request refinement input
- [ ] Step 5: Analyze new information
- [ ] Step 6: Show proposed changes
- [ ] Step 7: Validate changes
- [ ] Step 8: Apply updates
- [ ] Step 9: Provide summary
```

---

## Steps

### Step 1: Detect Provider

Detect provider configuration from CLAUDE.md. See [provider-detection.md](../../shared/provider-detection.md) for details.

Store provider name for Steps 2 and 8.

---

### Step 2: Fetch Specification

Command accepts Page ID, URL, or title in `$ARGUMENTS`.

**Use provider's `get_spec` operation:**
- If Page ID: Use directly
- If URL: Extract Page ID from URL
- If title: Search via `search_specs`, then use `get_spec`

---

### Step 3: Analyze Current State

Display current spec coverage:

```markdown
I found Specification: [Page Title]

**Specification:** [Title]
**URL:** [URL]
**Location:** [Location]
**Last Modified:** [Date]

## Current Coverage

**📋 Product Specification:**
- Overview: [Complete/Partial/Empty - brief summary]
- User Journey: [X workflows / Empty]
- Requirements: [Y requirements / Empty]
- Open Questions: [Z unresolved]

**🔧 Technical Specification:**
- Technical Approach: [Complete/Partial/Empty - brief summary]
- Architecture: [X diagrams / Empty]
- API Contracts: [Y endpoints / Empty]
- Data Models: [Z models / Empty]
- Open Questions: [W unresolved]

**Overall:** Product ~[X]% | Technical ~[Y]%
```

---

### Step 4: Request Refinement Input

```markdown
How would you like to provide new information for refinement?

**Option A: Meeting Transcript** - Paste a recent discussion transcript
**Option B: Document Update** - Paste updated documentation or decisions
**Option C: Describe Changes** - Tell me what needs updating
**Option D: Feedback/Review** - Paste review feedback or comments
```

---

### Step 5: Analyze New Information

**Smart Detection** - Don't force categorization:

Identify:
1. What's new vs what exists
2. What's changing vs what's being added
3. Which sections affected (Product, Technical, or both)

**Indicators:**
- **Product:** User stories, workflows, personas, requirements, business value, UI/UX
- **Technical:** Architecture, technologies, APIs, data models, performance, security

One input can update both specs!

---

### Step 6: Show Proposed Changes

**Present clear before/after:**

```markdown
Here are the proposed changes:

---

## 📋 Product Specification Changes

### Change 1: [Section Name]

**BEFORE:**
```
[Current content - enough for context]
```

**AFTER:**
```
[Proposed content with changes]
```

**Rationale:** [Why this change]
**Type:** [Addition/Modification/Clarification/Resolution]

---

## 🔧 Technical Specification Changes

### Change 1: [Section Name]

[Same pattern]

---

**Summary:**
- 📋 Product: [X sections updated, Y questions resolved]
- 🔧 Technical: [X sections updated, Y questions resolved]
- ✅ Resolved: [List resolved uncertainties]
- ⚠️ New: [List new uncertainties]

Does this look correct?
```

---

### Step 7: Validate Changes

**Validation Checklist:**

```
Change Validation:
- [ ] All changes have clear rationale
- [ ] Before/after shows enough context
- [ ] Uncertainty markers properly updated
- [ ] No hallucination - only documented changes
- [ ] Both specs remain internally consistent
```

If resolved uncertainties → Remove markers and section entries
If new uncertainties → Add markers and section entries

---

### Step 8: Apply Updates

Use Skill tool to invoke spec provider:

```
Skill(
  skill="[provider-name]",
  args="update_spec page_id=\"[PAGE-ID]\" body=\"[Updated Full Spec]\" version_message=\"[Brief description]\""
)
```

```markdown
Updating specification...

✅ Specification updated
✅ [X] Product sections modified
✅ [Y] Technical sections modified
✅ [Z] Questions resolved
✅ [W] New questions/uncertainties added
```

---

### Step 9: Provide Summary

```markdown
✅ Specifications refined successfully!

**Specification:** [Title] - [URL]

## What Was Updated

**📋 Product Specification:**
- Overview: [✅ No change / ✏️ Updated / ➕ Filled]
- User Journey: [Status - what changed]
- Requirements: [Status - what changed]
- Open Questions: [Resolved X, Added Y, Total: Z]

**🔧 Technical Specification:**
- Technical Approach: [Status]
- Architecture: [Status]
- API Contracts: [Status]
- Data Models: [Status]
- Open Questions: [Resolved X, Added Y, Total: Z]

## Key Changes

1. **[Change title]:** [What changed and why]
2. **[Change title]:** [What changed and why]
[List 3-5 most significant changes]

## Coverage Improvement

**Before:** Product ~[X]% | Technical ~[Y]%
**After:** Product ~[X]% | Technical ~[Y]%

## Remaining Gaps

[If sections still empty:]
**Still need to define:** [List empty sections]

[If questions remain:]
**Open questions:** [Total count] - [X] product, [Y] technical

## Next Steps

1. Review updated spec: [URL]
2. [If gaps] Schedule discussions for remaining sections
3. [If ready] Use `/d3:decompose [PAGE-ID]` to create stories
4. Continue refinement: `/d3:refine-spec [PAGE-ID]`
```

---

## Key Principles

### Smart Update Detection
1. **Don't force categorization** - Content determines which spec updates
2. **One input updates both** - Product and technical info often intermixed
3. **Preserve existing** - Only change what needs changing
4. **Track resolution** - Remove resolved uncertainty markers
5. **Add new uncertainties** - New information may raise questions

### Change Types
- **Addition:** New content in previously empty section
- **Enhancement:** Adding to existing content
- **Modification:** Changing existing content
- **Clarification:** Resolving uncertainty markers
- **Resolution:** Answering open questions

---

## Error Handling

- **No changes detected:** Inform user, ask for clarification
- **Conflicting info:** Show conflict, ask how to resolve
- **Ambiguous updates:** Ask which section to update
- **Major scope change:** Warn about impact, confirm
- **Update fails:** Provide full updated text for manual update
- **Page not found:** Verify page ID/URL, suggest search
- **Provider fails:** Fall back to providing content

---

## Example

**Quick reference** (see [examples.md](references/examples.md) for detailed scenarios):

```
User: /d3:refine-spec 123456789

Agent: Current: Product 70%, Technical 30%
       How would you like to provide new information?

User: Option A [pastes review meeting transcript]

Agent: Found updates:
       - Product: Adding 2 requirements
       - Technical: No changes
       [Shows before/after]

User: Apply changes

Agent: ✅ Updated! Product: 70% → 85%
```

---

## Important Notes

- **Smart detection:** Automatically determines which spec(s) to update
- **Preserves content:** Only modifies what needs changing
- **Progressive enhancement:** Specs grow with each refinement
- **Natural flow:** No forced structure
- **Uncertainty tracking:** Resolves old, adds new questions
- **Single source of truth:** Everything in one document
- **Version tracking:** Uses version history with messages (when supported)
- **Provider-agnostic:** Works with any platform

See [templates.md](references/templates.md) for template details and [examples.md](references/examples.md) for comprehensive examples.
