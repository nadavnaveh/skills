---
name: mcp-parts
description: Connects an agent to your tools through MCP in five parts (the server, the call, the result, permissions and many agents). Fixes "I connected my tools to the agent, and I don't know what it can reach or what it did with them." Use when you add an MCP server, when the agent used a tool you did not expect, before an agent can reach anything that can delete, and when several agents need the same tools. Also on /mcp-parts.
---

# MCP parts

You connected your tools, and you don't know what the agent can reach or what it did with them. A server hands over its whole list of tools at once, and nobody chose which ones the agent may use. This skill lists the tools, shows each call and its answer, sets what is allowed and shares one server across your agents.

## The principles
1. A server is a list of tools. Know the list before the agent uses it.
2. Show every call and its input before it is sent.
3. A result is evidence. Work from what came back, not from memory.
4. You choose what it may use: allow, ask or deny, one tool at a time.
5. One server, set up once, serves every agent that needs it.

## Steps
1. **The server.** Run `/mcp` to see which servers are connected. List each tool in one line (a GitHub server has search_code, list_prs and create_issue) and mark it read, change or delete.
2. **The call.** Before a tool runs, name the tool and the exact input: search_code with the query "login". If it picked a tool that changes something when a read would do, use the read.
3. **The result.** Say what came back: "three matches, auth.ts line 88 among them." Use it for the next step and name it next to the change it led to. If the call failed or came back empty, say so.
4. **Permissions.** Write rules under permissions in settings.json, one tool per line, named mcp__<server>__<tool>:
   - allow: read only, like mcp__github__search_code.
   - ask: changes something, like mcp__github__create_issue.
   - deny: deletes, or cannot be undone.
   Ask "Are these the right rules?" and save only after a yes.
5. Test the rules: an allowed tool runs, an ask tool stops for you, a denied tool is refused.
6. **Many agents.** Add the server once with `claude mcp add --scope project`, which writes it to the project's .mcp.json for you to commit. Keep keys in environment variables, not in the file. Every session and subagent now reaches the same server.
7. Report each tool and its rule, the calls made and what each result was used for.

## Rules
- A tool with no rule asks before it runs.
- Deny beats allow.
- An empty or failed call is not an answer. Never guess it.
- Adding a server or removing a deny is the owner's call.
