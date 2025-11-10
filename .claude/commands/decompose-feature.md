---
description: Decompose feature into user stories through conversational planning
---

Decompose a feature (Linear Project) into independently deliverable user stories using a conversational, engaging approach.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Linear Project ID as argument
2. Fetch project details and analyze current state
3. Ask if there's a decomposition meeting transcript
4. Analyze transcript or work conversationally
5. Discuss decomposition strategy
6. Ask clarifying questions about boundaries
7. Create user stories in Linear
8. Provide clear summary

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
- Feature Spec: [✅ path or ❌ Not found]
- Technical Spec: [✅ path or ❌ Not found]

**Current User Stories:** [N] stories
[If stories exist, list them:]
- [ISSUE-1]: [Title] - [Status]
- [ISSUE-2]: [Title] - [Status]

[If stories already exist, show warning:]
⚠️ This project already has [N] user stories. This command will ADD NEW stories to the project. If you want to modify existing stories, use `/refine-decomposition [PROJECT-KEY]` instead.

[If no stories, show:]
✅ Ready to decompose into user stories.
```

### Step 3: Read Documentation

Read all available documentation to understand the feature:

**Feature Spec (if available):**
- Feature overview and business value
- Target users
- User workflows
- Functional requirements
- Non-functional requirements
- Business rules and validation
- Scope boundaries

**Technical Spec (if available):**
- Architecture decisions
- Data models
- API contracts
- UI components
- Technical constraints

### Step 4: Request Decomposition Meeting Input

Ask user if they have a decomposition meeting:

```markdown
Before I decompose this feature into user stories, did you have a story decomposition or planning meeting?

**Option A: Yes, I have a transcript** - Paste your decomposition meeting transcript
**Option B: No, let's decompose it together** - I'll help you break it down conversationally

Which would you prefer?
```

### Step 5: Analyze Decomposition Input

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

Work through decomposition conversationally - see Step 6.

### Step 6: Discuss Decomposition Strategy

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

### Step 7: Ask Clarifying Questions

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

### Step 8: Propose Story Breakdown

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

### Step 9: Create User Stories in Linear

**IMPORTANT - Uncertainty Handling in Stories:**

Before creating stories, review the feature spec and technical spec for any remaining uncertainty markers (`[OPEN QUESTION]`, `[DECISION PENDING]`, `[CLARIFICATION NEEDED]`).

**If critical uncertainties still exist:**
- Warn the user that stories may need refinement once uncertainties are resolved
- Consider adding a note in the story description referencing the open question
- Flag the story with a "blocked" or "needs-clarification" label

**For each story, create with these guidelines:**
- If an AC references an `[OPEN QUESTION]` from the feature spec, note it in the story
- If implementation depends on a `[DECISION PENDING]` from the technical spec, add to Dependencies section
- Stories with unresolved uncertainties should be marked for refinement

For each approved story, create a Linear issue with complete details:

```markdown
Creating user stories in Linear Project [PROJECT-KEY]...

[For each story, show progress:]
✅ Created [ISSUE-XX]: [Story Title]
✅ Created [ISSUE-YY]: [Story Title]
[Continue for all stories]
```

**Linear Issue Format:**

**Title:** [Clear, action-oriented title, 3-7 words]

**Description:**
Create the user story description using the template from @.claude/templates/user-story.md

Fill in all sections based on the story scope and information from the feature and technical specs.

**Linear Issue Settings:**
- **Project:** [PROJECT-KEY]
- **Team:** [Team from project]
- **Labels:**
  - "user-story" (always)
  - [Additional labels from feature: "frontend", "backend", "api", "ui", "integration", etc.]
- **State:** "Backlog" (or ask user for preferred initial state)
- **Priority:** [If priority was discussed, set it; otherwise leave default]
- **Estimate:** [If team uses estimates and size was discussed]

### Step 10: Provide Comprehensive Summary

After creating all stories, provide a detailed summary:

```markdown
✅ Feature decomposed successfully!

**Linear Project:** [PROJECT-KEY] - [Project Name]
**URL:** [Project URL]

**Stories Created:** [N] user stories

**Story Breakdown:**

1. **[ISSUE-XX]: [Story Title]** - [URL]
   - Scope: [Frontend/Backend/Full-stack]
   - Focus: [1-line description]
   - ACs: [N] acceptance criteria
   - Dependencies: [None or list]
   - Labels: [Labels applied]

2. **[ISSUE-YY]: [Story Title]** - [URL]
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
1. [ISSUE-XX]: [Title] - Foundation story, no dependencies
2. [ISSUE-YY]: [Title] - Builds on ISSUE-XX
3. [ISSUE-ZZ]: [Title] - Enhancement, can be done in parallel
[Continue with recommended order]

**Coverage:**
- ✅ All user workflows from feature spec covered
- ✅ All functional requirements addressed
- ✅ Error handling and validation included
- ✅ Edge cases and empty states covered
- ✅ Non-functional requirements distributed across stories

**Next Steps:**

**Immediate:**
1. Review all stories in Linear and verify acceptance criteria
2. Prioritize stories in your backlog
3. Estimate stories if your team uses estimation
4. Assign stories to upcoming sprints

**For Implementation:**
1. Start with: [ISSUE-XX] - [Title]
2. Create TDD plan (optional): `/plan-user-story [ISSUE-XX]`
3. Implement story (optional): `/implement-story docs/specs/.../story_[ISSUE-XX]_tdd_tasks.md`

**For Refinement:**
If you need to adjust the decomposition (split, merge, add stories):
- Use `/refine-decomposition [PROJECT-KEY]`

The feature is now fully decomposed and ready for sprint planning and implementation! 🎉
```

## Guidelines

### Conversational Best Practices

1. **Show Current State**: Always display project state before asking questions
2. **Propose Options**: Offer decomposition strategies with pros/cons
3. **Explain Reasoning**: When suggesting story boundaries, explain why
4. **Confirm Before Creating**: Show proposed breakdown and get approval
5. **Reference Documentation**: Connect stories to feature spec and technical spec
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

1. **No Feature Spec**: Warn but continue using Linear project description
2. **No Technical Spec**: Warn but continue without technical references
3. **Stories Already Exist**: Warn and ask if user wants to continue or use `/refine-decomposition`
4. **Unclear Boundaries**: Ask specific questions about how to split
5. **Incomplete Transcript**: Identify gaps and work conversationally to fill them

## Examples

### Example: Transcript-Based Decomposition

```
User: /decompose-feature PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search with Filters

       Current Documentation:
       - Feature Spec: ✅ docs/features/advanced_search.md
       - Technical Spec: ✅ docs/specs/proj_42/technical_spec.md

       Current User Stories: 0 stories
       ✅ Ready to decompose into user stories.

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
          stories 4 also include both layers, or split them?

       3. Should error handling be included in each story's ACs, or separate
          stories?

User: 1. Keep them split - we have separate teams
      2. Story 4 should also include both layers
      3. Include error handling in each story

Agent: Perfect! Here's the final decomposition:

       [Shows 5 stories with details]

       Does this look good?

User: Yes, create them

Agent: [Creates stories and provides summary]
```

### Example: Conversational Decomposition

```
User: /decompose-feature PROJ-42

Agent: I found Linear Project PROJ-42: Advanced Search with Filters

       [Shows current state]

       Did you have a decomposition meeting?

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

Agent: [Creates stories and provides summary]
```

## Important Notes

- **Requires $ARGUMENTS**: Must provide Linear Project ID
- **Transcript is Optional**: Preferred but can work conversationally
- **Proposes Options**: Always offers decomposition strategies
- **Confirms Before Creating**: Shows proposed breakdown for approval
- **Complete ACs**: Every story gets comprehensive acceptance criteria
- **Maps to Specs**: References feature spec and technical spec
- **Includes Dependencies**: Makes dependencies explicit
- **Suggests Order**: Recommends implementation order

This conversational approach ensures stories are well-thought-out, properly scoped, and have comprehensive acceptance criteria while being engaging and collaborative.
