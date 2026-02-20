#!/usr/bin/env bash
set -euo pipefail

REPO="cdiniz/dialog-driven-delivery"
BRANCH="${D3_BRANCH:-main}"
REPO_NAME="dialog-driven-delivery"
ARCHIVE_PREFIX="${REPO_NAME}-${BRANCH}"

usage() {
  echo "Usage: $0 <platform>"
  echo ""
  echo "Platforms:"
  echo "  codex    - Install D3 for OpenAI Codex (.agents/skills/)"
  echo "  copilot  - Install D3 for GitHub Copilot (.github/prompts/ + .github/agents/)"
  echo "  cursor   - Install D3 for Cursor (.cursor/rules/)"
  echo ""
  echo "Example:"
  echo "  curl -sSL https://raw.githubusercontent.com/${REPO}/${BRANCH}/install.sh | bash -s -- copilot"
  exit 1
}

platform="${1:-}"
if [ -z "$platform" ]; then
  usage
fi

tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT

echo "Downloading D3..."
curl -sL "https://github.com/${REPO}/archive/${BRANCH}.tar.gz" \
  | tar xz -C "$tmpdir" --strip-components=3 "${ARCHIVE_PREFIX}/dist/${platform}/"

if [ ! -f "d3.config.md" ]; then
  cp "$tmpdir/d3.config.md" .
  echo "Created d3.config.md with default D3 configuration."
else
  echo "d3.config.md already exists, skipping."
fi

case "$platform" in
  codex)
    echo "Installing D3 for OpenAI Codex..."
    cp -r "$tmpdir/.agents" .
    echo ""
    echo "D3 installed for Codex."
    echo ""
    echo "Next steps:"
    echo "  1. Review d3.config.md and adjust provider configuration"
    echo "  2. Start using D3: \$d3-create-spec"
    ;;

  copilot)
    echo "Installing D3 for GitHub Copilot..."
    mkdir -p .github
    cp -r "$tmpdir/.github/prompts" .github/
    cp -r "$tmpdir/.github/agents" .github/
    cp -r "$tmpdir/.github/instructions" .github/
    cp -r "$tmpdir/.github/d3-templates" .github/
    echo ""
    echo "D3 installed for GitHub Copilot."
    echo ""
    echo "Next steps:"
    echo "  1. Review d3.config.md and adjust provider configuration"
    echo "  2. Start using D3: /d3-create-spec in Copilot chat"
    ;;

  cursor)
    echo "Installing D3 for Cursor..."
    cp -r "$tmpdir/.cursor" .
    echo ""
    echo "D3 installed for Cursor."
    echo ""
    echo "Next steps:"
    echo "  1. Review d3.config.md and adjust provider configuration"
    echo "  2. Start using D3: @d3-create-spec in Cursor agent mode"
    ;;

  *)
    echo "Error: Unknown platform '${platform}'"
    echo ""
    usage
    ;;
esac
