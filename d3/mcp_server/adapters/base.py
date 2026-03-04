from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseAdapter(ABC):
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config

    @abstractmethod
    def create_artifact(
        self,
        title: str,
        body: str,
        location_id: str = ".",
    ) -> dict:
        ...

    @abstractmethod
    def read_artifact(self, artifact_id: str) -> dict:
        ...

    @abstractmethod
    def update_artifact(
        self,
        artifact_id: str,
        body: str,
    ) -> dict:
        ...

    @abstractmethod
    def search_artifacts(
        self,
        title: str,
    ) -> dict:
        ...

