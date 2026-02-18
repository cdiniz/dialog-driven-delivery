#!/usr/bin/env bash
set -euo pipefail

REPO="cdiniz/dialog-driven-delivery"
BRANCH="cross-platform-support"
REPO_NAME="dialog-driven-delivery"
ARCHIVE_PREFIX="${REPO_NAME}-${BRANCH}"

usage() {
  echo "Usage: $0 <platform>"
  echo ""
  echo "Platforms:"
  echo "  codex    - Install D3 for OpenAI Codex (.agents/skills/ + AGENTS.md)"
  echo "  copilot  - Install D3 for GitHub Copilot (.github/agents/ + copilot-instructions.md)"
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

case "$platform" in
  codex)
    echo "Installing D3 for OpenAI Codex..."

    cp -r "$tmpdir/.agents" .

    if [ ! -f "AGENTS.md" ]; then
      cp "$tmpdir/AGENTS.md" .
      echo "Created AGENTS.md with D3 configuration."
    else
      echo "AGENTS.md already exists. Add D3 configuration manually."
    fi

    echo ""
    echo "D3 installed for Codex."
    echo ""
    echo "Next steps:"
    echo "  1. Review AGENTS.md and adjust D3 provider configuration"
    echo "  2. Start using D3: \$d3-create-spec"
    ;;

  copilot)
    echo "Installing D3 for GitHub Copilot..."

    existing_config=""
    if [ -f ".github/copilot-instructions.md" ]; then
      existing_config=$(cat ".github/copilot-instructions.md")
    fi

    cp -r "$tmpdir/.github" .

    if [ -n "$existing_config" ]; then
      echo "$existing_config" > ".github/copilot-instructions.md"
      echo ".github/copilot-instructions.md already exists. Add D3 configuration manually."
    else
      echo "Created .github/copilot-instructions.md with D3 configuration."
    fi

    echo ""
    echo "D3 installed for GitHub Copilot."
    echo ""
    echo "Next steps:"
    echo "  1. Review .github/copilot-instructions.md and adjust D3 provider configuration"
    echo "  2. Start using D3: @d3-create-spec in Copilot agent mode"
    ;;

  cursor)
    echo "Installing D3 for Cursor..."

    cp -r "$tmpdir/.cursor" .

    echo ""
    echo "D3 installed for Cursor."
    echo ""
    echo "Next steps:"
    echo "  1. Review .cursor/rules/d3-config/RULE.md and adjust D3 provider configuration"
    echo "  2. Start using D3: @d3-create-spec in Cursor agent mode"
    ;;

  *)
    echo "Error: Unknown platform '${platform}'"
    echo ""
    usage
    ;;
esac
