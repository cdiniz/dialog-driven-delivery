---
description: Create any D3 artifact from input context (meeting transcripts, documents, or conversational discussion). Supports all artifact types configured in the artifact catalog — Product Specs, Tech Specs, ADRs, Meeting Transcripts, or any custom type with a template. Use when starting a new feature, documenting a planning meeting, recording an architectural decision, capturing a transcript, or creating any structured artifact.
---

## Core Principle

**The template drives the structure. Fill only what you know. Empty sections are better than hallucinated content.**

This command creates any artifact type defined in the project's artifact catalog. The template determines what sections exist. The command provides scaffolding: config parsing, input gathering, uncertainty markers, validation, and provider dispatch. No domain-specific logic lives here — that lives in templates.

---

## Workflow

### 1. Read Configuration

- Read `d3.config.md` for D3 Configuration section
- Parse `### Artifacts` for available artifact types. Each artifact entry has:
  - **Name** (the `####` heading, e.g. "Product Spec", "ADR", "Meeting Transcript")
  - **Provider** — skill reference and plugin (e.g. `d3-markdown:markdown-spec-provider`)
  - **Provider Config** — directory, default location, and other provider-specific settings
- Parse `### Templates` for custom template paths (optional section — if absent, defaults are used)
- Parse `### Settings` for Quiet Mode (default: `false` when absent)
- Store configuration for later steps

**If no `### Artifacts` section found:** Check for legacy config format (`### Spec Provider`, `### Product Spec Provider`, etc.). If found, inform the user their config uses the old format and guide them to update. Do not proceed with legacy config.

### 2. Determine Artifact Type

Parse `$ARGUMENTS` for an artifact type name. Match against the available types from Step 1 (case-insensitive).

**If quiet mode and type is clear from `$ARGUMENTS`:** Use the matched type and proceed.

**If type is clear from `$ARGUMENTS` (not quiet mode):** Confirm the type with the user.

**If type is ambiguous or absent:** Present the available types and ask the user to pick:
```
What type of artifact would you like to create?

Available types:
1. Product Spec
2. Tech Spec
3. ADR
4. Meeting Transcript
[... all types from ### Artifacts]
```

### 3. Load Template

Resolve the template for the chosen artifact type:
1. Check `### Templates` section for a custom path matching the artifact type name
2. If custom path found → Read that file
3. If no custom path → Use d3-templates skill's default template lookup table
4. If no default match → Ask user for a template path

Read the template file. Store the template structure (section headings, expected content patterns).

### 4. Get Input

**If quiet mode and input text provided in `$ARGUMENTS`:** Use the provided text directly as input context. Skip the questions below.

**Otherwise:**
Ask user:
```
How would you like to provide the information?
A) Paste meeting transcript
B) Paste existing document
C) Describe conversationally
```

**Optional — Reference other artifacts as context:**

After receiving primary input, ask:
```
Would you like to reference any existing artifacts as additional context? (e.g. an existing spec, ADR, or transcript)
```

If yes:
1. Ask which artifact type to search
2. Use that type's provider to search/list artifacts
3. Fetch the selected artifact
4. Include its content as additional context for generation

### 5. Get Location

**If quiet mode:** Use Default Location from the artifact type's provider config. If no default is configured, use the provider's root location (`.`).

**Otherwise:**
Ask where to create the artifact. If needed, use the provider's `list_locations` operation.

### 6. Analyse Input and Propose Title

Analyse the input against the template structure:
- Identify which template sections have relevant information in the input
- Extract key themes, entities, and decisions
- Identify uncertainties: questions, ambiguities, assumptions, pending decisions

Propose a descriptive title.

**If quiet mode:** Accept the proposed title immediately.

**Otherwise:** Present the title and wait for confirmation.

### 7. Generate Artifact

**CRITICAL RULES:**

1. **Create FULL structure from template:**
   - ALL section headings from the template
   - Never skip sections
   - Preserve the template's heading hierarchy

2. **Fill ONLY what was discussed:**
   - Discussed → Real content
   - NOT discussed → `_To be defined - not yet discussed_`
   - Template examples are structure guides, NOT content

3. **NEVER invent:**
   - Details, decisions, names, or specifics not present in the input
   - When in doubt: placeholder, not guess

4. **Mark uncertainties:**
   - `[OPEN QUESTION: ...]` — User didn't answer or information is missing
   - `[CLARIFICATION NEEDED: ...]` — Requirement or statement is vague
   - `[ASSUMPTION: ...]` — Reasonable inference from context
   - `[DECISION PENDING: ...]` — Multiple approaches, not yet decided

Invoke the uncertainty-markers skill for detailed guidance on marker usage.

### 8. Validate Before Creation

**Structure validation:**
- [ ] ALL template headings present
- [ ] No sections skipped
- [ ] Each discussed section has real content
- [ ] Each non-discussed section has placeholder text
- [ ] No template examples treated as real content

**Uncertainty validation:**
- [ ] Count all markers: `[OPEN QUESTION]`, `[ASSUMPTION]`, `[CLARIFICATION NEEDED]`, `[DECISION PENDING]`
- [ ] Each `[OPEN QUESTION]` and `[CLARIFICATION NEEDED]` marker has a corresponding entry in an Open Questions section (if the template has one)
- [ ] No hallucinated content — every statement traces to the input

**If quiet mode:** Skip presenting to user. Leave all markers in place and proceed to creation.

**Otherwise — present to user:**
```
Artifact ready with [N] uncertainty markers:
- Open Questions: [X]
- Clarifications: [Y]
- Assumptions: [Z]
- Decisions Pending: [W]

Resolve now, leave marked, or review first?
```

### 9. Create via Provider

Invoke the artifact type's provider skill (see platform reference for invocation syntax).

The provider operation to use depends on the provider type. Read the provider skill to discover available operations. Common patterns:
- Spec-like providers: `create_spec location_id="[LOCATION]" title="[Title]" body="[FULL_CONTENT]"`
- Transcript providers: `store_transcript title="[Title]" meeting_type="[type]" meeting_date="[date]" participants="[list]" body="[FULL_CONTENT]"`

Use the operation that matches the provider's capabilities.

### 10. Provide Summary

```
Artifact created: [Type]: [Title] - [path/URL]

Coverage:
- Sections filled: [X/Y]
- Uncertainty markers: [N]
  - Open Questions: [X]
  - Assumptions: [Z]

Next steps:
- Review the artifact and resolve uncertainty markers
- Refine with new information: /d3:refine
- [Context-appropriate suggestions based on artifact type]
```

---

## Error Handling

| Issue | Action |
|-------|--------|
| No artifacts configured | Guide user to add `### Artifacts` section to `d3.config.md` |
| Artifact type not found | List available types, ask user to pick |
| Template not found | Ask user for template path |
| Ambiguous scope | Ask clarifying questions |
| Minimal concrete info | Warn artifact will be mostly empty, confirm |
| Conflicting info | Mark `[DECISION PENDING]` |
| Creation fails | Provide full artifact text for manual creation |
| Location not found | List available locations |
| Provider skill not found | Guide user to install the provider plugin |

---

## Key Principles

1. **Template-driven** — The template defines what sections exist; the command fills them
2. **Provider-agnostic** — Any provider skill works, operations discovered at runtime
3. **Fill only what you know** — Empty sections are better than hallucinated content
4. **Uncertainty is explicit** — Every unknown gets a marker, every marker gets tracked
5. **Transcript-first** — Meeting transcripts are the preferred input
6. **Progressive filling** — Artifacts grow through refinement, not guessing
