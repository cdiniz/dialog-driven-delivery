import re

import yaml


def extract_headings(content: str) -> list[tuple[str, str]]:
    return re.findall(r"^(#{1,4})\s+(.+)$", content, re.MULTILINE)


def heading_texts(content: str) -> list[str]:
    return [text.strip() for _, text in extract_headings(content)]


def heading_texts_lower(content: str) -> str:
    return " | ".join(h.lower() for h in heading_texts(content))


def has_placeholder(content: str) -> bool:
    lower = content.lower()
    indicators = [
        "to be defined",
        "not yet discussed",
        "not yet defined",
        "tbd",
        "[to be defined]",
        "not yet determined",
    ]
    return any(ind in lower for ind in indicators)


def extract_uncertainty_markers(content: str) -> dict[str, list[str]]:
    markers = {}
    for marker_type in [
        "OPEN QUESTION",
        "DECISION PENDING",
        "ASSUMPTION",
        "CLARIFICATION NEEDED",
    ]:
        pattern = rf"\[{marker_type}:\s*([^\]]+)\]"
        markers[marker_type] = re.findall(pattern, content)
    return markers


def total_markers(content: str) -> int:
    return sum(len(v) for v in extract_uncertainty_markers(content).values())



def extract_sections(content: str) -> dict[str, str]:
    sections = {}
    current = None
    lines: list[str] = []
    for line in content.split("\n"):
        match = re.match(r"^#{1,4}\s+(.+)$", line)
        if match:
            if current:
                sections[current] = "\n".join(lines)
            current = match.group(1).strip().lower()
            lines = []
        else:
            lines.append(line)
    if current:
        sections[current] = "\n".join(lines)
    return sections


def markers_tracked_in_open_questions(content: str) -> bool:
    markers = extract_uncertainty_markers(content)
    trackable = markers.get("OPEN QUESTION", []) + markers.get("CLARIFICATION NEEDED", [])
    if not trackable:
        return True
    lower = content.lower()
    return "open questions" in lower


def extract_frontmatter(content: str) -> dict | None:
    match = re.match(r"^---\n(.+?)\n---", content, re.DOTALL)
    if not match:
        return None
    return yaml.safe_load(match.group(1))
