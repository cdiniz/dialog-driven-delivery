#!/usr/bin/env bash
set -euo pipefail

REPO="cdiniz/dialog-driven-delivery"
BRANCH="cross-platform-support"
BASE_URL="https://raw.githubusercontent.com/${REPO}/${BRANCH}/dist"

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

case "$platform" in
  codex)
    echo "Installing D3 for OpenAI Codex..."

    files=(
      ".agents/skills/d3-create-spec/SKILL.md"
      ".agents/skills/d3-refine-spec/SKILL.md"
      ".agents/skills/d3-decompose/SKILL.md"
      ".agents/skills/d3-capture-transcript/SKILL.md"
      ".agents/skills/d3-create-adr/SKILL.md"
      ".agents/skills/d3-templates/SKILL.md"
      ".agents/skills/d3-templates/references/feature-product-spec.md"
      ".agents/skills/d3-templates/references/feature-tech-spec.md"
      ".agents/skills/d3-templates/references/user-story.md"
      ".agents/skills/d3-templates/references/adr.md"
      ".agents/skills/d3-templates/references/meeting-transcript.md"
      ".agents/skills/uncertainty-markers/SKILL.md"
      ".agents/skills/markdown-spec-provider/SKILL.md"
      ".agents/skills/markdown-story-provider/SKILL.md"
      ".agents/skills/markdown-transcript-provider/SKILL.md"
    )

    for file in "${files[@]}"; do
      dir=$(dirname "$file")
      mkdir -p "$dir"
      curl -sSL "${BASE_URL}/codex/${file}" -o "$file"
    done

    if [ ! -f "AGENTS.md" ]; then
      curl -sSL "${BASE_URL}/codex/AGENTS.md" -o "AGENTS.md"
      echo "Created AGENTS.md with D3 configuration."
    else
      echo "AGENTS.md already exists. Add D3 configuration manually:"
      echo "  See: ${BASE_URL}/codex/AGENTS.md"
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

    files=(
      ".github/skills/d3-create-spec/SKILL.md"
      ".github/skills/d3-refine-spec/SKILL.md"
      ".github/skills/d3-decompose/SKILL.md"
      ".github/skills/d3-capture-transcript/SKILL.md"
      ".github/skills/d3-create-adr/SKILL.md"
      ".github/skills/d3-templates/SKILL.md"
      ".github/skills/d3-templates/references/feature-product-spec.md"
      ".github/skills/d3-templates/references/feature-tech-spec.md"
      ".github/skills/d3-templates/references/user-story.md"
      ".github/skills/d3-templates/references/adr.md"
      ".github/skills/d3-templates/references/meeting-transcript.md"
      ".github/skills/uncertainty-markers/SKILL.md"
      ".github/skills/markdown-spec-provider/SKILL.md"
      ".github/skills/markdown-story-provider/SKILL.md"
      ".github/skills/markdown-transcript-provider/SKILL.md"
    )

    for file in "${files[@]}"; do
      dir=$(dirname "$file")
      mkdir -p "$dir"
      curl -sSL "${BASE_URL}/copilot/${file}" -o "$file"
    done

    if [ ! -f ".github/copilot-instructions.md" ]; then
      curl -sSL "${BASE_URL}/copilot/.github/copilot-instructions.md" -o ".github/copilot-instructions.md"
      echo "Created .github/copilot-instructions.md with D3 configuration."
    else
      echo ".github/copilot-instructions.md already exists. Add D3 configuration manually:"
      echo "  See: ${BASE_URL}/copilot/.github/copilot-instructions.md"
    fi

    echo ""
    echo "D3 installed for GitHub Copilot."
    echo ""
    echo "Next steps:"
    echo "  1. Review .github/copilot-instructions.md and adjust D3 provider configuration"
    echo "  2. Start using D3: /d3-create-spec in Copilot chat"
    ;;

  cursor)
    echo "Installing D3 for Cursor..."

    files=(
      ".cursor/rules/d3-create-spec/RULE.md"
      ".cursor/rules/d3-refine-spec/RULE.md"
      ".cursor/rules/d3-decompose/RULE.md"
      ".cursor/rules/d3-capture-transcript/RULE.md"
      ".cursor/rules/d3-create-adr/RULE.md"
      ".cursor/rules/d3-templates/RULE.md"
      ".cursor/rules/d3-templates/references/feature-product-spec.md"
      ".cursor/rules/d3-templates/references/feature-tech-spec.md"
      ".cursor/rules/d3-templates/references/user-story.md"
      ".cursor/rules/d3-templates/references/adr.md"
      ".cursor/rules/d3-templates/references/meeting-transcript.md"
      ".cursor/rules/uncertainty-markers/RULE.md"
      ".cursor/rules/markdown-spec-provider/RULE.md"
      ".cursor/rules/markdown-story-provider/RULE.md"
      ".cursor/rules/markdown-transcript-provider/RULE.md"
      ".cursor/rules/d3-config/RULE.md"
    )

    for file in "${files[@]}"; do
      dir=$(dirname "$file")
      mkdir -p "$dir"
      curl -sSL "${BASE_URL}/cursor/${file}" -o "$file"
    done

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
