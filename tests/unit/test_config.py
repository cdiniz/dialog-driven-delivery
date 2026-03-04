from pathlib import Path

from d3_config import D3Config, load_config


def _write_yaml(tmp_path: Path, content: str) -> Path:
    config_file = tmp_path / "d3.config.yaml"
    config_file.write_text(content)
    return config_file


class TestLoadConfig:
    def test_missing_file_returns_defaults(self, tmp_path):
        cfg = load_config(tmp_path / "nonexistent.yaml")
        assert cfg == D3Config()
        assert cfg.artifacts == {}
        assert cfg.adapters == {}
        assert cfg.settings == {}

    def test_empty_file_returns_defaults(self, tmp_path):
        config_file = _write_yaml(tmp_path, "")
        cfg = load_config(config_file)
        assert cfg == D3Config()

    def test_flat_artifact_fields(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  product_spec:
    adapter: markdown
    directory: ./specs
  user_story:
    adapter: markdown
    directory: ./stories
    mode: story

settings:
  quiet_mode: false
""")
        cfg = load_config(config_file)
        assert "product_spec" in cfg.artifacts
        assert "user_story" in cfg.artifacts
        assert cfg.artifacts["product_spec"].adapter == "markdown"
        assert cfg.artifacts["product_spec"].config["directory"] == "./specs"
        assert cfg.artifacts["user_story"].config["mode"] == "story"
        assert cfg.settings["quiet_mode"] is False

    def test_adapter_defaults_to_markdown(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  my_type:
    directory: ./things
""")
        cfg = load_config(config_file)
        assert cfg.artifacts["my_type"].adapter == "markdown"

    def test_empty_artifact_has_empty_config(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  my_type:
    adapter: markdown
""")
        cfg = load_config(config_file)
        assert cfg.artifacts["my_type"].config == {}

    def test_key_normalisation(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  Product Spec:
    adapter: markdown
    directory: ./specs
""")
        cfg = load_config(config_file)
        assert "product_spec" in cfg.artifacts

    def test_missing_settings_defaults_empty(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  spec:
    adapter: markdown
""")
        cfg = load_config(config_file)
        assert cfg.settings == {}

    def test_template_on_artifact(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  product_spec:
    adapter: markdown
    directory: ./specs
    template: ./templates/custom-product-spec.md
""")
        cfg = load_config(config_file)
        assert cfg.artifacts["product_spec"].template == "./templates/custom-product-spec.md"
        assert "template" not in cfg.artifacts["product_spec"].config

    def test_template_defaults_to_none(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  spec:
    adapter: markdown
    directory: ./specs
""")
        cfg = load_config(config_file)
        assert cfg.artifacts["spec"].template is None


class TestAdapterMerging:
    def test_shared_adapter_config_merges_into_artifact(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
adapters:
  confluence:
    base_url: https://example.atlassian.net
    email: user@example.com
    api_token_env: CONFLUENCE_API_TOKEN
    space_key: PROJ

artifacts:
  product_spec:
    adapter: confluence
    location_id: "12345"
""")
        cfg = load_config(config_file)
        art = cfg.artifacts["product_spec"]
        assert art.config["base_url"] == "https://example.atlassian.net"
        assert art.config["email"] == "user@example.com"
        assert art.config["space_key"] == "PROJ"
        assert art.config["location_id"] == "12345"

    def test_artifact_fields_override_shared(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
adapters:
  confluence:
    base_url: https://shared.atlassian.net
    space_key: SHARED

artifacts:
  product_spec:
    adapter: confluence
    space_key: OVERRIDE
""")
        cfg = load_config(config_file)
        assert cfg.artifacts["product_spec"].config["space_key"] == "OVERRIDE"
        assert cfg.artifacts["product_spec"].config["base_url"] == "https://shared.atlassian.net"

    def test_no_shared_adapter_config(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  transcript:
    adapter: markdown
    directory: ./transcripts
""")
        cfg = load_config(config_file)
        assert cfg.artifacts["transcript"].config["directory"] == "./transcripts"

    def test_adapters_section_stored_on_config(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
adapters:
  confluence:
    base_url: https://example.atlassian.net

artifacts:
  spec:
    adapter: markdown
    directory: ./specs
""")
        cfg = load_config(config_file)
        assert cfg.adapters["confluence"]["base_url"] == "https://example.atlassian.net"

    def test_reserved_keys_excluded_from_config(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  spec:
    adapter: confluence
    template: ./t.md
    location_id: "999"
""")
        cfg = load_config(config_file)
        assert "adapter" not in cfg.artifacts["spec"].config
        assert "template" not in cfg.artifacts["spec"].config
        assert cfg.artifacts["spec"].config["location_id"] == "999"
