---
description: Create comprehensive feature specification from any input context
---

# /create-spec

This command invokes the `create-spec` skill to create a comprehensive feature specification using your configured provider.

## Quick Usage

```
/create-spec
```

## What This Command Does

Creates a specification document containing both Product and Technical specifications from any input context (meeting transcript, document, or conversational discussion). The skill fills only known information and marks uncertainties explicitly, allowing specs to grow progressively over time.

## Examples

**From Meeting Transcript:**
```
/create-spec
[Paste transcript when prompted]
```

**Conversational:**
```
/create-spec
[Discuss feature interactively]
```

## Next Steps

- Refine specification: `/refine-spec [spec-identifier]`
- Decompose into stories: `/decompose [spec-identifier]`

## See Also

- [SPEC_README.md](./SPEC_README.md) - Complete spec-driven workflow
- [refine-spec](./refine-spec.md) - Update existing specifications
- [decompose](./decompose.md) - Create user stories from specs

---

**Note**: This command invokes the `create-spec` skill automatically.
