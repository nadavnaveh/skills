---
name: cloud-offload
description: Moves your agents' heavy work off your computer into Claude Code cloud sessions on Anthropic's machines. Fixes "my laptop freezes with several agents running." Use when your computer slows down with many agents, before a long build or test run, or when you want work to keep going after you close the laptop. Also on /cloud-offload.
---

# Cloud offload

When many agents run on one laptop, it slows down and gets stuck. Claude Code can run the work in a cloud session on Anthropic's machines instead. Your computer plans and reviews; the cloud does the long work.

## The principles
1. The cloud sees what is on GitHub, not what is on your laptop. Push first.
2. Your computer keeps what needs it: keys, deploys, databases, local apps.
3. One task per session, each on its own files and its own branch.
4. A session's "done" is a claim until you read the diff and the checks ran.

## Steps
1. Push the plan. Write the task and its done-test in a file, commit and push it.
2. In the cloud environment settings on claude.ai/code, give the session only the access the task needs.
3. Start a cloud session from the project folder:
   `claude --cloud "Implement plan.md. Done when npm test passes."`
   You can also start it from claude.ai/code.
4. For many agents, start one session per lane, each owning its own files.
5. Make each prompt stand alone (the cloud agent starts with no context): its branch, its files, its checks, and "push only your branch, never main, never deploy".
6. Close the laptop. Follow the sessions on claude.ai/code or the Claude mobile app, and answer their questions.
7. Bring each one back: read the diff, run the checks yourself, merge on your yes.

## Rules
- Never put a key in a prompt.
- Deploys and database changes stay on your computer.
- Start with one session, check the result, then add lanes.
- A session that cannot reach something (a private service, a local app) should stop and ask, not guess.
