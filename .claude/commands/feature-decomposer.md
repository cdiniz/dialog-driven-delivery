---
description: Decompose PRD feature into user stories in Linear
---

Decompose a PRD feature $ARGUMENTS into independently deliverable user stories and create them in Linear.

## Steps

1. **Locate PRD**: Search for the PRD file (typically `docs/prd.md`, `PRD.md`, or `README.md` with PRD content)
2. **Find Feature**: Locate the specified feature in the PRD
3. **Analyze**: Think carefully about the feature and ask any clarifying questions to the user
4. **Break Down**: Decompose into stories using natural boundaries (smaller units of complete, deliverable functionality that provides value end-to-end)
5. **Get Project Context**:
   - Identify the Linear workspace being used
   - Determine the team/project prefix (e.g., STR-, PROJ-, etc.)
   - Identify the Epic/Project name from the PRD
6. **Create Stories**: For each story, create Linear issue with:
   - Clear title: [Feature x.x] (few words with action verb)
   - User story: "As a [persona], I want [action] so that [benefit]"
   - User value statement (1-2 sentences)
   - Acceptance criteria in Gherkin format with descriptive names
   - Label: "user-story"
   - Project: [Epic Name from the PRD]

## Story Template

```markdown
## User Story
As a [persona], I want to [action] so that I can [benefit].

## User Value Statement
[1-2 sentences explaining value to users and system]

## Acceptance Criteria

### AC1: [Descriptive scenario name]
- **Given** [context]
- **When** [action]
- **Then** [outcome 1]
- **And** [outcome 2]

### AC2: [Error handling scenario]
- **Given** [error context]
- **When** [invalid action]
- **Then** [error message: "Exact text"]
- **And** [system behavior]

[Continue with AC3, AC4, etc.]
```

## AC Guidelines

- Include descriptive AC names (e.g., "AC1: Create something with validation etc")
- Specify exact error messages and notifications
- Cover happy paths, validation, edge cases, empty states for each story
- Focus on observable user behavior, not technical implementation
- Be specific with field names and UI elements

## Output

Provide summary after creating issues:

```markdown
Created [N] stories for Feature [X.Y]:

1. **[PREFIX-XX]: [Title]** - [URL] - [1-line focus]
2. **[PREFIX-YY]: [Title]** - [URL] - [1-line focus]
[etc.]
```

(Replace [PREFIX-XX] with the actual issue ID from Linear, e.g., STR-42, PROJ-123, etc.)
