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
        parent_id: str | None = None,
        metadata: dict | None = None,
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
        version_message: str | None = None,
    ) -> dict:
        ...

    @abstractmethod
    def search_artifacts(
        self,
        query: str,
        location_id: str | None = None,
    ) -> dict:
        ...

    @abstractmethod
    def list_locations(self) -> dict:
        ...

    def list_projects(self) -> dict:
        raise NotImplementedError("list_projects not supported by this adapter")

    def get_issue_types(self, project_key: str | None = None) -> dict:
        raise NotImplementedError("get_issue_types not supported by this adapter")

    def link_issues(
        self,
        from_key: str,
        to_key: str,
        link_type: str,
    ) -> dict:
        raise NotImplementedError("link_issues not supported by this adapter")
