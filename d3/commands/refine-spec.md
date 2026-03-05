---
description: Refine existing feature specifications based on new information (meeting transcripts, technical decisions, feedback, or discussions). Automatically detects whether changes are product-focused, technical, or both. Updates only affected sections while preserving existing content. When stories already exist for the spec, analyzes impact and proposes story updates. Use when updating specs, adding details to existing documentation, incorporating meeting notes into specs, or when user mentions refining/updating/improving an existing specification.
---

## Core Principle

**Update only what has new information. Preserve everything else.**

Automatically detect which sections need updating - Product, Technical, or both. Don't fill empty sections just because they exist.

**When stories exist:** Spec changes cascade to affected stories. Update story acceptance criteria, scope, and descriptions to stay in sync.

---

## Workflow

### 1. Load Configuration and Templates
- Read `d3.config.md`
- From the Storage table, find the rows matching "Specs" and "Stories"
- Read Quiet Mode from Settings
- Load templates from d3-templates skill (or custom paths if configured in Templates section)

### 2. Fetch Specification
Command accepts spec identifier, path, or title in `$ARGUMENTS`.

Read the spec from the Storage location for "Specs":
- Path → Read directly
- Title → Search in the Specs location, then read

### 3. Detect Existing Stories
Search the Storage location for "Stories" for stories matching the spec title.
- Store list for later impact analysis
- If no stories found, skip story impact steps later

### 4. Analyze Current State
Display coverage:
```
**Specification:** [Title] - [path]

Current Coverage:
- Product: ~[X]% ([sections with content])
- Technical: ~[Y]% ([sections with content])
- Open Questions: [Z] product, [W] technical

Linked Stories: [None / N stories found]
```

### 5. Request Refinement Input

**If quiet mode and new content provided in `$ARGUMENTS`:** Use the provided text directly as refinement input. Skip the question below.

**Otherwise:**
Ask user:
```
How would you like to provide new information?
A) Paste meeting transcript
B) Paste updated documentation
C) Describe changes
D) Paste review feedback
```

### 6. Analyze New Information

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

### 7. Show Proposed Changes

Present clear before/after:
```
Proposed Changes:

## Product Specification Changes

### [Section Name]
BEFORE: [Current content]
AFTER: [Proposed content]
Rationale: [Why]
Type: [Addition/Modification/Clarification/Resolution]

## Technical Specification Changes

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

**If quiet mode:** Skip presenting proposed changes. Accept all changes and proceed.

### 8. Analyze Story Impact (if stories exist)

**Skip this step if no stories were found in Step 3.**

For each spec change, determine if it affects existing stories:

**Impact Categories:**
- **AC Change:** Spec change modifies requirements covered by a story's acceptance criteria
- **Scope Change:** Spec change adds/removes functionality within a story's scope
- **New Story Needed:** Spec change introduces a new workflow not covered by any existing story
- **Story Obsolete:** Spec change removes functionality that was a story's primary purpose
- **No Impact:** Spec change is informational or affects sections not tied to any story

**Process:**
1. Read each existing story's description and acceptance criteria
2. Map spec changes to affected stories
3. For each affected story, determine the specific impact
4. Identify if new stories are needed for new workflows

**Present story impact:**
```
## Story Impact Analysis

### Affected Stories:

[STORY-KEY]: [Story Title]
- Impact: [AC Change / Scope Change]
- Reason: [Which spec change triggers this]
- Proposed Update: [What changes in the story]

### New Stories Needed:
- [Workflow description] - [Why existing stories don't cover it]

### Stories Potentially Obsolete:
- [STORY-KEY]: [Why this may no longer be needed]

### Unaffected Stories: [X stories unchanged]

Proceed with spec + story updates?
```

**If quiet mode:** Skip presenting story impact. Proceed with all updates.

### 9. Validate Changes

**Validation checklist:**
- [ ] All changes have clear rationale
- [ ] Before/after shows enough context
- [ ] Uncertainty markers properly updated
- [ ] No hallucination - only documented changes
- [ ] Spec remains internally consistent
- [ ] Updates maintain template structure
- [ ] Story updates match spec changes (no drift)
- [ ] New stories follow INVEST principles
- [ ] No story updated without a corresponding spec change

**Uncertainty handling:**
- Resolved → Remove markers and section entries
- New → Add markers and section entries

### 10. Apply Updates

Follow the Instructions column from the Storage table for "Specs".
Write the updated spec to the Location specified.

**Apply story updates (if stories are affected):**

Follow the Instructions column from the Storage table for "Stories".
Update affected stories at the Location specified.

For new stories needed, create them at the Stories location following the Instructions.

For obsolete stories (after user confirmation):
- Add a note explaining why the story is no longer needed
- Do NOT delete — let the user decide the final disposition

### 11. Provide Summary

```
Specification refined!

**Specification:** [Title] - [path]

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

Story Updates:
- Updated: [N stories]
- Created: [N new stories]
- Flagged obsolete: [N stories]
- Unchanged: [N stories]

Remaining Gaps: [Empty sections if any]

Next: Review → /d3:refine-spec (continue) → /d3:decompose (when ready)
```

---

## Key Principles

1. **Smart detection** - Content determines which sections and stories update
2. **Preserve existing** - Only change what needs changing
3. **Track resolution** - Remove resolved uncertainty markers
4. **Add new uncertainties** - New info may raise questions
5. **Spec-story sync** - Stories must reflect the current spec, not a stale version
6. **Minimal story churn** - Only update stories directly affected by spec changes

**Spec Change Types:**
- Addition: New content in empty section
- Enhancement: Adding to existing content
- Modification: Changing existing content
- Clarification: Resolving uncertainty markers
- Resolution: Answering open questions

**Story Impact Types:**
- AC Update: Acceptance criteria changed due to spec change
- Scope Change: Story gains or loses functionality
- New Story: New workflow requires a new story
- Obsolete: Story's purpose removed from spec
- No Impact: Spec change doesn't affect story

---

## Section-by-Section Guidance

**For each section, ask:**
"Does the new information explicitly discuss this?"

**Examples:**

New input mentions "user can filter by date":
- Update spec: User Journey, Requirements
- Update stories: Stories covering search/listing workflows → add filter AC
- Don't touch: API Contracts, Data Models (not discussed)

New input mentions "use PostgreSQL for storage":
- Update spec: Technical Approach, Data Models
- Update stories: Stories with technical notes referencing data layer
- Don't touch: User Journey, Requirements (not discussed)

New input removes a feature ("we decided not to support bulk export"):
- Update spec: Remove from Requirements, User Journey
- Flag story: Story covering bulk export → mark as potentially obsolete
- Don't auto-close: Let user decide

New input adds a new workflow ("we also need an admin approval step"):
- Update spec: Add to User Journey, Requirements
- New story needed: Admin approval workflow not covered by existing stories

---

## Expected Outcomes

**Progressive refinement:**
Each session adds only what was discussed. Empty sections remain empty until explicitly addressed.

**Typical refinement:**
- Input about product features → Product spec grows
- Input about technical decisions → Technical spec grows
- Mixed input → Both parts grow

This is CORRECT. Don't try to "complete" sections by guessing.

---

## Error Handling

| Issue | Action |
|-------|--------|
| No changes detected | Inform user, ask for clarification |
| Conflicting info | Show conflict, ask how to resolve |
| Ambiguous updates | Ask which section to update |
| Major scope change | Warn about impact on spec and stories, confirm |
| Spec update fails | Provide full updated text for manual update |
| Story update fails | Provide updated story content for manual update |
| Spec not found | Verify identifier/path, suggest search |
| Stories not found | Skip story impact analysis, proceed with spec-only refinement |
