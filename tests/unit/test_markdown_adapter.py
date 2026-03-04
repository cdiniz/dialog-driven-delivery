from pathlib import Path

import pytest

from adapters.markdown import MarkdownAdapter


@pytest.fixture
def spec_adapter(tmp_path):
    specs_dir = tmp_path / "specs"
    specs_dir.mkdir()
    return MarkdownAdapter({"directory": str(specs_dir)})


@pytest.fixture
def story_adapter(tmp_path):
    stories_dir = tmp_path / "stories"
    stories_dir.mkdir()
    return MarkdownAdapter({"directory": str(stories_dir), "mode": "story"})


@pytest.fixture
def transcript_adapter(tmp_path):
    transcripts_dir = tmp_path / "transcripts"
    transcripts_dir.mkdir()
    return MarkdownAdapter({"directory": str(transcripts_dir), "mode": "transcript"})


class TestSpecMode:
    def test_create_and_read(self, spec_adapter):
        result = spec_adapter.create_artifact(title="User Authentication", body="# User Authentication\n\nContent here.")
        assert result["title"] == "User Authentication"
        assert "user-authentication" in result["path"]
        assert result["path"].endswith(".md")

        read_result = spec_adapter.read_artifact(result["id"])
        assert read_result["title"] == "User Authentication"
        assert "Content here." in read_result["body"]

    def test_create_with_location(self, spec_adapter):
        result = spec_adapter.create_artifact(title="Auth Spec", body="# Auth\n", location_id="subdir")
        assert "subdir" in result["path"]
        assert Path(result["path"]).exists()

    def test_update(self, spec_adapter):
        create_result = spec_adapter.create_artifact(title="My Spec", body="# My Spec\n\nOriginal.")
        update_result = spec_adapter.update_artifact(
            artifact_id=create_result["id"],
            body="# My Spec\n\nUpdated content.",
        )
        assert update_result["id"] == create_result["id"]

        read_result = spec_adapter.read_artifact(create_result["id"])
        assert "Updated content." in read_result["body"]

    def test_search(self, spec_adapter):
        spec_adapter.create_artifact(title="Auth Feature", body="# Auth Feature\n\nOAuth2 authentication flow.")
        spec_adapter.create_artifact(title="Search Feature", body="# Search Feature\n\nElasticsearch integration.")

        results = spec_adapter.search_artifacts(query="OAuth2")
        assert len(results["results"]) == 1
        assert results["results"][0]["title"] == "Auth Feature"

    def test_search_no_results(self, spec_adapter):
        spec_adapter.create_artifact(title="Spec", body="# Spec\n\nContent.")
        results = spec_adapter.search_artifacts(query="nonexistent")
        assert len(results["results"]) == 0

    def test_list_locations(self, spec_adapter):
        locations = spec_adapter.list_locations()
        assert any(loc["id"] == "." for loc in locations["locations"])

    def test_list_locations_with_subdirs(self, spec_adapter):
        (Path(spec_adapter.directory) / "subdir").mkdir()
        locations = spec_adapter.list_locations()
        ids = [loc["id"] for loc in locations["locations"]]
        assert "." in ids
        assert "subdir" in ids

    def test_read_nonexistent_raises(self, spec_adapter):
        with pytest.raises(FileNotFoundError):
            spec_adapter.read_artifact("nonexistent-spec")

    def test_slug_special_characters(self, spec_adapter):
        result = spec_adapter.create_artifact(title="My Feature! (v2.0)", body="# Content")
        assert "my-feature-v20" in result["path"]


class TestStoryMode:
    def test_create_story(self, story_adapter):
        result = story_adapter.create_artifact(
            title="User Login",
            body="# Story: User Login\n\nAs a user...",
            metadata={"spec_id": "specs/user-authentication.md", "labels": ["backend"]},
        )
        assert result["key"] == "story-1"
        assert result["summary"] == "User Login"
        assert "user-authentication" in result["path"]

        content = Path(result["path"]).read_text()
        assert "type: story" in content
        assert "id: story-1" in content

    def test_sequential_ids(self, story_adapter):
        for i in range(3):
            result = story_adapter.create_artifact(
                title=f"Story {i}",
                body=f"Content {i}",
                metadata={"spec_id": "specs/feature.md"},
            )
        assert result["key"] == "story-3"

    def test_story_with_frontmatter(self, story_adapter):
        result = story_adapter.create_artifact(
            title="My Story",
            body="Body content",
            metadata={"spec_id": "specs/feat.md", "size": "small", "labels": ["frontend", "backend"]},
        )
        read_result = story_adapter.read_artifact(result["path"])
        assert read_result["frontmatter"]["size"] == "small"
        assert read_result["frontmatter"]["type"] == "story"
        assert "frontend" in read_result["frontmatter"]["labels"]

    def test_list_projects(self, story_adapter):
        projects = story_adapter.list_projects()
        assert len(projects["projects"]) == 1
        assert projects["projects"][0]["key"] == "LOCAL"

    def test_get_issue_types(self, story_adapter):
        types = story_adapter.get_issue_types()
        assert any(t["id"] == "story" for t in types["issue_types"])

    def test_link_issues(self, story_adapter):
        story_adapter.create_artifact(
            title="First",
            body="First story",
            metadata={"spec_id": "specs/feat.md"},
        )
        story_adapter.create_artifact(
            title="Second",
            body="Second story",
            metadata={"spec_id": "specs/feat.md"},
        )
        result = story_adapter.link_issues("story-1", "story-2", "blocks")
        assert result["success"] is True

        read_result = story_adapter.read_artifact(
            str(Path(story_adapter.directory) / "feat" / "story-1-first.md")
        )
        assert "story-2" in read_result["frontmatter"]["blocks"]


class TestTranscriptMode:
    def test_create_transcript(self, transcript_adapter):
        result = transcript_adapter.create_artifact(
            title="Sprint Kickoff",
            body="# Meeting Notes\n\nDiscussion content.",
            metadata={
                "meeting_type": "planning",
                "meeting_date": "2026-02-05",
                "participants": ["Alice", "Bob"],
            },
        )
        assert "Sprint Kickoff" in result["title"]
        assert "2026-02" in result["path"]
        assert "planning" in result["path"]

        content = Path(result["path"]).read_text()
        assert "type: transcript" in content
        assert "meeting_type: planning" in content

    def test_transcript_directory_structure(self, transcript_adapter):
        transcript_adapter.create_artifact(
            title="Meeting One",
            body="Content",
            metadata={"meeting_date": "2026-01-15", "meeting_type": "standup"},
        )
        transcript_adapter.create_artifact(
            title="Meeting Two",
            body="Content",
            metadata={"meeting_date": "2026-02-20", "meeting_type": "retro"},
        )

        month_dirs = [d.name for d in Path(transcript_adapter.directory).iterdir() if d.is_dir()]
        assert "2026-01" in month_dirs
        assert "2026-02" in month_dirs

    def test_transcript_filename_format(self, transcript_adapter):
        result = transcript_adapter.create_artifact(
            title="Database Migration",
            body="Content",
            metadata={"meeting_date": "2026-03-10", "meeting_type": "technical"},
        )
        filename = Path(result["path"]).name
        assert filename == "2026-03-10-technical-database-migration.md"

    def test_read_transcript(self, transcript_adapter):
        create_result = transcript_adapter.create_artifact(
            title="Planning",
            body="Notes here.",
            metadata={"meeting_date": "2026-01-01", "meeting_type": "planning", "participants": ["Eve"]},
        )
        read_result = transcript_adapter.read_artifact(create_result["path"])
        assert read_result["frontmatter"]["meeting_type"] == "planning"
        assert "Notes here." in read_result["body"]

    def test_search_transcripts(self, transcript_adapter):
        transcript_adapter.create_artifact(
            title="Auth Discussion",
            body="We discussed OAuth2 implementation.",
            metadata={"meeting_date": "2026-01-10", "meeting_type": "technical"},
        )
        results = transcript_adapter.search_artifacts(query="OAuth2")
        assert len(results["results"]) == 1

    def test_list_locations_with_month_dirs(self, transcript_adapter):
        transcript_adapter.create_artifact(
            title="Meeting",
            body="Content",
            metadata={"meeting_date": "2026-03-01", "meeting_type": "standup"},
        )
        locations = transcript_adapter.list_locations()
        ids = [loc["id"] for loc in locations["locations"]]
        assert "2026-03" in ids
