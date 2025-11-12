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
6. Discuss decomposition strategy
7. Ask clarifying questions about boundaries
8. Create user stories in Jira
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

### Step 7: Discuss Decomposition Strategy

Based on the feature spec, technical spec, and transcript (if available), propose a decomposition approach:

```markdown
Based on the feature spec and technical spec, I see several ways we could decompose this:

**Option A: By User Workflow** (Recommended)
Break into stories where each story delivers one complete user workflow end-to-end.

Example stories:
1. [Workflow 1 from feature spec]
2. [Workflow 2 from feature spec]
3. [Workflow 3 from feature spec]

Pros: Each story delivers user value, easy to demo
Cons: Stories might be larger, could span frontend and backend

**Option B: By Technical Layer**
Break into frontend stories, backend stories, etc.

Example stories:
1. Backend API for [feature]
2. Frontend UI for [feature]
3. Integration with [system]

Pros: Clear technical boundaries, easier to parallelize
Cons: No story delivers complete user value alone

**Option C: By Component/Entity**
Break into stories by major components or data entities.

Example stories:
1. [Entity A] CRUD operations
2. [Entity B] CRUD operations
3. [Entity C] integration

Pros: Clear scope per story
Cons: May not align with user workflows

**Option D: Hybrid Approach**
Combine approaches - e.g., first story is end-to-end minimal, then add enhancements.

Example stories:
1. Basic [feature] with minimal functionality (end-to-end)
2. Add [enhancement 1]
3. Add [enhancement 2]

Pros: First story delivers value, subsequent stories add increments
Cons: Requires careful scoping of "minimal"

Which decomposition approach makes sense for this feature, or do you have a different approach in mind?
```

[If user selects an approach or suggests their own, proceed with that strategy]

### Step 8: Ask Clarifying Questions

Based on the chosen decomposition strategy, ask targeted questions:

**Questions About Story Boundaries:**
```markdown
Let me clarify the story boundaries:

1. **Story Scope:**
   [If stories span layers:] Should story "[Story Name]" include both frontend and backend, or split them?

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

### Step 10: Create User Stories in Jira

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

### Step 11: Provide Comprehensive Summary

After creating all stories, provide a detailed summary:

```markdown
✅ Feature decomposed successfully!

**Confluence Page:** [Page Title] - [Page URL]
**Jira Project:** [PROJECT-KEY]

**Stories Created:** [N] user stories

**Story Breakdown:**

1. **[ISSUE-KEY]: [Story Title]** - [URL]
   - Scope: [Frontend/Backend/Full-stack]
   - Focus: [1-line description]
   - ACs: [N] acceptance criteria
   - Dependencies: [None or list]
   - Labels: [Labels applied]

2. **[ISSUE-KEY]: [Story Title]** - [URL]
   - Scope: [Frontend/Backend/Full-stack]
   - Focus: [1-line description]
   - ACs: [N] acceptance criteria
   - Dependencies: [None or list]
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
1. Review all stories in Jira and verify acceptance criteria
2. Prioritize stories in your backlog
3. Estimate stories if your team uses estimation
4. Assign stories to upcoming sprints

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
2. **Propose Options**: Offer decomposition strategies with pros/cons
3. **Explain Reasoning**: When suggesting story boundaries, explain why
4. **Confirm Before Creating**: Show proposed breakdown and get approval
5. **Reference Documentation**: Connect stories to Confluence page
6. **Discuss Dependencies**: Make dependencies explicit
7. **Consider Team Workflow**: Ask about team's preferred story size and scope

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

### Decomposition Strategies

**By User Workflow (Recommended):**
- Each story = one complete user journey
- Pros: Delivers user value, easy to demo, aligns with feature spec
- Cons: May span multiple layers, could be larger
- Best for: Features with clear user workflows

**By Technical Layer:**
- Separate stories for backend, frontend, integration
- Pros: Clear technical boundaries, easy to parallelize
- Cons: No story delivers complete value alone
- Best for: Large features with independent frontend/backend teams

**By Component/Entity:**
- Each story = one major component or entity
- Pros: Clear scope, manageable size
- Cons: May not align with user workflows
- Best for: CRUD-heavy features, data modeling features

**Hybrid (Recommended for Complex Features):**
- First story: Minimal end-to-end (walking skeleton)
- Subsequent stories: Add enhancements, edge cases, optimizations
- Pros: First story delivers value, subsequent stories are incremental
- Cons: Requires careful scoping of "minimal"
- Best for: Complex features, uncertain requirements

### Label Strategy

Apply these labels to help categorize stories:

**Always Apply:**
- `user-story` - Marks as a user story (vs bug, task, etc.)

**Technical Scope:**
- `frontend` - Has UI components
- `backend` - Has API/service layer
- `database` - Has data model changes
- `integration` - Integrates with external systems

**Feature Areas:**
- `api` - API endpoint changes
- `ui` - User interface changes
- `auth` - Authentication/authorization
- `reporting` - Reports or exports
- `search` - Search functionality

**Cross-Cutting:**
- `performance` - Performance-critical
- `security` - Security implications
- `accessibility` - Accessibility requirements

## Error Handling

If something goes wrong:

1. **No Product Spec in Confluence**: Warn but continue using Confluence page content
2. **No Technical Spec in Confluence**: Note that it's optional, continue with Product Spec
3. **Jira Project Not Found**: List available projects and ask user to select
4. **Story Issue Type Not Available**: List available issue types and ask which to use
5. **Unclear Boundaries**: Ask specific questions about how to split
6. **Incomplete Transcript**: Identify gaps and work conversationally to fill them

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

       **Decomposition Approach:**
       Hybrid - first story is minimal end-to-end for basic search, then
       incremental enhancements for filters.

       Let me clarify some boundaries:

       1. Stories 1 and 2 are split by layer - should they be combined into
          one end-to-end story instead?

       2. Story 3 includes both backend and frontend for status filter - should
          story 4 also include both layers, or split them?

       3. Should error handling be included in each story's ACs, or separate
          stories?

User: 1. Keep them split - we have separate teams
      2. Story 4 should also include both layers
      3. Include error handling in each story

Agent: Perfect! Here's the final decomposition:

       [Shows 5 stories with details]

       Does this look good?

User: Yes, create them

Agent: Creating user stories in Jira Project PROJ...

       ✅ Created PROJ-42: Basic text search - Backend API
       ✅ Created PROJ-43: Basic text search - Frontend UI
       ✅ Created PROJ-44: Add status filter
       ✅ Created PROJ-45: Add assignee and date filters
       ✅ Created PROJ-46: Save filter presets

       ✅ Feature decomposed successfully! [Shows summary]
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

Agent: Based on the feature spec, I see several ways to decompose this:

       **Option A: By User Workflow** (Recommended)
       1. Basic text search (end-to-end)
       2. Add filter by status (end-to-end)
       3. Add filter by assignee (end-to-end)
       4. Save filter presets (end-to-end)

       Pros: Each delivers user value
       Cons: Each spans frontend and backend

       **Option B: By Technical Layer**
       1. Backend API for search and filters
       2. Frontend UI for search
       3. Frontend UI for filters
       4. Filter persistence

       Pros: Clear technical boundaries
       Cons: No story delivers complete value alone

       Which approach fits your team better?

User: Option A, but can we split the first story into backend and frontend?
      We have separate teams.

Agent: Absolutely! So we'll use workflow-based decomposition, but split the
       first story by layer. Here's the updated breakdown:

       1. Basic text search - Backend API
       2. Basic text search - Frontend UI
       3. Add filter by status (backend + frontend)
       4. Add filter by assignee and date (backend + frontend)
       5. Save filter presets (backend + frontend)

       [Shows details for each story]

       Does this work for your team structure?

User: Perfect!

Agent: Creating stories in Jira...
       [Creates stories and provides summary]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide Confluence Page ID/URL
- **Reads from Confluence**: Fetches both Product and Technical specs from Confluence page
- **Creates in Jira**: Creates user stories as Jira issues with proper linking
- **Transcript is Optional**: Preferred but can work conversationally
- **Proposes Options**: Always offers decomposition strategies
- **Confirms Before Creating**: Shows proposed breakdown for approval
- **Complete ACs**: Every story gets comprehensive acceptance criteria
- **Maps to Specs**: References both Product and Technical specs from Confluence
- **Includes Dependencies**: Makes dependencies explicit with Jira issue keys
- **Suggests Order**: Recommends implementation order
- **Links Back**: Stories link back to Confluence page for full context

This conversational approach ensures stories are well-thought-out, properly scoped, and have comprehensive acceptance criteria while being engaging and collaborative.
