---
description: Generate technical specification for PRD feature
---

Generate a technical specification for PRD feature $ARGUMENTS and save it to the project's documentation structure.

## Steps

1. **Locate PRD**: Find the PRD file (typically `docs/prd.md`, `PRD.md`, or similar)
2. **Find Feature**: Locate the specified feature (e.g., "Feature 1.1") in the PRD
3. **Query Stories**: Query Linear to find all user stories for this feature (search by title prefix "[Feature X.X]")
4. **Analyze Requirements**: Review feature requirements, user stories, and acceptance criteria
5. **Generate Spec**: Create comprehensive technical specification following the template below
6. **Determine Structure**: Ask user for preferred location or use: `docs/specs/feature_[X.X]/` or `docs/epics/epic_[N]/feature_[X.X]/`
7. **Save Spec**: Create directory structure if needed and save the spec

## Technical Spec Template

<spec_template>
# Technical Specification: [Feature Name]

**Feature:** [Feature Number and Name from PRD]
**Epic:** [Epic Name]
**Date:** [Current Date]

---

## 1. Overview & Context

### Feature Summary
[Brief description of the feature from PRD]

### Related User Stories
- **[ISSUE-XX]:** [Story Title] - [URL]
- **[ISSUE-YY]:** [Story Title] - [URL]
[List all stories for this feature with actual issue IDs]

---

## 2. Architecture Overview

### Component Diagram
[mermaid component diagram showing data flow]

---

## 3. Data Models

### Database Schema 
[Changes to the Schema]

## 4. API Contracts

### OpenAPI Specification
[Changes to the API specification]

---

## 5. Security Considerations

[ Authentication & Authorization, Input Security, etc]

---

## 6. Testing Strategy

[High Level testing strategy]

---

## 7. Monitoring & Observability

### Key Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| [metric_name] | [What it measures] | [When to alert] |

### Log Events

- **Info Level:** Successful operations
- **Warning Level:** Validation failures, business rule violations
- **Error Level:** Unexpected errors, database failures

### Error Monitoring

- Track error rates by endpoint
- Alert on error rate spikes
- Detailed error context for debugging

### Performance Monitoring

- Response time percentiles (p50, p95, p99)
- Database query performance
- API endpoint throughput

---

## 8. Open Questions & Decisions

- [ ] [Question or decision needed]
- [ ] [Question or decision needed]

---

## 9. References

- PRD: [Path to PRD] - Feature [X.X]
- User Stories: [Links to Linear issues]
- Architecture Docs: [Link to project architecture documentation if available]
</spec_template>

## Guidelines

- **Extract exact error messages** from acceptance criteria
- **Reference specific user stories** for each requirement
- **Be concrete** - No placeholders in API specs, use actual field names
- **Follow project conventions** - Check project documentation for architecture patterns, testing approaches, and tech stack preferences
- **Include localization examples** where relevant (error messages, sample data in target language)
- **Cross-reference** - Link sections together (e.g., "See Section 5 for validation rules")
- **Adapt to project structure** - Review existing specs/docs to match the project's format and style

## Output

After generating and saving the spec:

```markdown
Generated technical specification for Feature [X.X]:

**Location:** [Path where spec was saved]

**Contents:**
- [N] API endpoints specified
- [N] database models defined
- [N] user stories covered
- [N] security considerations documented

Next steps:
1. Review the technical spec with stakeholders
2. Clarify any open questions
3. Begin implementation planning of user stories
```
