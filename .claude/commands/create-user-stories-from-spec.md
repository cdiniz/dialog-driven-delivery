---
description: Decompose feature into user stories through conversational planning
---

Decompose a feature (Confluence Page) into independently deliverable user stories in Jira using a conversational, engaging approach.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Confluence Page ID/URL as argument
2. Fetch page details and analyze specifications
3. Ask for target Jira project key
4. Ask if there's a decomposition meeting transcript
5. Analyze transcript or work conversationally
6. Propose workflow-based story breakdown
7. Ask clarifying questions about boundaries
8. Create Epic and user stories in Jira
9. Provide clear summary

## Steps

### Step 1: Get Page ID from Arguments

The command accepts the Confluence Page as `$ARGUMENTS`:
- Page ID (e.g., `123456789`)
- Page URL (e.g., `https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789`)
- Page Title (will search for it)

**Use MCP Tool:** `mcp__atlassian__getConfluencePage` to fetch the page content.

### Step 2: Fetch and Analyze Page

Query Confluence for the page and display current state:

```markdown
I found Confluence Page: [Page Title]

**Page:** [Page Title]
**URL:** [Confluence Page URL]
**Space:** [Space name]

**Product Spec:** [✅ Found in page or ❌ Not found]
**Technical Spec:** [✅ Found in page or ⏳ Minimal or ❌ Not found]

**Existing Jira Stories:** Checking for linked stories...
[If stories exist, list them after querying Jira]

[If no specs found, show warning:]
⚠️ I couldn't find Product and Technical Specifications in this Confluence page.
I recommend ensuring the page contains both specs created by `/create-spec` before decomposing.

[If specs found:]
✅ Ready to decompose into user stories.
```

### Step 3: Ask for Jira Project

Ask which Jira project to create stories in:

```markdown
Which Jira project should I create the user stories in?

**Jira Project Key:** [Ask for project key, e.g., "PROJ", "ENG", "PROD"]

If you're not sure, I can list available Jira projects for you.
```

**Use MCP Tool:** `mcp__atlassian__getVisibleJiraProjects` if user needs to see available projects.

Once project key is provided, verify it and get issue types:

**Use MCP Tool:** `mcp__atlassian__getJiraProjectIssueTypesMetadata` to get available issue types and ensure "Story" type exists.

### Step 4: Read Both Specs from Confluence Page

Read **both Product and Technical specifications** from the Confluence page content:

The Confluence page should contain both specs, structured as:

```markdown
## 📋 Product Specification
[Product spec content]

## 🔧 Technical Specification
[Technical spec content]
```

**Extract from Product Specification section:**
- Feature overview and business value
- Target users
- User workflows
- Functional requirements
- Non-functional requirements
- Business rules and validation
- Scope boundaries
- Open questions and assumptions

**Extract from Technical Specification section (if available):**
- Technical approach and architecture
- System changes (new components, modifications)
- Architecture diagrams
- Data models and database schema
- API contracts and endpoints
- UI components and interactions
- Integration points
- Testing requirements
- Technical open questions and assumptions

**If specs not found in Confluence page:**

If Product Spec not found:
- Warn: "⚠️ I couldn't find a Product Specification in the Confluence page. I recommend running `/create-spec` first. I'll proceed using the page content."

If Technical Spec is placeholder or not found:
- Note: "ℹ️ Technical Specification hasn't been created yet. I'll decompose based on Product Spec. For better technical guidance, consider running `/refine-spec [PAGE-ID]` first."

### Step 5: Request Decomposition Meeting Input

Ask user if they have a decomposition meeting:

```markdown
Before I decompose this feature into user stories, did you have a story decomposition or planning meeting?

**Option A: Yes, I have a transcript** - Paste your decomposition meeting transcript
**Option B: No, let's decompose it together** - I'll help you break it down conversationally

Which would you prefer?
```

### Step 6: Analyze Decomposition Input

**If transcript provided (Option A):**

Analyze the transcript and extract:
- **Proposed Stories:** List of stories discussed
- **Story Boundaries:** How the team discussed breaking things down
- **Priority/Order:** Any mentioned priority or sequence
- **Open Questions:** Any unresolved decomposition questions
- **Concerns:** Any concerns about story size or dependencies

Summarize findings:

```markdown
I've analyzed your decomposition meeting transcript. Here's what I found:

**Proposed Stories ([N] stories):**
1. [Story 1 name/description]
2. [Story 2 name/description]
3. [Story 3 name/description]
4. [Continue with all stories]

**Decomposition Approach:**
[How the team discussed breaking things down - by workflow, by component, by layer, etc.]

**Priority Order:**
[If discussed: priority or sequence]

**Open Questions from Meeting:**
- [Question 1 about decomposition]
- [Question 2 about decomposition]

**Concerns Raised:**
- [Concern 1 about story size/complexity/dependencies]
- [Concern 2 about story size/complexity/dependencies]
```

**If conversational (Option B):**

Work through decomposition conversationally - see Step 7.

### Step 7: Propose Workflow-Based Decomposition

Based on the feature spec, technical spec, and transcript (if available), propose a workflow-based decomposition where each story delivers one complete user workflow end-to-end.

```markdown
Based on the feature spec and technical spec, here's how I propose to break this down by user workflow:

**Proposed Stories ([N] stories):**

**Story 1: [Workflow 1 from feature spec]**
- Delivers: [What user value this provides]
- Scope: [Frontend/Backend/Full-stack]
- Key ACs: [Main scenarios]

**Story 2: [Workflow 2 from feature spec]**
- Delivers: [What user value this provides]
- Scope: [Frontend/Backend/Full-stack]
- Key ACs: [Main scenarios]

**Story 3: [Workflow 3 from feature spec]**
- Delivers: [What user value this provides]
- Scope: [Frontend/Backend/Full-stack]
- Key ACs: [Main scenarios]

[Continue for all workflows]

Each story delivers complete user value and can be demoed independently.

Before I finalize these, I have a few questions about the boundaries...
```

[Proceed directly to clarifying questions]

### Step 8: Ask Clarifying Questions

Based on the proposed workflow-based decomposition, ask targeted questions:

**Questions About Story Boundaries:**
```markdown
Let me clarify the story boundaries:

1. **Story Scope:**
   [If stories are workflows:] Should "[Workflow Name]" be one story or split into multiple steps?

2. **Dependencies:**
   Can these stories be implemented independently, or do some depend on others?

   If there are dependencies, what's the required order?

3. **Story Size:**
   Looking at the acceptance criteria, does story "[Story Name]" seem too large?

   Should we split it further? If so, how?

4. **Edge Cases:**
   Should error handling, validation, and edge cases be:
   - Included in each story's acceptance criteria?
   - Separate stories for complex error scenarios?

5. **Non-Functional Requirements:**
   Should performance, security, accessibility be:
   - Included in relevant functional stories?
   - Separate "technical debt" or "NFR" stories?

6. **Priority/Order:**
   What's the priority order for these stories?

   Which story should be implemented first?
```

[Adjust questions based on the specific feature and decomposition approach]

### Step 9: Propose Story Breakdown

Based on all gathered information, propose the final story breakdown:

```markdown
Perfect! Based on our discussion, here's how I propose to break down this feature:

**Story 1: [Story Title]**
- **Focus:** [What this story delivers]
- **Scope:** [Frontend/Backend/Full-stack]
- **Acceptance Criteria:** [N] scenarios covering:
  - [Main scenario]
  - [Error scenario]
  - [Edge case scenario]
- **Dependencies:** [None or references to other stories]
- **Estimated Scope:** [Small/Medium/Large]

**Story 2: [Story Title]**
- **Focus:** [What this story delivers]
- **Scope:** [Frontend/Backend/Full-stack]
- **Acceptance Criteria:** [N] scenarios covering:
  - [Main scenario]
  - [Error scenario]
  - [Edge case scenario]
- **Dependencies:** [None or references to other stories]
- **Estimated Scope:** [Small/Medium/Large]

[Continue for all stories]

**Total:** [N] stories

**Implementation Order:**
1. [Story X] - Foundation
2. [Story Y] - Builds on X
3. [Story Z] - Enhancement
[Continue with recommended order]

Does this decomposition look good, or would you like to adjust any stories?
```

[Wait for user confirmation or adjustments]

### Step 10: Create Epic in Jira

Before creating the individual stories, create an Epic that will serve as the parent for all stories in this feature:

```markdown
Creating Epic for this feature in Jira Project [PROJECT-KEY]...
```

**Use MCP Tool:** `mcp__atlassian__createJiraIssue`

**Epic Settings:**
- **projectKey:** [PROJECT-KEY from user]
- **issueTypeName:** "Epic"
- **summary:** [Feature name from Confluence page title]
- **description:**
  ```markdown
  Feature specification: [Confluence Page Title]

  [Brief overview from Product Spec - 1-2 sentences]

  ## Reference
  - **Confluence Spec:** [Page URL]
  - **Space:** [Space name]

  ## User Stories
  This Epic contains [N] user stories that deliver this feature incrementally.
  ```
- **labels:** ["feature", "epic", plus context labels from the feature]

**Store the Epic key** for linking stories in the next step.

```markdown
✅ Created Epic [EPIC-KEY]: [Feature Name]
   [Epic URL]

Now creating [N] user stories under this Epic...
```

### Step 11: Create User Stories in Jira

**CRITICAL - Jira Project Type Detection:**

Before creating stories, you should detect the Jira project type to use the correct Epic linking method:

1. **Ask the user**: "Is this a Team-managed (Next-Gen) or Company-managed (Classic) Jira project?"
2. Or **detect automatically**: Try Option 2 first (additional_fields), fall back to Option 1 if needed
3. **Default recommendation**: Use `additional_fields` approach (Option 2) as it works for most configurations

This is crucial because Epic-Story relationships work differently in different Jira project types.

**IMPORTANT - Uncertainty Handling in Stories:**

Before creating stories, review **both Product and Technical specs** from the Confluence page for any remaining uncertainty markers (`[OPEN QUESTION]`, `[DECISION PENDING]`, `[CLARIFICATION NEEDED]`). See @.claude/uncertainty-markers.md for complete marker definitions.

**If critical uncertainties still exist:**
- Warn the user that stories may need refinement once uncertainties are resolved
- Consider adding a note in the story description referencing the open question and linking to the Confluence page
- Flag the story with a "blocked" or "needs-clarification" label

**For each story, create with these guidelines:**
- If an AC references an `[OPEN QUESTION]` from the Product Spec, note it in the story with link to Confluence page
- If implementation depends on a `[DECISION PENDING]` from the Technical Spec, add to description with link
- Stories with unresolved uncertainties should be marked for refinement
- Link back to the Confluence page for full context

For each approved story, create a Jira issue with complete details:

```markdown
Creating user stories in Jira Project [PROJECT-KEY]...

[For each story, show progress:]
✅ Created [ISSUE-KEY]: [Story Title]
✅ Created [ISSUE-KEY]: [Story Title]
[Continue for all stories]
```

**Use MCP Tool:** `mcp__atlassian__createJiraIssue`

**Jira Issue Format:**

**Summary (Title):** [Clear, action-oriented title, 3-7 words]

**Description:**
Create the user story description using the template from @.claude/templates/user-story.md

Fill in all sections based on the story scope and information from the feature and technical specs.

**Structure:**
```markdown
**User Story:** As a [persona], I want [capability], so that [benefit]

**Value:** [What value this delivers to users/business]

**Confluence Spec:** [Link to Confluence page]

---

## Acceptance Criteria

**AC1: [Scenario name]**
**Given** [context]
**When** [action]
**Then** [expected outcome]

**AC2: [Scenario name]**
**Given** [context]
**When** [action]
**Then** [expected outcome]

[Continue with all ACs]

---

## Technical Notes

[Any technical considerations from technical spec]

**Dependencies:** [List other story keys if dependencies exist]

**References:**
- Confluence Spec: [Page URL]
- Related Technical Docs: [If applicable]
```

**Jira Issue Settings:**
- **projectKey:** [PROJECT-KEY from user]
- **issueTypeName:** "Story"
- **summary:** [Story title]
- **description:** [Full description in Markdown]
- **labels:** ["user-story", plus additional context labels like "frontend", "backend", "api", etc.]
- **priority:** [If priority was discussed, set it using priority field]

**CRITICAL - Epic-Story Linking:**

Jira has different approaches for linking Stories to Epics depending on project type. Here's how to use the MCP tool correctly:

**RECOMMENDED: Use additional_fields (works for most Jira configurations)**

```javascript
// When calling mcp__atlassian__createJiraIssue for a Story:
{
  cloudId: "[CLOUD-ID]",
  projectKey: "[PROJECT-KEY]",
  issueTypeName: "Story",
  summary: "[Story Title]",
  description: "[Story Description in Markdown]",
  additional_fields: {
    parent: {
      key: "[EPIC-KEY from Step 10]"  // e.g., "PROJ-41"
    }
  },
  labels: ["user-story", "frontend", "backend", ...]
}
```

**ALTERNATIVE: For Team-Managed (Next-Gen) Projects Only**

If the above doesn't work (very rare), try:
```javascript
{
  cloudId: "[CLOUD-ID]",
  projectKey: "[PROJECT-KEY]",
  issueTypeName: "Story",
  summary: "[Story Title]",
  description: "[Story Description in Markdown]",
  parent: "[EPIC-KEY from Step 10]",  // Direct parent field
  labels: ["user-story", ...]
}
```

**Implementation Strategy:**
1. **Default**: Always try `additional_fields` approach first (works 95% of the time)
2. **If it fails**: Create the story without parent, then inform user to link manually
3. **Never try both**: Pick one approach and stick with it for all stories in the Epic

**If Epic Linking Fails:**

If neither approach works and stories are created without Epic links:
1. Inform the user that stories were created successfully but Epic linking failed
2. Provide manual linking instructions:
   ```markdown
   ⚠️ Stories created but Epic linking failed. Please link manually:

   **In Jira:**
   1. Open each story ([STORY-KEY])
   2. Click on the "Epic" field or "Parent" field in the details
   3. Select or search for Epic [EPIC-KEY]
   4. Save the story

   **Or use bulk operations:**
   1. Go to Jira board or backlog
   2. Select all stories: [STORY-1], [STORY-2], etc.
   3. Click "Bulk Change" → "Edit Issues"
   4. Set "Parent" or "Epic Link" to [EPIC-KEY]
   ```

### Step 12: Provide Comprehensive Summary

After creating all stories, provide a detailed summary:

```markdown
✅ Feature decomposed successfully!

**Confluence Page:** [Page Title] - [Page URL]
**Jira Project:** [PROJECT-KEY]

**Epic Created:** [EPIC-KEY]: [Feature Name] - [Epic URL]
  - All user stories are linked to this Epic
  - Epic contains reference to Confluence specification

**Stories Created:** [N] user stories under Epic [EPIC-KEY]

**Story Breakdown:**

1. **[ISSUE-KEY]: [Story Title]** - [URL]
   - Parent Epic: [EPIC-KEY]
   - Scope: [Frontend/Backend/Full-stack]
   - Focus: [1-line description]
   - ACs: [N] acceptance criteria
   - Dependencies: [None or "Blocked by [ISSUE-KEY]" - documented in story description]
   - Labels: [Labels applied]

2. **[ISSUE-KEY]: [Story Title]** - [URL]
   - Parent Epic: [EPIC-KEY]
   - Scope: [Frontend/Backend/Full-stack]
   - Focus: [1-line description]
   - ACs: [N] acceptance criteria
   - Dependencies: [None or "Blocked by [ISSUE-KEY]" - documented in story description]
   - Labels: [Labels applied]

[Continue for all stories]

**Decomposition Approach:**
[Summary of the decomposition strategy used: by workflow, by layer, hybrid, etc.]

**Implementation Order:**
Based on dependencies and value delivery, recommended order:
1. [ISSUE-KEY]: [Title] - Foundation story, no dependencies
2. [ISSUE-KEY]: [Title] - Builds on previous story
3. [ISSUE-KEY]: [Title] - Enhancement, can be done in parallel
[Continue with recommended order]

**Coverage:**
- ✅ All user workflows from feature spec covered
- ✅ All functional requirements addressed
- ✅ Error handling and validation included
- ✅ Edge cases and empty states covered
- ✅ Non-functional requirements distributed across stories

**Next Steps:**

**Immediate:**
1. ✅ Review all stories in Jira and verify acceptance criteria
2. [If dependencies exist:] Create dependency links manually (see instructions above)
3. Prioritize stories in your backlog
4. Estimate stories if your team uses estimation
5. Assign stories to upcoming sprints

**For Implementation:**
1. Start with: [ISSUE-KEY] - [Title]
2. Create TDD plan (optional): `/plan-user-story [ISSUE-KEY]`
3. Implement story (optional): `/implement-story docs/specs/.../story_[ISSUE-KEY]_tdd_tasks.md`

**For Refinement:**
If you need to adjust the decomposition (split, merge, add stories):
- Use `/refine-decomposition [PROJECT-KEY]`

The feature is now fully decomposed and ready for sprint planning and implementation! 🎉
```

## Guidelines

### Conversational Best Practices

1. **Show Current State**: Always display page state before asking questions
2. **Propose Workflow-Based Breakdown**: Present stories based on user workflows from the feature spec
3. **Explain Reasoning**: When suggesting story boundaries, explain why
4. **Ask Clarifying Questions**: Adapt to team structure (split by layer if needed)
5. **Confirm Before Creating**: Show proposed breakdown and get approval
6. **Reference Documentation**: Connect stories to Confluence page
7. **Discuss Dependencies**: Make dependencies explicit

### Transcript Analysis Tips

1. **Extract Story Ideas**: Look for mentions of "story," "we should," "what if"
2. **Note Disagreements**: If team debated boundaries, capture both perspectives
3. **Identify Concerns**: Note concerns about story size, complexity, dependencies
4. **Find Priority**: Look for discussion about what to build first
5. **Spot Gaps**: Identify workflows or requirements not mentioned in decomposition

### Decomposition Best Practices

1. **Natural Boundaries**: Break at logical points (complete workflows, layers, entities)
2. **Independent Stories**: Minimize dependencies between stories
3. **End-to-End Value**: Each story should deliver visible value (especially first story)
4. **Consistent Size**: Aim for stories of similar size (adjust based on team velocity)
5. **Complete ACs**: Every story should have comprehensive acceptance criteria
6. **Cover All Cases**: Include happy path, errors, edge cases, empty states

### Acceptance Criteria Quality

1. **Use Gherkin Format**: Given-When-Then structure for clarity
2. **Descriptive Names**: AC titles should explain the scenario
3. **Specific Values**: Use actual data/values, not placeholders
4. **Exact Error Messages**: Include exact error text from feature spec
5. **Observable Behavior**: Focus on what users see/experience
6. **Complete Workflows**: Cover entire user journey, not just happy path
7. **Reference Requirements**: Map ACs back to feature spec requirements

### Story Size Guidelines

**Small Story (1-3 days):**
- Single UI component
- Single API endpoint
- Simple CRUD operation
- 3-5 acceptance criteria

**Medium Story (3-5 days):**
- Multiple related components
- Multiple related endpoints
- Complete workflow (simple)
- 5-8 acceptance criteria

**Large Story (5-10 days):**
- Complex workflow
- Multiple layers (frontend + backend + integration)
- Significant business logic
- 8-12 acceptance criteria

**Too Large (>10 days):**
- Should be split into smaller stories
- Ask user how to split

### Decomposition Strategy

**This command uses "By User Workflow" decomposition:**
- Each story = one complete user journey end-to-end
- Each story delivers user value independently
- Each story can be demoed to stakeholders
- Stories align naturally with the feature spec's user workflows

**Key Benefits:**
- Clear user value in every story
- Easy to prioritize by user impact
- Aligns with product requirements
- Natural mapping to feature spec workflows

**When workflows span multiple layers:**
If your team has separate frontend/backend teams, you can still split individual workflows by layer during the clarifying questions phase. The decomposition will adapt to your team structure while maintaining the workflow-based foundation.


## Error Handling

If something goes wrong:

1. **No Product Spec in Confluence**: Warn but continue using Confluence page content
2. **No Technical Spec in Confluence**: Note that it's optional, continue with Product Spec
3. **Jira Project Not Found**: List available projects and ask user to select
4. **Epic Issue Type Not Available**: Check available issue types, use "Story" with label "epic" as fallback
5. **Story Issue Type Not Available**: List available issue types and ask which to use
6. **Epic Creation Fails**: Provide Epic details for manual creation, continue with stories (without parent link)
7. **Epic-Story Linking Fails**: Stories created but not linked to Epic - provide manual linking instructions (see Step 11)
8. **Unclear Boundaries**: Ask specific questions about how to split
9. **Incomplete Transcript**: Identify gaps and work conversationally to fill them

## Examples

### Example: Transcript-Based Decomposition

```
User: /decompose-feature 123456789

Agent: I found Confluence Page: Advanced Search with Filters

       Product Spec: ✅ Found in page
       Technical Spec: ✅ Found in page

       Which Jira project should I create the user stories in?

User: PROJ

Agent: Great! I'll create stories in Jira project PROJ.

       Before I decompose this feature, did you have a story decomposition meeting?

       **Option A: Yes, I have a transcript**
       **Option B: No, let's decompose it together**

User: Option A
      [Pastes meeting transcript]

Agent: I've analyzed your decomposition meeting transcript. Here's what I found:

       **Proposed Stories (5 stories):**
       1. Basic text search backend API
       2. Basic text search frontend UI
       3. Add status filter (backend + frontend)
       4. Add assignee and date filters
       5. Save filter presets

       **Approach:**
       The team discussed splitting the first workflow (basic search) by layer
       since you have separate backend/frontend teams, then keeping subsequent
       filter workflows as full-stack stories.

       Let me clarify some boundaries:

       1. Should error handling be included in each story's ACs, or separate
          stories?

       2. Story 4 includes assignee AND date filters - should these be split
          into separate stories for smaller scope?

       3. What's the dependency order - does story 2 (frontend) need story 1
          (backend) completed first?

User: 1. Include error handling in each story
      2. Keep story 4 as is - both filters together is fine
      3. Yes, story 2 depends on story 1

Agent: Perfect! Here's the final decomposition:

       [Shows 5 stories with details]

       Does this look good?

User: Yes, create them

Agent: Creating Epic for this feature in Jira Project PROJ...

       ✅ Created Epic PROJ-41: Advanced Search with Filters
          https://yoursite.atlassian.net/browse/PROJ-41

       Now creating 5 user stories under this Epic...

       ✅ Created PROJ-42: Basic text search - Backend API (under Epic PROJ-41)
       ✅ Created PROJ-43: Basic text search - Frontend UI (under Epic PROJ-41)
       ✅ Created PROJ-44: Add status filter (under Epic PROJ-41)
       ✅ Created PROJ-45: Add assignee and date filters (under Epic PROJ-41)
       ✅ Created PROJ-46: Save filter presets (under Epic PROJ-41)

       ✅ Feature decomposed successfully!

       [Shows summary with Epic details and manual dependency linking instructions]
```

### Example: Conversational Decomposition

```
User: /decompose-feature Advanced Search

Agent: [Searches and finds Confluence page]
       I found Confluence Page: Advanced Search with Filters

       [Shows current state]

       Which Jira project should I create stories in?

User: ENG

Agent: Did you have a decomposition meeting?

       **Option A: Yes, I have a transcript**
       **Option B: No, let's decompose it together**

User: Option B

Agent: Based on the feature spec, here's how I propose to break this down by
       user workflow:

       **Proposed Stories (4 stories):**

       **Story 1: Basic text search**
       - Delivers: Users can search for items using text input
       - Scope: Full-stack (backend API + frontend UI)
       - Key ACs: Search input, results display, empty states, error handling

       **Story 2: Add filter by status**
       - Delivers: Users can filter search results by item status
       - Scope: Full-stack (backend filtering + frontend filter UI)
       - Key ACs: Status dropdown, filtered results, clear filters

       **Story 3: Add filter by assignee and date**
       - Delivers: Users can filter by assignee and date range
       - Scope: Full-stack (backend filtering + frontend filter UI)
       - Key ACs: Assignee selector, date pickers, multiple filters

       **Story 4: Save filter presets**
       - Delivers: Users can save and reuse their filter combinations
       - Scope: Full-stack (backend persistence + frontend preset UI)
       - Key ACs: Save preset, load preset, manage presets

       Each story delivers complete user value and can be demoed independently.

       Before I finalize these, a few questions:

       1. Story 1 spans both backend and frontend - should we split it into
          two stories (API + UI) or keep it as one end-to-end story?

       2. Should error handling and edge cases be included in each story's ACs?

       3. What's your preferred implementation order?

User: 1. Split story 1 into backend and frontend - we have separate teams
      2. Yes, include error handling in each story
      3. Backend first, then frontend, then the filter stories

Agent: Perfect! Here's the updated breakdown:

       1. Basic text search - Backend API
       2. Basic text search - Frontend UI (depends on story 1)
       3. Add filter by status (backend + frontend)
       4. Add filter by assignee and date (backend + frontend)
       5. Save filter presets (backend + frontend)

       [Shows details for each story with dependencies]

       Does this work for your team structure?

User: Yes, create them!

Agent: Creating Epic for this feature in Jira Project ENG...

       ✅ Created Epic ENG-100: Advanced Search with Filters
          https://yoursite.atlassian.net/browse/ENG-100

       Now creating 5 user stories under this Epic...

       ✅ Created ENG-101: Basic text search - Backend API
       ✅ Created ENG-102: Basic text search - Frontend UI
       ✅ Created ENG-103: Add filter by status
       ✅ Created ENG-104: Add filter by assignee and date
       ✅ Created ENG-105: Save filter presets

       ✅ Feature decomposed successfully!

       Epic: ENG-100
       Stories: 5 stories (ENG-101 to ENG-105)

       [Shows summary with manual dependency linking instructions]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide Confluence Page ID/URL
- **Reads from Confluence**: Fetches both Product and Technical specs from Confluence page
- **Creates Epic First**: Creates an Epic issue to organize all stories for the feature
- **Epic-Story Hierarchy**: All stories are linked to the Epic as parent
- **Creates in Jira**: Creates user stories as Jira issues with proper Epic linking
- **Dependencies Documented**: Dependencies are documented in story descriptions and Technical Notes sections
- **Manual Dependency Links**: Issue links (blocks/is blocked by) must be created manually in Jira (instructions provided in summary)
- **Transcript is Optional**: Preferred but can work conversationally
- **Workflow-Based Decomposition**: Always decomposes by user workflow for maximum value delivery
- **Adapts to Team Structure**: Can split workflows by layer during clarifying questions if needed
- **Confirms Before Creating**: Shows proposed breakdown for approval
- **Complete ACs**: Every story gets comprehensive acceptance criteria
- **Maps to Specs**: References both Product and Technical specs from Confluence
- **Explicit Dependencies**: Dependencies clearly documented in story descriptions with instructions for manual linking
- **Suggests Order**: Recommends implementation order based on dependencies
- **Links Back**: Epic and stories link back to Confluence page for full context

This streamlined, opinionated approach ensures stories are well-thought-out, deliver user value, and have comprehensive acceptance criteria while being fast and collaborative.
