---
description: Refine any existing D3 artifact with new information (meeting transcripts, technical decisions, feedback, or discussions). Automatically detects artifact type from provider, loads the matching template, and applies non-greedy updates — only sections with new information change. Use when updating specs, adding details to existing documentation, incorporating meeting notes, or when user mentions refining/updating/improving an existing artifact.
---

## Core Principle

**Update only what has new information. Preserve everything else.**

Detect which sections need updating based on the new input. Don't fill empty sections just because they exist. The template validates structure is maintained.

---

## Workflow

### 1. Read Configuration

- Read `d3.config.yaml` from the project root
- Parse `artifacts` map for available artifact types, their adapters, and adapter configs
- Parse `templates` map for custom template paths (optional)
- Parse `settings` for `quiet_mode` (default: `false` when absent)
- Store configuration for later steps

**If `d3.config.yaml` not found:** Check for legacy `d3.config.md`. If found, inform the user their config uses the old format and guide them to create a `d3.config.yaml`.

### 2. Fetch Existing Artifact

Parse `$ARGUMENTS` for an artifact identifier (filename, ID, URL, or title).

Determine which artifact type owns it by trying each configured artifact type:
1. If the identifier clearly matches a type (e.g. filename contains "product-spec", title suffix) → use that type directly
2. If ambiguous → try `search_artifacts(artifact_type="...", query="...")` for each type until one returns a match
3. If the user provides a type hint in `$ARGUMENTS` (e.g. `/d3:refine Product Spec about-page`) → use that type directly

Fetch the artifact using `read_artifact(artifact_type="...", artifact_id="...")`.

Store the artifact content, identifier, and detected type.

### 3. Load Template

Resolve the template for the detected artifact type:
1. Check `### Templates` section for a custom path matching the artifact type name
2. If custom path found → Read that file
3. If no custom path → Use d3-templates skill's default template lookup table
4. If no default match → Proceed without template validation

### 4. Display Current State

```
**Artifact:** [Type]: [Title] - [path/URL]

Current State:
- Sections with content: [X/Y]
- Sections empty/placeholder: [Z]
- Uncertainty markers: [N]
```

### 5. Get New Input

**If quiet mode and new content provided in `$ARGUMENTS`:** Use the provided text directly as refinement input. Skip the question below.

**Otherwise:**
Ask user:
```
How would you like to provide new information?
A) Paste meeting transcript
B) Paste updated documentation
C) Describe changes
D) Paste review feedback
```

**Optional — Reference other artifacts as context:**

After receiving primary input, ask:
```
Would you like to reference any existing artifacts as additional context?
```

If yes: use `search_artifacts` and `read_artifact` to find and fetch the reference artifact, include as context.

### 6. Analyse New Information

**Smart Detection:**
- Identify what's new vs. what already exists in the artifact
- Determine which sections are affected by the new input
- Map new information to specific template sections

**CRITICAL — Non-Greedy Updates:**

Update ONLY sections explicitly addressed in new input.

**DO NOT:**
- Invent details not discussed
- Elaborate beyond what was stated
- Fill empty sections just because they're empty
- Remove `_To be defined_` placeholders without replacement content
- Treat template examples as prompts to fill

**DO:**
- Add only explicitly stated information
- Replace placeholders when new content addresses them
- Add uncertainty markers for ambiguous new info
- Preserve empty sections if not discussed
- Update Open Questions when markers are resolved or added

**Section-by-Section Process:**
1. Does new information explicitly address this section?
2. YES → Update with actual content
3. NO → Leave unchanged (existing content OR placeholder)

### 7. Show Proposed Changes

Present clear before/after:
```
Proposed Changes:

### [Section Name]
BEFORE: [Current content]
AFTER: [Proposed content]
Rationale: [Why this section is being updated]
Type: [Addition/Modification/Clarification/Resolution]

[Repeat for each affected section]

---
Summary:
- Sections updated: [X]
- Questions resolved: [Y]
- New uncertainties: [Z]

Does this look correct?
```

**If quiet mode:** Skip presenting proposed changes. Accept all changes and proceed.

### 8. Validate Changes

**Validation checklist:**
- [ ] All changes have clear rationale
- [ ] Before/after shows enough context
- [ ] Uncertainty markers properly updated (resolved removed, new ones added)
- [ ] No hallucination — only documented changes
- [ ] Template structure maintained (all headings still present)

**Uncertainty handling:**
- Resolved → Remove markers and corresponding Open Questions entries
- New → Add markers and corresponding Open Questions entries

### 9. Update via MCP

Use the D3 MCP server's `update_artifact` tool:
```
update_artifact(
  artifact_type="[type_key]",
  artifact_id="[artifact-id]",
  body="[UPDATED_CONTENT]",
  version_message="[description of changes]"
)
```

### 10. Provide Summary

```
Artifact refined: [Type]: [Title] - [path/URL]

What Was Updated:
- [Section]: [Brief description of change]
- [Section]: [Brief description of change]

Coverage Change:
- Before: [X/Y] sections filled
- After: [X/Y] sections filled

Uncertainty Markers:
- Resolved: [N]
- Added: [M]
- Remaining: [Total]

Next steps:
- Continue refining: /d3:refine
- [Context-appropriate suggestions]
```

---

## Error Handling

| Issue | Action |
|-------|--------|
| Artifact not found | Verify identifier, suggest search via `search_artifacts` |
| No changes detected | Inform user, ask for clarification |
| Conflicting info | Show conflict, ask how to resolve |
| Ambiguous updates | Ask which section to update |
| Major scope change | Warn about impact, confirm |
| MCP tool failed | Show error, provide full updated text for manual update |
| Template not found | Proceed without template validation, warn user |

---

## Key Principles

1. **Non-greedy** — Only change what has new information
2. **Template-validated** — Structure is checked against template after updates
3. **Adapter-agnostic** — MCP server routes to the correct adapter based on config
4. **Track resolution** — Remove resolved uncertainty markers, add new ones
5. **Preserve existing** — Content not addressed by new input stays exactly as-is
6. **Rationale required** — Every change must have a clear reason

**Change Types:**
- Addition: New content in empty/placeholder section
- Enhancement: Adding to existing content
- Modification: Changing existing content
- Clarification: Resolving uncertainty markers
- Resolution: Answering open questions
