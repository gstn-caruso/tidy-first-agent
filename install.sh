#!/usr/bin/env sh
# Instala (o actualiza) el agente tidier en ~/.claude/agents/.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
SRC="$HERE/agents/tidier.md"
DST="${CLAUDE_HOME:-$HOME/.claude}/agents/tidier.md"

mkdir -p "$(dirname "$DST")"
if [ -f "$DST" ] && cmp -s "$SRC" "$DST"; then
  echo "tidier ya está al día en $DST"
  exit 0
fi
cp "$SRC" "$DST"
echo "tidier instalado en $DST"
echo "Si ya tenés una sesión de Claude Code abierta, reiniciala para que el agente aparezca."
