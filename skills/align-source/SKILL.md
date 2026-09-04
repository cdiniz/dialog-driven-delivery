---
name: align-source
description: Cross-check an existing D3 artifact against the source input it was generated from — a meeting transcript, a document, or a captured conversation — and report where they disagree. Runs a bidirectional traceability audit: every claim in the artifact must be supported by a line in the source, and every decision, constraint, concern and disagreement in the source must appear somewhere in the artifact. Classifies findings as Fabrication, Omission, Certainty Drift, False Uncertainty, or Attribution Error. Report only — does not modify the artifact. Use whenever the user wants a second pass over a freshly created or distilled artifact, wants to confirm a spec faithfully reflects the meeting it came from, suspects signal was lost or invented in the write-up, or says things like "cross-check this spec against the transcript", "did we lose anything from the meeting", "recheck the artifact against the source", "verify the spec matches what we actually discussed", "audit the distilled transcript against the raw one". The hallmark is an existing artifact plus the raw input it came from, and a question about whether the artifact is faithful to that input.
---

# D3 — Align Artifact with Source

This skill compares an artifact against the raw input it was generated from and reports where they diverge. It is a **reporting** skill — it does not modify the artifact or the source. The output is a findings report a human can act on, usually by feeding it into **d3:refine**.

## Core principle

**The source is the record of what was said. The artifact is an interpretation of it. Interpretation drifts.**

**d3:create** and **d3:distill** apply preventive rules — "could I cite the exact sentence from the input that supports this line?" This skill is that citation test, actually executed, in a fresh context. Verification done in the same pass as generation mostly produces agreement: the model still holds its own reasoning and will rationalise it. Reading the source cold, with a checking mandate rather than a drafting mandate, is what makes the second hop worth taking.

**Two directions, both necessary:**
- **Artifact → source** catches invented content. This is the failure mode everyone anticipates.
- **Source → artifact** catches dropped signal — the concern someone raised that never made it into the write-up. This is the failure mode nobody catches by eye, because absent content is invisible on review.

## Workflow

### 1. Load configuration

- Read `d3.config.md` at the repo root. If missing, stop and tell the user to run **d3:init** first.
- Read Quiet Mode from `### Settings`.
- Invoke the sibling **d3:uncertainty-markers** skill — steps 6 and 7 need the exact semantics of each marker to judge whether one is used correctly.

### 2. Locate the artifact

The user identifies the artifact by path, title, or description. Match it to a row in the Storage table the same way **d3:refine** does:

1. Does the path fall under a Storage row's Location?
2. If ambiguous, does the artifact's structure match one row's Template better than the others?

If it still can't be determined, ask which artifact type it is, presenting the options from the Storage table. Read the artifact's current content following the row's Instructions.

### 3. Locate the source

D3 templates do not record provenance, so the source usually has to be established explicitly rather than followed from a link.

In order of preference:
1. **The user named or pasted it** — use it directly.
2. **The artifact references it** — some artifacts (ADRs in particular) cite the originating discussion in prose. Follow that reference.
3. **Search the Transcripts Location** for files whose title or subject matches the artifact. Propose the best match and ask for confirmation — never assume.
4. **Ask.** If nothing matches, ask the user for the source. Without a source there is nothing to align against; stop rather than guessing.

### 4. Establish source coverage

**This step is what keeps the report from being noise.** Ask — or infer from the user's message:

> Is this the complete set of inputs the artifact was built from, or one of several?

An artifact that was created from one transcript and then refined three times contains a great deal of legitimate content that appears in none of the sources at hand. Checking it against the original transcript alone would flag all of it as invented.

Record the coverage as one of:

- **Complete** — every input that shaped the artifact is available. Both directions of the audit are valid.
- **Partial** — this is one source among several, or the artifact has been refined since creation.

Under **partial** coverage, apply this rule:

| Direction | Valid under partial coverage? |
|-----------|-------------------------------|
| Source → artifact (Omission) | **Yes.** If the source says it and the artifact doesn't, that holds regardless of what other sources exist. |
| Artifact → source (Fabrication) | **No.** Unsupported content may have come from an input you can't see. |

So under partial coverage, findings that would be **Fabrication** are reported as **Unverified** instead, in their own section, described as "no support in the sources provided" rather than "invented". State the coverage mode at the top of the report so nobody reads Unverified as an accusation.

### 5. Choose the audit mode

Two artifact shapes need different checks:

- **Structured artifact** (spec, ADR, story, template-structured transcript) → run the **fidelity audit**, steps 6–7.
- **Distilled transcript compared against its raw original** → run the **removal audit**, step 8. Distill's output is meant to be near-verbatim, so the question is not "is this faithful" but "was everything removed genuinely noise, and were the splits right".

If unclear which applies, ask.

### 6. Build the two inventories

Work through both directions before classifying anything. Findings that look damning in one direction often resolve in the other — content missing from the section you expected frequently turns up somewhere else in the artifact.

**Inventory A — claims (artifact → source).** Walk the artifact section by section and list every substantive assertion: requirements, acceptance criteria, decisions, constraints, numbers, names, rationales. For each, find the supporting line in the source and record it verbatim.

Skip: template headings, placeholder text (`_To be defined - not yet discussed_`), and structural boilerplate. An empty section is not a claim and is never a finding here — **d3:create** is explicitly designed to leave sections empty.

**Inventory B — signal (source → artifact).** Read the source in full and list every piece of substantive signal:

- Decisions and commitments ("we'll cap it at three")
- Constraints, hard limits, deadlines, budgets
- Concerns and objections raised — **including ones nobody answered**
- Disagreements and alternative positions
- Questions asked and left open
- Rationale — the *why* behind a decision, which is the first thing lost in a write-up

For each, locate where it landed in the artifact. Anything that landed nowhere is a candidate Omission.

**Bounded exploration:** for a long source, work through it in passes and note how much was covered. It is better to report confidently on the portion audited than to skim the whole thing. Say in the report what was not fully covered.

### 7. Classify the findings

| Category | Meaning |
|----------|---------|
| **Fabrication** | The artifact asserts something no part of the source supports. Under partial coverage, report as **Unverified** instead. |
| **Omission** | Signal in the source appears nowhere in the artifact — dropped, not deliberately scoped out. |
| **Certainty Drift** | Both mention it, but the artifact **overstates** how settled it is. A "maybe we could" became a Must Have; a live disagreement was flattened into a decision; one speaker's suggestion became the team's position. |
| **False Uncertainty** | The artifact **understates** certainty — something is marked `[OPEN QUESTION]` or `[DECISION PENDING]` that the source actually resolves. Marker noise is corrosive: it trains reviewers to skim past markers, which is exactly when a real one gets missed. |
| **Attribution Error** | A decision, rationale, or ownership is credited to the wrong person or the wrong reason. |

**Severity:**

- **Critical** — a fabricated or drifted claim sitting in a Must Have, an acceptance criterion, or a recorded decision; an omitted firm decision or hard constraint. These get implemented as if they were true.
- **Moderate** — certainty drift on a secondary requirement; an omitted concern, disagreement, or rationale.
- **Minor** — attribution errors, false uncertainty, omitted detail that changes nothing downstream.

**Guards against false positives — do not report these as findings:**

- Paraphrase that preserves meaning. The artifact is a write-up, not a transcript; different words are expected. Only flag when the *meaning* moved.
- Reasonable structural inference — turning "users pick a size then check out" into a two-step user journey is interpretation, not fabrication.
- Content correctly marked with an uncertainty marker. A marked assumption is the system working as designed, not a fabrication.
- Empty sections and `_To be defined_` placeholders.
- Signal the artifact explicitly places out of scope or defers. It was handled, not dropped.

Every finding must quote the source line that supports it, or state plainly that no such line exists. A finding that cannot do either is not a finding.

### 8. Removal audit (distilled transcript mode)

When the artifact is a distilled transcript and the source is the raw original:

1. **Removal check** — diff the two and classify everything removed against **d3:distill**'s own list: greetings, filler, meta-discussion, tangents, restated points. Anything removed that does *not* classify as noise is an Omission, and substantive dialogue removed is Critical.
2. **Preservation check** — verify what distill promises to keep: speaker labels, timestamps, chronological order, exact phrasing on decisions and commitments, and disagreements.
3. **Fidelity check** — flag any summarising, paraphrasing, reordering, or added structure. Distill is meant to cut, not rewrite.
4. **Split check** — if the transcript was split, apply distill's test in reverse to each pair of outputs: *would these reasonably live in the same document if written by hand?* If yes, report an over-split. Related aspects of one subject separated across files is the common error, since distill's stated bias is to keep together.

Report using the same categories and severities as step 7.

### 9. Generate the alignment report

```
## Alignment Report: [Artifact Title]

**Artifact:** [path/URL]
**Source:** [path/URL or description]
**Source coverage:** Complete | Partial — [what's missing]
**Audited:** [N] claims, [M] signal items[, X% of source covered]

---

### Critical Findings

[FIND-1] **[Category]:** [Brief title]
- **Artifact says:** [quote from the artifact, with section]
- **Source says:** [verbatim quote from the source] | *No supporting line found.*
- **Severity:** Critical
- **Recommendation:** [what a refine pass should do]

### Moderate Findings

[FIND-2] ...

### Minor Findings

[FIND-3] ...

### Unverified
*(partial coverage only — content with no support in the sources provided; may originate from an input not audited)*

[FIND-4] ...

---

**Summary:**
- Fabrication: [N]   Omission: [N]   Certainty Drift: [N]
- False Uncertainty: [N]   Attribution Error: [N]
- Faithful: [sections that trace cleanly to the source]
- Coverage gaps: [portions of the source not fully audited]
```

Write the report so it can be **pasted straight into d3:refine as review feedback** — each finding self-contained, quoting both sides, with a concrete recommendation. That is the intended handoff, and a finding that needs the report's surrounding context to make sense will not survive it.

### 10. Provide a final summary

```
Source alignment complete!

**Artifact:** [Title] — [path]
**Source:** [path]  ([Complete / Partial] coverage)

Findings:
- Critical: [N]
- Moderate: [N]
- Minor: [N]
- Unverified: [N]

Faithful areas:
- [sections that trace cleanly to the source]

Coverage gaps:
- [what wasn't fully audited, and why]

Suggested next steps (based on findings):
- Fabrication or Certainty Drift? → d3:refine, pasting this report as review feedback (option D)
- Omission? → d3:refine with the dropped signal quoted from the source
- False Uncertainty? → d3:refine option E, to walk the markers and resolve the ones the source already answers
- Nothing above Minor? → the artifact is faithful to its source; no follow-up needed
```

If nothing above Minor was found, say so plainly and suggest no follow-up. A clean report is a real result, and manufacturing findings to look thorough is the failure mode this skill has to avoid most.

**Quiet mode:** emit the report and the summary without interactive confirmation at any step. Ask nothing; if the source cannot be established from the user's message, report that and stop.

## Error handling

| Issue | Action |
|-------|--------|
| `d3.config.md` missing | Stop. Ask the user to run **d3:init** first. |
| Source cannot be found or named | Stop. There is nothing to align against — ask the user for the source. |
| Artifact not found | Verify the identifier/path; suggest a search |
| Source coverage unclear | Assume **Partial** and say so. Reporting Fabrication as Unverified costs little; the reverse costs trust. |
| Artifact has been refined since creation | Treat as Partial coverage; ask for the later inputs if the user has them |
| Artifact is almost entirely placeholders | Report that it is a stub — run the Omission direction only, and note that the fidelity check has little to work on |
| Source is very long | Audit in passes, report the coverage percentage, name the portions not reached |
| Multiple sources | Audit against all of them together; treat as Complete only if the user confirms the set is exhaustive |
| Findings are all paraphrase-level | Report zero findings. Do not pad a clean result. |

## Key principles

1. **Both directions, every time** — invented content and dropped signal are different failures with different causes; checking one is half a check
2. **Cite or drop it** — every finding quotes the source line or states that none exists
3. **Coverage honesty** — partial coverage downgrades Fabrication to Unverified; never accuse an artifact of inventing what a source you can't see may have said
4. **Paraphrase is not drift** — flag moved meaning, never moved wording
5. **A clean report is a result** — no padding, no manufactured findings
6. **Report only** — present findings and recommendations; **d3:refine** applies them
7. **Fresh eyes** — this runs as its own pass precisely because self-checking inside the generating context finds nothing

## Related skills

- **d3:init** — prerequisite (creates `d3.config.md`)
- **d3:create** — the usual upstream: this skill audits what create produced against what create was given
- **d3:distill** — the other upstream; triggers the removal audit in step 8
- **d3:refine** — the follow-up that applies findings; paste the report in as review feedback (option D)
- **d3:uncertainty-markers** — loaded inline; defines the markers judged in False Uncertainty and Certainty Drift
- **d3:align-spec** — the sibling audit in the other direction: artifact against code, rather than artifact against the conversation it came from
