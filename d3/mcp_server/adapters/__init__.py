from __future__ import annotations

from typing import Any

from .base import BaseAdapter
from .markdown import MarkdownAdapter

ADAPTERS: dict[str, type[BaseAdapter]] = {
    "markdown": MarkdownAdapter,
}


def create_adapter(adapter_name: str, config: dict[str, Any]) -> BaseAdapter:
    adapter_cls = ADAPTERS.get(adapter_name)
    if adapter_cls is None:
        raise ValueError(f"Unknown adapter: {adapter_name}. Available: {list(ADAPTERS)}")
    return adapter_cls(config)
