# E2E Tests

End-to-end tests that run multi-turn Claude conversations against the D3 skills.

## Prerequisites

- `claude` CLI installed and authenticated
- `uv sync --group dev`

## Running

```bash
# parallel (default) — tests run concurrently via pytest-xdist
uv run pytest tests/e2e

# sequential with timing logs
uv run pytest tests/e2e -n0 -s

# single test
uv run pytest tests/e2e -n0 -s -k test_create_spec_from_transcript
```

## Test suites

| Suite                      | Tests                                                                          | Description                                          |
| -------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------- |
| `TestMarkdownWorkflow`     | create_spec_from_transcript, refine_existing_spec, decompose_spec_into_stories | Each test uses its own fixture with pre-seeded state  |
| `TestMarkdownConfiguration`| create_spec_uses_custom_template                                               | Independent — runs in parallel with the above         |

## How it works

1. **Plugin isolation** — plugins (`d3`, `d3-markdown`) are copied to `tests/e2e/.workspaces/plugin-fixtures/<worker>/` with template files swapped for simplified e2e versions
2. **Workspaces** — each test gets its own directory under `tests/e2e/.workspaces/<test_name>/`
3. **Parallelism** — `pytest-xdist` with `-n auto` runs tests concurrently across workers

## Inspecting failures

Workspaces persist after runs. Check the generated specs and stories in:

```
tests/e2e/.workspaces/<test_name>/specs/
tests/e2e/.workspaces/<test_name>/stories/
```

When running with `-n0`, `<test_name>` is the full test node name (e.g. `test_create_spec_from_transcript`).

## Design decisions

- **Multi-turn conversations** — uses `--resume` to chain turns rather than single-turn prompt-stuffing. Slower but far more reliable since skill confirmation gates work as designed
- **Template swapping** — plugins are copied with minimal template files. The model fills every template section regardless of input, so smaller templates = faster generation
- **SKILL.md drives behaviour** — the model follows the skill description more than the actual template files. Swapping templates alone had no effect until SKILL.md was also swapped
- **Simplified fixtures** — a 2-line transcript about a static page. Template size drives generation time, not input complexity
- **Haiku is not viable** — hallucinates file creation (claims to write files without actually doing it)

## Profiling

Run with `-n0 -s` to see per-turn timing:

```
[claude] turn 2/3 | wall=99.4s api=96.7s cli=1.4s turns=14 in=34 out=3905 cost=$0.3182
```

| Field  | Meaning                                        |
| ------ | ---------------------------------------------- |
| wall   | Total wall-clock time for this turn            |
| api    | Time in API calls (inference + tool execution) |
| cli    | Claude Code CLI overhead                       |
| turns  | Internal tool-use turns the model took         |
| in/out | Input/output token counts                      |
| cost   | API cost in USD                                |
