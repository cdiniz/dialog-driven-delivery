# Archived Commands (v1.0)

These commands were used in version 1.0 of the Spec-Driven Development workflow and have been superseded by the simplified v2.0 commands.

## Archived Commands

### Product-Focused Commands
- `generate-feature-brief.md` - Created Product Specification only
- `refine-feature-brief.md` - Updated Product Specification only

### Technical-Focused Commands
- `create-technical-spec.md` - Created Technical Specification only
- `refine-technical-spec.md` - Updated Technical Specification only

## Migration to v2.0

These commands have been consolidated into:
- `/create-spec` - Creates both Product and Technical specs in one go
- `/refine-spec PROJECT-KEY` - Updates any part of the specs based on content

## Why Archived?

The v1.0 approach forced an artificial separation between product and technical information. The v2.0 approach:
- Uses single commands that handle both aspects naturally
- Fills only what's available from the input
- Allows progressive enhancement
- Reduces cognitive load on users

## If You Need These Commands

While not recommended, you can still reference these commands if needed for:
- Understanding the evolution of the workflow
- Maintaining projects that were started with v1.0
- Extracting specific logic for custom implementations

For new projects, please use the v2.0 commands in the parent directory.