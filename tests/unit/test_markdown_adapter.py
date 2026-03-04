from pathlib import Path

import pytest

from adapters.markdown import MarkdownAdapter


@pytest.fixture
def adapter(tmp_path):
    specs_dir = tmp_path / "specs"
    specs_dir.mkdir()
    return MarkdownAdapter({"directory": str(specs_dir)})


class TestCreateArtifact:
    def test_creates_file_and_returns_metadata(self, adapter):
        result = adapter.create_artifact(title="User Authentication", body="# User Authentication\n\nContent here.")
        assert result["title"] == "User Authentication"
        assert "user-authentication.md" in result["id"]
        assert Path(result["id"]).exists()

    def test_creates_in_subdirectory(self, adapter):
        result = adapter.create_artifact(title="Auth Spec", body="# Auth\n", location_id="subdir")
        assert "subdir" in result["id"]
        assert Path(result["id"]).exists()

    def test_slugifies_special_characters(self, adapter):
        result = adapter.create_artifact(title="My Feature! (v2.0)", body="# Content")
        assert "my-feature-v20" in result["id"]


class TestReadArtifact:
    def test_reads_created_artifact(self, adapter):
        created = adapter.create_artifact(title="User Authentication", body="# User Authentication\n\nContent here.")
        result = adapter.read_artifact(created["id"])
        assert result["title"] == "user-authentication"
        assert "Content here." in result["body"]

    def test_nonexistent_raises(self, adapter):
        with pytest.raises(FileNotFoundError):
            adapter.read_artifact("nonexistent-spec")


class TestUpdateArtifact:
    def test_updates_body(self, adapter):
        created = adapter.create_artifact(title="My Spec", body="# My Spec\n\nOriginal.")
        updated = adapter.update_artifact(artifact_id=created["id"], body="# My Spec\n\nUpdated content.")
        assert updated["id"] == created["id"]

        result = adapter.read_artifact(created["id"])
        assert "Updated content." in result["body"]


class TestSearchArtifacts:
    def test_finds_by_title(self, adapter):
        adapter.create_artifact(title="Auth Feature", body="# Auth Feature\n\nOAuth2 authentication flow.")
        adapter.create_artifact(title="Search Feature", body="# Search Feature\n\nElasticsearch integration.")

        results = adapter.search_artifacts(title="Auth")
        assert len(results["results"]) == 1
        assert results["results"][0]["title"] == "auth-feature"

    def test_no_results(self, adapter):
        adapter.create_artifact(title="Spec", body="# Spec\n\nContent.")
        results = adapter.search_artifacts(title="nonexistent")
        assert len(results["results"]) == 0

    def test_empty_directory(self, tmp_path):
        empty = tmp_path / "empty"
        adapter = MarkdownAdapter({"directory": str(empty)})
        results = adapter.search_artifacts(title="anything")
        assert results["results"] == []


class TestDirectoryResolution:
    def test_missing_directory_config_raises(self):
        adapter = MarkdownAdapter({})
        with pytest.raises(ValueError, match="directory"):
            _ = adapter.directory

    def test_absolute_directory_used_as_is(self, tmp_path):
        adapter = MarkdownAdapter({"directory": str(tmp_path / "abs")})
        assert adapter.directory == tmp_path / "abs"
