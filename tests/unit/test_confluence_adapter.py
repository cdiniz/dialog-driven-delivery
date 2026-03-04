from unittest.mock import MagicMock, patch

import httpx
import pytest

from adapters.confluence import ConfluenceAdapter, _md_to_storage, _storage_to_md


SAMPLE_CONFIG = {
    "base_url": "https://test.atlassian.net",
    "email": "user@example.com",
    "space_key": "PROJ",
}

SPACE_RESPONSE = {
    "results": [{"id": "space-123", "key": "PROJ", "name": "Project"}],
}

PAGE_RESPONSE = {
    "id": "page-1",
    "title": "My Page",
    "version": {"number": 3},
    "_links": {
        "base": "https://test.atlassian.net/wiki",
        "webui": "/spaces/PROJ/pages/page-1/My+Page",
    },
    "body": {
        "storage": {
            "value": "<h1>Hello</h1><p>World</p>",
        },
    },
}


@pytest.fixture
def adapter():
    with patch.dict("os.environ", {"CONFLUENCE_API_TOKEN": "fake-token"}):
        return ConfluenceAdapter(SAMPLE_CONFIG)


@pytest.fixture
def mock_client(adapter):
    client = MagicMock(spec=httpx.Client)
    adapter._client = client
    return client


def _json_response(data, status_code=200):
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.json.return_value = data
    resp.raise_for_status = MagicMock()
    return resp


class TestFormatConversion:
    def test_md_to_storage_converts_heading(self):
        result = _md_to_storage("# Hello")
        assert "<h1>Hello</h1>" in result

    def test_md_to_storage_converts_paragraph(self):
        result = _md_to_storage("Some text")
        assert "<p>Some text</p>" in result

    def test_md_to_storage_converts_table(self):
        md = "| A | B |\n|---|---|\n| 1 | 2 |"
        result = _md_to_storage(md)
        assert "<table>" in result

    def test_md_to_storage_converts_fenced_code(self):
        md = "```python\nprint('hi')\n```"
        result = _md_to_storage(md)
        assert "<pre>" in result
        assert "print" in result

    def test_storage_to_md_converts_heading(self):
        result = _storage_to_md("<h1>Hello</h1>")
        assert "# Hello" in result

    def test_storage_to_md_converts_paragraph(self):
        result = _storage_to_md("<p>Some text</p>")
        assert "Some text" in result


class TestCreateArtifact:
    def test_creates_page(self, adapter, mock_client):
        mock_client.get.return_value = _json_response(SPACE_RESPONSE)
        mock_client.post.return_value = _json_response(PAGE_RESPONSE)

        result = adapter.create_artifact(title="My Page", body="# Hello\n\nWorld")

        assert result["id"] == "page-1"
        assert result["title"] == "My Page"
        assert "test.atlassian.net" in result["url"]

        call_kwargs = mock_client.post.call_args
        payload = call_kwargs.kwargs.get("json") or call_kwargs[1]["json"]
        assert payload["spaceId"] == "space-123"
        assert payload["body"]["representation"] == "storage"
        assert "<h1>Hello</h1>" in payload["body"]["value"]

    def test_creates_page_with_parent(self, adapter, mock_client):
        mock_client.get.return_value = _json_response(SPACE_RESPONSE)
        mock_client.post.return_value = _json_response(PAGE_RESPONSE)

        adapter.create_artifact(title="Child", body="Content", location_id="parent-42")

        call_kwargs = mock_client.post.call_args
        payload = call_kwargs.kwargs.get("json") or call_kwargs[1]["json"]
        assert payload["parentId"] == "parent-42"

    def test_creates_page_without_parent_when_dot(self, adapter, mock_client):
        mock_client.get.return_value = _json_response(SPACE_RESPONSE)
        mock_client.post.return_value = _json_response(PAGE_RESPONSE)

        adapter.create_artifact(title="Root", body="Content", location_id=".")

        call_kwargs = mock_client.post.call_args
        payload = call_kwargs.kwargs.get("json") or call_kwargs[1]["json"]
        assert "parentId" not in payload


class TestReadArtifact:
    def test_reads_page(self, adapter, mock_client):
        mock_client.get.return_value = _json_response(PAGE_RESPONSE)

        result = adapter.read_artifact("page-1")

        assert result["id"] == "page-1"
        assert result["title"] == "My Page"
        assert "Hello" in result["body"]
        assert "test.atlassian.net" in result["url"]

        mock_client.get.assert_called_once_with(
            "/pages/page-1",
            params={"body-format": "storage"},
        )

    def test_reads_page_converts_storage_to_markdown(self, adapter, mock_client):
        mock_client.get.return_value = _json_response(PAGE_RESPONSE)

        result = adapter.read_artifact("page-1")

        assert "# Hello" in result["body"]
        assert "World" in result["body"]


class TestUpdateArtifact:
    def test_updates_page_with_incremented_version(self, adapter, mock_client):
        mock_client.get.return_value = _json_response(PAGE_RESPONSE)
        mock_client.put.return_value = _json_response(PAGE_RESPONSE)

        result = adapter.update_artifact("page-1", body="# Updated")

        assert result["id"] == "page-1"
        assert "test.atlassian.net" in result["url"]

        call_kwargs = mock_client.put.call_args
        payload = call_kwargs.kwargs.get("json") or call_kwargs[1]["json"]
        assert payload["version"]["number"] == 4
        assert "<h1>Updated</h1>" in payload["body"]["value"]

    def test_preserves_title_on_update(self, adapter, mock_client):
        mock_client.get.return_value = _json_response(PAGE_RESPONSE)
        mock_client.put.return_value = _json_response(PAGE_RESPONSE)

        adapter.update_artifact("page-1", body="New content")

        call_kwargs = mock_client.put.call_args
        payload = call_kwargs.kwargs.get("json") or call_kwargs[1]["json"]
        assert payload["title"] == "My Page"


class TestSearchArtifacts:
    def test_searches_by_title(self, adapter, mock_client):
        search_response = {
            "results": [
                {
                    "id": "page-1",
                    "title": "Auth Spec",
                    "_links": {
                        "base": "https://test.atlassian.net/wiki",
                        "webui": "/spaces/PROJ/pages/page-1",
                    },
                },
                {
                    "id": "page-2",
                    "title": "Auth Design",
                    "_links": {
                        "base": "https://test.atlassian.net/wiki",
                        "webui": "/spaces/PROJ/pages/page-2",
                    },
                },
            ],
        }
        mock_client.get.side_effect = [
            _json_response(SPACE_RESPONSE),
            _json_response(search_response),
        ]

        result = adapter.search_artifacts("Auth")

        assert len(result["results"]) == 2
        assert result["results"][0]["id"] == "page-1"
        assert result["results"][1]["title"] == "Auth Design"

    def test_search_no_results(self, adapter, mock_client):
        mock_client.get.side_effect = [
            _json_response(SPACE_RESPONSE),
            _json_response({"results": []}),
        ]

        result = adapter.search_artifacts("Nonexistent")

        assert result["results"] == []


class TestConfiguration:
    def test_missing_token_env_raises(self):
        with patch.dict("os.environ", {}, clear=True):
            adapter = ConfluenceAdapter(SAMPLE_CONFIG)
            with pytest.raises(ValueError, match="CONFLUENCE_API_TOKEN"):
                _ = adapter.client

    def test_space_not_found_raises(self, adapter, mock_client):
        mock_client.get.return_value = _json_response({"results": []})

        with pytest.raises(ValueError, match="Space not found"):
            adapter.create_artifact(title="Test", body="Content")
