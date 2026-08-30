#!/usr/bin/env sh
# Installs (or updates) the tidier agent in ~/.claude/agents/.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
SRC="$HERE/agents/tidier.md"
DST="${CLAUDE_HOME:-$HOME/.claude}/agents/tidier.md"

mkdir -p "$(dirname "$DST")"
if [ -f "$DST" ] && cmp -s "$SRC" "$DST"; then
  echo "tidier is already up to date at $DST"
  exit 0
fi
cp "$SRC" "$DST"
echo "tidier installed at $DST"
echo "In an open session it shows up from the next message on; otherwise restart the session."
