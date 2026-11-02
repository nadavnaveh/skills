#!/usr/bin/env python3
# PreToolUse hook: blocks commands you can't undo before they run. Exit 2 = blocked, the reason goes back to the agent.
# It fails closed: input it can't read blocks, because a guard that breaks quietly is worse than no guard. A short list: add your own.
import json, re, sys
BAD = [r"\brm\s+-[a-zA-Z]*[rf]", r"git\s+push\b.*(--force|\s-f\b)", r"git\s+reset\s+--hard", r"\bdrop\s+(table|database)\b"]
try:
    cmd = json.loads(sys.stdin.read())["tool_input"]["command"]
    if not isinstance(cmd, str): raise TypeError("command is not text")
except Exception as ex:
    print(f"BLOCKED by guard: could not read the command ({ex}). Ask the owner first.", file=sys.stderr); sys.exit(2)
for p in BAD:
    if re.search(p, cmd, re.I):
        print(f"BLOCKED by guard: '{cmd}' matches {p}. Ask the owner first.", file=sys.stderr); sys.exit(2)
sys.exit(0)
