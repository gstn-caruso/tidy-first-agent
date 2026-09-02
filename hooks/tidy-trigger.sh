#!/usr/bin/env sh
# UserPromptSubmit hook: when the prompt asks for a Tidy First pass, remind the
# main session to delegate to the tidier agent. Prints nothing otherwise.
set -eu
prompt=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("prompt",""))' 2>/dev/null || cat)
if printf '%s' "$prompt" | grep -qiE 'tidy[ -]?(first|after|this|it|up)|tidyings?|which tidyings|limpi[aá] .*antes|orden[aá] .*antes|tidy antes|separate structure from behavior|structural (from|vs\.?) behavior'; then
  cat <<'MSG'
[tidy-first plugin] This is a Tidy First request: delegate the whole job to the `tidy-first:tidier` agent (Agent tool) with the target, the behavior change that comes next (or the one that just landed), and the test command. Do not tidy inline yourself; do not read the target first — the agent does that. Only if the user asks for a plan without changes, answer from the `tidy-first` skill instead.
MSG
fi
exit 0
