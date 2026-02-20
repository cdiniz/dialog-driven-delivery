#!/usr/bin/env python3
import argparse
import json
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
PLATFORM_FILE = ROOT / "d3.platform.yaml"
METADATA_DIR = ROOT / "metadata"
CONFIG_DIR = ROOT / "config"

D3_DIR = ROOT / "d3"
D3_MARKDOWN_DIR = ROOT / "d3-markdown"
D3_ATLASSIAN_DIR = ROOT / "d3-atlassian"

PLATFORMS = ["claude", "codex", "copilot", "cursor"]



def load_platforms():
    with open(PLATFORM_FILE) as f:
        return yaml.safe_load(f)["platforms"]


def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content

    end = content.index("---", 3)
    fm_text = content[3:end].strip()
    body = content[end + 3:].lstrip("\n")
    fm = yaml.safe_load(fm_text) or {}
    return fm, body


def build_frontmatter(fields):
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, list):
            lines.append(f"{k}: {json.dumps(v)}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def transform_frontmatter(fm, body, file_type, platform_cfg):
    fm_spec = platform_cfg.get("frontmatter", {})
    spec = fm_spec.get(file_type) or fm_spec.get(next(iter(fm_spec), None), {})

    if isinstance(spec, dict):
        allowed_fields = spec.get("fields", list(fm.keys()))
        defaults = spec.get("defaults", {})
    else:
        allowed_fields = spec or list(fm.keys())
        defaults = {}

    new_fm = {k: v for k, v in fm.items() if k in allowed_fields}
    for k, v in defaults.items():
        if k not in new_fm:
            new_fm[k] = v

    return build_frontmatter(new_fm) + "\n" + body


def read_source(src_path, file_type, platform_cfg):
    content = src_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    return fm, body, transform_frontmatter(fm, body, file_type, platform_cfg)


def write_output(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_references(src_dir, dest_dir):
    refs_dir = src_dir / "references"
    if refs_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)
        for ref_file in refs_dir.glob("*.md"):
            shutil.copy2(ref_file, dest_dir / ref_file.name)


def generate_platform_md(platform_cfg):
    tools = platform_cfg["tools"]
    tool_rows = [
        ("read tool", tools["read"]),
        ("write tool", tools["write"]),
        ("search tool", tools["search"]),
        ("glob tool", tools["glob"]),
        ("shell tool", tools["bash"]),
    ]

    invoke_example = platform_cfg["invoke_skill"].replace(
        "{name}", "<skill-name>"
    ).replace("{args}", "<arguments>")

    lines = [
        "# D3 Platform Reference",
        "",
        "## Tool Mapping",
        "| Reference | Tool |",
        "|---|---|",
    ]
    for label, tool in tool_rows:
        lines.append(f"| {label} | `{tool}` |")

    lines.extend([
        "",
        "## Skill Invocation",
        "To invoke a skill, use this syntax:",
        "```",
        invoke_example,
        "```",
    ])

    refs_path = platform_cfg.get("references_path")
    if refs_path:
        lines.extend([
            "",
            "## Template References",
            "D3 template files are located at:",
            "```",
            refs_path,
            "```",
        ])

    return "\n".join(lines) + "\n"


def _platform_md_with_frontmatter(platform_name, platform_cfg, file_type):
    body = generate_platform_md(platform_cfg)
    fm = {
        "name": "d3-platform",
        "description": f"D3 platform-specific tool and configuration mappings for {platform_name}. Read this before executing D3 commands or skills.",
    }

    fm_spec = platform_cfg.get("frontmatter", {})
    spec = fm_spec.get(file_type) or fm_spec.get(next(iter(fm_spec), None), {})

    if isinstance(spec, dict):
        allowed_fields = spec.get("fields", list(fm.keys()))
        defaults = spec.get("defaults", {})
    else:
        allowed_fields = spec or list(fm.keys())
        defaults = {}

    final_fm = {k: v for k, v in fm.items() if k in allowed_fields}
    for k, v in defaults.items():
        if k not in final_fm:
            final_fm[k] = v

    return build_frontmatter(final_fm) + "\n" + body


# --- Source iterators ---

def iter_commands():
    for cmd_file in sorted((D3_DIR / "commands").glob("*.md")):
        yield cmd_file.stem, cmd_file


def iter_skills():
    for skill_dir in sorted((D3_DIR / "skills").iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == "d3-platform":
            continue
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            yield skill_dir.name, skill_file, skill_dir


def iter_providers():
    for provider_dir in (D3_MARKDOWN_DIR, D3_ATLASSIAN_DIR):
        skills_dir = provider_dir / "skills"
        if not skills_dir.exists():
            continue
        for skill_dir in sorted(skills_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_file = skill_dir / "SKILL.md"
            if skill_file.exists():
                yield skill_dir.name, skill_file


# --- Platform generators ---

def generate_claude(platforms, output_root=None):
    cfg = platforms["claude"]
    base = output_root or ROOT

    plugin_dirs = {
        "d3": base / "d3",
        "d3-markdown": base / "d3-markdown",
        "d3-atlassian": base / "d3-atlassian",
    }

    metas = {
        name: yaml.safe_load((METADATA_DIR / f"{name}.yaml").read_text())
        for name in plugin_dirs
    }

    for name, meta in metas.items():
        plugin_json = {
            k: meta[k]
            for k in ("name", "version", "description", "author", "homepage", "repository", "keywords", "license")
        }
        write_output(
            plugin_dirs[name] / ".claude-plugin" / "plugin.json",
            json.dumps(plugin_json, indent=2) + "\n",
        )

    d3_meta = metas["d3"]
    marketplace = {
        "name": "d3-marketplace",
        "owner": {"name": "D3 Team", "email": "claudio@cdiniz.com"},
        "metadata": {
            "description": d3_meta["description"],
            "version": d3_meta["version"],
        },
        "plugins": [],
    }
    for name, source_dir, category in [
        ("d3", "./d3", "productivity"),
        ("d3-atlassian", "./d3-atlassian", "integrations"),
        ("d3-markdown", "./d3-markdown", "productivity"),
    ]:
        meta = metas[name]
        marketplace["plugins"].append(
            {
                k: meta[k]
                for k in ("name", "description", "version", "author", "homepage", "repository", "license", "keywords")
            }
            | {"source": source_dir, "category": category}
        )
    write_output(
        base / ".claude-plugin" / "marketplace.json",
        json.dumps(marketplace, indent=2) + "\n",
    )

    platform_md = _platform_md_with_frontmatter("Claude Code", cfg, "skill")
    write_output(base / "d3" / "skills" / "d3-platform" / "SKILL.md", platform_md)


def generate_codex(platforms):
    cfg = platforms["codex"]
    out = DIST / "codex"
    d3_dir = out / ".agents" / "skills" / "d3"

    if out.exists():
        shutil.rmtree(out)

    for name, cmd_file in iter_commands():
        fm, body, _ = read_source(cmd_file, "command", cfg)
        skill_name = f"d3-{name}"
        fm["name"] = skill_name
        final = transform_frontmatter(fm, body, "command", cfg)
        write_output(d3_dir / skill_name / "SKILL.md", final)

    for name, skill_file, skill_dir in iter_skills():
        _, _, final = read_source(skill_file, "skill", cfg)
        write_output(d3_dir / name / "SKILL.md", final)
        copy_references(skill_dir, d3_dir / name / "references")

    for name, provider_file in iter_providers():
        fm, body, _ = read_source(provider_file, "skill", cfg)
        final = transform_frontmatter(fm, body, "skill", cfg)
        write_output(d3_dir / name / "SKILL.md", final)

    platform_md = _platform_md_with_frontmatter("Codex", cfg, "skill")
    write_output(d3_dir / "d3-platform" / "SKILL.md", platform_md)

    config_content = (CONFIG_DIR / "example-config.md").read_text(encoding="utf-8")
    write_output(out / "d3.config.md", config_content)


def _copilot_name(name):
    return name if name.startswith("d3-") else f"d3-{name}"


def generate_copilot(platforms):
    cfg = platforms["copilot"]
    out = DIST / "copilot"
    prompts_dir = out / ".github" / "prompts"
    agents_dir = out / ".github" / "agents"

    if out.exists():
        shutil.rmtree(out)

    for name, cmd_file in iter_commands():
        fm, body, _ = read_source(cmd_file, "command", cfg)
        prompt_name = f"d3-{name}"
        fm["name"] = prompt_name
        final = transform_frontmatter(fm, body, "command", cfg)
        write_output(prompts_dir / f"{prompt_name}.prompt.md", final)

    for name, skill_file, skill_dir in iter_skills():
        fm, body, _ = read_source(skill_file, "skill", cfg)
        agent_name = _copilot_name(name)
        fm["name"] = agent_name
        final = transform_frontmatter(fm, body, "skill", cfg)
        write_output(agents_dir / f"{agent_name}.agent.md", final)
        copy_references(skill_dir, out / ".github" / agent_name / "references")

    for name, provider_file in iter_providers():
        fm, body, _ = read_source(provider_file, "skill", cfg)
        agent_name = _copilot_name(name)
        fm["name"] = agent_name
        final = transform_frontmatter(fm, body, "skill", cfg)
        write_output(agents_dir / f"{agent_name}.agent.md", final)

    instructions_dir = out / ".github" / "instructions"
    platform_body = generate_platform_md(cfg)
    platform_fm = build_frontmatter({"applyTo": '"**"'})
    write_output(instructions_dir / "d3-platform.instructions.md", platform_fm + "\n" + platform_body)

    config_content = (CONFIG_DIR / "example-config.md").read_text(encoding="utf-8")
    write_output(out / "d3.config.md", config_content)


def generate_cursor(platforms):
    cfg = platforms["cursor"]
    out = DIST / "cursor"
    d3_dir = out / ".cursor" / "rules" / "d3"
    cmd_dir = out / ".cursor" / "commands"

    if out.exists():
        shutil.rmtree(out)

    for name, cmd_file in iter_commands():
        _, body, _ = read_source(cmd_file, "command", cfg)
        write_output(cmd_dir / f"d3-{name}.md", body)

    for name, skill_file, skill_dir in iter_skills():
        _, _, final = read_source(skill_file, "rule", cfg)
        write_output(d3_dir / name / "RULE.md", final)
        copy_references(skill_dir, d3_dir / name / "references")

    for name, provider_file in iter_providers():
        fm, body, _ = read_source(provider_file, "rule", cfg)
        final = transform_frontmatter(fm, body, "rule", cfg)
        write_output(d3_dir / name / "RULE.md", final)

    platform_md = _platform_md_with_frontmatter("Cursor", cfg, "rule")
    write_output(d3_dir / "d3-platform" / "RULE.md", platform_md)

    config_content = (CONFIG_DIR / "example-config.md").read_text(encoding="utf-8")
    write_output(out / "d3.config.md", config_content)


GENERATORS = {
    "claude": generate_claude,
    "codex": generate_codex,
    "copilot": generate_copilot,
    "cursor": generate_cursor,
}


def main():
    parser = argparse.ArgumentParser(description="Generate D3 platform-specific output")
    parser.add_argument(
        "--platform",
        choices=PLATFORMS,
        help="Generate for a specific platform",
    )
    parser.add_argument("--all", action="store_true", help="Generate for all platforms")

    args = parser.parse_args()

    if not any([args.platform, args.all]):
        parser.print_help()
        sys.exit(1)

    platforms = load_platforms()

    if args.platform:
        targets = [args.platform]
    elif args.all:
        targets = PLATFORMS
    else:
        targets = []

    for target in targets:
        print(f"Generating {target}...")
        GENERATORS[target](platforms)
        if target == "claude":
            print("  Output: d3/ (metadata + platform ref)")
        else:
            print(f"  Output: dist/{target}/")

    print("\nDone.")


if __name__ == "__main__":
    main()
