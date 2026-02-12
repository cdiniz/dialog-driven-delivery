import re

import yaml


def extract_headings(content: str) -> list[tuple[str, str]]:
    return re.findall(r"^(#{1,4})\s+(.+)$", content, re.MULTILINE)


def heading_texts(content: str) -> list[str]:
    return [text.strip() for _, text in extract_headings(content)]


def heading_texts_lower(content: str) -> str:
    return " | ".join(h.lower() for h in heading_texts(content))


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


def has_placeholder(content: str) -> bool:
    lower = content.lower()
    indicators = [
        "to be defined",
        "not yet discussed",
        "tbd",
        "[to be defined]",
        "not yet determined",
    ]
    return any(ind in lower for ind in indicators)


def extract_frontmatter(content: str) -> dict | None:
    match = re.match(r"^---\n(.+?)\n---", content, re.DOTALL)
    if not match:
        return None
    return yaml.safe_load(match.group(1))
