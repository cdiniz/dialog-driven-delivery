---
description: Generate technical specification for Linear Project (feature)
---

Generate a comprehensive technical specification for a Linear Project using a conversational, engaging approach.

## Conversational Workflow

This command uses an **engaging, conversational approach**:
1. Accept Linear Project ID as argument
2. Fetch project details and analyze current state
3. Ask if there's a technical discussion transcript
4. Analyze transcript or work conversationally
5. Review codebase architecture
6. Ask clarifying technical questions
7. Generate technical spec with smart section selection
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

**Product Spec:** [✅ In Linear project description or ❌ Not found]
**Technical Spec:** [✅ In Linear project description or ⏳ Placeholder (ready to populate) or ❌ Not found]

**User Stories:** [N] stories in this project
- [ISSUE-1]: [Title]
- [ISSUE-2]: [Title]
- [Continue listing all stories]

[If no feature spec found in project description, warn: "⚠️ I recommend creating a feature spec first with `/generate-feature-brief`, but I can proceed with creating a technical spec based on the Linear project description and user stories."]
```

### Step 3: Read Feature Spec from Linear Project

Read the feature specification from the Linear project description:

The feature spec should be in the project description (created by `/generate-feature-brief`).

Extract key information from the project description:
  - User workflows
  - Functional requirements
  - Non-functional requirements
  - Business rules and validation
  - Dependencies and constraints
  - Compliance requirements
  - Open questions and assumptions

**If the project description contains the feature spec:**
- Parse the structured markdown sections
- Note any uncertainty markers that may affect technical decisions
- Extract requirements that need technical implementation

**If the project description is minimal:**
- Warn that the technical spec will be based on limited information
- Proceed using available information from project description and user stories

### Step 4: Analyze User Stories

Read all user stories from the Linear project:
- Extract acceptance criteria
- Identify technical requirements
- Note data models needed
- Identify API endpoints
- Spot UI components
- Find integration points
- Identify security considerations

### Step 5: Request Technical Discussion Input

Ask user if they have a technical design discussion:

```markdown
Before I create the technical spec, did you have a meeting to discuss the technical approach for this feature?

**Option A: Yes, I have a transcript** - Paste your technical design meeting transcript
**Option B: No, let's discuss it now** - I'll ask you technical questions

Which would you prefer?
```

### Step 6: Analyze Technical Input

**If transcript provided (Option A):**

Analyze the transcript and extract:
- **Architecture Decisions:** Component structure, layers, patterns
- **Technology Choices:** Frameworks, libraries, tools
- **Data Model Decisions:** Database schema, entities, relationships
- **API Design:** Endpoints, request/response formats, error handling
- **Frontend Approach:** Components, state management, routing
- **Integration Strategy:** Third-party services, webhooks, events
- **Security Approach:** Authentication, authorization, data protection
- **Performance Considerations:** Caching, optimization, scalability
- **Testing Strategy:** Unit, integration, e2e approaches
- **Deployment Approach:** Infrastructure, CI/CD, monitoring

Summarize findings:

```markdown
I've analyzed your technical discussion transcript. Here's what I found:

**Architecture:**
- [Key architectural decision 1]
- [Key architectural decision 2]

**Technology Stack:**
- [Technology 1 and its purpose]
- [Technology 2 and its purpose]

**Key Design Decisions:**
- [Decision 1]
- [Decision 2]
- [Decision 3]

[Continue with all extracted information]
```

**If conversational (Option B):**

Ask structured technical questions based on the feature type.

### Step 7: Review Codebase Architecture

Before asking questions, analyze the existing codebase:

```markdown
Let me review your codebase to understand existing patterns...

I've reviewed your codebase and found:

**Project Structure:**
- [Architecture pattern: MVC, Hexagonal, Layered, etc.]
- [Frontend framework and version]
- [Backend framework and version]
- [Database type and version]

**Existing Patterns:**
- API endpoints follow: [pattern found]
- Database models use: [ORM/pattern found]
- Frontend components use: [pattern found]
- State management: [approach found]
- Testing approach: [strategy found]

**Relevant Existing Code:**
- Similar feature: [path to similar feature]
- Reusable components: [paths to components]
- Shared utilities: [paths to utilities]

I'll create the technical spec following these established patterns.
```

### Step 8: Ask Clarifying Technical Questions

**IMPORTANT - Track Question Responses:**
As you ask clarifying technical questions, keep track of which ones the user answered and which they skipped or deferred. This tracking is critical for uncertainty marking in Step 10.

Based on the feature type, transcript analysis, and codebase review, ask targeted questions:

**For Backend/API Features:**
```markdown
Let me clarify some technical details:

1. **Data Model:**
   - [Question about database schema based on requirements]
   - [Question about relationships based on workflows]

2. **API Design:**
   - [Question about endpoint structure]
   - [Question about authentication/authorization]

3. **Performance:**
   - [Question about expected load/volume]
   - [Question about caching strategy]

4. **Error Handling:**
   - [Question about error scenarios]
   - [Question about retry/fallback logic]

[Continue with relevant questions]
```

**For Frontend Features:**
```markdown
Let me clarify the frontend approach:

1. **Component Structure:**
   - [Question about component hierarchy]
   - [Question about component reusability]

2. **State Management:**
   - [Question about state structure]
   - [Question about state persistence]

3. **User Experience:**
   - [Question about loading states]
   - [Question about error feedback]

4. **Data Fetching:**
   - [Question about when to fetch data]
   - [Question about caching/invalidation]

[Continue with relevant questions]
```

**For Integration Features:**
```markdown
Let me understand the integration requirements:

1. **External Service:**
   - [Question about service selection]
   - [Question about API credentials/auth]

2. **Integration Pattern:**
   - [Question about sync vs async]
   - [Question about webhooks vs polling]

3. **Error Handling:**
   - [Question about service unavailability]
   - [Question about retry strategy]

4. **Data Sync:**
   - [Question about data mapping]
   - [Question about conflict resolution]

[Continue with relevant questions]
```

### Step 9: Determine Relevant Sections

Based on the feature type and requirements, decide which optional sections to include:

**Always Include (Core):**
- Overview & Context
- Architecture Overview
- Testing Strategy
- Open Questions & Decisions
- References

**Conditionally Include (Optional):**

**Include "Data Models" if:**
- Feature creates/modifies database entities
- User stories mention data persistence
- Transcript discusses schema changes

**Include "API Contracts" if:**
- Feature creates/modifies API endpoints
- User stories describe API interactions
- Transcript discusses REST/GraphQL APIs

**Include "UI Components" if:**
- Feature has frontend elements
- User stories describe UI
- Transcript discusses components

**Include "State Management" if:**
- Feature has complex frontend state
- User stories mention state synchronization
- Transcript discusses Redux/Vuex/Context

**Include "Integration Points" if:**
- Feature integrates with third-party services
- User stories mention external systems
- Transcript discusses webhooks/events

**Include "Security Considerations" if:**
- Feature handles authentication/authorization
- Feature handles sensitive data
- User stories mention security requirements
- Transcript discusses security concerns

**Include "Monitoring & Observability" if:**
- Feature is performance-critical
- User stories mention SLAs
- Transcript discusses monitoring/alerts

**Include "Infrastructure/Deployment" if:**
- Feature requires infrastructure changes
- Transcript discusses deployment strategy
- Feature requires new services/containers

Explain your section selection:

```markdown
Based on this feature, I'll include these sections in the technical spec:

**Core Sections:**
- Overview & Context (always included)
- Architecture Overview (always included)
- Testing Strategy (always included)
- Open Questions & Decisions (always included)
- References (always included)

**Optional Sections:**
✅ **Data Models** - This feature creates new database tables for [entities]
✅ **API Contracts** - This feature adds [N] new API endpoints
✅ **UI Components** - This feature requires [N] new frontend components
❌ **State Management** - Not needed, state is simple and component-local
✅ **Security Considerations** - This feature handles [sensitive data/auth]
❌ **Monitoring & Observability** - Not performance-critical, standard monitoring is sufficient
❌ **Infrastructure/Deployment** - No infrastructure changes needed

[Explain reasoning for each decision]
```

### Step 10: Generate Technical Specification

**CRITICAL - Uncertainty Marker Policy:**

Before generating the spec, review the documentation in `.claude/uncertainty-markers.md`.

When generating the technical specification, you MUST follow these rules:

1. **If user didn't answer a technical question** → Use uncertainty markers:
   - `[DECISION PENDING: option A vs option B - see Open Questions QX]` - for architectural/technical choices
   - `[CLARIFICATION NEEDED: what needs defining]` - for vague technical requirements

2. **If you infer a technical approach** → Mark it explicitly:
   - `[ASSUMPTION: statement of what you're assuming based on codebase patterns]`

3. **If technology choice is uncertain** → Mark the decision:
   - `[DECISION PENDING: PostgreSQL vs MongoDB - see Q3]`

4. **NEVER make silent technical assumptions.** If you infer from codebase, mark with `[ASSUMPTION]`.

5. **Link all markers** → Every inline marker must have corresponding entry in:
   - Section 12 (Open Questions & Decisions) for `[DECISION PENDING]` and `[CLARIFICATION NEEDED]`
   - Appendix A (Technical Assumptions) for `[ASSUMPTION]`

**Examples:**

❌ BAD (silent technical decision):
```
Data will be stored in MongoDB with the following schema...
```

✅ GOOD (explicit decision marker):
```
Data will be stored in [DECISION PENDING: PostgreSQL vs MongoDB - see Q3] with the following schema...
```

❌ BAD (unmarked inference):
```
We'll use JWT tokens for authentication
```

✅ GOOD (explicit assumption):
```
We'll use [ASSUMPTION: JWT tokens based on existing auth pattern in codebase] for authentication
```

Now create a comprehensive technical spec with only relevant sections:

Use the technical specification template from @.claude/templates/technical-spec.md

Remember to only include the sections that are relevant based on Step 9 (Determine Relevant Sections). Fill in all included sections with information gathered from the project, feature spec, technical discussion, and codebase review.

### Step 10.5: Uncertainty Validation (NEW)

**CRITICAL STEP - Do not skip this!**

Before saving the technical spec, scan the generated specification and validate uncertainty markers:

1. **Count all uncertainty markers:**
   ```
   Uncertainty Marker Summary:
   - [DECISION PENDING]: X occurrences
   - [CLARIFICATION NEEDED]: Y occurrences
   - [ASSUMPTION]: Z occurrences

   Total uncertainties: [X+Y+Z]
   ```

2. **Verify each marker is tracked:**
   - Check that each `[DECISION PENDING]` and `[CLARIFICATION NEEDED]` has a corresponding entry in Section 12 (Open Questions & Decisions)
   - Check that each `[ASSUMPTION]` has a corresponding entry in Appendix A (Technical Assumptions)
   - List any markers that are NOT properly tracked

3. **Present summary to user:**
   ```markdown
   I've generated the technical specification with [N] uncertainty markers:

   **Technical Decisions Pending:** [X] items requiring architectural/technology decisions
   **Clarifications Needed:** [Y] items requiring more specific technical definitions
   **Technical Assumptions:** [Z] items inferred from codebase patterns that need validation

   [If uncertainties exist:]
   These technical uncertainties should be resolved before story decomposition. Would you like to:

   **Option A:** Resolve them now - I'll ask follow-up technical questions
   **Option B:** Leave them marked for resolution during sprint planning
   **Option C:** Review the spec first, then resolve

   Which would you prefer?
   ```

4. **If user chooses Option A (Resolve now):**
   - Go through each `[DECISION PENDING]` and `[CLARIFICATION NEEDED]`
   - Ask the user for technical decisions
   - Update the spec to replace markers with actual choices
   - Move resolved questions to "Decisions Made" in Section 12

5. **If user chooses Option B or C:**
   - Proceed to next step
   - Include uncertainty count in final summary

**Quality Gates:**

⚠️ **Warning if:**
- More than 5 `[DECISION PENDING]` markers exist (too many unresolved technical choices)
- Critical architecture decisions have `[DECISION PENDING]` markers (blocks decomposition)
- Database choice or major technology decisions are still pending

✅ **Acceptable:**
- A few `[ASSUMPTION]` markers based on codebase patterns (can validate during implementation)
- `[CLARIFICATION NEEDED]` on performance thresholds or scaling details (can refine during implementation)

### Step 11: Update Linear Project with Technical Spec

**Update the Linear project description** to add the Technical Specification section.

**Process:**

1. **Fetch the current project description** from Linear
2. **Locate the Technical Specification section** (should be the placeholder created by `/generate-feature-brief`)
3. **Replace the placeholder** with the complete technical specification
4. **Update the documentation status header** to mark Technical Spec as complete

**Updated Project Description Structure:**

```markdown
# Feature: [Feature Name]

## 📋 Product Specification

[Existing product spec - DO NOT MODIFY]

---

## 🔧 Technical Specification

[REPLACE placeholder with full technical spec from Step 10]

[Include all sections from technical spec template: Technical Approach, System Changes, Architecture, Technical Specifications, Integrations, Testing Requirements, Open Questions, etc.]
```

**IMPORTANT:**
- Preserve the entire Product Specification section unchanged
- Only replace the Technical Specification section
- Update the documentation status header with completion date and uncertainty counts
- The Linear project description is now the single source of truth for BOTH specs

### Step 12: Provide Comprehensive Summary

After completing all steps, provide a detailed summary:

```markdown
✅ Technical specification created successfully!

**Feature:** [Feature Name]
**Linear Project:** [PROJECT-KEY] - [Project URL]
**Specs Location:** Linear project description (Product + Technical specs)
[If local backup created:] **Local Backup:** `[path to backup file]`

**Sections Included:**

**Core Sections:**
- ✅ Overview & Context
- ✅ Architecture Overview with diagrams
- ✅ Testing Strategy
- ✅ Open Questions & Decisions
- ✅ References

**Optional Sections:**
[List which optional sections were included with brief reasoning]
- ✅ Data Models: [N] tables defined for [entities]
- ✅ API Contracts: [N] endpoints specified
- ✅ UI Components: [N] components specified
- ✅ Security Considerations: Covers [auth/data protection/etc.]
- ❌ State Management: Not needed (simple state)
- ❌ Monitoring: Standard monitoring sufficient

**Contents Summary:**
- [N] user stories covered with AC mapping
- [N] Mermaid diagrams (architecture, data flow, state, etc.)
- [N] API endpoints with complete request/response specs
- [N] database tables with schema and migrations
- [N] UI components with props and behavior
- [N] open technical questions to resolve
- [N] technical assumptions to validate

**Uncertainty Status:**
[If uncertainties exist:]
⚠️ This specification contains [N] technical uncertainties:
- [X] technical decisions pending (Section 12)
- [Y] clarifications needed for technical details (Section 12)
- [Z] technical assumptions based on codebase patterns (Appendix A)

[If critical decisions pending:]
🚨 **CRITICAL:** The following decisions must be resolved before story decomposition:
- [List critical DECISION PENDING items]

[If no uncertainties:]
✅ No unresolved technical uncertainties - specification is ready for story decomposition.

**Codebase Alignment:**
- Follows existing [architecture pattern] pattern
- Uses established [technology] stack
- Matches [coding conventions] conventions
- Integrates with [existing components]

**Collaboration:**
- Both Product and Technical specs are now in Linear: [Project URL]
- Team members can comment and collaborate on both specs in one place
- Update the Linear project description as technical decisions are made

**Next Steps:**
1. [If uncertainties exist:] Review and resolve technical uncertainties in the Technical Spec section (Open Questions) and validate assumptions
2. Share Linear project with development team for technical review
3. Team can comment directly on the Technical Spec section in Linear
4. When ready to break into stories: `/decompose-feature [PROJECT-KEY]` (reads both specs from Linear)
5. After stories created, start implementation: `/plan-user-story [ISSUE-ID]`

**Open Technical Questions:**
[List questions from Technical Spec section that need resolution - link to Linear project]

The Linear project now contains complete Product and Technical specifications, ready for team review and story decomposition.
```

## Guidelines

### Conversational Best Practices

1. **Check State First**: Always show current project state before asking questions
2. **Acknowledge Input**: Summarize what you found in transcripts before asking questions
3. **Explain Decisions**: When selecting sections, explain why you included/excluded them
4. **Review Codebase**: Always check existing patterns before asking questions
5. **Be Specific**: Ask concrete technical questions, not vague ones
6. **Reference ACs**: Connect technical decisions to acceptance criteria
7. **Provide Context**: Explain why you need certain information

### Transcript Analysis Tips

1. **Extract Decisions**: Look for architecture decisions, technology choices, patterns
2. **Note Trade-offs**: If transcript discusses pros/cons, capture both perspectives
3. **Identify Constraints**: Extract technical constraints and limitations
4. **Find Patterns**: Look for mentions of existing code to reuse
5. **Spot Gaps**: Identify technical details not discussed but needed

### Technical Spec Quality

1. **Use Actual Names**: No placeholders - use real field names, endpoint paths, component names
2. **Extract Error Messages**: Get exact error messages from acceptance criteria
3. **Follow Patterns**: Match existing codebase patterns and conventions
4. **Be Complete**: Include all sections needed, exclude irrelevant ones
5. **Map to ACs**: Every AC should map to implementation and tests
6. **Include Diagrams**: Use Mermaid for architecture, data flow, state, ERD
7. **Specify Exactly**: API contracts should have complete request/response with validation

### Smart Section Selection

1. **Analyze Before Deciding**: Review feature type, user stories, and transcript
2. **Include Only What's Needed**: Don't add sections just to be thorough
3. **Explain Reasoning**: Document why sections were included/excluded
4. **Cover Requirements**: Ensure all acceptance criteria are addressed somewhere
5. **Match Feature Type**: Backend features need different sections than frontend

### Codebase Review

1. **Find Patterns**: Look for similar existing features
2. **Extract Conventions**: Naming, structure, testing approaches
3. **Identify Reusable Code**: Components, utilities, services to reuse
4. **Understand Stack**: Framework versions, libraries, tools in use
5. **Match Style**: Follow existing code style and architecture

### Question Strategy

**Backend/API Features - Ask About:**
- Data model design
- API endpoint structure
- Authentication/authorization approach
- Error handling strategy
- Performance requirements
- Caching strategy

**Frontend Features - Ask About:**
- Component hierarchy
- State management approach
- User experience details
- Data fetching strategy
- Loading and error states

**Integration Features - Ask About:**
- External service selection
- Integration pattern (sync/async)
- Error/failure handling
- Data mapping
- Retry/fallback strategy

## Error Handling

If something goes wrong:

1. **No Feature Spec in Linear**: Warn but continue using Linear project description and user stories
2. **No User Stories**: Warn that decomposition should happen first, but continue
3. **Can't Determine Sections**: Ask user which sections they want
4. **Incomplete Transcript**: Identify gaps and ask targeted questions
5. **No Codebase Access**: Proceed without pattern matching, ask more questions

## Important Notes

- **Requires $ARGUMENTS**: Must provide Linear Project ID
- **Transcript is Optional**: Preferred but can work conversationally
- **Smart Section Selection**: Only include relevant sections, explain reasoning
- **Codebase Integration**: Always review existing code to match patterns
- **AC Mapping**: Every acceptance criterion should map to implementation
- **Multiple Interaction Points**: Check state, analyze transcript, ask questions, confirm sections
- **Diagrams Required**: Always include Mermaid diagrams for architecture and data flow

This conversational approach ensures the technical spec is comprehensive, follows project conventions, and provides clear implementation guidance while being engaging and collaborative.