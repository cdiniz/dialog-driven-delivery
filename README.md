# Spec-Driven Development (SDD) with Claude Code

A markdown-based workflow system for managing product development from feature planning through implementation. This framework provides conversational Claude Code slash commands that help you create specifications, decompose features into user stories, and implement them incrementally.

## Philosophy

**Documentation-first development** where specifications are the single source of truth, stored as markdown files alongside your code in git. Features originate from meetings and discussions, are documented comprehensively, decomposed into actionable stories, and then implemented incrementally with testing and code review.

## Quick Start

### 1. Create a Feature Specification

```bash
/create-spec
```

Provide meeting transcripts, documents, or discuss conversationally. Creates `docs/[feature-name]/spec.md` with both Product and Technical specifications.

### 2. Refine the Specification (as needed)

```bash
/refine-spec [feature-name]
```

Add new information from follow-up meetings, design reviews, or stakeholder feedback.

### 3. Create User Stories

```bash
/create-user-stories-from-spec [feature-name]
```

Decomposes the feature into independently deliverable user stories as markdown files in `docs/[feature-name]/story-*.md`.

### 4. Implement Stories

```bash
/implement-story
```

Implements a user story with complete test coverage. Updates story status from `todo` → `in_progress` → `done`.

### 5. Manual Testing

```bash
/manual-test-story
```

Launch the app and manually verify acceptance criteria in the browser with Chrome DevTools.

### 6. Commit and Create PR

```bash
/commit-and-open-pr
```

Create structured commits and pull requests with test plans.

### 7. Address PR Feedback

```bash
/address-pr-feedback
```

Systematically handle code review comments and feedback.

## Directory Structure

```
your-project/
├── docs/
│   ├── feature-name-1/
│   │   ├── spec.md                    # Feature specification
│   │   ├── story-01-basic-search.md   # User story 1
│   │   ├── story-02-add-filters.md    # User story 2
│   │   └── ...
│   ├── feature-name-2/
│   │   ├── spec.md
│   │   └── ...
├── .claude/
│   ├── commands/                      # Slash command definitions
│   ├── templates/                     # Spec and story templates
│   └── uncertainty-markers.md         # Standards for handling unknowns
└── ...your code...
```

## Available Commands

| Command | Purpose |
|---------|---------|
| `/create-spec` | Create feature specs from transcripts/discussions |
| `/refine-spec [feature-name]` | Update existing specs with new information |
| `/create-user-stories-from-spec [feature-name]` | Decompose specs into user stories |
| `/implement-story` | Implement a story with tests |
| `/manual-test-story` | Browser testing with Chrome DevTools |
| `/commit-and-open-pr` | Create commits and pull requests |
| `/address-pr-feedback` | Handle PR review feedback |

## Key Features

### Documentation-First
- Specifications before code
- Single source of truth in markdown
- Git-tracked alongside code
- Portable and platform-independent

### Conversational
- Commands ask clarifying questions
- Meeting transcripts as input
- Agent proposes options and confirms
- Shows understanding before creating artifacts

### Incremental Delivery
- Features decomposed into independent stories
- Stories tracked with frontmatter metadata
- Clear dependencies and ordering
- Story-by-story implementation

### Quality Through Process
- Comprehensive acceptance criteria (Gherkin format)
- Testing required before merge
- Code review workflows
- Architecture validation

### Uncertainty Management
- Explicit markers (`[OPEN QUESTION: ...]`, `[ASSUMPTION: ...]`)
- Forces explicit answers to ambiguous questions
- Prevents silent assumptions
- Creates audit trail of decisions

## Workflow Example

```
Meeting Discussion
    ↓
/create-spec (paste transcript)
    ↓
docs/advanced-search/spec.md
    ↓
/refine-spec advanced-search (add new info)
    ↓
Updated spec.md
    ↓
/create-user-stories-from-spec advanced-search
    ↓
story-01-backend-api.md
story-02-frontend-ui.md
story-03-add-filters.md
    ↓
/implement-story (for each story)
    ↓
Code + Tests + Feature Branch
    ↓
/manual-test-story
    ↓
/commit-and-open-pr
    ↓
Pull Request
    ↓
/address-pr-feedback
    ↓
Merge to Main
```

## Story Status Tracking

Each user story file has frontmatter metadata:

```yaml
---
title: Add basic search functionality
status: todo  # or in_progress, done, blocked
priority: high  # or medium, low
tags: [backend, api, search]
dependencies: []  # or [1, 2] for story numbers
blocked_by: ""  # description if blocked
story_number: 1
---
```

Update the `status` field as you work through stories:
- `todo` - Not started
- `in_progress` - Currently being implemented
- `done` - Completed and merged
- `blocked` - Waiting on dependencies or clarifications

## Benefits

✅ **Version Controlled** - All specs and stories tracked in git
✅ **No Vendor Lock-in** - Plain markdown files work everywhere
✅ **Portable** - Move between tools easily
✅ **Searchable** - Use git grep, IDE search, or any text search tool
✅ **Diff-friendly** - See changes in PRs
✅ **Collaborative** - Easy to review and comment on
✅ **Offline-capable** - No need for external services
✅ **Fast** - No API calls to external systems
✅ **Flexible** - Customize templates and workflows as needed

## Design Principles

1. **Documentation-first** — Specs before code
2. **Conversational** — Commands ask clarifying questions
3. **Uncertainty markers** — Explicit handling of ambiguity
4. **Incremental delivery** — Stories are independently deliverable
5. **Test coverage required** — Integration tests preferred
6. **Git-native** — Everything version controlled
7. **Platform-independent** — Pure markdown, no vendor lock-in

## Learn More

- **Planning Workflow**: See `.claude/commands/SPEC_README.md` for detailed planning steps
- **Coding Workflow**: See `.claude/commands/CODING_README.md` for implementation steps
- **Uncertainty Markers**: See `.claude/uncertainty-markers.md` for handling ambiguity
- **Templates**: Check `.claude/templates/` for spec and story templates

## Migration from Atlassian

If you were previously using this framework with Jira/Confluence:

- Feature specs now live in `docs/[feature-name]/spec.md` instead of Confluence
- User stories are markdown files instead of Jira issues
- Story status tracked in frontmatter instead of Jira workflow
- Dependencies tracked in frontmatter arrays
- All content is git-tracked and portable

The workflow remains the same - only the storage format has changed from cloud services to local markdown files.
