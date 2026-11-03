---
name: objector
description: Adds an objector to the agent's decisions. Before a decision that costs money or is hard to undo, a fresh subagent that did not make the decision argues that it is wrong, point by point. The first agent answers each point and changes the decision only for a fact it can check. Fixes "The agent made a call that cost money, and nobody argued with it." Use before a payment, a purchase, a booking, a price, a date or time someone will act on, a delete, a migration, a release, or any choice that is expensive to reverse. Skip it for cheap, reversible choices. Also on /objector.
---

# Objector

The agent made a call that cost money, and it was wrong. Nobody argued with it, because an agent checking its own decision agrees with itself. This skill adds an objector: a second agent whose only job is to prove the decision wrong before anyone acts on it.

## The principles
1. The agent that decided cannot be the one that objects.
2. Only a fact you can check changes a decision. A good argument without one changes nothing.
3. It costs tokens, so keep it for decisions that cost money or are hard to undo.

## Steps
1. Decide whether it is worth it. If the choice is cheap and easy to undo, skip this skill and say so in one line.
2. Write the decision and its reasons in a few lines: what you decided, and each reason with the fact it rests on.
3. Start a fresh objector that did not write the decision. In Claude Code, use a subagent (the Agent tool). Anywhere else, run a second `claude -p` with no shared context. Give it only the decision and the reasons. Its brief: "Make the strongest case that this decision is wrong, point by point. Tie each point to something checkable: a date, a number, a doc line or a command to run."
4. Answer every point, one at a time. Check the fact it names yourself: open the doc, run the command or do the arithmetic. Mark each point as **holds** (the fact checks out and changes the decision), **fails** (the fact is wrong, and say what you found) or **no fact** (nothing to check, so nothing changes).
5. Change the decision only for a point that holds, and name the fact that changed it.
6. Show the person four things: the decision, the objections, your answer to each one, and what changed, or "nothing changed". Act only after they say yes.

## Rules
- The objector never sees the first agent's hidden reasoning. It sees only the decision and its reasons.
- An objection without a checkable fact changes nothing.
- This is a second opinion, not a proof. It does not make the decision safe.
- Our run used Haiku on ten decisions with known answers, run three times. Alone, it got 29 of 30 right, and the one miss was the New York to Tel Aviv time after the US clock change. With a separate objector, the same question was missed once in a first answer, the objector caught it, and no right answer was flipped. It cost about 3x the tokens. One fix in 30 decisions is one event, not a rate.
