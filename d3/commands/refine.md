---
description: Refine an existing D3 artifact based on new information (meeting transcripts, technical decisions, feedback, or discussions). Automatically detects artifact type from the Storage table in d3.config.md and which sections need updating. Updates only affected sections while preserving existing content. When related artifacts exist (e.g., stories for a spec), analyzes impact and proposes updates. Use when updating any artifact, adding details, incorporating meeting notes, or when user mentions refining/updating/improving an existing artifact.
---

## Core Principle

**Update only what has new information. Preserve everything else.**

Automatically detect which sections need updating. Don't fill empty sections just because they exist.

---

## Workflow

### 1. Load Configuration and Templates
- Read `d3.config.md`
- Read Quiet Mode from Settings
- Load templates from paths configured in Templates section

### 2. Fetch Artifact
Command accepts artifact identifier, path, or title in `$ARGUMENTS`.

Determine artifact type by matching the artifact's path or content against the Storage table rows in `d3.config.md`:
- Check if the path falls under a Storage row's Location
- If ambiguous, check content structure against the matching template

If the type cannot be determined, ask the user which artifact type this is (presenting options from the Storage table).

Read the artifact from the Storage location.

### 3. Detect Related Artifacts
Search the Storage table for other artifact types that may be affected by changes to this artifact (e.g., stories linked to a spec). Store for later impact analysis.

### 4. Analyze Current State
Display the artifact's current coverage: title, path, sections with content vs placeholders, and uncertainty marker count.

### 5. Request Refinement Input

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

### 6. Analyze New Information

**CRITICAL - Non-Greedy Updates:**

Update ONLY sections explicitly addressed in new input.

**DO NOT:**
- Invent details not discussed
- Elaborate beyond what was stated
- Fill empty sections just because they're empty
- Remove `_To be defined_` without replacement content
- Treat template examples as prompts to fill

**DO:**
- Add only explicitly stated information
- Replace placeholders when discussed
- Add uncertainty markers for ambiguous info
- Preserve empty sections if not discussed

**Section-by-Section Process:**
1. Does new information explicitly address this section?
2. YES → Update with actual content
3. NO → Leave unchanged (existing content OR placeholder)

### 7. Show Proposed Changes

Present clear before/after for each changed section with rationale.

**If quiet mode:** Skip presenting proposed changes. Accept all changes and proceed.

### 8. Analyze Related Artifact Impact

**Skip if no related artifacts were found in Step 3.**

For each change, determine if it affects related artifacts. Present the impact analysis and proposed updates.

**If quiet mode:** Skip presenting impact. Proceed with all updates.

### 9. Validate Changes

**Validation checklist:**
- [ ] All changes have clear rationale
- [ ] Uncertainty markers properly updated (resolved → removed, new → added)
- [ ] No hallucination — only documented changes
- [ ] Artifact remains internally consistent
- [ ] Updates maintain template structure
- [ ] Related artifact updates match the changes (no drift)

### 10. Apply Updates

Follow the Instructions column from the Storage table for the matching artifact type.
Write the updated artifact to the Location specified.

If related artifacts are affected, update them following their Storage table row's Instructions.

### 11. Provide Summary

Report what was updated: sections changed, questions resolved, new uncertainties, related artifact updates, and suggest next steps.

---

## Error Handling

| Issue | Action |
|-------|--------|
| No changes detected | Inform user, ask for clarification |
| Conflicting info | Show conflict, ask how to resolve |
| Major scope change | Warn about impact, confirm |
| Update fails | Provide full updated text for manual update |
| Artifact not found | Verify identifier/path, suggest search |
| Cannot detect artifact type | Ask user to specify |
