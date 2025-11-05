# Spec-Driven Product Development Workflow

A comprehensive, project-agnostic methodology for building software products through documentation-first development with Product Requirements Documents (PRDs), feature specifications, and technical design. Optionally includes AI-assisted TDD implementation with Claude Code.

## Philosophy

This workflow emphasizes:

1. **Specification-First**: Start with clear product requirements and technical design before writing code
2. **Incremental Delivery**: Break features into independently deliverable user stories
3. **Quality Through Design**: Thoughtful architecture and specifications prevent issues before they occur
4. **Flexibility**: Use the parts that add value - structured TDD implementation is optional
5. **AI-Augmented Development**: Leverage Claude Code for specification generation and optional automated implementation

## Prerequisites

- **Claude Code** installed and configured
- **Linear** (or similar issue tracking) for managing user stories (optional)
- **Git** for version control
- **Testing framework** (optional, required only for automated TDD workflow in steps 4-5)

## Installation

Copy the `.claude/commands/` directory to your project:

```bash
# From this repository
cp -r .claude/commands /path/to/your/project/.claude/

# Or clone individual commands you need
mkdir -p /path/to/your/project/.claude/commands
cp .claude/commands/generate-prd.md /path/to/your/project/.claude/commands/
cp .claude/commands/create-feature-and-stories.md /path/to/your/project/.claude/commands/
cp .claude/commands/create-feature-spec.md /path/to/your/project/.claude/commands/
cp .claude/commands/plan-user-story.md /path/to/your/project/.claude/commands/
cp .claude/commands/implement-story.md /path/to/your/project/.claude/commands/
```

## The Complete Workflow

```
Product Idea
     │
     ├─ 1. Generate PRD (/generate-prd)
     │
     ▼
Product Requirements Document (Strategic Direction)
     │
     ├─ 2. Create Feature + User Stories (/create-feature-and-stories "feature description or transcript")
     │
     ▼
Linear Project (Feature) + Feature Spec + User Stories
     │
     ├─ 3. Create Technical Spec (/create-feature-spec PROJECT-KEY)
     │
     ▼
Technical Specification
     │
     ├─ 4. [OPTIONAL] Plan User Story (/plan-user-story ISSUE-ID)
     │
     ▼
TDD Task List
     │
     ├─ 5. [OPTIONAL] Implement Story (/implement-story path/to/tdd_plan.md)
     │
     ▼
Completed, Tested, Reviewed Code
```

**Note on Workflow Flexibility:**

Steps 1-3 establish the documentation foundation (PRD, Feature Spec, Technical Spec) which is valuable for any project.

Steps 4-5 are **optional** and provide a structured TDD approach:
- **Use them if**: You want a systematic TDD workflow with planning, implementation, review, and refinement
- **Skip them if**: You prefer your own development methodology or want to implement directly with Claude using the technical spec as a guide

The workflow is designed to be modular - use the parts that add value to your team's process.

---

## Slash Commands Reference

### 1. `/generate-prd`

**Purpose**: Create a comprehensive Product Requirements Document from a description, meeting transcript, or interactive discussion.

**When to use**: At the very beginning of a new product or major feature initiative.

**What it does**:
- Accepts optional description or meeting transcript
- Extracts information from transcript or asks questions interactively
- Generates a strategic PRD with:
  - Executive summary (vision, problem, solution, metrics)
  - Scope (MVP and out-of-scope items)
  - User personas
  - **Epics**: Not included - features are created on-demand from descriptions
  - Risk assessment and mitigations

**Example usage**:

Interactive mode (Claude asks questions):
```
/generate-prd
```

With a product description:
```
/generate-prd "Building a project management tool for remote teams. Need task tracking, time management, team collaboration, and reporting. Target market is small to medium businesses with distributed teams."
```

With a meeting transcript:
```
/generate-prd "
Product Planning Meeting Notes:
- CEO: We need a solution for managing remote teams
- CTO: Focus on async collaboration, not another Slack
- Product: Core features - tasks, time tracking, reporting
- Sales: Target SMBs, 10-50 employees, $20/user/month
- Main problem: Teams using 5+ disconnected tools
- MVP: Task management + time tracking + basic reporting
- Out of scope: Video calls, chat, file storage (use integrations)
- Risk: Competition from established players like Asana
"
```

Claude will ask clarifying questions only for missing critical information.

**Output**: `docs/prd.md` (or location you specify)

**Note**: The PRD is streamlined to focus on strategic direction:
- **Included**: Vision, scope, personas, risks
- **NOT included**: Epics, features, technical details
- **Deferred to features**: All detailed specifications created separately

Use `/create-feature-and-stories` with a feature description or meeting transcript to create features.

---

### 2. `/create-feature-and-stories`

**Purpose**: Generate a detailed feature specification from a description or meeting transcript, create it as a Linear Project, AND decompose it into user stories.

**When to use**: After the PRD is complete, when you're ready to develop a specific feature. You provide a description or transcript, and Claude creates the full feature specification.

**What it does**:

**Part 1 - Feature Generation:**
- Reads the PRD for strategic context (vision, personas, scope)
- Asks clarifying questions about the feature
- Generates comprehensive feature specification with:
  - Feature overview and business value
  - User workflows
  - Functional and non-functional requirements
  - Business rules and validation
  - Dependencies and constraints
  - Out of scope items
- Creates a Linear Project for the feature
- Saves feature specification document

**Part 2 - User Story Decomposition:**
- Analyzes the feature spec just created
- Asks clarifying questions about story breakdown
- Decomposes feature into independently deliverable user stories
- Creates Linear Issues within the project with:
  - User story format with value statement
  - Detailed acceptance criteria in Gherkin format
  - Proper labels and project assignment

**Example usage**:

With a feature description:
```
/create-feature-and-stories "User authentication with email/password and social login (Google, GitHub)"
```

With a meeting transcript:
```
/create-feature-and-stories "
Transcript from feature discussion:
- Need user authentication
- Support email/password
- Add Google and GitHub OAuth
- Include password reset flow
- 2FA optional for sensitive accounts
"
```

Or just a simple idea:
```
/create-feature-and-stories "Task management with assignments and due dates"
```

**Output**:
- Linear Project (e.g., `PROJ-5`) with feature details
- Feature spec saved to `docs/features/[feature_name].md`
- Multiple user stories created as Linear Issues in the project

**What happens next**: Review user stories, then use `/create-feature-spec` to create technical specification.

---

### 3. `/create-feature-spec`

**Purpose**: Generate a detailed technical specification for a Linear Project (feature) based on the feature spec and user stories.

**When to use**: After user stories are created in Linear, before implementation begins.

**What it does**:
- Queries Linear for the project (feature)
- Reads the feature specification document
- Queries Linear for all user stories in the project
- Analyzes acceptance criteria
- Reviews existing codebase architecture
- Generates comprehensive technical spec with:
  - Architecture overview (component diagrams)
  - Data models and schemas
  - API contracts
  - Security considerations
  - Testing strategy
  - Monitoring and observability
  - Open questions and decisions

**Example usage**:
```
/create-feature-spec PROJ-5
```

Or with project name:
```
/create-feature-spec "User Registration"
```

**Output**: Technical specification document saved to `docs/specs/[project_key]/technical_spec.md`

**Spec includes**:
- Mermaid diagrams for architecture
- Detailed API specifications
- Database schema changes
- Security and compliance considerations
- Testing approach
- Monitoring requirements

---

### 4. `/plan-user-story` *(Optional)*

**Purpose**: Create a detailed TDD task list for implementing a specific user story.

**When to use**: When you want a structured TDD approach with Red-Green-Refactor cycles. Skip this if you prefer to implement directly with Claude using the technical spec.

**Note**: This command is optional. You can implement stories using your own methodology or work directly with Claude without a structured plan.

**What it does**:
- Fetches story details from Linear
- Reads the technical specification
- Analyzes existing codebase patterns
- Generates a comprehensive TDD task list with:
  - Prerequisites
  - Backend tasks (models, services, APIs)
  - Frontend tasks (services, state management, UI components)
  - Documentation tasks
  - Each task follows Red-Green-Refactor cycle

**Example usage**:
```
/plan-user-story 42
```

Or with full issue ID:
```
/plan-user-story PROJ-42
```

**Output**: TDD task list saved to project documentation structure

**Task Structure** (for each task):
```markdown
#### Task N: [Task Name]
**File:** [path to file]

**Tests to Write (RED):**
- [ ] Test: Create test file
- [ ] Test: test_specific_behavior
- [ ] Test: test_error_handling

**Implementation (GREEN):**
- [ ] Create implementation file
- [ ] Implement minimal code to pass tests
- [ ] Run tests - all should pass

**Refactor:**
- [ ] Clean up code
- [ ] Remove duplication
- [ ] Improve naming
```

**TDD Principles Enforced**:
1. **RED**: Write a failing test first
2. **GREEN**: Write minimal code to make it pass
3. **REFACTOR**: Improve code without changing behavior

---

### 5. `/implement-story` *(Optional)*

**Purpose**: Orchestrate the complete development workflow: implementation, review, and refinement using specialized agents.

**When to use**: When you want a fully automated TDD workflow with systematic implementation, code review, and refinement. Skip this if you prefer manual development or direct Claude interaction.

**Note**: This command is optional. Many teams implement stories manually or use Claude directly with the technical spec and TDD plan as guides.

**What it does**:
- Uses specialized AI agents to:
  1. **story-developer**: Implements all tasks following TDD
  2. **story-reviewer**: Reviews code for quality, tests, and standards
  3. **refinement-developer**: Addresses review feedback

**Example usage**:
```
/implement-story docs/specs/feature_1.1/story_42_tdd_tasks.md
```

**Orchestration Flow**:
1. Story developer implements all tasks
2. Story reviewer performs comprehensive review
3. Refinement developer fixes any issues
4. Process repeats until all criteria met

**Completion Criteria**:
- All TDD tasks completed
- All tests passing
- Code review approved
- No linting errors
- All acceptance criteria met

---

## Best Practices

### PRD Creation

1. **Be Specific**: Avoid vague requirements; use concrete, measurable criteria
2. **Think MVP**: Clearly distinguish between MVP and future features
3. **Consider Compliance**: Include relevant regulatory/legal requirements early
4. **Define Success**: Create measurable success metrics
5. **Identify Risks**: Proactively identify and plan mitigations

### Feature Decomposition

1. **Natural Boundaries**: Break features by complete, deliverable functionality
2. **User Value**: Each story should deliver value end-to-end
3. **Independent Stories**: Stories should be implementable independently
4. **Clear Acceptance Criteria**: Use Gherkin format with descriptive names
5. **Cover All Cases**: Include happy paths, errors, edge cases, empty states

### Technical Specifications

1. **Extract Exact Requirements**: Pull exact error messages and validations from ACs
2. **Reference User Stories**: Link every requirement to a specific story
3. **No Placeholders**: Use actual field names and concrete examples
4. **Follow Project Conventions**: Match existing architecture and patterns
5. **Include Diagrams**: Use Mermaid for architecture and flow diagrams

### TDD Implementation *(Optional - for automated workflow)*

If using the optional TDD workflow (steps 4-5):

1. **Write Tests First**: Never write production code without a failing test
2. **Simplest Test**: Write the simplest test that could possibly fail
3. **Simplest Code**: Write the simplest code that could possibly pass
4. **Refactor When Green**: Only improve code when tests are passing
5. **Follow Task Order**: Complete tasks sequentially, don't skip around

### Code Quality

1. **Prefer Integration Tests**: Test real behavior, not mocks
2. **Avoid Over-Mocking**: Never mock the method you're testing
3. **Specific Assertions**: Use exact values, not ranges or negations
4. **Never Skip Tests**: Fix failing tests, don't disable them
5. **Clean Commits**: Commit working code with all tests passing

---

## Adapting to Your Project

### Backend Architecture

The commands work with various architectures:
- **Hexagonal/Ports & Adapters**: Separate domain, services, adapters
- **Layered Architecture**: Controllers, services, repositories
- **MVC**: Models, views, controllers
- **Microservices**: Service-based architecture

**Customize by**:
- Adjusting file path conventions in generated plans
- Modifying task templates for your specific layers
- Adding project-specific testing requirements

### Frontend Framework

The commands support multiple frameworks:
- **React** (with React Query, Redux, Context API)
- **Vue** (with Pinia, Vuex, Composition API)
- **Angular** (with RxJS, Services, NgRx)
- **Svelte** (with Svelte stores)

**Customize by**:
- Specifying your state management approach
- Adjusting component testing strategies
- Modifying task templates for your framework

### Testing Approach

Works with various testing strategies:
- **Unit Tests**: Jest, Vitest, pytest, JUnit
- **Integration Tests**: Testing Library, Testcontainers, Supertest
- **E2E Tests**: Playwright, Cypress, Selenium

**Customize by**:
- Specifying test file locations
- Adjusting test setup/teardown patterns
- Modifying assertion styles

---

## Integration with Linear

### Required Linear Setup

1. **Issue Tracking**: Stories tracked as Linear issues
2. **Labels**: Use consistent labels (e.g., "user-story")
3. **Projects**: Features created as Linear projects using `/create-feature-and-stories`
4. **Workflows**: Define clear workflow states

### Linear Best Practices

1. **Consistent Naming**: Use clear, descriptive names for stories
2. **Complete ACs**: Include all acceptance criteria in issue description
3. **Link Stories**: Connect related stories and features
4. **Update Status**: Keep issue status current as work progresses
5. **Document Blockers**: Note blockers and dependencies

---

## Project Structure Recommendations

```
project-root/
├── .claude/
│   ├── commands/           # Slash commands
│   │   ├── generate-prd.md
│   │   ├── create-feature-and-stories.md
│   │   ├── create-feature-spec.md
│   │   ├── plan-user-story.md
│   │   └── implement-story.md
│   └── agents/            # Specialized agents
│       ├── story-developer.md
│       ├── story-reviewer.md
│       ├── refinement-developer.md
│       └── test-fix-specialist.md
├── docs/
│   ├── prd.md             # Product Requirements Document (strategic only)
│   ├── features/          # Feature specifications
│   │   └── [feature_name].md
│   ├── specs/             # Technical specifications
│   │   └── [project_key]/
│   │       ├── technical_spec.md
│   │       ├── story_[issue_id]_tdd_tasks.md
│   │       └── mockups/
│   └── architecture/      # Architecture documentation
├── src/                   # Source code
│   ├── backend/
│   └── frontend/
└── tests/                 # Tests
    ├── unit/
    ├── integration/
    └── e2e/
```

---

## Example: Complete Workflow Walkthrough

### Scenario: Building a Task Management Feature

#### Step 1: Generate PRD

Option A - Interactive:
```bash
/generate-prd
```

Option B - With meeting transcript:
```bash
/generate-prd "
Planning Meeting - Task Management System:
- Vision: Simple task management for small teams
- Problem: Existing tools too complex and expensive
- Users: Small teams (5-15 people), project managers, freelancers
- MVP Scope: Create/assign/track tasks, due dates, priorities
- Out of scope: Time tracking, invoicing, advanced reporting
- Risks: Market saturation, need clear differentiation
"
```

**Output**: `docs/prd.md` with strategic direction (vision, scope, personas, risks - no epics or features).

#### Step 2: Create Feature & User Stories

```bash
/create-feature-and-stories "Task management feature with the ability to create, assign, and track tasks with due dates and priority levels"
```

Claude uses the PRD context, asks clarifying questions about the task management feature, then automatically creates the feature spec and decomposes it into user stories.

**Output:**
- Linear Project PROJ-8 "Task Creation & Management"
- Feature spec: `docs/features/task_management/task_creation_and_management.md`
- 5 User stories created:
  - PROJ-15: Create task with title and description
  - PROJ-16: Assign task to team member
  - PROJ-17: Set task due date
  - PROJ-18: Mark task as complete
  - PROJ-19: View task list with filters

#### Step 3: Create Technical Spec

```bash
/create-feature-spec PROJ-8
```

Claude generates `docs/specs/proj_8/technical_spec.md` with:
- API endpoints: POST /tasks, GET /tasks, PATCH /tasks/:id
- Database schema for tasks table
- Frontend components and state management
- Security and validation requirements

**At this point, you have everything needed to start implementation:**
- PRD with strategic direction
- Feature spec with detailed requirements
- User stories with acceptance criteria in Linear
- Technical spec with architecture and design

**The following steps are OPTIONAL** - use them if you want a structured TDD workflow:

---

#### Step 4 (Optional): Plan First Story

```bash
/plan-user-story PROJ-15
```

Claude reads PROJ-15 from Linear and generates:
`docs/specs/proj_8/story_PROJ-15_tdd_tasks.md`

Contains 8 tasks:
1. Task model/entity with validation
2. Database repository
3. Task service with business logic
4. API endpoint for task creation
5. API service layer (frontend)
6. React Query hook
7. Task creation form component
8. Integration and routing

**Alternative**: Implement directly with Claude using the technical spec as a guide, without a formal TDD plan.

---

#### Step 5 (Optional): Implement Story

```bash
/implement-story docs/specs/proj_8/story_PROJ-15_tdd_tasks.md
```

Claude orchestrates:
1. **story-developer** agent: Implements all 8 tasks following TDD
2. **story-reviewer** agent: Reviews code, runs tests, checks quality
3. **refinement-developer** agent: Fixes any issues found

Result: PROJ-15 is complete, tested, reviewed, and ready to merge.

**Alternative**: Implement manually, or work directly with Claude in a conversational way using the specs as reference.

---

#### Repeat Steps 4-5 for remaining stories (if using structured workflow)

Continue with PROJ-16, PROJ-17, PROJ-18, PROJ-19 until the feature is complete.

---

## Troubleshooting

### "Claude can't find the PRD"

- Ensure PRD is in `docs/prd.md` or specify the location
- Check file permissions
- Verify PRD follows the expected format

### "Linear issues not created"

- Verify Linear MCP integration is configured
- Check Linear API permissions
- Ensure team/project exists in Linear

### "Generated tests don't match project style"

- Update the TDD task template in `/plan-user-story` command
- Reference existing test files as examples
- Specify testing conventions in project documentation

### "Tasks are too large/too small"

- Adjust the feature decomposition guidelines
- Provide feedback to Claude about desired task size
- Break down or combine tasks manually

---

## Customization Guide

### Modifying Templates

All templates are in the slash command files. To customize:

1. Open the command file (e.g., `.claude/commands/plan-user-story.md`)
2. Locate the `<plan_template>` or similar section
3. Modify the template structure
4. Save and test with a sample story

### Adding Project-Specific Guidelines

Update the `## Guidelines` section in each command to include:
- Project-specific naming conventions
- Required code patterns
- Mandatory security checks
- Compliance requirements
- Performance standards

### Creating New Commands

Follow this structure:

```markdown
---
description: Brief description of what the command does
---

[Main prompt explaining the task]

## Steps

1. [Step 1]
2. [Step 2]
...

## Template

<template_name>
[Template content]
</template_name>

## Guidelines

- [Guideline 1]
- [Guideline 2]

## Output

[Expected output format]
```

---

## Contributing

To improve these commands:

1. Test on diverse projects
2. Document issues and edge cases
3. Propose improvements to templates
4. Share successful adaptations
5. Contribute back enhancements

---

## FAQ

**Q: Do I need to use all commands?**
A: No, the workflow is modular. Steps 1-3 (PRD, Feature + Stories, Technical Spec) provide valuable documentation. Steps 4-5 (TDD planning and automated implementation) are entirely optional.

**Q: Can I use this without Linear?**
A: Yes, adapt the commands to use your issue tracker (Jira, GitHub Issues, etc.)

**Q: Does this work for non-web projects?**
A: Yes! Adapt frontend sections for mobile, desktop, CLI, or remove them for backend-only projects.

**Q: How do I handle urgent bugs/hotfixes?**
A: For urgent fixes, implement directly with Claude. Document decisions in the technical spec afterward for future reference.

**Q: Can I use this with legacy codebases?**
A: Absolutely. The specification workflow helps document new features clearly. Start with specs for new features and gradually expand coverage.

**Q: What if my project doesn't use TDD?**
A: Simply skip steps 4-5. The core value is in the specification workflow (steps 1-3). You can implement features using any methodology you prefer with the specs as your guide.

---

## License

These commands are provided as-is for use in your projects. Feel free to modify and adapt them to your needs.

---

## Credits

Developed for use with Claude Code by Anthropic. Part of a comprehensive spec-driven development methodology focused on clear specifications, incremental delivery, and AI-augmented development.

---

**Version**: 1.0
**Last Updated**: 2025
**Maintained By**: Your team/organization

For questions or improvements, open an issue or submit a pull request in your project repository.
