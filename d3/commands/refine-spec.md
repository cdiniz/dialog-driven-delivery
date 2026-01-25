---
description: Refine existing feature specifications based on new information
---

# /refine-spec

This command invokes the `refine-spec` skill to update existing Confluence specifications with new information.

## Quick Usage

```
/refine-spec [PAGE-ID or URL]
```

## What This Command Does

Updates any part of existing Product and Technical specifications based on new input (meeting transcripts, technical decisions, feedback, or discussions). Automatically detects which sections need updating, shows before/after changes, and preserves existing content.

## Examples

**Update from Meeting:**
```
/refine-spec 123456789
[Paste transcript when prompted]
```

**Add Technical Details:**
```
/refine-spec https://yoursite.atlassian.net/wiki/spaces/PROJ/pages/123456789
[Provide technical decisions]
```

**Combined Update:**
```
/refine-spec "Feature Name"
[Updates both Product and Technical specs]
```

## Next Steps

- Continue refining: `/refine-spec [PAGE-ID]`
- Decompose into stories: `/decompose [PAGE-ID]`

## See Also

- [SPEC_README.md](./SPEC_README.md) - Complete spec-driven workflow
- [create-spec](./create-spec.md) - Create new specifications
- [decompose](./decompose.md) - Create user stories from specs

---

**Note**: This command invokes the `refine-spec` skill automatically.
