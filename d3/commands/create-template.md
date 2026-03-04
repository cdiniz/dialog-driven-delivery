---
description: Create a new D3 artifact template. Guides through section structure design, ensures Open Questions section exists (required for uncertainty markers), and generates a template markdown file. Use when a team needs a custom artifact type beyond the built-in templates, or when adapting D3 to domain-specific workflows.
---

## Core Principle

**Templates define artifact structure. Every template needs an Open Questions section for uncertainty tracking.**

Templates are plain markdown files with heading structure. D3 commands use them to scaffold artifacts — filling sections with content from input and marking unknowns. A well-designed template captures the essential structure of an artifact type without being prescriptive about content.

---

## Workflow

### 1. Ask What the Template Is For

Ask the user:
```
What type of artifact is this template for?

For example: "Design Review", "Risk Assessment", "API Contract", "Sprint Retrospective"
```

Store the artifact type name for later use.

### 2. Guide Section Structure

Suggest starting from a similar existing template:
```
Would you like to start from an existing template as a base?

Available templates:
1. Product Spec (5 sections — good for requirements-focused artifacts)
2. Tech Spec (8 sections — good for implementation-focused artifacts)
3. ADR (7 sections — good for decision-focused artifacts)
4. Meeting Transcript (5 sections — good for capture-focused artifacts)
5. Start from scratch
```

If starting from an existing template, load it and present its structure for modification.

Work with the user to define sections:
- What main sections does this artifact need?
- What subsections, if any?
- What metadata fields (title, date, status, etc.)?
- Are there sections that should be optional vs required?

### 3. Ensure Open Questions Section

Check whether the user's section list includes an Open Questions section (or equivalent — "Questions", "Unknowns", "Open Items").

**If missing:** Explain why it's needed and add it:
```
D3 uses uncertainty markers ([OPEN QUESTION], [CLARIFICATION NEEDED], etc.)
to prevent AI hallucination. These markers need a tracking section.

Adding "Open Questions" section to your template.
```

The Open Questions section should include:
- Questions raised during artifact creation
- Assumptions made that need validation
- Items needing clarification

### 4. Generate Template File

Generate a markdown template file with:
- All agreed sections as headings
- Brief guidance text under each heading (what content belongs there)
- The Open Questions section with standard subsections (Questions, Assumptions)
- Any metadata fields as a header block

### 5. Write Template File

Ask where to save the template file. Suggest `.d3/templates/[artifact-type-slug].md` as the default path.

Write the template file to the specified path.

### 6. Suggest Config Addition

Show the user what to add to their `d3.config.md` to register the new artifact type:

```
Add this to your d3.config.md:

Under ### Artifacts:

#### [Artifact Type Name]
- Provider: [suggest appropriate provider, e.g. d3-markdown:markdown-spec-provider]
- Provider Config:
  - Directory: ./[suggested-directory]
  - Default Location: .

Under ### Templates:
- [Artifact Type Name]: [path-to-template-file]
```

---

## Error Handling

| Issue | Action |
|-------|--------|
| User wants to overwrite existing template | Warn, confirm before overwriting |
| Template path not writable | Suggest alternative path |
| No sections defined | Guide user through minimum viable structure |

---

## Key Principles

1. **Open Questions required** — Every template must have a section for tracking uncertainties
2. **Start from existing** — Building on a similar template is faster than starting blank
3. **Guidance not prescription** — Template text guides content, doesn't constrain it
4. **Config integration** — Always suggest the config addition to register the new type
