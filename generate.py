#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CANONICAL = ROOT / "d3"
DIST = ROOT / "dist"
PLATFORM_FILE = CANONICAL / "d3.platform.yaml"

PLATFORMS = ["claude", "codex", "copilot", "cursor"]

TEMPLATE_VAR_PATTERN = re.compile(r"\{\{[a-z_]+(?:\([^)]*\))?\}\}")


def load_platforms():
    with open(PLATFORM_FILE) as f:
        return yaml.safe_load(f)["platforms"]


def substitute_variables(content, platform_cfg):
    content = content.replace("{{config_file}}", platform_cfg["config_file"])

    for tool_key in ("read", "write", "search", "glob", "bash"):
        content = content.replace(
            "{{" + tool_key + "_tool}}", platform_cfg["tools"][tool_key]
        )

    pattern = r'\{\{invoke_skill\("([^"]*)",\s*"((?:[^"\\]|\\.)*)"\)\}\}'
    template = platform_cfg["invoke_skill"]

    def replace_invoke(match):
        name = match.group(1)
        args = match.group(2)
        return template.replace("{name}", name).replace("{args}", args)

    return re.sub(pattern, replace_invoke, content)


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


def write_output(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def process_file(src_path, platform_cfg, file_type):
    content = src_path.read_text(encoding="utf-8")
    content = substitute_variables(content, platform_cfg)
    fm, body = parse_frontmatter(content)
    return fm, body, transform_frontmatter(fm, body, file_type, platform_cfg)


def copy_references(skill_dir, dest_dir):
    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)
        for ref_file in refs_dir.glob("*.md"):
            shutil.copy2(ref_file, dest_dir / ref_file.name)


def generate_claude(platforms):
    cfg = platforms["claude"]
    out = DIST / "claude"

    if out.exists():
        shutil.rmtree(out)

    metadata_dir = CANONICAL / "metadata"
    plugin_names = ["d3", "d3-markdown", "d3-atlassian"]
    metas = {
        name: yaml.safe_load((metadata_dir / f"{name}.yaml").read_text())
        for name in plugin_names
    }

    for name, meta in metas.items():
        plugin_json = {k: meta[k] for k in ("name", "version", "description", "author", "homepage", "repository", "keywords", "license")}
        write_output(
            out / name / ".claude-plugin" / "plugin.json",
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
        marketplace["plugins"].append({
            k: meta[k] for k in ("name", "description", "version", "author", "homepage", "repository", "license", "keywords")
        } | {"source": source_dir, "category": category})
    write_output(
        out / ".claude-plugin" / "marketplace.json",
        json.dumps(marketplace, indent=2) + "\n",
    )

    for cmd_file in (CANONICAL / "commands").glob("*.md"):
        _, _, final = process_file(cmd_file, cfg, "command")
        write_output(out / "d3" / "commands" / cmd_file.name, final)

    for skill_dir in (CANONICAL / "skills").iterdir():
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            _, _, final = process_file(skill_file, cfg, "skill")
            write_output(out / "d3" / "skills" / skill_dir.name / "SKILL.md", final)
        copy_references(skill_dir, out / "d3" / "skills" / skill_dir.name / "references")

    provider_map = {
        "markdown": ("d3-markdown", "markdown"),
        "atlassian": ("d3-atlassian", "atlassian"),
    }
    for provider_dir_name, (plugin_name, prefix) in provider_map.items():
        provider_dir = CANONICAL / "providers" / provider_dir_name
        if not provider_dir.exists():
            continue
        for provider_file in provider_dir.glob("*.md"):
            _, _, final = process_file(provider_file, cfg, "skill")
            skill_name = f"{prefix}-{provider_file.stem}"
            write_output(out / plugin_name / "skills" / skill_name / "SKILL.md", final)


def generate_codex(platforms):
    cfg = platforms["codex"]
    out = DIST / "codex"

    if out.exists():
        shutil.rmtree(out)

    for cmd_file in (CANONICAL / "commands").glob("*.md"):
        fm, body, final = process_file(cmd_file, cfg, "command")
        fm["name"] = f"d3-{cmd_file.stem}"
        final = transform_frontmatter(fm, body, "command", cfg)
        write_output(out / ".agents" / "skills" / f"d3-{cmd_file.stem}" / "SKILL.md", final)

    for skill_dir in (CANONICAL / "skills").iterdir():
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            _, _, final = process_file(skill_file, cfg, "skill")
            write_output(out / ".agents" / "skills" / skill_dir.name / "SKILL.md", final)
        copy_references(skill_dir, out / ".agents" / "skills" / skill_dir.name / "references")

    for provider_dir in (CANONICAL / "providers").iterdir():
        if not provider_dir.is_dir():
            continue
        for provider_file in provider_dir.glob("*.md"):
            fm, body, _ = process_file(provider_file, cfg, "skill")
            skill_name = fm.get("name", f"{provider_dir.name}-{provider_file.stem}")
            final = transform_frontmatter(fm, body, "skill", cfg)
            write_output(out / ".agents" / "skills" / skill_name / "SKILL.md", final)

    config_content = (CANONICAL / "config" / "example-config.md").read_text(encoding="utf-8")
    write_output(out / "AGENTS.md", config_content)


def generate_copilot(platforms):
    cfg = platforms["copilot"]
    out = DIST / "copilot"

    if out.exists():
        shutil.rmtree(out)

    for cmd_file in (CANONICAL / "commands").glob("*.md"):
        fm, body, _ = process_file(cmd_file, cfg, "command")
        fm["name"] = f"d3-{cmd_file.stem}"
        final = transform_frontmatter(fm, body, "command", cfg)
        write_output(out / ".github" / "skills" / f"d3-{cmd_file.stem}" / "SKILL.md", final)

    for skill_dir in (CANONICAL / "skills").iterdir():
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            _, _, final = process_file(skill_file, cfg, "skill")
            write_output(out / ".github" / "skills" / skill_dir.name / "SKILL.md", final)
        copy_references(skill_dir, out / ".github" / "skills" / skill_dir.name / "references")

    for provider_dir in (CANONICAL / "providers").iterdir():
        if not provider_dir.is_dir():
            continue
        for provider_file in provider_dir.glob("*.md"):
            fm, body, _ = process_file(provider_file, cfg, "skill")
            skill_name = fm.get("name", f"{provider_dir.name}-{provider_file.stem}")
            final = transform_frontmatter(fm, body, "skill", cfg)
            write_output(out / ".github" / "skills" / skill_name / "SKILL.md", final)

    config_content = (CANONICAL / "config" / "example-config.md").read_text(encoding="utf-8")
    write_output(out / ".github" / "copilot-instructions.md", config_content)


def generate_cursor(platforms):
    cfg = platforms["cursor"]
    out = DIST / "cursor"

    if out.exists():
        shutil.rmtree(out)

    for cmd_file in (CANONICAL / "commands").glob("*.md"):
        _, _, final = process_file(cmd_file, cfg, "command")
        write_output(out / ".cursor" / "rules" / f"d3-{cmd_file.stem}" / "RULE.md", final)

    for skill_dir in (CANONICAL / "skills").iterdir():
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            _, _, final = process_file(skill_file, cfg, "rule")
            write_output(out / ".cursor" / "rules" / skill_dir.name / "RULE.md", final)
        copy_references(skill_dir, out / ".cursor" / "rules" / skill_dir.name / "references")

    for provider_dir in (CANONICAL / "providers").iterdir():
        if not provider_dir.is_dir():
            continue
        for provider_file in provider_dir.glob("*.md"):
            fm, body, _ = process_file(provider_file, cfg, "rule")
            rule_name = fm.get("name", f"{provider_dir.name}-{provider_file.stem}")
            final = transform_frontmatter(fm, body, "rule", cfg)
            write_output(out / ".cursor" / "rules" / rule_name / "RULE.md", final)

    config_content = (CANONICAL / "config" / "example-config.md").read_text(encoding="utf-8")
    config_fm = {
        "description": "D3 provider and template configuration. Always include in context.",
        "alwaysApply": True,
    }
    final = build_frontmatter(config_fm) + "\n" + config_content
    write_output(out / ".cursor" / "rules" / "d3-config" / "RULE.md", final)


GENERATORS = {
    "claude": generate_claude,
    "codex": generate_codex,
    "copilot": generate_copilot,
    "cursor": generate_cursor,
}


def validate_canonical():
    unresolved = []
    for md_file in CANONICAL.rglob("*.md"):
        if md_file.is_relative_to(CANONICAL / "skills" / "d3-templates" / "references"):
            continue
        content = md_file.read_text(encoding="utf-8")
        matches = TEMPLATE_VAR_PATTERN.findall(content)
        if matches:
            unresolved.append((md_file.relative_to(ROOT), matches))
    return unresolved


def validate_output(platform_name):
    out_dir = DIST / platform_name
    if not out_dir.exists():
        return [("(not generated)", ["directory does not exist"])]

    issues = []
    for md_file in out_dir.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        matches = TEMPLATE_VAR_PATTERN.findall(content)
        if matches:
            issues.append((md_file.relative_to(DIST), matches))
    return issues


def main():
    parser = argparse.ArgumentParser(description="Generate D3 platform-specific output")
    parser.add_argument(
        "--platform",
        choices=PLATFORMS,
        help="Generate for a specific platform",
    )
    parser.add_argument("--all", action="store_true", help="Generate for all platforms")
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate no unresolved variables in output",
    )
    parser.add_argument(
        "--validate-canonical",
        action="store_true",
        help="List template variables in canonical source",
    )

    args = parser.parse_args()

    if not any([args.platform, args.all, args.validate, args.validate_canonical]):
        parser.print_help()
        sys.exit(1)

    platforms = load_platforms()

    if args.validate_canonical:
        unresolved = validate_canonical()
        if unresolved:
            print("Template variables found in canonical source:")
            for path, matches in unresolved:
                print(f"  {path}: {', '.join(set(matches))}")
        else:
            print("No template variables found in canonical source.")
        return

    if args.platform:
        targets = [args.platform]
    elif args.all:
        targets = PLATFORMS
    else:
        targets = []

    for target in targets:
        print(f"Generating {target}...")
        GENERATORS[target](platforms)
        print(f"  Output: dist/{target}/")

    if args.validate or targets:
        check_targets = targets or PLATFORMS
        all_clean = True
        for target in check_targets:
            issues = validate_output(target)
            if issues:
                all_clean = False
                print(f"\nUnresolved variables in {target}:")
                for path, matches in issues:
                    print(f"  {path}: {', '.join(set(matches))}")

        if all_clean and check_targets:
            print("\nValidation passed: no unresolved variables in output.")


if __name__ == "__main__":
    main()
