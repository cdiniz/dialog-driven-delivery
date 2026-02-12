import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

DEFAULT_FLAGS = [
    "--model", "sonnet",
    "--dangerously-skip-permissions",
    "--output-format", "text",
    "--plugin-dir", str(REPO_ROOT / "d3"),
    "--plugin-dir", str(REPO_ROOT / "d3-markdown"),
]


def run_claude(prompt: str, cwd: str, timeout: int = 300, model: str | None = None) -> str:
    flags = list(DEFAULT_FLAGS)
    if model:
        flags[flags.index("sonnet")] = model
    result = subprocess.run(
        ["claude", "-p", *flags],
        cwd=cwd,
        input=prompt,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0 and result.stderr:
        raise RuntimeError(f"claude -p failed: {result.stderr[:500]}")
    return result.stdout
