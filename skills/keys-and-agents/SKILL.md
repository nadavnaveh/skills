---
name: keys-and-agents
description: Keeps keys, tokens and passwords out of the chat and out of git, scoped to the task, read-only where it can be, and replaced the day it leaks. Fixes "I ran the agent in a sandbox, and it could still see my keys." Use when a task needs an API key, token, password or database URL, or when one shows up in a chat, a log or a commit. Also on /keys-and-agents.
---

# Keys and agents

You ran the agent in a sandbox and thought your keys were safe. A sandbox limits what the agent can change, not always what it can read: a pasted key, a printed key, a key in a file it can open. This skill keeps every key out of sight, scoped, limited and rotated.

## The principles
1. A key pasted in chat stays in the log for good.
2. A key typed into hidden input and saved to a gitignored file stays out of git and chat. The agent can still read that file unless something stops it.
3. A session sees only the keys its task needs.
4. A key does no more than the task needs. Reading data does not need a key that can delete it.
5. A leaked key gets replaced. Deleting the message or the commit does not take it back.

## Steps
1. List the keys the task needs by name only, for example DB_URL. Never ask for a value in chat. If one is pasted anyway, go to step 5.
2. Check .env.local is gitignored. Have the person type each key into hidden input in their own terminal, not the chat:
   `(umask 077; printf 'DB_URL: '; read -rs v; echo; printf 'DB_URL=%s\n' "$v" >> .env.local)`
   If the file already existed, also run `chmod 600 .env.local`. That stops other users on the machine, not the agent.
3. Scope it. Keep keys for other jobs in their own file, for example the payment key in .env.pay. To keep this session out of it, turn on the sandbox with that file blocked, or deny shell reads of it. A `Read(./.env.pay)` rule under `permissions.deny` alone does not stop `cat .env.pay`, and shell deny patterns are easy to get around, so the sandbox is the safer choice.
4. When the person creates a key, ask for the smallest scope: read yes, write and delete no. For a database, use a user that can only read. If the provider has no scopes, say so.
5. Rotate. A key seen in chat, a log, a screenshot or a commit has leaked. Tell the person where to revoke it today, have them make a new one through step 2, and ask them to confirm the old key now fails.
6. Report each key by name: its file, what it can do, which session can read it, and whether it was rotated.

## Rules
- Never print or repeat a key's value, not even part of it.
- The person revokes and issues keys. The agent names where, and reads the result the person reports.
- Ask before a task gets another key or a wider scope.
