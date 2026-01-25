# Specification Templates Reference

This file provides pointers to the specification templates used by create-spec.

## Template Locations

### Product Specification Template
**Path:** `.claude/templates/feature-spec.md`

Complete product specification structure for features.

### Technical Specification Template
**Path:** `.claude/templates/technical-spec.md`

Complete technical specification structure for implementation guidance.

## Combined Specification Structure

The create-spec skill creates a single Confluence page with both specifications:

```markdown
# Feature: [Feature Name]

## 📋 Product Specification
[Product spec sections from .claude/templates/feature-spec.md]

---

## 🔧 Technical Specification
[Technical spec sections from .claude/templates/technical-spec.md]
```

## Usage Guidelines

1. **Read both templates** to understand complete structure
2. **Fill only what you know** - use placeholders for empty sections
3. **Use uncertainty markers** - invoke the `uncertainty-markers` skill for complete guidelines
4. **Progressive enhancement** - specs grow over time through refinement
