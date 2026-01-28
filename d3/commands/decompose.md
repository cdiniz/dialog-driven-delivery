---
description: Decompose feature into user stories through conversational planning
---

# /decompose

This command invokes the `decompose` skill to break down feature specifications into user stories using your configured provider.

## Quick Usage

```
/decompose [spec-identifier or URL]
```

## What This Command Does

Decomposes a feature specification into independently deliverable user stories. Creates an Epic to organize stories, uses workflow-based decomposition for maximum value delivery, and supports both transcript-based and conversational planning. Links all stories to specifications and manages dependencies.

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

- Review created stories in your work tracking tool
- Create dependency links manually (instructions provided)
- Begin implementation: Use superpowers skills

## See Also

- [SPEC_README.md](./SPEC_README.md) - Complete spec-driven workflow
- [create-spec](./create-spec.md) - Create feature specifications
- [refine-spec](./refine-spec.md) - Update specifications

---

**Note**: This command invokes the `decompose` skill automatically.
