---
description: Refine existing story decomposition - split, merge, add, or modify stories
---

Refine an existing feature decomposition by splitting large stories, merging small ones, adding new stories, or modifying existing stories based on team learnings and refinement discussions.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Linear Project ID as argument
2. Fetch project and display ALL existing stories
3. Ask if there's a refinement meeting transcript
4. Analyze transcript or work conversationally
5. Propose specific changes (split/merge/add/modify)
6. Confirm changes before executing
7. Execute changes in Linear
8. Provide clear summary of what changed

## Steps

### Step 1: Get Project ID from Arguments

The command accepts the Linear Project as `$ARGUMENTS`:
- Project Key (e.g., `PROJ-42`)
- Project Name (e.g., `Advanced Search`)
- Project ID (UUID)

### Step 2: Fetch and Display Current State

Query Linear for the project and display complete current state:

```markdown
I found Linear Project $ARGUMENTS:

**Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Linear Project URL]
**Status:** [Current status]
**Team:** [Team name]

**Current User Stories:** [N] stories

### Story 1: [ISSUE-XX] - [Story Title]
**Status:** [Status]
**URL:** [URL]
**Labels:** [Labels]
**Assigned to:** [Assignee or Unassigned]
**Brief:** [1-line description of what this story covers]
**Acceptance Criteria:** [N] ACs
**Dependencies:** [Lists other stories this depends on or blocks]

### Story 2: [ISSUE-YY] - [Story Title]
**Status:** [Status]
**URL:** [URL]
**Labels:** [Labels]
**Assigned to:** [Assignee or Unassigned]
**Brief:** [1-line description]
**Acceptance Criteria:** [N] ACs
**Dependencies:** [Lists dependencies]

[Continue listing ALL stories with details]

---

**Story Status Summary:**
- Backlog: [N] stories
- Todo: [N] stories
- In Progress: [N] stories
- Done: [N] stories
- Cancelled: [N] stories

[If there are In Progress or Done stories, show warning:]
⚠️ Note: [N] stories are already in progress or completed. I can still refine the decomposition, but be aware that changes may affect ongoing work.
```

### Step 3: Read Story Details

For each story, read the complete Linear issue:
- Full description with user story format
- All acceptance criteria
- Comments and discussion
- Current status and assignee
- Labels and metadata
- Links to other stories or docs

### Step 4: Request Refinement Meeting Input

Ask user if they have a refinement meeting:

```markdown
What prompted this refinement?

**Option A: Refinement meeting** - Paste your refinement meeting transcript
**Option B: Discovered during development** - Let's discuss what needs to change
**Option C: Sprint planning feedback** - Describe what the team learned

Which scenario describes your situation?
```

### Step 5: Analyze Refinement Input

**If transcript provided (Option A):**

Analyze the transcript and extract:
- **Stories to Split:** Which stories are too large
- **Stories to Merge:** Which stories are too small or tightly coupled
- **Stories to Add:** New stories identified during refinement
- **Stories to Modify:** Changes to acceptance criteria or scope
- **Stories to Remove/Cancel:** Stories no longer needed
- **Priority Changes:** Changes to story priority or order
- **Concerns Raised:** Any concerns about current decomposition

Summarize findings:

```markdown
I've analyzed your refinement meeting transcript. Here's what I found:

**Changes Needed:**

**Split Stories:**
- **[ISSUE-XX]: [Title]** → Split into [N] smaller stories
  - Reason: [Why it's too large - from transcript]
  - Proposed split: [How to split it]

**Merge Stories:**
- **[ISSUE-YY]** + **[ISSUE-ZZ]** → Merge into one story
  - Reason: [Why they should be merged - from transcript]

**Add New Stories:**
- **[New story 1 name]**
  - Reason: [Why it's needed - from transcript]
  - Scope: [What it covers]

**Modify Stories:**
- **[ISSUE-AA]: [Title]**
  - Change: [What needs to change - from transcript]
  - Reason: [Why]

**Cancel Stories:**
- **[ISSUE-BB]: [Title]**
  - Reason: [Why no longer needed - from transcript]

**Priority Changes:**
- [ISSUE-XX] should move up in priority
- [ISSUE-YY] can be deprioritized

**Concerns from Meeting:**
- [Concern 1]
- [Concern 2]
```

**If conversational (Option B or C):**

Ask targeted questions - see Step 6.

### Step 6: Ask Clarifying Questions

Based on the refinement input, ask specific questions:

```markdown
Let me clarify the refinement approach:

[If splitting stories:]
**Story Split: [ISSUE-XX] - [Title]**

I see this story is being split. How should we split it?

**Option A:** Split by layer (backend story + frontend story)
**Option B:** Split by workflow (story 1 = minimal workflow, story 2 = advanced features)
**Option C:** Split by component ([component A] story + [component B] story)
**Option D:** Custom split - describe how

Which approach makes sense?

[After user selects, ask:]
- Should the original story [ISSUE-XX] become one of the new stories, or should I create all new stories and cancel the original?
- How should acceptance criteria be distributed across the new stories?
- Do the new stories have dependencies on each other?

[If merging stories:]
**Story Merge: [ISSUE-YY] + [ISSUE-ZZ]**

I see these stories should be merged. Questions:

- Which story should be kept ([ISSUE-YY] or [ISSUE-ZZ])?
- Should I combine all acceptance criteria from both stories?
- What should be the title of the merged story?

[If adding stories:]
**New Story: [Proposed title]**

For this new story, I need to understand:

- What user persona is this for? (from feature spec)
- What user value does it deliver?
- What are the acceptance criteria? (or should I draft them based on the feature spec?)
- Does it depend on any existing stories?
- What's the priority relative to existing stories?

[If modifying stories:]
**Modify Story: [ISSUE-AA] - [Title]**

What needs to change?

**Option A:** Acceptance criteria (add/remove/modify ACs)
**Option B:** Scope (expand or reduce what's included)
**Option C:** Description (clarify user story or value)
**Option D:** Technical notes (update technical approach)

[Continue with targeted questions based on selection]

[If cancelling stories:]
**Cancel Story: [ISSUE-BB] - [Title]**

Before I cancel this story, let me confirm:

- Why is it no longer needed?
- Is the functionality covered elsewhere, or is it out of scope now?
- Should I add a comment explaining why it was cancelled?
```

### Step 7: Propose Changes

Based on all gathered information, propose specific changes:

```markdown
Perfect! Based on our discussion, here are the changes I'll make to the story decomposition:

---

## Changes Summary

**Total Changes:** [N] operations ([X] splits, [Y] merges, [Z] additions, [W] modifications, [V] cancellations)

---

### 1. Split [ISSUE-XX]: [Original Title]

**Reason:** [Why it's being split]

**Original Story:**
- [Brief description]
- [N] acceptance criteria
- [Current status]

**New Stories:**

**[ISSUE-XX-A]: [New Title 1]** (keeping original issue number)
- **Scope:** [What this covers]
- **Acceptance Criteria:** [N] ACs including:
  - [AC1 summary]
  - [AC2 summary]
- **Dependencies:** [Dependencies]
- **Labels:** [Labels to apply]

**[NEW-ISSUE]: [New Title 2]** (new issue)
- **Scope:** [What this covers]
- **Acceptance Criteria:** [N] ACs including:
  - [AC1 summary]
  - [AC2 summary]
- **Dependencies:** Depends on [ISSUE-XX-A]
- **Labels:** [Labels to apply]

---

### 2. Merge [ISSUE-YY] + [ISSUE-ZZ]

**Reason:** [Why they're being merged]

**Keeping:** [ISSUE-YY] (updating title and description)
**Cancelling:** [ISSUE-ZZ] (with comment explaining merge)

**Merged Story: [ISSUE-YY]: [New Title]**
- **Scope:** [Combined scope]
- **Acceptance Criteria:** [N] ACs from both stories:
  - [ACs from ISSUE-YY]
  - [ACs from ISSUE-ZZ]
- **Labels:** [Combined labels]

---

### 3. Add New Story: [NEW-ISSUE]: [Title]

**Reason:** [Why it's needed]

**New Story Details:**
- **User Story:** As a [persona], I want [capability], so that [benefit]
- **Value:** [User value statement]
- **Acceptance Criteria:** [N] ACs including:
  - [AC1 summary]
  - [AC2 summary]
- **Dependencies:** [Dependencies if any]
- **Priority:** [Relative priority]
- **Labels:** [Labels to apply]

---

### 4. Modify [ISSUE-AA]: [Title]

**Reason:** [Why it's being modified]

**Changes:**
- **Add Acceptance Criteria:**
  - [New AC1]
  - [New AC2]
- **Remove Acceptance Criteria:**
  - [Removed AC]
- **Update Description:**
  - Old: [Old description snippet]
  - New: [New description snippet]

---

### 5. Cancel [ISSUE-BB]: [Title]

**Reason:** [Why it's no longer needed]

**Action:** Mark as Cancelled with comment: "[Reason for cancellation]"

---

## Impact Analysis

**Stories Before:** [N] stories
**Stories After:** [M] stories (net change: [+/-X])

**Dependency Changes:**
- [Change 1: e.g., ISSUE-XX now depends on new ISSUE-XX-A]
- [Change 2: e.g., ISSUE-CC no longer blocked]

**Priority Order (Recommended):**
1. [ISSUE-XX-A]: [Title] (was #1, still #1)
2. [NEW-ISSUE]: [Title] (new, inserted at #2)
3. [ISSUE-YY]: [Title] (was #2, now #3 but merged with ISSUE-ZZ)
4. [Continue with updated order]

---

Does this refinement plan look good, or would you like to adjust anything?
```

[Wait for user confirmation or adjustments]

### Step 8: Execute Changes

Once confirmed, execute changes in Linear with progress updates:

```markdown
Executing refinement changes...

[For each change, show progress:]

✅ Split [ISSUE-XX]: [Original Title]
   - Updated [ISSUE-XX] to: [New Title 1]
   - Created [NEW-ISSUE-1]: [New Title 2]
   - Updated dependencies

✅ Merged [ISSUE-YY] + [ISSUE-ZZ]
   - Updated [ISSUE-YY] with merged content
   - Cancelled [ISSUE-ZZ] with comment

✅ Added [NEW-ISSUE-2]: [Title]
   - Created with complete ACs and labels

✅ Modified [ISSUE-AA]: [Title]
   - Added [N] acceptance criteria
   - Updated description

✅ Cancelled [ISSUE-BB]: [Title]
   - Marked as Cancelled with reason

All changes completed successfully!
```

### Step 9: Provide Comprehensive Summary

After executing all changes, provide a detailed summary:

```markdown
✅ Story decomposition refined successfully!

**Linear Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Project URL]

---

## Changes Applied

**Split Stories:** [N]
- [ISSUE-XX] → [ISSUE-XX-A] + [NEW-ISSUE-1]

**Merged Stories:** [N]
- [ISSUE-YY] + [ISSUE-ZZ] → [ISSUE-YY]

**New Stories:** [N]
- [NEW-ISSUE-2]: [Title]
- [NEW-ISSUE-3]: [Title]

**Modified Stories:** [N]
- [ISSUE-AA]: [Title] (updated ACs)

**Cancelled Stories:** [N]
- [ISSUE-BB]: [Title] (reason: [reason])

---

## Updated Story List

**Total Stories:** [M] stories (was [N], change: [+/-X])

### Story 1: [ISSUE-XX-A] - [Title]
**Status:** [Status]
**URL:** [URL]
**Brief:** [1-line description]
**ACs:** [N] acceptance criteria
**Dependencies:** [None or list]
**Labels:** [Labels]
**Note:** Split from original [ISSUE-XX]

### Story 2: [NEW-ISSUE-1] - [Title]
**Status:** Backlog
**URL:** [URL]
**Brief:** [1-line description]
**ACs:** [N] acceptance criteria
**Dependencies:** Depends on [ISSUE-XX-A]
**Labels:** [Labels]
**Note:** Split from original [ISSUE-XX]

### Story 3: [ISSUE-YY] - [Title]
**Status:** [Status]
**URL:** [URL]
**Brief:** [1-line description]
**ACs:** [N] acceptance criteria (merged from [ISSUE-ZZ])
**Dependencies:** [None or list]
**Labels:** [Labels]
**Note:** Merged with [ISSUE-ZZ]

[Continue with all remaining stories]

---

## Updated Implementation Order

Based on dependencies and refinements:

1. **[ISSUE-XX-A]: [Title]** (Priority: High)
   - Foundation story
   - No dependencies
   - Should be implemented first

2. **[NEW-ISSUE-1]: [Title]** (Priority: High)
   - Depends on: [ISSUE-XX-A]
   - Blocked until [ISSUE-XX-A] is done

3. **[ISSUE-YY]: [Title]** (Priority: Medium)
   - Merged story with expanded scope
   - Can start in parallel with [NEW-ISSUE-1]

[Continue with recommended order]

---

## Story Status After Refinement

- **Backlog:** [N] stories
- **Todo:** [N] stories
- **In Progress:** [N] stories (unchanged)
- **Done:** [N] stories (unchanged)
- **Cancelled:** [N] stories (including newly cancelled)

---

## Next Steps

**Immediate:**
1. Review updated stories in Linear and verify changes
2. Update sprint planning based on new story breakdown
3. Communicate changes to team (especially for in-progress work)
4. Re-estimate stories if using estimation

**For Implementation:**
- Next story to start: [ISSUE-XX-A] - [Title]
- Create TDD plan: `/plan-user-story [ISSUE-XX-A]`
- Implement: `/implement-story docs/specs/.../story_[ISSUE-XX-A]_tdd_tasks.md`

**Future Refinements:**
- If further refinement needed: `/refine-decomposition [PROJECT-KEY]`
- This command can be run multiple times as the team learns

The story decomposition has been successfully refined based on team learnings! 🎉
```

## Guidelines

### Conversational Best Practices

1. **Show Complete State**: Display ALL current stories before proposing changes
2. **Be Specific**: Propose exact changes with before/after details
3. **Explain Impact**: Show how changes affect dependencies and order
4. **Confirm Before Acting**: Always get approval before making changes in Linear
5. **Track Changes**: Clearly mark what changed and why
6. **Update Dependencies**: Ensure dependencies are updated when stories are split/merged
7. **Preserve History**: Add comments to cancelled or significantly modified stories

### Transcript Analysis Tips

1. **Identify Problems**: Look for "too large," "too small," "should split," "should combine"
2. **Extract Reasoning**: Understand WHY the team wants to refine
3. **Note New Requirements**: Identify newly discovered stories or requirements
4. **Track Learnings**: Look for "we learned," "we discovered," "we realized"
5. **Capture Concerns**: Note any concerns about current decomposition

### Refinement Operations

**Split Story:**
- Keep original issue for one part (preserves history)
- Create new issues for other parts
- Distribute acceptance criteria logically
- Update dependencies (new stories may depend on each other)
- Add comments explaining the split

**Merge Stories:**
- Keep one issue (usually lower number)
- Combine all acceptance criteria
- Update title to reflect merged scope
- Cancel other issue(s) with comment explaining merge
- Update any stories that depended on cancelled story

**Add Story:**
- Create complete Linear issue with all details
- Follow same format as original decomposition
- Insert in priority order
- Update dependencies if it blocks/depends on existing stories

**Modify Story:**
- Add/remove/update acceptance criteria
- Update description or scope
- Add comment explaining modification
- Don't change issue number or URL

**Cancel Story:**
- Mark as Cancelled (don't delete)
- Add comment explaining why (out of scope, merged, no longer needed, etc.)
- Update any stories that depended on it

### Change Impact Analysis

Before executing changes, analyze impact:

1. **Dependency Impact:**
   - Which stories depend on the story being split/merged/cancelled?
   - Do dependencies need to be updated?

2. **Priority Impact:**
   - Does this change the recommended implementation order?
   - Are any stories now blocked or unblocked?

3. **Team Impact:**
   - Are any changed stories already in progress?
   - Will this affect current sprint?

4. **Scope Impact:**
   - Does total project scope increase or decrease?
   - Are we adding technical debt or clarifying requirements?

### Handling Edge Cases

**Stories In Progress:**
```markdown
⚠️ Warning: [ISSUE-XX] is currently "In Progress"

Splitting/modifying this story will affect ongoing work. Options:

**Option A:** Proceed with refinement and update current work
**Option B:** Wait until [ISSUE-XX] is completed
**Option C:** Only refine future stories

Which approach works for your team?
```

**Stories with Dependencies:**
```markdown
⚠️ Note: [ISSUE-XX] is depended on by:
- [ISSUE-YY]: [Title]
- [ISSUE-ZZ]: [Title]

If I split [ISSUE-XX], I need to know:
- Which new story should [ISSUE-YY] and [ISSUE-ZZ] depend on?
- Or should they depend on BOTH new stories?
```

**Conflicting Changes:**
```markdown
⚠️ Conflict detected:

You want to:
- Split [ISSUE-AA] into [ISSUE-AA-1] and [ISSUE-AA-2]
- Merge [ISSUE-AA] with [ISSUE-BB]

These changes conflict. Should I:
- First split, then merge one of the split stories with [ISSUE-BB]?
- First merge, then split the merged story?
- Skip one of these changes?
```

## Error Handling

If something goes wrong:

1. **No Stories Exist**: Error - use `/decompose-feature` first
2. **Story Not Found**: Verify story exists and is in this project
3. **Can't Update Linear**: Explain error and provide manual steps
4. **Invalid Split**: Ask for clarification on how to split
5. **Circular Dependencies**: Warn and ask user to resolve

## Examples

### Example: Split Large Story

```
User: /refine-decomposition PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search with Filters

       Current User Stories: 5 stories

       [Lists all 5 stories with details]

       What prompted this refinement?

User: Option A
      [Pastes transcript: "PROJ-42 is too large, we need to split it into
       backend and frontend stories..."]

Agent: I've analyzed your refinement meeting. Here's what I found:

       **Split Stories:**
       - PROJ-42: Basic search → Split into backend + frontend
         Reason: Too large for one sprint, separate teams

       Let me clarify:
       - Should PROJ-42 become the backend story, and I create a new story
         for frontend?
       - Or should I create two new stories and cancel PROJ-42?

User: Keep PROJ-42 as backend, create new story for frontend

Agent: Perfect! Here's the refinement plan:

       **1. Split PROJ-42: Basic text search**

       **PROJ-42: Basic text search - Backend API**
       - Scope: API endpoints, database, business logic
       - ACs: [Lists backend ACs]

       **PROJ-50: Basic text search - Frontend UI** (new)
       - Scope: UI components, search input, results display
       - ACs: [Lists frontend ACs]
       - Dependencies: Depends on PROJ-42

       Does this look good?

User: Yes

Agent: [Executes changes and provides summary]
```

### Example: Add New Story

```
User: /refine-decomposition PROJ-42

Agent: [Shows current state with 5 stories]

       What prompted this refinement?

User: Option B - During development, we discovered we need a "Clear all
      filters" button

Agent: For this new story "Clear all filters button", I need to understand:

       1. What user persona is this for?
       2. Where does it fit in the implementation order?
       3. What are the acceptance criteria?

User: 1. Project managers (same as other stories)
      2. After we implement the filters (after PROJ-45)
      3. It should clear all active filters and reset to default search

Agent: Perfect! Here's the new story:

       **PROJ-51: Clear all filters button**
       - User Story: As a project manager, I want to clear all active filters
         with one click, so that I can quickly reset to default search
       - Value: Improves UX by providing quick reset functionality
       - ACs:
         - AC1: Clear all filters button is visible when filters are active
         - AC2: Clicking button clears all filters and resets search
         - AC3: Button is disabled when no filters are active
       - Dependencies: Depends on PROJ-45
       - Priority: After PROJ-45

       Should I create this story?

User: Yes

Agent: [Creates story and provides summary]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide Linear Project ID
- **Shows Complete State**: Displays ALL stories before proposing changes
- **Change Tracking**: Clearly documents what changed and why
- **Preserves History**: Doesn't delete stories, marks as cancelled
- **Updates Dependencies**: Ensures dependencies are correct after changes
- **Impact Analysis**: Analyzes impact on in-progress work and dependencies
- **Repeatable**: Can be run multiple times as team learns

This conversational refinement approach ensures the story decomposition evolves with team learnings while preserving history and maintaining clear traceability.
