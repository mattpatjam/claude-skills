#!/bin/bash
f=$(jq -r '.tool_input.file_path // ""')
if echo "$f" | grep -q 'Projects/olc-method' && ! echo "$f" | grep -qE '(tracker|skills-to-build)\.md$'; then
  jq -n --arg f "$f" '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"OLC file modified: \($f) — check if tracker.md (file index, session log, blockers, follow-ups) or skills-to-build.md need updating."}}'
fi
