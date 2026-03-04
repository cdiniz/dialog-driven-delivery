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
        assert cfg.templates == {}
        assert cfg.settings == {}

    def test_empty_file_returns_defaults(self, tmp_path):
        config_file = _write_yaml(tmp_path, "")
        cfg = load_config(config_file)
        assert cfg == D3Config()

    def test_full_config(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  product_spec:
    adapter: markdown
    config:
      directory: ./specs
  user_story:
    adapter: markdown
    config:
      directory: ./stories
      mode: story

templates:
  product_spec: ./templates/custom-product-spec.md

settings:
  quiet_mode: false
""")
        cfg = load_config(config_file)
        assert "product_spec" in cfg.artifacts
        assert "user_story" in cfg.artifacts
        assert cfg.artifacts["product_spec"].adapter == "markdown"
        assert cfg.artifacts["product_spec"].config["directory"] == "./specs"
        assert cfg.artifacts["user_story"].config["mode"] == "story"
        assert cfg.templates["product_spec"] == "./templates/custom-product-spec.md"
        assert cfg.settings["quiet_mode"] is False

    def test_adapter_defaults_to_markdown(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  my_type:
    config:
      directory: ./things
""")
        cfg = load_config(config_file)
        assert cfg.artifacts["my_type"].adapter == "markdown"

    def test_config_defaults_to_empty_dict(self, tmp_path):
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
    config:
      directory: ./specs

templates:
  Product Spec: ./templates/ps.md
""")
        cfg = load_config(config_file)
        assert "product_spec" in cfg.artifacts
        assert "product_spec" in cfg.templates

    def test_missing_settings_defaults_empty(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  spec:
    adapter: markdown
""")
        cfg = load_config(config_file)
        assert cfg.settings == {}

    def test_missing_templates_defaults_empty(self, tmp_path):
        config_file = _write_yaml(tmp_path, """\
artifacts:
  spec:
    adapter: markdown
""")
        cfg = load_config(config_file)
        assert cfg.templates == {}
