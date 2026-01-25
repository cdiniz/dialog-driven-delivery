# Refinement Patterns Reference

This file provides guidance for refining existing specifications.

## Template Locations

### Product Specification Template
**Path:** `.claude/templates/feature-spec.md`

Product specification structure - reference for section names and organization.

### Technical Specification Template
**Path:** `.claude/templates/technical-spec.md`

Technical specification structure - reference for section names and organization.

## Smart Detection Logic

The refine-spec skill automatically detects which sections need updating:

**Product Indicators** → Update Product Spec:
- User stories, workflows, personas
- Requirements, features, scope
- Success metrics, business value
- UI/UX decisions

**Technical Indicators** → Update Technical Spec:
- Architecture, design patterns
- Technology choices, frameworks
- APIs, data models, integrations
- Performance, security, testing

**Mixed Content** → Update Both Specs:
- One input can affect both specifications
- Don't force artificial categorization

## Change Presentation Pattern

Always show before/after for each change:

```markdown
### Change 1: [Section Name]

**BEFORE:**
[Current content with enough context]

**AFTER:**
[Proposed content with changes]

**Rationale:** [Why this change]
**Type:** [Addition/Modification/Clarification/Deletion]
```

## Change Types

1. **Addition** - New content in previously empty section (➕ Filled)
2. **Enhancement** - Adding to existing content (✏️ Updated - added X items)
3. **Modification** - Changing existing content (✏️ Updated)
4. **Clarification** - Resolving uncertainty markers (✅ Resolved questions)
5. **Deletion** - Removing obsolete content (❌ Removed)

## Progressive Refinement Strategy

Specs grow through multiple refinement cycles - each cycle may focus on Product, Technical, or both.

## Uncertainty Tracking

Use the `uncertainty-markers` skill for complete guidelines on tracking uncertainties:

**Resolving Uncertainties:**
- Replace `[OPEN QUESTION: ...]` with actual answer
- Replace `[CLARIFICATION NEEDED: ...]` with specific value
- Validate `[ASSUMPTION: ...]` and either confirm or update

**Adding New Uncertainties:**
- New information may raise new questions
- Mark new unknowns with appropriate markers

## Key Principles

1. **Preserve existing content** - only change what needs changing
2. **Show clear before/after** - make changes transparent
3. **Don't force categorization** - let content determine which spec to update
4. **Track uncertainty resolution** - mark questions answered
5. **Maintain consistency** - ensure both specs stay aligned
6. 