#!/usr/bin/env python3
# PreToolUse hook: blocks destructive shell commands before they run (exit 2 = blocked, the reason goes back to the agent)
import json, re, sys
d = json.load(sys.stdin)
cmd = (d.get("tool_input") or {}).get("command", "")
BAD = [r"\brm\s+-[a-zA-Z]*[rf]", r"git\s+push\s+.*--force", r"\bdrop\s+(table|database)\b", r"git\s+reset\s+--hard"]
for p in BAD:
    if re.search(p, cmd, re.I):
        print(f"BLOCKED by guard: '{cmd}' matches {p}. Ask the owner first.", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
