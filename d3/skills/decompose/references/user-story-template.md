# User Story Template Reference

This file provides decompose-specific guidance for creating user stories in Jira.

## Template Location

**Path:** `claude./templates/user-story.md`

Complete user story template with Gherkin-style acceptance criteria.

## Workflow-Based Decomposition

The decompose skill uses workflow-based decomposition:

**Principle**: Each story = one complete user journey end-to-end

**Benefits:**
- Clear user value in every story
- Easy to prioritize by user impact
- Natural mapping to feature spec workflows
- Each story can be demoed independently

## Team Structure Adaptations

**Full-Stack Teams:**
Keep workflows as single stories (backend + frontend together)

**Split Teams (Backend/Frontend):**
Split first workflow by layer, keep others as full-stack to maintain momentum

## Story Size Guidelines

**Small (1-3 days):** Single component/endpoint, 3-5 ACs, minimal dependencies
**Medium (3-5 days):** Multiple components, 5-8 ACs, some dependencies
**Large (5-10 days):** Complex workflow, 8-12 ACs, multiple dependencies - consider splitting

## Uncertainty Handling

Before creating stories, check specs for uncertainty markers. Use the `uncertainty-markers` skill for complete guidelines:

**If uncertainties exist:**
- `[OPEN QUESTION]` → Note in story description with spec link
- `[DECISION PENDING]` → Flag story with "needs-clarification" label
- `[CLARIFICATION NEEDED]` → Add to Technical Notes section
- `[ASSUMPTION]` → Document in Technical Notes for validation

## Epic-Story Linking

Stories are linked to Epic as parent using provider-specific mechanisms. For example, Jira uses `additional_fields`:

```javascript
{
  additional_fields: {
    parent: {
      key: "[EPIC-KEY]"
    }
  }
}
```

If linking fails, manual linking instructions are provided in the decompose summary.

## Dependency Documentation

Dependencies are documented in story descriptions under Technical Notes section. Manual issue links must be created in your work tracking tool after stories are created (instructions provided in summary).

## Key Principles

1. **One workflow = one story** (default approach)
2. **End-to-end value** in each story
3. **Complete ACs** covering all scenarios
4. **Clear dependencies** documented
5. **Link to specification** for full context
6. **Adapt to team structure** when needed
7. **Handle uncertainties** explicitly
   