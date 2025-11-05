---
description: Create feature from description/transcript, Linear Project, and user stories in one step
---

Create a detailed feature specification from $ARGUMENTS (can be a feature description, meeting transcript, or feature idea), create it as a Linear Project, and decompose it into user stories.

## Steps

### Part 1: Feature Generation

1. **Locate PRD**: Find the PRD file (typically `docs/prd.md`, `PRD.md`, or similar) for strategic context
2. **Understand Feature Input**: Analyze $ARGUMENTS which can be:
   - A feature description (e.g., "User authentication with social login")
   - A meeting transcript discussing the feature
   - A detailed feature idea or concept
3. **Gather Context**: Review PRD vision, user personas, scope, and risks
4. **Ask Clarifying Questions**: Gather specific feature details:
   - What specific capabilities should this feature provide?
   - What are the key user workflows?
   - What are the expected inputs and outputs?
   - Are there any specific technical constraints?
   - What are the success metrics for this feature?
   - Are there any compliance or security considerations?
5. **Generate Feature Spec**: Create comprehensive feature specification
6. **Create Linear Project**: Create a new Linear Project with the feature details
7. **Save Feature Spec**: Save the feature specification to `docs/features/[feature_name].md`

### Part 2: User Story Decomposition

8. **Analyze Feature**: Review the feature spec, workflows, and functional requirements just created
9. **Ask Decomposition Questions**: Clarify any ambiguities about breaking down into stories
10. **Break Down into Stories**: Decompose the feature into independently deliverable user stories using natural boundaries
11. **Create User Stories**: For each story, create a Linear issue in the project with:
    - Clear title (few words with action verb)
    - User story format: "As a [persona], I want [action] so that [benefit]"
    - User value statement (1-2 sentences)
    - Acceptance criteria in Gherkin format with descriptive names
    - Label: "user-story"
    - Assigned to the Linear project created in step 6

## Feature Specification Template

<feature_template>
# Feature: [Feature Name]

**Date:** [Current Date]
**Linear Project:** [Project URL]

---

## 1. Feature Overview

### 1.1 Description
[Detailed description of what this feature does and why it's important]

### 1.2 Business Value
[Clear explanation of the business value and strategic importance]

### 1.3 Target Users
[Which personas from the PRD will use this feature]

### 1.4 Success Criteria
* [Measurable criterion 1]
* [Measurable criterion 2]
* [Measurable criterion 3]

---

## 2. User Workflows

### Workflow 1: [Primary Workflow Name]
1. User [action]
2. System [response]
3. User [action]
4. System [response]

### Workflow 2: [Secondary Workflow Name]
1. User [action]
2. System [response]
3. User [action]
4. System [response]

[Add more workflows as needed]

---

## 3. Functional Requirements

### 3.1 Core Functionality
* [Requirement 1]
* [Requirement 2]
* [Requirement 3]

### 3.2 Input Requirements
* [Input 1: format, validation rules]
* [Input 2: format, validation rules]

### 3.3 Output Requirements
* [Output 1: format, content]
* [Output 2: format, content]

### 3.4 Business Rules
* [Rule 1]
* [Rule 2]
* [Rule 3]

### 3.5 Validation Rules
* [Validation 1]
* [Validation 2]
* [Validation 3]

---

## 4. Non-Functional Requirements

### 4.1 Performance
* [Performance requirement 1]
* [Performance requirement 2]

### 4.2 Security
* [Security requirement 1]
* [Security requirement 2]

### 4.3 Accessibility
* [Accessibility requirement 1]
* [Accessibility requirement 2]

### 4.4 Usability
* [Usability requirement 1]
* [Usability requirement 2]

---

## 5. Dependencies & Constraints

### 5.1 Dependencies
* [Dependency 1]
* [Dependency 2]

### 5.2 Technical Constraints
* [Constraint 1]
* [Constraint 2]

### 5.3 Compliance Requirements
* [Compliance requirement 1]
* [Compliance requirement 2]

---

## 6. Out of Scope

* [Item 1 explicitly not included]
* [Item 2 explicitly not included]
* [Item 3 explicitly not included]

---

## 7. User Stories Overview

After this feature is defined, it will be decomposed into user stories (see Part 2 of this command).

Expected story areas:
* [Story area 1]
* [Story area 2]
* [Story area 3]

---

## 8. Open Questions

- [ ] [Question 1 that needs resolution]
- [ ] [Question 2 that needs resolution]
- [ ] [Question 3 that needs resolution]

---

## 9. References

- **PRD:** `[path to PRD]`
- **Linear Project:** [Linear Project URL]
- **Related Documentation:** [Links to any related docs]

</feature_template>

## Linear Project Creation

When creating the Linear Project, include:

**Project Name:** [Feature Name]

**Project Description:**
```markdown
## Feature: [Feature Name]

[Feature description from spec]

## Success Criteria
* [Criterion 1]
* [Criterion 2]
* [Criterion 3]

## Workflows
[List key workflows]

## References
- Feature Spec: [Link to feature spec document]
- PRD: [Link to PRD]
```

**Project Settings:**
- Team: [Appropriate team]
- State: "Planned" or "Backlog"
- Target Date: [If applicable]

## User Story Template

After creating the feature, use this template for each user story:

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

## Guidelines

### Feature Generation Guidelines

1. **Use All Context**: Combine the input description/transcript with PRD vision, personas, and scope
2. **Ask Questions**: Don't assume - clarify ambiguities with the user
3. **Be Specific**: Include concrete examples, not abstract descriptions
4. **Think User-First**: Focus on user needs and workflows
5. **Define Boundaries**: Clearly state what's in scope and out of scope
6. **Connect to PRD**: Reference personas and risks from PRD
7. **Enable Decomposition**: Write requirements at a level that can be broken into user stories
8. **Consider Compliance**: Include any compliance or security requirements from PRD

### User Story Decomposition Guidelines

1. **Natural Boundaries**: Break features by complete, deliverable functionality
2. **User Value**: Each story should deliver value end-to-end
3. **Independent Stories**: Stories should be implementable independently
4. **Clear Acceptance Criteria**: Use Gherkin format with descriptive names
5. **Cover All Cases**: Include happy paths, errors, edge cases, empty states for each story
6. **Descriptive AC Names**: E.g., "AC1: Create task with valid data and required fields"
7. **Exact Error Messages**: Specify the exact text users will see
8. **Observable Behavior**: Focus on what users see/experience, not technical implementation
9. **Specific Fields**: Use actual field names and UI elements from the feature spec

## Output

After completing both parts:

```markdown
Generated feature and user stories:

**Feature Name:** [Feature Name]
**Linear Project:** [PROJECT-KEY] - [URL]
**Feature Spec:** `[path to feature spec]`

**Feature Summary:**
- [N] user workflows defined
- [N] functional requirements specified
- [N] non-functional requirements documented
- [N] open questions to resolve

**User Stories Created:**
1. **[ISSUE-ID]: [Title]** - [URL]
   Focus: [1-line description]

2. **[ISSUE-ID]: [Title]** - [URL]
   Focus: [1-line description]

3. **[ISSUE-ID]: [Title]** - [URL]
   Focus: [1-line description]

[Continue for all stories]

Next steps:
1. Review feature spec and resolve open questions
2. Review user stories in Linear and refine acceptance criteria as needed
3. Run `/create-feature-spec [PROJECT-KEY]` to create technical specification
4. Start implementation with `/plan-user-story [ISSUE-ID]` for the first story
```
