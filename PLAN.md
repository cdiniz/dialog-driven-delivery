# LLM Wiki Integration — Plan

Working branch: `llm-wiki`. Design & rationale: see [`DESIGN.md`](./DESIGN.md).

- [x] Decide on separate team-brain repo (not inside product repo)
- [x] Add optional `Brain Source` setting to config samples (all 3 variants)
- [x] Add option D "pull from brain" to `d3/skills/create/SKILL.md`
- [x] Add option F "pull from brain" to `d3/skills/refine/SKILL.md`
- [x] Draft fake product (Pageturner — used-book marketplace)
- [x] Write 5 seed transcripts under `team-brain/raw/meetings/`
- [x] Ingest transcripts → brain produced summaries, decisions, concepts, project hub
- [x] Fix D3 retrieval flow in SKILL.md — current wording assumes flat topic tags, real brain is hub-and-spoke with keyword-bearing titles
- [x] Create fake product repo at `/Users/asier/dev/play/team-wiki-d3/pageturner`
- [x] Install local D3 plugin in fake product repo
- [x] Run `/d3:init` and set `Brain Source: ../team-brain`
- [x] Validate: `/d3:create product-spec catalog-browse` pulls the 2 browse decisions + 2 relevant summaries + concept; ignores ceremonies/people; reflects the 2026-04-06 supersession
- [x] Validate: `/d3:create product-spec checkout` pulls fee + mechanics decisions + refinement summary; ignores browse-specific files
- [x] Validate: `/d3:refine` option F applies delta-only updates from a new ingested transcript
- [x] Validate failure case: remove `wiki/index.md` → D3 falls back to paste flow without hard-failing
- [ ] Resolve open questions (from DESIGN.md)
  - [ ] Publish D3-generated artifacts back to the brain? (risk: telephone-game drift)
  - [x] ~~Remove `distill` from D3 and drop the `Transcripts` artifact row?~~ **Decided: keep.** Brain is an alternative to D3's transcript handling, not a replacement. Teams without a brain still need `distill` and `/d3:create transcript`.
  - [ ] Topic taxonomy discipline — how to prevent naming drift across ingestions?
- [ ] Remove `PLAN.md` and `DESIGN.md`
- [ ] Bump plugin version in `d3/.claude-plugin/plugin.json`
