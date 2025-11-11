---
description: Refine existing product specification based on meeting transcript or conversation
---

You are tasked with refining an existing Product Specification (Feature Brief) in a Linear Project based on new discussions, feedback, or changes in requirements.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Linear Project ID as argument
2. Fetch project and show current state
3. Read existing Product Spec from Linear project description
4. Ask for refinement input (transcript or conversation)
5. Analyze what needs to be updated
6. Ask clarifying questions
7. Show proposed changes (before/after)
8. Update Linear project description
9. Provide clear summary

## Steps

### Step 1: Get Project ID from Arguments

The command accepts the Linear Project as `$ARGUMENTS`:
- Project Key (e.g., `PROJ-42`)
- Project Name (e.g., `Advanced Search`)
- Project ID (UUID)

### Step 2: Fetch and Analyze Project

Query Linear for the project and display current state:

```markdown
I found Linear Project $ARGUMENTS:

**Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Linear Project URL]
**Status:** [Current status]
**Team:** [Team name]

**Current Documentation:**
- **Product Spec:** [✅ Found in Linear project description or ❌ Not found]
- **Technical Spec:** [✅ Found in Linear project description or ⏳ Placeholder or ❌ Not found]

**User Stories:** [N] stories
[If stories exist, list a few:]
- [ISSUE-1]: [Title] - [Status]
- [ISSUE-2]: [Title] - [Status]
```

### Step 3: Read Existing Product Spec

Read the **Product Specification** from the Linear project description.

The Linear project description should contain:

```markdown
## 📋 Product Specification
[Product spec content - THIS IS WHAT WE'LL REFINE]

## 🔧 Technical Specification
[Technical spec content]
```

**Extract from Product Specification section:**
- Feature overview (what, why, who)
- Success metrics
- User workflows/journeys
- Functional requirements
- Non-functional requirements
- Business rules and validation
- Scope boundaries (in/out of scope)
- Constraints and dependencies
- Open questions and assumptions

**If Product Spec not found:**

Show clear error:
```markdown
❌ I couldn't find an existing Product Specification in the Linear project description.

This command is for refining EXISTING product specs. To create a new product spec, use:
`/generate-feature-brief`

Would you like me to create a new feature brief instead?
```

### Step 4: Show Current Product Spec Summary

Before asking for refinement input, show a summary of what exists:

```markdown
**Current Product Specification Summary:**

**Feature Overview:**
- What: [Brief description of what the feature does]
- Why: [Business value]
- Who: [Target users]

**Success Metrics:**
- [Metric 1]: [Target]
- [Metric 2]: [Target]
[If N>2:] - [+N more metrics]

**User Workflows:** [N] workflows defined
1. [Primary workflow name]
2. [Secondary workflow name]
[If more:] - [+N more workflows]

**Requirements:**
- Must Have: [N] core features
- Out of Scope: [N] items explicitly excluded
- Constraints: [N] constraints identified

**Open Questions:** [N] unresolved questions
[If any exist, list them:]
- [ ] Q1: [Question text]
- [ ] Q2: [Question text]

**Assumptions:** [N] assumptions
[If any exist, list a few:]
- [Assumption 1]
- [Assumption 2]

**Last Updated:** [If available from Linear metadata]
```

### Step 5: Request Refinement Input

Ask user what prompted the refinement and how they want to provide information:

```markdown
What prompted this product spec refinement?

**Common Reasons:**
- User feedback revealed new requirements
- Stakeholder review requested changes
- Scope needs adjustment (add/remove features)
- Success metrics need updating
- User workflows need clarification
- Requirements were too vague and need detail
- Business constraints changed
- Open questions now have answers

How would you like to provide the refinement information?

**Option A: Refinement Meeting Transcript** - Paste transcript from your product review/feedback session
**Option B: Describe Changes Conversationally** - We'll discuss the changes together

Which would you prefer?
```

### Step 6: Analyze Refinement Input

**If transcript provided (Option A):**

Analyze the transcript and extract:
- **What's Changing:** Specific sections or requirements being updated
- **Why It's Changing:** Reason for the change (feedback, new info, pivot)
- **New Requirements:** Any new features or capabilities being added
- **Removed Requirements:** Any features being cut or moved out of scope
- **Clarified Requirements:** Vague requirements now made specific
- **Resolved Questions:** Any open questions now answered
- **New Questions:** Any new uncertainties discovered
- **Impact:** How this affects existing user stories or technical spec

Summarize findings:

```markdown
I've analyzed your refinement meeting transcript. Here's what I found:

**Changes Requested:**

1. **[Section/Topic]:** [What needs to change]
   - **Current State:** [What it says now]
   - **Requested Change:** [What it should say]
   - **Reason:** [Why this change is needed]
   - **Type:** [Addition/Modification/Deletion/Clarification]

2. **[Section/Topic]:** [What needs to change]
   - **Current State:** [What it says now]
   - **Requested Change:** [What it should say]
   - **Reason:** [Why this change is needed]
   - **Type:** [Addition/Modification/Deletion/Clarification]

[Continue for all identified changes]

**Scope Changes:**
- ➕ Added to scope: [New features/requirements]
- ➖ Removed from scope: [Cut features/requirements]
- 📝 Clarified: [Vague requirements now specific]

**Questions Resolved:**
- ✅ [Previously open question that's now answered]
- ✅ [Previously open question that's now answered]

**New Questions Discovered:**
- ❓ [New question that emerged from discussion]
- ❓ [New question that emerged from discussion]

**Potential Impact:**
- [Impact on existing user stories]
- [Impact on technical specification]
- [Impact on timeline or resources]
```

**If conversational (Option B):**

Ask structured questions:
```markdown
Let's discuss what needs to be refined in the product spec.

1. Which sections need updating?
   - Feature Overview (what/why/who)?
   - Success Metrics?
   - User Workflows?
   - Requirements (must have/out of scope)?
   - Constraints?
   - Other?

2. What triggered this refinement?
   - User feedback?
   - Stakeholder review?
   - Market changes?
   - Implementation learnings?
   - Changed priorities?

3. What specifically needs to change?
```

### Step 7: Ask Clarifying Questions

Based on the identified changes, ask targeted questions:

```markdown
Let me clarify some details about these changes:

**For [Change 1]:**
1. [Specific question about the new requirement]
2. [Question about acceptance criteria]
3. [Question about priority/urgency]

**For [Change 2]:**
1. [Specific question about workflow changes]
2. [Question about user impact]
3. [Question about edge cases]

**Scope Questions:**
1. Should items removed from scope be documented as "Future Enhancements" or truly out of scope?
2. Do new requirements affect the success metrics?
3. Are there new constraints or dependencies to consider?

**Impact Questions:**
1. Should existing user stories be updated to reflect these changes?
2. Does the technical spec need to be reviewed/updated?
3. Are there any new compliance or security considerations?
```

### Step 8: Show Proposed Changes (Before/After)

**CRITICAL - Present clear before/after for each change:**

```markdown
Here are the proposed changes to the Product Specification:

---

### Change 1: [Section/Topic Name]

**BEFORE:**
```
[Current text from the spec - show enough context]
```

**AFTER:**
```
[Proposed updated text with changes highlighted in context]
```

**Rationale:** [Why this change is being made]
**Type:** [Addition/Modification/Deletion/Clarification]
**Impact:** [How this affects implementation/stories]

---

### Change 2: [Section/Topic Name]

**BEFORE:**
```
[Current text]
```

**AFTER:**
```
[Proposed text]
```

**Rationale:** [Why this change]
**Type:** [Addition/Modification/Deletion/Clarification]
**Impact:** [How this affects implementation]

---

[Continue for all changes]

**Summary of Changes:**
- [N] sections updated
- [N] requirements added
- [N] requirements removed or moved out of scope
- [N] requirements clarified (vague → specific)
- [N] open questions resolved
- [N] new questions added
- [N] success metrics updated

**Sections Modified:**
- ✏️ Section 1: Overview
- ✏️ Section 2: User Journey
- ✏️ Section 3: Requirements
- ✏️ Section 4: Open Questions & Assumptions

Does this look correct? Should I proceed with updating the Linear project description?
```

### Step 9: Apply Uncertainty Markers to New/Updated Content

**CRITICAL - Uncertainty Marker Policy for Refinements:**

Review the documentation in `.claude/uncertainty-markers.md`.

When refining the specification, follow these rules:

1. **If new information is vague** → Use `[CLARIFICATION NEEDED: what needs defining]`
2. **If new requirements lack details** → Use `[OPEN QUESTION: question]`
3. **If you make new inferences** → Use `[ASSUMPTION: statement]`
4. **If resolving an existing marker** → Remove the marker and add the resolved value
5. **If partially resolving** → Update the marker to reflect new status

**Examples:**

❌ BAD (removes old marker but makes new silent assumption):
```
BEFORE: Users can filter by [OPEN QUESTION: which criteria?]
AFTER: Users can filter by status, priority, assignee, tags, and date range
```

✅ GOOD (resolves some, marks remaining uncertainty):
```
BEFORE: Users can filter by [OPEN QUESTION: which criteria?]
AFTER: Users can filter by status, priority, and assignee. Additional filters: [OPEN QUESTION: should we include tags and date range?]
```

❌ BAD (adds vague requirement without marker):
```
AFTER: API response time should be fast enough for good user experience
```

✅ GOOD (marks vague requirement explicitly):
```
AFTER: API response time should be [CLARIFICATION NEEDED: define threshold - <500ms, <1s, <3s?] for good user experience
```

**Validation:**
- Count all new/updated uncertainty markers
- Link all markers to Section 4 (Open Questions & Assumptions)
- Show uncertainty summary to user

### Step 10: Update Linear Project Description

Update the Product Specification section in the Linear project description:

```markdown
Updating Product Specification in Linear Project [PROJECT-KEY]...

✅ Linear project description updated
✅ Product Spec section modified
✅ [N] sections updated
✅ [N] uncertainties resolved
✅ [N] new uncertainties added (if any)

**Linear Project URL:** [URL to view updated spec]
```

### Step 11: Provide Comprehensive Summary

After updating, provide a detailed summary:

```markdown
✅ Product specification refined successfully!

**Linear Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Project URL]

**Refinement Summary:**

**Sections Modified:** [N] sections
- Section 1: Overview - [✏️ Updated / ✅ No change]
  - What & Why: [✏️ Updated / ✅ No change]
  - Target Users: [✏️ Updated / ✅ No change]
  - Success Metrics: [✏️ Updated / ✅ No change / ➕ Added metrics]
- Section 2: User Journey - [✏️ Updated / ✅ No change / ➕ Added workflows]
- Section 3: Requirements - [✏️ Updated / ✅ No change]
  - Must Have: [➕ Added N / ➖ Removed N / ✏️ Modified N]
  - Out of Scope: [➕ Added N / ➖ Removed N]
  - Constraints: [✏️ Updated / ✅ No change]
- Section 4: Open Questions & Assumptions - [✏️ Updated / ✅ No change]

**Key Changes Made:**

1. **[Change 1 Title]**
   - What changed: [Brief description]
   - Why: [Reason]
   - Type: [Addition/Modification/Deletion/Clarification]
   - Impact: [How this affects implementation]

2. **[Change 2 Title]**
   - What changed: [Brief description]
   - Why: [Reason]
   - Type: [Addition/Modification/Deletion/Clarification]
   - Impact: [How this affects implementation]

[Continue for major changes]

**Scope Changes:**

**Added to Scope:** [N] new requirements
- [New requirement 1]
- [New requirement 2]

**Removed from Scope:** [N] requirements cut
- [Removed requirement 1] - [Reason for removal]
- [Removed requirement 2] - [Reason for removal]

**Clarified:** [N] vague requirements made specific
- [Requirement that was clarified]
- [Requirement that was clarified]

**Questions Resolved:** [N] questions
- ✅ [Question that was resolved with answer]
- ✅ [Question that was resolved with answer]

**New Questions Added:** [N] questions
[If any:]
- ❓ [New question]
- ❓ [New question]

**Uncertainty Status:**
[If new uncertainties exist:]
⚠️ The refined spec contains [N] new/updated uncertainties:
- [X] open questions requiring decisions (Section 4)
- [Y] clarifications needed (Section 4)
- [Z] new assumptions that need validation (Section 4)

[If no new uncertainties:]
✅ No new unresolved uncertainties introduced.

**Impact on User Stories:**

[If stories might be affected:]
⚠️ These changes may impact existing user stories:
- [ISSUE-XX]: [Story Title] - [Why it might be affected - e.g., "New requirements added"]
- [ISSUE-YY]: [Story Title] - [Why it might be affected - e.g., "Scope reduced"]
- [ISSUE-ZZ]: [Story Title] - [Why it might be affected - e.g., "Workflow changed"]

[Recommendation:]
Consider running `/refine-decomposition [PROJECT-KEY]` to update affected stories.

**Impact on Technical Specification:**

[If technical spec might be affected:]
⚠️ The technical specification may need review due to:
- [Reason 1 - e.g., "New integration requirement added"]
- [Reason 2 - e.g., "Performance requirements changed"]

[Recommendation:]
Consider running `/refine-technical-spec [PROJECT-KEY]` to update technical details.

**Recommended Actions:**
1. Review the updated Product Spec in Linear: [URL]
2. [If stories affected:] Review and update impacted user stories
3. [If tech spec affected:] Review and update technical specification
4. [If new questions:] Schedule follow-up discussion to resolve new open questions
5. [If assumptions:] Validate new assumptions with stakeholders
6. Communicate changes to the team and stakeholders

**What Changed vs What Stayed:**
- ✏️ Updated: [List key sections that changed]
- ✅ Unchanged: [List sections that stayed the same]
- ➕ Added: [List any new sections or content]
- ➖ Removed: [List content that was cut]

**Collaboration:**
- View refined spec in Linear: [Project URL]
- Both Product and Technical specs remain in the Linear project description
- Team members can comment on the updated spec directly in Linear

**Next Steps:**
1. [If uncertainties:] Resolve new open questions in Section 4
2. [If stories affected:] Update affected user stories with `/refine-decomposition [PROJECT-KEY]`
3. [If tech spec affected:] Update technical spec with `/refine-technical-spec [PROJECT-KEY]`
4. Share updates with the team and stakeholders
5. [If needed:] Schedule another refinement session if more changes emerge
```

## Guidelines

### Conversational Best Practices

1. **Show What Exists First**: Always display current state before asking for changes
2. **Be Specific About Changes**: Show exact before/after for clarity
3. **Explain Impact**: Help user understand how changes affect stories and tech spec
4. **Confirm Before Updating**: Show all proposed changes and get approval
5. **Track Scope Changes**: Clearly identify what's added vs removed vs clarified
6. **Track Uncertainties**: Apply uncertainty markers to new/vague content
7. **Flag Downstream Impact**: Identify which stories or tech specs might need updates

### Transcript Analysis Tips for Refinement

1. **Identify Change Type**: Addition, modification, deletion, or clarification?
2. **Find Root Cause**: Why is this change needed? (feedback, pivot, learning, new info)
3. **Extract Decisions**: What product decisions were made?
4. **Note Disagreements**: If discussion shows debate, capture resolution
5. **Spot Dependencies**: What else might need to change as a result?
6. **Track Scope**: What moved in/out of scope?

### Refinement Quality

1. **Minimal Changes**: Only update what needs updating, preserve the rest
2. **Clear Rationale**: Document why each change is being made
3. **Consistency**: Ensure changes are consistent across all affected sections
4. **Update Success Metrics**: If requirements change significantly, metrics may need adjustment
5. **Complete Updates**: If changing a workflow, update related requirements too
6. **Preserve History**: Document what changed and why in the summary

### Change Categories

**Common Refinement Types:**

1. **Scope Addition**: Adding new features or requirements
2. **Scope Reduction**: Removing features or moving them out of scope
3. **Clarification**: Making vague requirements more specific
4. **Workflow Changes**: Updating user journeys based on feedback
5. **Metric Updates**: Adjusting success criteria
6. **Constraint Changes**: New business or technical constraints
7. **Question Resolution**: Answering previously open questions
8. **Reprioritization**: Moving items between must-have and should-have

### Before/After Quality

**Good Before/After shows:**
- Enough context to understand what's changing
- Exact location in the spec (section number, heading)
- Complete content (not truncated mid-sentence)
- Clear highlighting of what's different
- Rationale for the change
- Type of change (addition/modification/deletion/clarification)

**Example:**

✅ GOOD:
```
**BEFORE (Section 3.1 - Must Have):**
* **FR1:** Users can create tasks with title and description
  - Title: Required field
  - Description: Optional field

**AFTER (Section 3.1 - Must Have):**
* **FR1:** Users can create tasks with title, description, and due date
  - Title: Required field, max 200 characters
  - Description: Optional field, supports markdown formatting
  - Due date: Optional field, must be today or future date
  - Validation: Show error messages inline for each field

**Rationale:** User feedback revealed need for due dates and clearer validation. Length limits prevent database issues.

**Type:** Modification + Clarification

**Impact:** All user stories involving task creation need updated acceptance criteria
```

### Uncertainty Marker Guidelines for Refinements

1. **Resolving Markers**: When refining, check if any existing markers can be resolved
2. **Adding Markers**: If new content is vague or uncertain, mark it explicitly
3. **Updating Markers**: If partially resolving, update the marker to reflect new status
4. **Removing Markers**: Only remove when uncertainty is fully resolved

**Examples:**

✅ Resolving a marker:
```
BEFORE: Users authenticate via [OPEN QUESTION: OAuth2, password, or social login?]
AFTER: Users authenticate via OAuth2 using Google and Microsoft providers
```

✅ Partially resolving:
```
BEFORE: Users can export reports as [OPEN QUESTION: which formats?]
AFTER: Users can export reports as PDF and [OPEN QUESTION: should we support Excel and CSV?]
```

✅ Adding marker for new vague requirement:
```
NEW REQUIREMENT: Search results should be ranked [CLARIFICATION NEEDED: by relevance, recency, or user-configurable?]
```

## Error Handling

If something goes wrong:

1. **No Product Spec Found**: Guide user to `/generate-feature-brief` instead
2. **Unclear Changes**: Ask specific questions about what needs updating
3. **Conflicting Changes**: Present the conflict and ask user to clarify
4. **Incomplete Transcript**: Identify gaps and work conversationally to fill them
5. **Linear Update Fails**: Provide the refined spec text so user can manually update

## Examples

### Example: Transcript-Based Refinement

```
User: /refine-feature-brief PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search with Filters

       **Current Documentation:**
       - Product Spec: ✅ In Linear project description
       - Technical Spec: ✅ In Linear project description

       **Current Product Specification Summary:**

       **Feature Overview:**
       - What: Advanced search with multiple filters
       - Why: Reduce time to find tasks by 50%
       - Who: Project managers and team leads

       **Success Metrics:**
       - Search usage: 70% of users use search weekly
       - Time to find: Reduce from 2 min to 1 min average

       **User Workflows:** 3 workflows defined
       1. Basic text search
       2. Apply filters
       3. Save filter presets

       **Requirements:**
       - Must Have: 8 core features
       - Out of Scope: 3 items explicitly excluded
       - Constraints: 2 constraints identified

       **Open Questions:** 2 unresolved questions
       - Q1: Should saved filters be shareable across teams?
       - Q2: Real-time search or acceptable delay?

       What prompted this product spec refinement?

       **Option A: Refinement Meeting Transcript**
       **Option B: Describe Changes Conversationally**

User: Option A
      [Pastes transcript: "After user testing, we found users need to
       share saved filters with their team. Also, they want to search
       within search results. The real-time search expectation was too
       aggressive - users are fine with a 1-2 second delay..."]

Agent: I've analyzed your refinement meeting transcript. Here's what I found:

       **Changes Requested:**

       1. **Saved Filter Sharing:** Add team sharing capability
          - Current State: Saved filters are per-user only
          - Requested Change: Users can share saved filters with team members
          - Reason: User testing revealed strong need for team collaboration
          - Type: Addition

       2. **Search-within-Search:** Add refinement capability
          - Current State: Not mentioned in requirements
          - Requested Change: Users can refine/narrow existing search results
          - Reason: User testing showed this is a key workflow
          - Type: Addition

       3. **Search Performance:** Relax real-time requirement
          - Current State: "Real-time search required"
          - Requested Change: "1-2 second delay acceptable"
          - Reason: User testing showed this is acceptable, reduces complexity
          - Type: Modification + Clarification

       **Scope Changes:**
       - ➕ Added to scope: Filter sharing, search refinement
       - 📝 Clarified: Performance expectations

       **Questions Resolved:**
       - ✅ Q1: Saved filters should be shareable across teams (YES)
       - ✅ Q2: 1-2 second search delay is acceptable (not real-time)

       **New Questions Discovered:**
       - ❓ Should shared filters be read-only or can team members edit them?
       - ❓ How should search-within-search be indicated in the UI?

       **Potential Impact:**
       - User stories need updating for filter sharing functionality
       - New user story needed for search refinement
       - Technical spec may need update for sharing permissions

       Let me clarify some details:

       1. For filter sharing: Should there be permission controls (admin can
          share, all can share, etc.)?

       2. For search-within-search: Should this work on all search results or
          only certain types?

       3. Should these new features be in the current scope or a future phase?

User: 1. All team members can share filters with their team, no special permissions
      2. Works on all search results
      3. Current scope - essential based on user feedback

Agent: Perfect! Here are the proposed changes:

       ---

       ### Change 1: Add Filter Sharing (Section 3 - Requirements)

       **BEFORE:**
       ```
       * **FR5:** Users can save frequently-used filter combinations as presets
         - Presets stored per-user
         - Users can name their presets
         - Users can edit or delete their presets
       ```

       **AFTER:**
       ```
       * **FR5:** Users can save and share filter combinations as presets
         - Presets can be personal (private) or team-shared
         - Any team member can create shared presets
         - Shared presets visible to all team members
         - Users can name their presets (personal and shared)
         - Users can edit or delete their own presets
         - [OPEN QUESTION: Can users edit or delete team-shared presets
           created by others?]
       ```

       **Rationale:** User testing revealed strong need for team collaboration on filters
       **Type:** Addition + Modification
       **Impact:** Requires new user story for sharing functionality

       ---

       ### Change 2: Add Search Refinement (Section 2 - User Journey)

       **BEFORE:**
       [Primary workflow ends at "System displays filtered results"]

       **AFTER:**
       ```
       **Primary Workflow:** Search and Filter Tasks
       [... existing steps ...]
       4. System displays filtered results
       5. User [NEW] enters additional search term to refine results
       6. System [NEW] searches within current results and updates display
       7. User reviews refined results
       ```

       **Rationale:** User testing showed this is a key workflow pattern
       **Type:** Addition
       **Impact:** Requires new user story for search refinement feature

       ---

       ### Change 3: Add Search Refinement Requirement (Section 3)

       **BEFORE:**
       [Not present]

       **AFTER:**
       ```
       * **FR8:** Users can refine search results with additional search terms
         - Refinement searches within current results only
         - Works with all search result sets (text search, filtered results)
         - Preserves original search context
         - Users can clear refinement to return to original results
         - UI indication: [CLARIFICATION NEEDED: how should refined search be
           visually indicated?]
       ```

       **Rationale:** User testing showed essential workflow
       **Type:** Addition
       **Impact:** Requires new user story

       ---

       ### Change 4: Update Performance Requirements (Section 3)

       **BEFORE:**
       ```
       * **NFR2:** Search must provide real-time results as user types
         - Results update on each keystroke
         - Maximum acceptable latency: 100ms
       ```

       **AFTER:**
       ```
       * **NFR2:** Search provides results within acceptable timeframe
         - Results can display with 1-2 second delay
         - Delay allows for more complex search algorithms
         - Show loading indicator during search
         - No need for real-time keystroke updates
       ```

       **Rationale:** User testing showed 1-2s delay is acceptable, simplifies implementation
       **Type:** Modification + Clarification
       **Impact:** Technical spec can use simpler architecture (no real-time requirements)

       ---

       ### Change 5: Resolve Open Questions (Section 4)

       **BEFORE:**
       ```
       - [ ] Q1: Should saved filters be shareable across teams?
       - [ ] Q2: Real-time search or acceptable delay?
       ```

       **AFTER:**
       ```
       - [x] Q1: Should saved filters be shareable across teams?
         - **Answer:** Yes, any team member can create and share filters with their team
       - [x] Q2: Real-time search or acceptable delay?
         - **Answer:** 1-2 second delay is acceptable based on user testing
       ```

       ---

       ### Change 6: Add New Open Questions (Section 4)

       **NEW QUESTIONS:**
       ```
       - [ ] Q3: Can users edit or delete team-shared filter presets created by others?
         - **Owner:** Product
         - **Needed by:** Before technical design
         - **Context:** Related to FR5 (filter sharing)

       - [ ] Q4: How should search refinement be visually indicated in the UI?
         - **Owner:** Design
         - **Needed by:** Before UI implementation
         - **Context:** Related to FR8 (search refinement)
       ```

       **Rationale:** New questions emerged from the new requirements
       **Type:** Addition

       ---

       **Summary of Changes:**
       - 3 sections updated
       - 2 requirements added (FR8, updated FR5)
       - 1 requirement modified (NFR2)
       - 2 open questions resolved
       - 2 new questions added
       - 1 workflow extended

       Does this look correct? Should I proceed with updating the Linear project?

User: Yes, update it

Agent: ✅ Product specification refined successfully!

       **Linear Project:** PROJ-42 - Advanced Search with Filters
       **URL:** [Project URL]

       **Refinement Summary:**

       **Sections Modified:** 3 sections
       - Section 2: User Journey - ✏️ Updated (added refinement workflow)
       - Section 3: Requirements - ✏️ Updated (2 added, 1 modified)
       - Section 4: Open Questions - ✏️ Updated (2 resolved, 2 added)

       **Key Changes Made:**

       1. **Filter Sharing Added**
          - What changed: FR5 now includes team sharing capability
          - Why: User testing revealed strong collaboration need
          - Type: Addition + Modification
          - Impact: Requires new user story

       2. **Search Refinement Added**
          - What changed: New FR8 and extended workflow
          - Why: Key workflow pattern identified in user testing
          - Type: Addition
          - Impact: Requires new user story

       3. **Performance Requirements Relaxed**
          - What changed: Real-time → 1-2 second delay acceptable
          - Why: User testing validated acceptable delay
          - Type: Modification + Clarification
          - Impact: Technical spec can be simplified

       **Scope Changes:**

       **Added to Scope:** 2 new capabilities
       - Filter sharing across team members
       - Search-within-search refinement

       **Clarified:** 1 vague requirement
       - Performance requirements (real-time → 1-2s delay)

       **Questions Resolved:** 2 questions
       - ✅ Q1: Saved filters should be shareable (YES)
       - ✅ Q2: 1-2 second delay is acceptable (YES)

       **New Questions Added:** 2 questions
       - ❓ Q3: Can users edit shared filters created by others?
       - ❓ Q4: How to visually indicate search refinement?

       **Impact on User Stories:**

       ⚠️ These changes require story updates:
       - PROJ-44: Filter Presets - Needs update for sharing capability
       - NEW STORY NEEDED: Search refinement feature

       Consider running `/refine-decomposition PROJ-42` to:
       - Update PROJ-44 with sharing requirements
       - Add new story for search refinement

       **Impact on Technical Specification:**

       ⚠️ The technical specification may need review due to:
       - Sharing permissions/authorization for filters
       - Search refinement implementation approach
       - Relaxed performance requirements (simpler architecture possible)

       Consider running `/refine-technical-spec PROJ-42` to update technical details.

       **Recommended Actions:**
       1. Review the updated Product Spec in Linear: [URL]
       2. Run `/refine-decomposition PROJ-42` to update user stories
       3. Run `/refine-technical-spec PROJ-42` after reviewing impact
       4. Resolve Q3 and Q4 before implementation
       5. Communicate changes to the team

       The product specification is now updated with user testing insights! 🎉
```

### Example: Conversational Refinement

```
User: /refine-feature-brief PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search with Filters

       [Shows current state]

       What prompted this product spec refinement?

       **Option A: Refinement Meeting Transcript**
       **Option B: Describe Changes Conversationally**

User: Option B
      We need to remove the "save filter presets" feature from scope.
      It's too complex for V1.

Agent: Got it - removing "save filter presets" from scope for V1.
       Let me understand the change:

       1. Should this feature be:
          - Moved to "Out of Scope" (not doing it)?
          - Moved to "Future Enhancements" (doing it later)?

       2. What's the reason for descoping?
          - Too complex technically?
          - Lower priority than other features?
          - Timeline constraints?

       3. Does removing this affect any success metrics or user workflows?

       4. Are there any user stories already created for this feature?

User: Move to Future Enhancements - we'll do it in V2
      Timeline constraints - need to ship faster
      Yes, it might affect our usage metrics
      Yes, there's a story PROJ-45 for this

Agent: Perfect! Here are the proposed changes:

       [Shows before/after for affected sections]

       **Impact on User Stories:**
       - PROJ-45: Filter Presets - Should be moved to backlog/future

       **Impact on Success Metrics:**
       - May need to adjust "Search usage" metric if presets were key to adoption

       Does this look correct?

User: Yes, but keep the search usage metric - we'll hit it other ways

Agent: [Updates and provides comprehensive summary]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide Linear Project ID
- **Reads from Linear**: Fetches existing Product Spec from project description
- **Updates Linear**: Modifies the Product Spec section in project description
- **Shows Before/After**: Clear comparison of what's changing and why
- **Tracks Scope Changes**: Explicitly identifies additions, deletions, clarifications
- **Tracks Impact**: Identifies affected user stories and technical specs
- **Validates Uncertainties**: Applies uncertainty markers to new/vague content
- **Preserves Context**: Keeps Technical Spec and other sections intact

This conversational approach ensures product specs stay aligned with stakeholder feedback, user testing insights, and evolving business needs, while maintaining clear traceability of what changed and why.
