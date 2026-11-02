---
name: agent-limits
description: Maps which steps your agent may take alone, from its real config, and writes one LIMITS.md: each action, whether it can be undone, its tier, the stop outside the agent, and whether that stop was tested, plus a halt plan. Fixes "I can't say which steps my agent takes alone, or what would stop it." Use when you point it at a workflow or a set of agent permissions, when you describe what an agent does, before a long or unattended run, and when an agent gets a new tool or key. Also on /agent-limits.
---

# Agent limits

Nobody can say which steps the agent takes alone, or what would stop it. The limits sit in someone's head or in a line of the prompt, and the agent decides on every turn whether to follow that line. This skill maps every action to a tier and a stop, tests a stop, and decides the halt before the run.

## The principles
1. A person keeps what can't be undone.
2. A stop lives outside the agent. If the agent can change it, it is not a stop.
3. Decide the halt before the run, not halfway through it.

## Steps
1. List every action the agent can take. Read the real config, tools, hooks and scripts where you can. Mark anything you could not read as inferred.
2. Sort each action: reversible alone, reversible with effort, or can't be undone. Can't be undone means things like deleting data, sending to a customer, paying, publishing, force-pushing and production changes.
3. Give each a tier: the agent acts alone, the agent acts and reports, or a person approves first. Every can't-be-undone action starts at a person approves. Only the owner may lower it.
4. Name the stop for each action: a permission rule, a hook, a credential the agent doesn't hold, a budget cap. If you find only a line in a prompt, or a file the agent can edit, write "no stop".
5. Test one stop. Try the blocked action in a dry run, against a throwaway target where nothing real can be hit. Write down what happened. A stop that let the action through is marked failed.
6. Write the halt plan for each long job: what state it may stop in, who is told, who takes over, and what to do if the agent refuses or fails halfway.
7. Write LIMITS.md: one table with the columns action, can it be undone, tier, the stop, tested or not. Put the halt plans under it. Show the owner every gap, and ask before you close any of them.

## Rules
- A rule written only in the agent's prompt isn't a stop. Say so in the table.
- Don't change permissions without the owner's yes.
- A stop not tested is marked not tested.
- Say what this does not prove: a map lowers risk, it doesn't guarantee safety. A passed test shows one stop held once.
