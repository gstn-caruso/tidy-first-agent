#!/usr/bin/env sh
# Installs (or updates) the tidier agent, its skill and the book references.
#
#   ~/.claude/agents/tidier.md
#   ~/.claude/skills/tidier/SKILL.md
#   ~/.claude/skills/tidier/references/     <- one copy, read by both
#
# Everything this project installs lives under the name "tidier", so it cannot
# collide with anything else in ~/.claude. The agent reaches the references by
# absolute path and the skill by relative path, so they have to be one copy.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
CLAUDE="${CLAUDE_HOME:-$HOME/.claude}"
SKILL_DST="$CLAUDE/skills/tidier"

mkdir -p "$CLAUDE/agents" "$SKILL_DST"
cp "$HERE/agents/tidier.md" "$CLAUDE/agents/tidier.md"
cp "$HERE/skills/tidier/SKILL.md" "$SKILL_DST/SKILL.md"

rm -rf "$SKILL_DST/references"
cp -R "$HERE/references" "$SKILL_DST/references"

echo "agent       -> $CLAUDE/agents/tidier.md"
echo "skill       -> $SKILL_DST/SKILL.md"
echo "references  -> $SKILL_DST/references ($(ls "$SKILL_DST/references" | wc -l | tr -d ' ') files)"
echo "In an open session both show up from the next message on; otherwise restart the session."
