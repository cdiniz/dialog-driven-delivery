# D3 Quiet Mode Convention

Defines the quiet mode behavioural contract for all D3 skills.

## What Quiet Mode Means

Quiet mode suppresses interactive steps so the skill can run non-interactively (e.g. from a script or CI pipeline). It is enabled by setting `Quiet Mode: true` in the `### Settings` section of `d3.config.md`.

## Default Behaviour in Quiet Mode

- **Input:** Use text provided in `$ARGUMENTS` directly. Do not ask the user for input.
- **Questions:** Skip any step that asks the user to choose or confirm.
- **Proposals:** Auto-accept proposed values (titles, dates, statuses, decomposition options).
- **Defaults:** Use default values from provider configuration (e.g. Default Location, Default Project).
- **Uncertainty markers:** Leave markers in place rather than resolving them interactively.
- **Validation and review:** Skip steps that present content for user approval; proceed directly to creation or storage.

## How to Write Quiet Mode Branches in Skills

Keep inline conditionals short. The shared contract provides the reasoning; the skill only needs to state the specific action:

```
**If quiet mode:** [specific action] — e.g. "accept the proposed title immediately", "skip this question", "use Default Location from config".

**Otherwise:** [interactive step]
```
