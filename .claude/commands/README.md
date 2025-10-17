# TDD-Driven Product Development Workflow

A comprehensive, project-agnostic methodology for building software products using Test-Driven Development (TDD), Product Requirements Documents (PRDs), and AI-assisted development with Claude Code.

## Philosophy

This workflow emphasizes:

1. **Documentation-First**: Start with clear product requirements before writing code
2. **Test-Driven Development**: Write tests before implementation (Red-Green-Refactor)
3. **Incremental Delivery**: Break features into independently deliverable user stories
4. **Quality Built-In**: Testing, code review, and refinement are part of the process, not afterthoughts
5. **AI-Augmented Development**: Leverage Claude Code to automate repetitive tasks while maintaining quality standards

## Prerequisites

- **Claude Code** installed and configured
- **Linear** (or similar issue tracking) for managing user stories
- **Git** for version control
- Project uses **TDD practices** and has a testing framework set up

## Installation

Copy the `.claude/commands/` directory to your project:

```bash
# From this repository
cp -r .claude/commands /path/to/your/project/.claude/

# Or clone individual commands you need
mkdir -p /path/to/your/project/.claude/commands
cp .claude/commands/generate-prd.md /path/to/your/project/.claude/commands/
cp .claude/commands/feature-decomposer.md /path/to/your/project/.claude/commands/
# ... and so on
```

## The Complete Workflow

```
Product Idea
     │
     ├─ 1. Generate PRD (/generate-prd)
     │
     ▼
Product Requirements Document (PRD)
     │
     ├─ 2. Decompose Feature (/feature-decomposer "Feature X.X")
     │
     ▼
User Stories in Linear
     │
     ├─ 3. Create Technical Spec (/create-feature-spec "Feature X.X")
     │
     ▼
Technical Specification
     │
     ├─ 4. Plan User Story (/plan-user-story ISSUE-ID)
     │
     ▼
TDD Task List
     │
     ├─ 5. Implement Story (/implement-story path/to/tdd_plan.md)
     │
     ▼
Completed, Tested, Reviewed Code
```

## Slash Commands Reference

### 1. `/generate-prd`

**Purpose**: Create a comprehensive Product Requirements Document from a product description.

**When to use**: At the very beginning of a new product or major feature initiative.

**What it does**:
- Asks questions about your product idea
- Generates a structured PRD with:
  - Executive summary (vision, problem, solution, metrics)
  - Scope (MVP and out-of-scope items)
  - User personas
  - Epics and features breakdown
  - Technical requirements
  - Implementation priorities
  - Success criteria
  - Risk assessment

**Example usage**:
```
/generate-prd
```

Claude will ask:
- Product vision and goals
- Target users and market
- Core problems being solved
- Key features you envision
- Technical constraints
- Compliance requirements

**Output**: `docs/prd.md` (or location you specify)

---

### 2. `/feature-decomposer`

**Purpose**: Break down a PRD feature into independently deliverable user stories and create them in Linear.

**When to use**: After PRD is complete, when you're ready to start planning a specific feature.

**What it does**:
- Reads the PRD and locates the specified feature
- Analyzes the feature requirements
- Breaks it down into smaller, deliverable stories
- Creates Linear issues with:
  - User story format: "As a [persona], I want [action] so that [benefit]"
  - User value statement
  - Acceptance criteria in Gherkin format
  - Proper labels and project assignment

**Example usage**:
```
/feature-decomposer "Feature 1.1"
```

Or with the feature name:
```
/feature-decomposer "Patient Enrollment & Onboarding"
```

**Output**: Multiple user stories created in Linear with complete acceptance criteria

**Story Template**:
```markdown
## User Story
As a [persona], I want to [action] so that I can [benefit].

## User Value Statement
[1-2 sentences explaining value to users and system]

## Acceptance Criteria

### AC1: [Descriptive scenario name]
- **Given** [context]
- **When** [action]
- **Then** [outcome]
- **And** [additional outcome]

### AC2: [Error handling scenario]
...
```

---

### 3. `/create-feature-spec`

**Purpose**: Generate a detailed technical specification for a feature based on the PRD and user stories.

**When to use**: After user stories are created, before implementation begins.

**What it does**:
- Reads the PRD feature requirements
- Queries Linear for all related user stories
- Analyzes acceptance criteria
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
/create-feature-spec "Feature 1.1"
```

**Output**: Technical specification document (location determined by project structure)

**Spec includes**:
- Mermaid diagrams for architecture
- Detailed API specifications
- Database schema changes
- Security and compliance considerations
- Testing approach
- Monitoring requirements

---

### 4. `/plan-user-story`

**Purpose**: Create a detailed TDD task list for implementing a specific user story.

**When to use**: When you're ready to start development on a user story.

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

### 5. `/implement-story`

**Purpose**: Orchestrate the complete development workflow: implementation, review, and refinement.

**When to use**: When you have a TDD task list and are ready to implement the story.

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

### TDD Implementation

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
3. **Projects**: Map PRD epics to Linear projects
4. **Workflows**: Define clear workflow states

### Linear Best Practices

1. **Consistent Naming**: Use "[Feature X.X]" prefix in story titles
2. **Complete ACs**: Include all acceptance criteria in issue description
3. **Link Stories**: Connect related stories and features
4. **Update Status**: Keep issue status current as work progresses
5. **Document Blockers**: Note blockers and dependencies

---

## Project Structure Recommendations

```
project-root/
├── .claude/
│   └── commands/           # Slash commands
│       ├── generate-prd.md
│       ├── feature-decomposer.md
│       ├── create-feature-spec.md
│       ├── plan-user-story.md
│       └── implement-story.md
├── docs/
│   ├── prd.md             # Product Requirements Document
│   ├── specs/             # Technical specifications
│   │   └── feature_X.X/
│   │       ├── technical_spec.md
│   │       ├── story_XX_tdd_tasks.md
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

```bash
/generate-prd
```

Claude asks questions, you describe a task management system. Output: `docs/prd.md` with Feature 2.1: Task Creation & Management.

#### Step 2: Decompose Feature

```bash
/feature-decomposer "Feature 2.1"
```

Claude analyzes Feature 2.1 and creates 5 user stories in Linear:
- TASK-15: Create task with title and description
- TASK-16: Assign task to team member
- TASK-17: Set task due date
- TASK-18: Mark task as complete
- TASK-19: View task list with filters

#### Step 3: Create Technical Spec

```bash
/create-feature-spec "Feature 2.1"
```

Claude generates `docs/specs/feature_2.1/technical_spec.md` with:
- API endpoints: POST /tasks, GET /tasks, PATCH /tasks/:id
- Database schema for tasks table
- Frontend components and state management
- Security and validation requirements

#### Step 4: Plan First Story

```bash
/plan-user-story TASK-15
```

Claude reads TASK-15 from Linear and generates:
`docs/specs/feature_2.1/story_TASK-15_tdd_tasks.md`

Contains 8 tasks:
1. Task model/entity with validation
2. Database repository
3. Task service with business logic
4. API endpoint for task creation
5. API service layer (frontend)
6. React Query hook
7. Task creation form component
8. Integration and routing

#### Step 5: Implement Story

```bash
/implement-story docs/specs/feature_2.1/story_TASK-15_tdd_tasks.md
```

Claude orchestrates:
1. **story-developer** agent: Implements all 8 tasks following TDD
2. **story-reviewer** agent: Reviews code, runs tests, checks quality
3. **refinement-developer** agent: Fixes any issues found

Result: TASK-15 is complete, tested, reviewed, and ready to merge.

#### Repeat Steps 4-5 for remaining stories

Continue with TASK-16, TASK-17, TASK-18, TASK-19 until Feature 2.1 is complete.

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
A: No, use what fits your workflow. Some teams skip PRDs for small features, others might have existing technical specs.

**Q: Can I use this without Linear?**
A: Yes, adapt the commands to use your issue tracker (Jira, GitHub Issues, etc.)

**Q: Does this work for non-web projects?**
A: Yes! Adapt frontend sections for mobile, desktop, CLI, or remove them for backend-only projects.

**Q: How do I handle urgent bugs/hotfixes?**
A: For urgent fixes, skip to `/plan-user-story` or implement directly. Document decisions for future reference.

**Q: Can I use this with legacy codebases?**
A: Absolutely. The TDD planning adapts to existing patterns. Start with new features and gradually adopt for refactoring.

**Q: What if my project doesn't use TDD?**
A: Adapt the task templates to focus on implementation-first. However, adding tests incrementally is highly recommended.

---

## License

These commands are provided as-is for use in your projects. Feel free to modify and adapt them to your needs.

---

## Credits

Developed for use with Claude Code by Anthropic. Part of a comprehensive development methodology focused on quality, testing, and AI-augmented development.

---

**Version**: 1.0
**Last Updated**: 2025
**Maintained By**: Your team/organization

For questions or improvements, open an issue or submit a pull request in your project repository.
