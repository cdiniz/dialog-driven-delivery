# LLM Wiki Integration — Design

Progress and tasks: see [`PLAN.md`](./PLAN.md).

## Goal

Add a team-wide knowledge repo ("brain" / llm-wiki) as an optional input source for D3. Teams using the brain stop pasting transcripts into D3 and ask D3 to pull relevant context from the wiki.

Inspiration: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Repos

- **product repo** — source code. Installs D3 plugin. Holds D3-generated artifacts only.
- **team-brain repo** — knowledge store. Raw inputs + distilled wiki. Multi-product. No D3 plugin.
- **d3 plugin repo (this one)** — the plugin. Consumed by product repos.

### Why the brain is a separate repo

- Different lifecycle (append-heavy knowledge vs versioned code).
- Different access control (transcripts may contain sensitive content).
- Multi-product reality (knowledge rarely maps 1:1 to one codebase).
- Scale (raw transcripts outweigh code quickly).
- Tooling independence (may migrate to Confluence/Notion/vector DB later — keep that a config change).

## Brain contract (what D3 needs from any llm-wiki)

D3 is not coupled to any specific brain layout. It needs only:

- An **entry-point index file** the brain exposes at a known path (configured via `Brain Source` + conventional filename, e.g. `index.md`).
- Entries in that index with **topic-bearing titles** and links to readable markdown files.
- Files reachable by following those links (relative paths, plain markdown).

Everything else — folder structure, categorisation, brain-side commands — is the brain repo's business and varies per team.

## Diagram

```mermaid
flowchart LR
    subgraph Inputs["Raw inputs"]
        M[Meetings]
        S[Slack]
        D[Docs]
    end

    subgraph Brain["team-brain repo"]
        RAW["raw/"]
        WIKI["wiki/<br/>(distilled content)"]
        IDX["index.md"]
        RAW -->|ingest| WIKI
        WIKI --> IDX
    end

    subgraph Product["product repo"]
        CFG["d3.config.md<br/>Brain Source: ../team-brain"]
        D3[D3 plugin]
        ART["specs / ADRs / stories"]
        CFG --> D3 --> ART
    end

    M --> RAW
    S --> RAW
    D --> RAW
    IDX -.-> D3
    WIKI -.-> D3
    USER([User]) -->|/d3:create topic| D3
```

Solid = writes. Dashed = reads. Brain is read-only from D3's side.

## Retrieval flow (D3 side)

1. Read the brain's entry-point index file.
2. Keyword-match the user's topic against entry titles across all sections (case/punctuation/whitespace tolerant).
3. If hub pages are linked from the index (project overview, topic hub), optionally read them to discover further relevant links.
4. Confirm matched files with the user before reading.
5. Read the confirmed files and feed them as input context to the existing `create` / `refine` flow.

Rules:
- Missing/malformed index → warn and fall back to paste flow. Never hard-fail.
- D3 never writes to the brain.
- Supersession, freshness, and conflict resolution are the brain's responsibility (typically via dated files).

Known limitations:
- Retrieval quality depends entirely on ingest quality (topic keywords must appear in titles).
- No alias layer — title drift between ingestions causes misses.

## D3 changes (on branch `llm-wiki`)

- `config-samples/*.md` — optional `Brain Source` setting.
- `d3/skills/create/SKILL.md` — reads Brain Source; step 3 gains option D when set.
- `d3/skills/refine/SKILL.md` — reads Brain Source; step 5 gains option F; defaults to current artifact title.
- Nothing removed. Paste-based flow still works.

## Reference brain (used for validation)

Located at `/Users/asier/dev/play/team-wiki-d3/team-brain`.

Structure:
- `raw/` — inputs (`meetings/`, `slack/`, `other/`).
- `wiki/` — distilled output (`summaries/`, `decisions/`, `concepts/`, `projects/`, `people/`).
- `wiki/index.md` — entry point.
- `.claude/commands/` — brain-side `/ingest`, `/query`, `/lint`.

Seed product: **Pageturner**, a used-book marketplace. 5 transcripts across kickoff, roadmap, ceremonies, refinement, and a three-amigos. Ingestion produced summaries + dated decisions (including one that supersedes a refinement open question) + a concept page + a project hub.

## Open questions

- Publish D3-generated artifacts back to the brain? (risk: telephone-game drift)
- Remove `distill` / `capture-transcript` from D3 once the brain flow is proven?
- Topic taxonomy discipline — how to prevent naming drift across ingestions?

## Out of scope / future

- Remove `distill` / `capture-transcript` (later, after validation).
- Publish D3 artifacts back to the brain.
- MCP server / remote API integration for the brain.
- Auth, access control, multi-tenant brains.
- Embeddings / semantic search.
- Automate ingestion (Slack bot, meeting recorder integration, scheduled pulls). Core logic already exists in the brain's ingest prompt — open question is trigger + quality.
