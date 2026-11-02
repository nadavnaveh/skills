---
name: faster-same
description: The text you paste into your agent when it offers to make code faster, so it keeps the original, compares old and new on at least 1,000 inputs, times both and adds a switch back, and you own the check. Fixes "The agent offered to make my code faster, and I won't read every line." Use when an agent offers to speed up a file or function, when you ask it to make slow code faster, or before you accept a speed-up you have not read. Also on /faster-same.
---

# Faster, same

The agent offers to make your code faster, and you won't read every line. A rewrite can look right and still behave differently. This skill is the text you paste into your agent, and it has two parts: show it behaves the same, keep the way back. You own the check.

## When to use it
Use it when the agent offers to make code faster and you won't read every line.

## The principles
1. Show it behaves the same. Run old and new on the same inputs and compare every output.
2. Keep the way back. The original stays, and one switch returns to it.
3. You own the check. The agent's report is a claim until you read it and run the switch.

## Steps
1. If TARGET is not named, ask which file or function it is.
2. Look for side effects in TARGET. If there are any, follow the side-effects rule below.
3. Follow the text below word for word, with TARGET filled in.
4. End with its four lines, then ask the person to read them and run the switch once.

## The text you paste

```text
Paste this to your agent, and put your file or function where it says TARGET:

Make TARGET faster without changing what it does. Work in this order:
1. Keep the current version. Copy it next to the new one as <name>_original and do not delete it.
2. Prove it is the same. Write a test that runs the original and the new version on at least 1,000 inputs (random ones plus edge cases: empty, a single item, duplicates, very large values) and checks that every output is identical. Run it and show me the result.
3. Measure. Time both versions on the same realistic input and show me both numbers.
4. Keep a way back. Add a switch (the environment variable USE_ORIGINAL=1) that runs the original instead.
5. Do not change the function's name, its inputs or its outputs. If the test fails and you cannot fix it, stop and tell me. Never ship a version that did not pass.
End with four lines: the test result (passed or failed, on how many inputs), the old time, the new time, and how to switch back.
```

## Example
Our run, on a function we made slow on purpose: a Haiku agent kept the original and compared 1,220 inputs, all with identical outputs. The time went from 0.42 s to 0.003 s. USE_ORIGINAL=1 switches back. Our separate check agreed.

## Rules
- Passing on 1,000 inputs is a test, not a mathematical proof.
- A large speed-up here doesn't predict yours.
- The check stays with you: read the four-line ending and run the switch once.
- If the code has side effects (writes, network, randomness, time), comparing outputs isn't enough. Stop and say what wasn't compared.
