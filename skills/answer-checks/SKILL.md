---
name: answer-checks
description: Checks an answer before you act on it, using five checks. It opens the source, makes the agent argue against its own answer, asks a fresh session that never saw the answer, runs the method on a case where the result is already known, and sets how hard to check by what an error would cost. Fixes "It sounded right, I used it, and it was wrong." Use before you act on a number, a fact, a quote, a summary or a piece of code the agent gave you, before you send or publish anything built on it, when an answer cites a source, and when you are about to trust an answer because the agent agreed with you. Also on /answer-checks.
---

# Answer checks

The answer sounded right, and it was wrong. The agent sounds just as sure when it guessed as when it checked, and asking "are you sure?" only gets a yes. This skill checks the answer against something outside the conversation before you use it.

## The principles
1. Agreement is not proof. An agent that agrees with itself, or with you, has checked nothing.
2. A source counts only when someone opened it. A link the agent gave you is a claim until the page says the same thing.
3. Check by the cost. A cheap error gets a glance. A costly one gets a full check.

## Steps
1. List the claims the answer rests on: each number, fact, quote and result. Mark the ones the decision depends on.
2. Set the bar for each claim by the cost of being wrong. A typo in a draft gets a glance. A number on an invoice, in a contract or in a live system gets every check below that fits. State the bar for each claim in one line.
3. Open the source. For each claim with a source, open the page, file or document, find the exact place (page 12, line 40) and quote it. If the answer says "grew 40%" and page 12 says 14%, the claim fails. If you cannot open the source, mark the claim not checked.
4. Ask for the opposite. Have the agent argue against its own answer: what is weak, what it assumed, what would make it wrong. Fix the weak spots that hold up. For any you leave, say which and why.
5. Do a blind reread. Give only the question, not the answer, to a fresh session (a subagent, or a new session after /clear). Compare its answer with the first one. If they differ, go back to the source. Do not just pick the one you like.
6. Run a known case. For code, a formula or a method, first run it on a case where you already know the answer. If case 17 should give 4 and it gives 4, that is a pass. If it does not, the method is wrong, whatever it says on new cases.
7. Report each key claim as:
   - **Pass**, with the evidence: the quote, the page, the output.
   - **Fail**, with what the check found instead.
   - **Not checked**, with why, and the exact step the owner can take to check it.

## Rules
- Never report a number or quote as checked without the place you saw it.
- "I am confident" and "the agent agreed" are not evidence.
- The fresh session gets the question only, never the first answer.
- When the checks disagree, the source wins.
