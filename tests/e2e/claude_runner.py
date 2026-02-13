import json
import subprocess
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

def _log_timing(label: str, wall_s: float, parsed: dict):
    api_ms = parsed.get("duration_api_ms", 0)
    total_ms = parsed.get("duration_ms", 0)
    turns = parsed.get("num_turns", "?")
    cost = parsed.get("total_cost_usd", 0)
    usage = parsed.get("usage", {})
    in_tok = usage.get("input_tokens", 0)
    out_tok = usage.get("output_tokens", 0)
    cli_ms = total_ms - api_ms
    print(
        f"\n[claude] {label} | wall={wall_s:.1f}s "
        f"api={api_ms / 1000:.1f}s cli={cli_ms / 1000:.1f}s "
        f"turns={turns} in={in_tok} out={out_tok} cost=${cost:.4f}"
    )


def run_claude_conversation(
    messages: list[str],
    cwd: str,
    plugin_dirs: list[str],
    timeout_per_turn: int = 300,
    model: str = "sonnet",
) -> str:
    plugin_flags = []
    for d in plugin_dirs:
        plugin_flags.extend(["--plugin-dir", d])

    json_flags = [
        "--model", model,
        "--dangerously-skip-permissions",
        "--setting-sources", "",
        "--output-format", "json",
        *plugin_flags,
    ]

    session_id = None
    output = ""

    for i, message in enumerate(messages):
        flags = list(json_flags)
        if session_id:
            flags.extend(["--resume", session_id])

        start = time.monotonic()
        result = subprocess.run(
            ["claude", "-p", *flags],
            cwd=cwd,
            input=message,
            capture_output=True,
            text=True,
            timeout=timeout_per_turn,
        )
        elapsed = time.monotonic() - start

        if result.returncode != 0 and result.stderr:
            raise RuntimeError(f"claude -p failed (turn {i + 1}): {result.stderr[:500]}")

        parsed = json.loads(result.stdout)
        _log_timing(f"turn {i + 1}/{len(messages)}", elapsed, parsed)
        session_id = parsed["session_id"]
        output = parsed.get("result", "")

    return output
