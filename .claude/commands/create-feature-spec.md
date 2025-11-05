---
description: Generate technical specification for Linear Project (feature)
---

Generate a technical specification for Linear Project (feature) $ARGUMENTS and save it to the project's documentation structure.

## Steps

1. **Get Project**: Query Linear for the project using $ARGUMENTS (accepts project key, project name, or project ID)
2. **Find Feature Spec**: Look for the feature specification document (typically in `docs/features/`)
3. **Query Stories**: Get all user stories (issues) associated with this Linear project
4. **Analyze Requirements**: Review feature spec, user stories, and acceptance criteria
5. **Analyze Codebase**: Review existing architecture patterns and integration points
6. **Determine Relevant Sections**: Based on the feature type and requirements, decide which optional sections to include (see Section Selection Guide below)
7. **Generate Spec**: Create technical specification with core sections and relevant optional sections
8. **Determine Structure**: Ask user for preferred location or use: `docs/specs/[project_key]/` or `docs/features/[feature_name]/technical_spec.md`
9. **Save Spec**: Create directory structure if needed and save the spec

## Section Selection Guide

### Core Sections (Always Include)
These sections are required for every technical spec:
- **Overview & Context**: Feature summary and related user stories
- **Architecture Overview**: Component diagrams and data flow
- **Testing Strategy**: High-level testing approach
- **Open Questions & Decisions**: Unresolved questions and decisions
- **References**: Links to relevant documentation

### Optional Sections (Include When Relevant)

**Include "Data Models" if:**
- Feature creates, modifies, or deletes database entities
- User stories mention data persistence or database schema changes
- Feature requires new tables, columns, or relationships

**Include "API Contracts" if:**
- Feature creates new API endpoints
- Feature modifies existing API endpoints
- User stories mention REST APIs, GraphQL, or other API interactions

**Include "UI Components" if:**
- Feature is frontend-focused
- User stories describe user interface elements
- Feature requires new or modified visual components

**Include "State Management" if:**
- Feature involves complex frontend state (Redux, Vuex, Context API, etc.)
- User stories mention state synchronization across components
- Feature requires state persistence or caching strategies

**Include "Integration Points" if:**
- Feature integrates with third-party services or APIs
- User stories mention external systems
- Feature requires webhooks, message queues, or event streaming

**Include "Security Considerations" if:**
- Feature involves authentication or authorization
- Feature handles sensitive data (PII, passwords, payment info)
- User stories mention security or compliance requirements
- Feature exposes new attack surfaces

**Include "Monitoring & Observability" if:**
- Feature is performance-critical
- Feature requires specific alerts or monitoring
- User stories mention SLAs or performance requirements
- Feature handles high-volume operations

**Include "Infrastructure/Deployment" if:**
- Feature requires infrastructure changes
- User stories mention deployment, scaling, or DevOps concerns
- Feature requires new services, containers, or cloud resources

## Technical Spec Template

<spec_template>
# Technical Specification: [Feature Name]

**Linear Project:** [PROJECT-KEY] - [Project URL]
**Date:** [Current Date]

---

## 1. Overview & Context *(Core - Always Include)*

### Feature Summary
[Brief description from the Linear project and feature spec]

### Related User Stories
- **[ISSUE-XX]:** [Story Title] - [URL]
- **[ISSUE-YY]:** [Story Title] - [URL]
[List all user stories from the Linear project with actual issue IDs]

---

## 2. Architecture Overview *(Core - Always Include)*

### Component Diagram
[Mermaid component diagram showing data flow and interactions]

### Key Components
[List main components and their responsibilities]

---

## 3. Data Models *(Optional - Include if database changes)*

### Database Schema Changes
[Detailed schema changes, new tables, modified columns]

### Entity Relationships
[ER diagrams or relationship descriptions]

### Migration Strategy
[How to migrate existing data if applicable]

---

## 4. API Contracts *(Optional - Include if API changes)*

### Endpoints

#### [METHOD] /path/to/endpoint
**Description:** [What this endpoint does]

**Request:**
```json
{
  "field": "value"
}
```

**Response:**
```json
{
  "field": "value"
}
```

**Error Responses:**
- `400`: [Error scenario and exact message]
- `404`: [Error scenario and exact message]

[Repeat for each endpoint]

---

## 5. UI Components *(Optional - Include if frontend changes)*

### Component Structure
[List of React/Vue/Angular components to create/modify]

### Component Hierarchy
```
ParentComponent
├── ChildComponent1
└── ChildComponent2
```

### Props/Events
[Key props and events for major components]

---

## 6. State Management *(Optional - Include if complex state)*

### State Structure
[Redux store structure, Vuex modules, React Context, etc.]

### State Flow
[How state updates flow through the application]

### Side Effects
[Async operations, API calls, etc.]

---

## 7. Integration Points *(Optional - Include if third-party integrations)*

### External Services
- **[Service Name]**: [Purpose and integration method]
- **[Service Name]**: [Purpose and integration method]

### Webhooks/Events
[Webhooks to subscribe to or events to emit]

### Error Handling
[How to handle external service failures]

---

## 8. Security Considerations *(Optional - Include if security relevant)*

### Authentication & Authorization
[Auth requirements and access control]

### Data Protection
[Sensitive data handling, encryption, etc.]

### Input Validation
[Validation rules and sanitization]

### Compliance
[GDPR, HIPAA, or other compliance requirements]

---

## 9. Testing Strategy *(Core - Always Include)*

### Unit Tests
[What needs unit test coverage]

### Integration Tests
[What needs integration testing]

### E2E Tests
[Critical user flows to test end-to-end]

### Test Data
[Test data requirements and setup]

---

## 10. Monitoring & Observability *(Optional - Include if performance critical)*

### Key Metrics
| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| [metric_name] | [What it measures] | [When to alert] |

### Logging
- **Info Level:** [What to log]
- **Warning Level:** [What to log]
- **Error Level:** [What to log]

### Alerts
[Specific alerts to configure]

---

## 11. Infrastructure/Deployment *(Optional - Include if infrastructure changes)*

### Infrastructure Changes
[New services, containers, cloud resources]

### Deployment Strategy
[How to deploy this feature]

### Rollback Plan
[How to rollback if issues occur]

### Scaling Considerations
[Horizontal/vertical scaling needs]

---

## 12. Open Questions & Decisions *(Core - Always Include)*

- [ ] [Question or decision needed]
- [ ] [Question or decision needed]

---

## 13. References *(Core - Always Include)*

- **Linear Project:** [PROJECT-KEY] - [URL]
- **Feature Spec:** [Path to feature spec document]
- **User Stories:** [Links to Linear issues in this project]
- **PRD:** [Path to PRD]
- **Architecture Docs:** [Link to project architecture documentation if available]
</spec_template>

## Guidelines

### Section Selection
1. **Analyze First**: Before generating the spec, analyze the feature type and user stories to determine which optional sections are needed
2. **Only Include Relevant Sections**: Don't include optional sections just to fill space - only add them when they provide value
3. **Document Why**: In the spec, briefly note why certain sections were included or excluded if it's not obvious
4. **Use the Guide**: Refer to the Section Selection Guide above to make consistent decisions

### Content Quality
1. **Extract exact error messages** from acceptance criteria
2. **Reference specific user stories** for each requirement
3. **Be concrete** - No placeholders in API specs, use actual field names
4. **Follow project conventions** - Check project documentation for architecture patterns, testing approaches, and tech stack preferences
5. **Include localization examples** where relevant (error messages, sample data in target language)
6. **Cross-reference** - Link sections together (e.g., "See Section 8 for security validation rules")
7. **Adapt to project structure** - Review existing specs/docs to match the project's format and style

### Examples of Section Combinations

**Backend API Feature:**
- Core sections
- Data Models
- API Contracts
- Security Considerations
- Monitoring (if high-traffic)

**Frontend UI Feature:**
- Core sections
- UI Components
- State Management (if complex)

**Integration Feature:**
- Core sections
- Integration Points
- Security Considerations
- Monitoring (for external service health)

**Infrastructure Feature:**
- Core sections
- Infrastructure/Deployment
- Monitoring & Observability

## Output

After generating and saving the spec:

```markdown
Generated technical specification for Linear Project [PROJECT-KEY]:

**Feature:** [Feature Name]
**Linear Project:** [PROJECT-KEY] - [URL]
**Location:** [Path where spec was saved]

**Sections Included:**
- Core: Overview, Architecture, Testing, Open Questions, References
- Optional: [List which optional sections were included and why]
  - Data Models: [Brief reason]
  - API Contracts: [Brief reason]
  - UI Components: [Brief reason]
  - [etc.]

**Contents Summary:**
- [N] user stories covered
- [Specific counts based on included sections, e.g.:]
  - [N] API endpoints specified (if API Contracts included)
  - [N] database models defined (if Data Models included)
  - [N] UI components specified (if UI Components included)
  - [N] integration points documented (if Integration Points included)

Next steps:
1. Review the technical spec with stakeholders
2. Clarify any open questions in the Open Questions section
3. Begin implementation with `/plan-user-story [ISSUE-ID]` for the first story
```
