---
description: Decompose feature into user stories through conversational planning
---

# /decompose

This command invokes the `decompose` skill to break down feature specifications into user stories in Jira.

## Quick Usage

```
/decompose [PAGE-ID or URL]
```

## What This Command Does

Decomposes a Confluence feature specification into independently deliverable user stories in Jira. Creates an Epic to organize stories, uses workflow-based decomposition for maximum value delivery, and supports both transcript-based and conversational planning. Links all stories to Confluence specs and manages dependencies.

## Examples

**From Decomposition Meeting:**
```
/decompose 123456789
[Paste meeting transcript when prompted]
```

**Conversational Planning:**
```
/decompose https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789
[Work through decomposition interactively]
```

**By Page Title:**
```
/decompose "Feature Name"
[Agent finds page and guides decomposition]
```

## Next Steps

- Review stories in Jira
- Create dependency links manually (instructions provided)
- Begin implementation: Use superpowers skills

## See Also

- [SPEC_README.md](./SPEC_README.md) - Complete spec-driven workflow
- [create-spec](./create-spec.md) - Create feature specifications
- [refine-spec](./refine-spec.md) - Update specifications

---

**Note**: This command invokes the `decompose` skill automatically.
