---
description: Refine existing feature specifications based on new information (meeting transcripts, technical decisions, feedback, or discussions). Automatically detects whether changes are product-focused, technical, or both. Updates only affected sections while preserving existing content. Use when updating specs, adding details to existing documentation, incorporating meeting notes into specs, or when user mentions refining/updating/improving an existing specification.
alwaysApply: false
---
## Core Principle

**Update only what has new information. Preserve everything else.**

Automatically detect which sections need updating - Product, Technical, or both. Don't fill empty sections just because they exist.

---

## Workflow

### 1. Detect Provider and Templates
- Read .cursor/rules/d3-config/RULE.md for D3 config
- Search for ### D3 Config  ### Templates
- If templates (tech and product spec templates) are not configure use skill d3-templates 
- Store for later steps

### 2. Fetch Specification
Command accepts spec identifier, URL, or title in `$ARGUMENTS`.

Use provider's `get_spec`:
- Identifier → Use directly
- URL → Extract identifier
- Title → Search, then get_spec

### 3. Analyze Current State
Display coverage:
```
**Specification:** [Title] - [URL]
**Last Modified:** [Date]

Current Coverage:
- Product: ~[X]% ([sections with content])
- Technical: ~[Y]% ([sections with content])
- Open Questions: [Z] product, [W] technical
```

### 4. Request Refinement Input
Ask user:
```
How would you like to provide new information?
A) Paste meeting transcript
B) Paste updated documentation
C) Describe changes
D) Paste review feedback
```

### 5. Analyze New Information

**Smart Detection:**
- Identify what's new vs. what exists
- Determine which sections are affected
- Detect if Product, Technical, or both need updates

**CRITICAL - Non-Greedy Updates:**

Update ONLY sections explicitly addressed in new input.

**DO NOT:**
- Invent details not discussed (endpoints, schemas, architectures)
- Elaborate beyond what was stated
- Fill empty sections just because they're empty
- Remove `_To be defined_` without replacement content
- Treat template examples as prompts to fill

**DO:**
- Add only explicitly stated information
- Replace placeholders when discussed
- Add uncertainty markers for ambiguous info
- Preserve empty sections if not discussed

**Section-by-Section Process:**
1. Does new information explicitly address this section?
2. YES → Update with actual content
3. NO → Leave unchanged (existing content OR placeholder)

### 6. Show Proposed Changes

Present clear before/after:
```
Proposed Changes:

## 📋 Product Specification Changes

### [Section Name]
BEFORE: [Current content]
AFTER: [Proposed content]
Rationale: [Why]
Type: [Addition/Modification/Clarification/Resolution]

## 🔧 Technical Specification Changes

### [Section Name]
[Same pattern]

---
Summary:
- Product: [X sections updated, Y questions resolved]
- Technical: [X sections updated, Y questions resolved]
- Resolved: [List]
- New uncertainties: [List]

Does this look correct?
```

### 7. Validate Changes

**Validation checklist:**
- [ ] All changes have clear rationale
- [ ] Before/after shows enough context
- [ ] Uncertainty markers properly updated
- [ ] No hallucination - only documented changes
- [ ] Both specs remain internally consistent
- [ ] Updates maintain template structure

**Uncertainty handling:**
- Resolved → Remove markers and section entries
- New → Add markers and section entries

### 8. Apply Updates

Use provider:
```
@[provider-name] update_spec page_id=\"[spec-id]\" body=\"[UPDATED_SPEC]\" version_message=\"[description]\"
```

### 9. Provide Summary

```
✅ Specification refined!

**Specification:** [Title] - [URL]

What Was Updated:
- Product: [Status per section]
- Technical: [Status per section]
- Resolved questions: [X]
- New questions: [Y]

Key Changes:
1. [Change title]: [What and why]
2. [Change title]: [What and why]
[3-5 most significant]

Coverage Improvement:
- Before: Product ~[X]% | Technical ~[Y]%
- After: Product ~[X]% | Technical ~[Y]%

Remaining Gaps: [Empty sections if any]

Next: Review → /d3:refine-spec (continue) → /d3:decompose (when ready)
```

---

## Key Principles

1. **Smart detection** - Content determines which spec(s) update
2. **Preserve existing** - Only change what needs changing
3. **One input, both specs** - Product and technical info often intermixed
4. **Track resolution** - Remove resolved uncertainty markers
5. **Add new uncertainties** - New info may raise questions

**Change Types:**
- Addition: New content in empty section
- Enhancement: Adding to existing content
- Modification: Changing existing content
- Clarification: Resolving uncertainty markers
- Resolution: Answering open questions

---

## Section-by-Section Guidance

**For each section, ask:**
"Does the new information explicitly discuss this?"

**Examples:**

New input mentions "user can filter by date":
- ✅ Update: User Journey, Requirements
- ❌ Don't touch: API Contracts, Data Models (not discussed)

New input mentions "use PostgreSQL for storage":
- ✅ Update: Technical Approach, Data Models
- ❌ Don't touch: User Journey, Requirements (not discussed)

New input has both product and technical details:
- ✅ Update: Both specs (whatever was discussed)
- ❌ Don't invent: Missing technical details for product discussion

---

## Expected Outcomes

**Progressive refinement:**
Each session adds only what was discussed. Empty sections remain empty until explicitly addressed.

**Typical refinement:**
- Input about product features → Product spec grows
- Input about technical decisions → Technical spec grows
- Mixed input → Both specs grow

This is CORRECT. Don't try to "complete" sections by guessing.

---

## Error Handling

| Issue | Action |
|-------|--------|
| No changes detected | Inform user, ask for clarification |
| Conflicting info | Show conflict, ask how to resolve |
| Ambiguous updates | Ask which section to update |
| Major scope change | Warn about impact, confirm |
| Update fails | Provide full updated text for manual update |
| Spec not found | Verify identifier/URL, suggest search |
