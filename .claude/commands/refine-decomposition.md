---
description: Refine existing story decomposition - split, merge, add, or modify stories
---

Refine an existing feature decomposition by splitting large stories, merging small ones, adding new stories, or modifying existing stories based on team learnings and refinement discussions.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Jira Project Key as argument
2. Fetch all existing stories for the project
3. Ask if there's a refinement meeting transcript
4. Analyze transcript or work conversationally
5. Propose specific changes (split/merge/add/modify)
6. Confirm changes before executing
7. Execute changes in Jira
8. Provide clear summary of what changed

## Steps

### Step 1: Get Project Key from Arguments

The command accepts the Jira Project Key as `$ARGUMENTS`:
- Project Key (e.g., `PROJ`, `ENG`, `PRODUCT`)

**Use MCP Tool:** `mcp__atlassian__searchJiraIssuesUsingJql` with JQL like `project = PROJ AND type = Story` to fetch all stories.

### Step 2: Fetch and Display Current State

Query Jira for all stories in the project and display complete current state:

```markdown
I found Jira Project: [PROJECT-KEY]

**Project:** [PROJECT-KEY]
**Total Stories:** [N] stories

**Current User Stories:** [N] stories

### Story 1: [ISSUE-KEY] - [Story Title]
**Status:** [Status]
**URL:** [URL]
**Labels:** [Labels]
**Assigned to:** [Assignee or Unassigned]
**Brief:** [1-line description of what this story covers]
**Acceptance Criteria:** [N] ACs
**Dependencies:** [Lists other stories this depends on or blocks]

### Story 2: [ISSUE-KEY] - [Story Title]
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
- Todo/Selected for Development: [N] stories
- In Progress: [N] stories
- Done: [N] stories

[If there are In Progress or Done stories, show warning:]
⚠️ Note: [N] stories are already in progress or completed. I can still refine the decomposition, but be aware that changes may affect ongoing work.
```

### Step 3: Read Story Details

For each story, read the complete Jira issue:

**Use MCP Tool:** `mcp__atlassian__getJiraIssue` for each story to get:
- Full description with user story format
- All acceptance criteria
- Comments and discussion
- Current status and assignee
- Labels and metadata
- Links to other stories or Confluence pages

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
- **[ISSUE-KEY]: [Title]** → Split into [N] smaller stories
  - Reason: [Why it's too large - from transcript]
  - Proposed split: [How to split it]

**Merge Stories:**
- **[ISSUE-KEY]** + **[ISSUE-KEY]** → Merge into one story
  - Reason: [Why they should be merged - from transcript]

**Add New Stories:**
- **[New story 1 name]**
  - Reason: [Why it's needed - from transcript]
  - Scope: [What it covers]

**Modify Stories:**
- **[ISSUE-KEY]: [Title]**
  - Change: [What needs to change - from transcript]
  - Reason: [Why]

**Cancel Stories:**
- **[ISSUE-KEY]: [Title]**
  - Reason: [Why no longer needed - from transcript]

**Priority Changes:**
- [ISSUE-KEY] should move up in priority
- [ISSUE-KEY] can be deprioritized

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
**Story Split: [ISSUE-KEY] - [Title]**

I see this story is being split. How should we split it?

**Option A:** Split by layer (backend story + frontend story)
**Option B:** Split by workflow (story 1 = minimal workflow, story 2 = advanced features)
**Option C:** Split by component ([component A] story + [component B] story)
**Option D:** Custom split - describe how

Which approach makes sense?

[After user selects, ask:]
- Should the original story [ISSUE-KEY] become one of the new stories, or should I create all new stories and transition the original to Done/Cancelled?
- How should acceptance criteria be distributed across the new stories?
- Do the new stories have dependencies on each other?

[If merging stories:]
**Story Merge: [ISSUE-KEY] + [ISSUE-KEY]**

I see these stories should be merged. Questions:

- Which story should be kept ([ISSUE-KEY] or [ISSUE-KEY])?
- Should I combine all acceptance criteria from both stories?
- What should be the title of the merged story?

[If adding stories:]
**New Story: [Proposed title]**

For this new story, I need to understand:

- What user persona is this for?
- What user value does it deliver?
- What are the acceptance criteria? (or should I draft them based on specs?)
- Does it depend on any existing stories?
- What's the priority relative to existing stories?

[If modifying stories:]
**Modify Story: [ISSUE-KEY] - [Title]**

What needs to change?

**Option A:** Acceptance criteria (add/remove/modify ACs)
**Option B:** Scope (expand or reduce what's included)
**Option C:** Description (clarify user story or value)
**Option D:** Technical notes (update technical approach)

[Continue with targeted questions based on selection]

[If cancelling stories:]
**Cancel Story: [ISSUE-KEY] - [Title]**

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

### 1. Split [ISSUE-KEY]: [Original Title]

**Reason:** [Why it's being split]

**Original Story:**
- [Brief description]
- [N] acceptance criteria
- [Current status]

**New Stories:**

**[ISSUE-KEY-A]: [New Title 1]** (update original issue)
- **Scope:** [What this covers]
- **Acceptance Criteria:** [N] ACs including:
  - [AC1 summary]
  - [AC2 summary]
- **Dependencies:** [Dependencies]
- **Labels:** [Labels to apply]

**[NEW-ISSUE-KEY]: [New Title 2]** (new issue)
- **Scope:** [What this covers]
- **Acceptance Criteria:** [N] ACs including:
  - [AC1 summary]
  - [AC2 summary]
- **Dependencies:** Depends on [ISSUE-KEY-A]
- **Labels:** [Labels to apply]

---

### 2. Merge [ISSUE-KEY] + [ISSUE-KEY]

**Reason:** [Why they're being merged]

**Keeping:** [ISSUE-KEY] (updating title and description)
**Cancelling:** [ISSUE-KEY] (with comment explaining merge)

**Merged Story: [ISSUE-KEY]: [New Title]**
- **Scope:** [Combined scope]
- **Acceptance Criteria:** [N] ACs from both stories:
  - [ACs from first story]
  - [ACs from second story]
- **Labels:** [Combined labels]

---

### 3. Add New Story: [NEW-ISSUE-KEY]: [Title]

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

### 4. Modify [ISSUE-KEY]: [Title]

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

### 5. Cancel [ISSUE-KEY]: [Title]

**Reason:** [Why it's no longer needed]

**Action:** Transition to Cancelled/Done with comment: "[Reason for cancellation]"

---

## Impact Analysis

**Stories Before:** [N] stories
**Stories After:** [M] stories (net change: [+/-X])

**Dependency Changes:**
- [Change 1: e.g., ISSUE-XX now depends on new ISSUE-XX-A]
- [Change 2: e.g., ISSUE-CC no longer blocked]

**Priority Order (Recommended):**
1. [ISSUE-KEY]: [Title] (was #1, still #1)
2. [NEW-ISSUE-KEY]: [Title] (new, inserted at #2)
3. [ISSUE-KEY]: [Title] (was #2, now #3 but merged)
4. [Continue with updated order]

---

Does this refinement plan look good, or would you like to adjust anything?
```

[Wait for user confirmation or adjustments]

### Step 8: Execute Changes

Once confirmed, execute changes in Jira with progress updates:

**Use MCP Tools:**
- `mcp__atlassian__editJiraIssue` - Update existing issues
- `mcp__atlassian__createJiraIssue` - Create new issues
- `mcp__atlassian__transitionJiraIssue` - Change status (e.g., to Cancelled)
- `mcp__atlassian__addCommentToJiraIssue` - Add explanatory comments

```markdown
Executing refinement changes...

[For each change, show progress:]

✅ Split [ISSUE-KEY]: [Original Title]
   - Updated [ISSUE-KEY] to: [New Title 1]
   - Created [NEW-ISSUE-KEY]: [New Title 2]
   - Updated dependencies

✅ Merged [ISSUE-KEY] + [ISSUE-KEY]
   - Updated [ISSUE-KEY] with merged content
   - Transitioned [ISSUE-KEY] to Cancelled with comment

✅ Added [NEW-ISSUE-KEY]: [Title]
   - Created with complete ACs and labels

✅ Modified [ISSUE-KEY]: [Title]
   - Added [N] acceptance criteria
   - Updated description

✅ Cancelled [ISSUE-KEY]: [Title]
   - Transitioned to Cancelled with reason

All changes completed successfully!
```

### Step 9: Provide Comprehensive Summary

After executing all changes, provide a detailed summary:

```markdown
✅ Story decomposition refined successfully!

**Jira Project:** [PROJECT-KEY]

---

## Changes Applied

**Split Stories:** [N]
- [ISSUE-KEY] → [ISSUE-KEY-A] + [NEW-ISSUE-KEY]

**Merged Stories:** [N]
- [ISSUE-KEY] + [ISSUE-KEY] → [ISSUE-KEY]

**New Stories:** [N]
- [NEW-ISSUE-KEY]: [Title]
- [NEW-ISSUE-KEY]: [Title]

**Modified Stories:** [N]
- [ISSUE-KEY]: [Title] (updated ACs)

**Cancelled Stories:** [N]
- [ISSUE-KEY]: [Title] (reason: [reason])

---

## Updated Story List

**Total Stories:** [M] stories (was [N], change: [+/-X])

### Story 1: [ISSUE-KEY] - [Title]
**Status:** [Status]
**URL:** [URL]
**Brief:** [1-line description]
**ACs:** [N] acceptance criteria
**Dependencies:** [None or list]
**Labels:** [Labels]
**Note:** Split from original [OLD-ISSUE-KEY]

### Story 2: [NEW-ISSUE-KEY] - [Title]
**Status:** Backlog
**URL:** [URL]
**Brief:** [1-line description]
**ACs:** [N] acceptance criteria
**Dependencies:** Depends on [ISSUE-KEY]
**Labels:** [Labels]
**Note:** Split from original [OLD-ISSUE-KEY]

### Story 3: [ISSUE-KEY] - [Title]
**Status:** [Status]
**URL:** [URL]
**Brief:** [1-line description]
**ACs:** [N] acceptance criteria (merged from [OLD-ISSUE-KEY])
**Dependencies:** [None or list]
**Labels:** [Labels]
**Note:** Merged with [OLD-ISSUE-KEY]

[Continue with all remaining stories]

---

## Updated Implementation Order

Based on dependencies and refinements:

1. **[ISSUE-KEY]: [Title]** (Priority: High)
   - Foundation story
   - No dependencies
   - Should be implemented first

2. **[NEW-ISSUE-KEY]: [Title]** (Priority: High)
   - Depends on: [ISSUE-KEY]
   - Blocked until [ISSUE-KEY] is done

3. **[ISSUE-KEY]: [Title]** (Priority: Medium)
   - Merged story with expanded scope
   - Can start in parallel with [NEW-ISSUE-KEY]

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
1. Review updated stories in Jira and verify changes
2. Update sprint planning based on new story breakdown
3. Communicate changes to team (especially for in-progress work)
4. Re-estimate stories if using estimation

**For Implementation:**
- Next story to start: [ISSUE-KEY] - [Title]
- Create TDD plan: `/plan-user-story [ISSUE-KEY]`
- Implement: `/implement-story docs/specs/.../story_[ISSUE-KEY]_tdd_tasks.md`

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
4. **Confirm Before Acting**: Always get approval before making changes in Jira
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
- Update original issue for one part (preserves history)
- Create new issues for other parts
- Distribute acceptance criteria logically
- Update dependencies (new stories may depend on each other)
- Add comments explaining the split

**Merge Stories:**
- Keep one issue (usually lower number)
- Combine all acceptance criteria
- Update title to reflect merged scope
- Transition other issue(s) to Cancelled with comment explaining merge
- Update any stories that depended on cancelled story

**Add Story:**
- Create complete Jira issue with all details
- Follow same format as original decomposition
- Insert in priority order
- Update dependencies if it blocks/depends on existing stories

**Modify Story:**
- Add/remove/update acceptance criteria
- Update description or scope
- Add comment explaining modification
- Don't change issue key or URL

**Cancel Story:**
- Transition to Cancelled state (don't delete)
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
⚠️ Warning: [ISSUE-KEY] is currently "In Progress"

Splitting/modifying this story will affect ongoing work. Options:

**Option A:** Proceed with refinement and update current work
**Option B:** Wait until [ISSUE-KEY] is completed
**Option C:** Only refine future stories

Which approach works for your team?
```

**Stories with Dependencies:**
```markdown
⚠️ Note: [ISSUE-KEY] is depended on by:
- [ISSUE-KEY]: [Title]
- [ISSUE-KEY]: [Title]

If I split [ISSUE-KEY], I need to know:
- Which new story should dependent stories reference?
- Or should they depend on BOTH new stories?
```

**Conflicting Changes:**
```markdown
⚠️ Conflict detected:

You want to:
- Split [ISSUE-KEY] into [ISSUE-KEY-1] and [ISSUE-KEY-2]
- Merge [ISSUE-KEY] with [ISSUE-KEY]

These changes conflict. Should I:
- First split, then merge one of the split stories?
- First merge, then split the merged story?
- Skip one of these changes?
```

## Error Handling

If something goes wrong:

1. **No Stories Exist**: Error - use `/decompose-feature` first
2. **Story Not Found**: Verify story exists and is in this project
3. **Can't Update Jira**: Explain error and provide manual steps
4. **Invalid Split**: Ask for clarification on how to split
5. **Circular Dependencies**: Warn and ask user to resolve

## Examples

### Example: Split Large Story

```
User: /refine-decomposition PROJ

Agent: I found Jira Project: PROJ

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

Agent: Executing refinement changes...

       ✅ Updated PROJ-42: Basic text search - Backend API
       ✅ Created PROJ-50: Basic text search - Frontend UI
       ✅ Updated dependencies

       [Provides comprehensive summary]
```

### Example: Add New Story

```
User: /refine-decomposition PROJ

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

Agent: Creating story in Jira...

       ✅ Created PROJ-51: Clear all filters button

       [Provides summary]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide Jira Project Key
- **Shows Complete State**: Displays ALL stories before proposing changes
- **Change Tracking**: Clearly documents what changed and why
- **Preserves History**: Doesn't delete stories, transitions to Cancelled
- **Updates Dependencies**: Ensures dependencies are correct after changes
- **Impact Analysis**: Analyzes impact on in-progress work and dependencies
- **Repeatable**: Can be run multiple times as team learns

This conversational refinement approach ensures the story decomposition evolves with team learnings while preserving history and maintaining clear traceability.
