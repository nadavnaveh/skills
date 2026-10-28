# Claude Code docs, fetched 2026-10-28 by lane-b, verbatim lines

## https://code.claude.com/docs/en/sandboxing
> By default, sandboxed commands can write to the current working directory, the per-user temp directory, and any directories you've added with `--add-dir`, `/add-dir`, or `permissions.additionalDirectories`.
> The sandbox is off by default. To turn it on, run `/sandbox` in a session, as Get started shows, or set `sandbox.enabled` to `true` in a settings file such as `~/.claude/settings.json`.
> `touch ~/sandbox-probe` | Fails with `Operation not permitted` on macOS, or `Read-only file system` on Linux and WSL2.
> If Claude asks to retry a failed command outside the sandbox, decline the retry.
> You can disable the unsandboxed retry by setting `"allowUnsandboxedCommands": false` in your sandbox settings. With the retry disabled, Claude Code ignores the `dangerouslyDisableSandbox` parameter.
> claude --settings '{"sandbox": {"enabled": true, "allowUnsandboxedCommands": false}}'
> The sandbox covers shell commands only. Claude's file tools, MCP servers, and hooks run outside it.
> tools such as Read, Edit, Write, WebFetch, and WebSearch follow permission rules instead.
> The sandbox runs on macOS, Linux, and WSL2. On native Windows, Claude Code runs commands unsandboxed. To use the sandbox on a Windows machine, run Claude Code inside a WSL2 distribution.

## https://code.claude.com/docs/en/permissions
> The `:*` suffix is an equivalent way to write a trailing wildcard, so `Bash(ls:*)` matches the same commands as `Bash(ls *)`.
> > Claude Code is aware of shell operators, so a rule like `Bash(safe-cmd *)` won't give it permission to run the command `safe-cmd && other-cmd`. The recognized command separators are `&&`, `||`, `;`, `|`, `|&`, `&`, and newlines. Every subcommand must be allowed for a compound command to run without a prompt, for example because the subcommand matches an allow rule or is a [read-only command](#read-only-commands).
> Deny and ask rules apply when any subcommand matches them, including a command nested inside a subshell, a command substitution, or a control-flow body such as a `for` loop. An ask rule like `Bash(git clean *)` still prompts you for `cd /tmp && git clean -f` or `echo "$(git clean -f)"`, even in [auto mode](https://code.claude.com/docs/en/permission-modes.md#eliminate-prompts-with-auto-mode).
> A Bash rule matches the command text Claude writes, after Claude Code splits [compound commands](#compound-commands) and strips [wrappers](#process-wrappers). It doesn't match the same program invoked in a different form, so a deny or ask rule covers the invocation Claude usually produces and isn't a security boundary around the program. These rules in `deny` or `ask` stop the first form and not the others:
> For filesystem and network enforcement that doesn't depend on the command text, use [sandboxing](https://code.claude.com/docs/en/sandboxing.md). To inspect the full command text with your own logic before it runs, use a [PreToolUse hook](#extend-permissions-with-hooks).

## https://code.claude.com/docs/en/checkpointing (fetched 2026-10-28)
> A file that only Bash commands changed isn't tracked and stays as it is. To revert it, use version control, such as Git.
> Checkpoints are designed for quick, session-level recovery. For permanent version history and collaboration, continue using version control, such as Git, for commits, branches, and long-term history.
