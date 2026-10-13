# Skills for running AI like a company

You use AI. I run it like a company.

These are the skills I use to manage the agents that run my work. Each one is small, and each one fixes a failure you have probably already had. They work the same whether you write code or not.

## The failures, and the skill for each

### "It did exactly what I asked, and it's not what I wanted."

You said "make it better". The agent picked a meaning and ran. The problem started before the agent: the want was a feeling with a direction, and nobody wrote down where it ends.

**[`/what-do-i-want`](./skills/what-do-i-want/SKILL.md)** reads your want, shows you the two or three ways it could be read, asks the few questions that change the result, and writes one statement with a done-test. The work starts only after your yes. [Docs and a real example](./docs/skills/what-do-i-want.md).

### "The answer looks reasonable, but it misses my world."

The agent was not weak. It was never in the room. Your goal, your audience, what you tried last month and the words your team uses were all in your head.

**`/into-the-room`** (draft, coming next) checks what is in your head and not in the agent's context before you hand off.

### "The agent said it was done, and it wasn't."

"Done" meant "I stopped working", not "it works". Nobody said what works means, so the agent picked a finish line it could reach.

**[`/done-test`](./skills/done-test/SKILL.md)** writes one to three yes/no checks before the work starts, then runs each one at the end and reports pass, fail or not run, with the evidence. No "done" without them. [Docs and a real example](./docs/skills/done-test.md).

### "It says it's done. Is it good?"

If you did not decide what good means before the work, you will decide it afterwards, by feel, and argue with the agent about it.

**`/define-good`** (draft) writes the success test first, for code and for everything that is not code.

### "I gave it one big job and it came back a mess."

A big ask needs to be split by what depends on what, so each step knows what it receives and what it hands on.

**`/break-by-dependency`** (draft) does the split.

### "It ran for two hours and failed quietly." / "I keep correcting the same thing."

You either watch every step or find out too late. A failure once is a retry. The same failure twice means the plan is wrong, not the output.

**`/when-to-step-in`** (draft) sets the checkpoints where you come back in.

Drafts live in [`skills/in-progress/`](./skills/in-progress/). They are not installed by the plugin until they are ready.

## Where these come from

Each skill is one practice I use every day to run my work with AI agents. Each skill states the principles behind it, so you can see the reasoning and disagree with it.

## Install

Pick one. Installing two ways gives you every skill twice.

### 1. Claude Code plugin

```bash
claude plugin marketplace add nadavnaveh/skills
claude plugin install nadavnaveh-skills@nadavnaveh
```

Or, from inside a session:

```
/plugin marketplace add nadavnaveh/skills
/plugin install nadavnaveh-skills@nadavnaveh
```

Updates arrive when I release. The skills are read-only.

### 2. Any agent, with `npx skills`

```bash
npx skills@latest add nadavnaveh/skills
```

This copies editable skill files into your project and works with Claude Code, Codex, Cursor and other agents that read `SKILL.md` files.

### 3. Clone

```bash
git clone https://github.com/nadavnaveh/skills.git
mkdir -p ~/.claude/skills
ln -s "$PWD/skills/skills/what-do-i-want" ~/.claude/skills/what-do-i-want
```

Copy or link any skill folder into your agent's skills folder.

Then type `/what-do-i-want` followed by what you want, or just ask for something vague and let the agent reach for it.

## Credits

- Built on the [Agent Skills](https://code.claude.com/docs/en/skills) format and the Claude Code plugin format.

## License

[MIT](./LICENSE). Use them, change them, make them yours.
