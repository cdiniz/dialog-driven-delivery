from __future__ import annotations

import os
from typing import Any

import httpx
import markdown
import markdownify

from .base import BaseAdapter


def _md_to_storage(md_body: str) -> str:
    return markdown.markdown(md_body, extensions=["tables", "fenced_code"])


def _storage_to_md(html: str) -> str:
    return markdownify.markdownify(html, heading_style="ATX", strip=["style"])


class ConfluenceAdapter(BaseAdapter):

    def __init__(self, config: dict[str, Any]) -> None:
        super().__init__(config)
        self._client: httpx.Client | None = None

    @property
    def base_url(self) -> str:
        return self.config["base_url"].rstrip("/")

    @property
    def space_key(self) -> str:
        return self.config["space_key"]

    @property
    def client(self) -> httpx.Client:
        if self._client is None:
            api_token = os.environ.get("CONFLUENCE_API_TOKEN")
            if not api_token:
                raise ValueError("Environment variable CONFLUENCE_API_TOKEN is not set")

            self._client = httpx.Client(
                base_url=f"{self.base_url}/wiki/api/v2",
                auth=(self.config["email"], api_token),
                headers={"Accept": "application/json"},
            )
        return self._client

    def _get_space_id(self) -> str:
        resp = self.client.get("/spaces", params={"keys": self.space_key})
        resp.raise_for_status()
        results = resp.json().get("results", [])
        if not results:
            raise ValueError(f"Space not found: {self.space_key}")
        return results[0]["id"]

    def _page_url(self, page: dict) -> str:
        base = page.get("_links", {}).get("base", self.base_url)
        webui = page.get("_links", {}).get("webui", "")
        return f"{base}{webui}"

    def create_artifact(
        self,
        title: str,
        body: str,
        location_id: str = ".",
    ) -> dict:
        space_id = self._get_space_id()
        payload: dict[str, Any] = {
            "spaceId": space_id,
            "status": "current",
            "title": title,
            "body": {
                "representation": "storage",
                "value": _md_to_storage(body),
            },
        }
        parent = location_id if location_id and location_id != "." else self.config.get("location_id")
        if parent:
            payload["parentId"] = str(parent)

        resp = self.client.post("/pages", json=payload)
        resp.raise_for_status()
        page = resp.json()

        return {
            "id": page["id"],
            "title": page["title"],
            "url": self._page_url(page),
        }

    def read_artifact(self, artifact_id: str) -> dict:
        resp = self.client.get(
            f"/pages/{artifact_id}",
            params={"body-format": "storage"},
        )
        resp.raise_for_status()
        page = resp.json()

        storage_html = page.get("body", {}).get("storage", {}).get("value", "")

        return {
            "id": page["id"],
            "title": page["title"],
            "body": _storage_to_md(storage_html),
            "url": self._page_url(page),
        }

    def update_artifact(
        self,
        artifact_id: str,
        body: str,
    ) -> dict:
        current = self.client.get(f"/pages/{artifact_id}")
        current.raise_for_status()
        current_page = current.json()

        current_version = current_page.get("version", {}).get("number", 1)

        payload = {
            "id": artifact_id,
            "status": "current",
            "title": current_page["title"],
            "body": {
                "representation": "storage",
                "value": _md_to_storage(body),
            },
            "version": {
                "number": current_version + 1,
            },
        }

        resp = self.client.put(f"/pages/{artifact_id}", json=payload)
        resp.raise_for_status()
        page = resp.json()

        return {
            "id": page["id"],
            "url": self._page_url(page),
        }

    def search_artifacts(
        self,
        title: str,
    ) -> dict:
        space_id = self._get_space_id()
        resp = self.client.get(
            "/pages",
            params={"space-id": space_id, "title": title},
        )
        resp.raise_for_status()
        pages = resp.json().get("results", [])

        return {
            "results": [
                {
                    "id": p["id"],
                    "title": p["title"],
                    "url": self._page_url(p),
                }
                for p in pages
            ],
        }
