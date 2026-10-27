---
name: draft-only-mail
description: Sets email access to draft-only. The agent reads mail and writes drafts, every send tool or route is denied in Claude Code's permission settings, and the block is tested. Fixes "the agent sent an email in my name without asking." Use when you connect email to an agent, before it works in your inbox, when send, reply or forward shows in its tool list, or when it offers another way to send. Also on /draft-only-mail.
---

# Draft-only mail

The agent sent an email in your name, and nobody checked it first. One setting decided that: it could send, not only draft. This skill keeps read and draft, denies every send path and tests the block.

## The principles
1. Read and draft, yes. Send, no. The person presses send.
2. Reply and forward send too, so deny them with send.
3. Block every send path. With one tool gone, an agent may offer another route.
4. A block you did not test is not a block.

## Steps
1. List the agent's email tools. scripts/gmail-tools-2026-10-27.txt shows five from one Claude Code session: create_draft, update_draft, send_message, reply and forward. If your connector is not Gmail, use the names from your own tool list.
2. Sort each tool into keep (read, search, create or update a draft) or deny (anything that sends, even a saved draft). If a name is unclear, deny it and ask.
3. Look for other send paths: a second email connector, or mail sent through the terminal. Deny each extra tool. The terminal route stays open until the person picks a rule for it, so ask.
4. Show the list and ask "Deny these?" Change no setting before a yes.
5. Add the exact names under "deny" in .claude/settings.json (this project) or ~/.claude/settings.json (every project), leaving the draft tools out:
   `"permissions": { "deny": ["mcp__claude_ai_Gmail__send_message", "mcp__claude_ai_Gmail__reply", "mcp__claude_ai_Gmail__forward"] }`
   Start a fresh session, then run /permissions to check the deny lines loaded.
6. Test in an interactive session with the connector loaded: ask the agent to list its email tools. Pass means send, reply and forward are absent. A headless run may not load the connector, so it counts as not run. Try a real send only after the person's explicit yes, to their own address, body marked "test, do not act". If it offers another route, deny that and retest.
7. Report each tool as kept or denied, the terminal route as blocked or open, and the test as pass, fail or not run, quoting the agent.

## Rules
- Never send mail in the person's name without their explicit yes.
- If you find a send route that is not denied, stop and ask. Never take it.
- A denied tool stays denied until the person removes the line.
- The proof does not show a real Gmail send blocked (scripts/deny-run-2026-10-27.txt used WebFetch as a stand-in), or the rule in scripts/gmail-tools-2026-10-27.txt applied to anyone's settings. Only step 6 proves your setup.
