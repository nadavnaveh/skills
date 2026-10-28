---
name: rubric-numbers
description: Rewrites every check you give an AI judge as a number with a unit and a pass/fail line, makes the judge name the failing element and its value, and measures in code what code can measure. Fixes "I asked the AI to check the same thing twice, and it gave me opposite answers." Use when you ask a model to grade, review or approve work (a screenshot, a video frame, a page, an agent's output), when a check says "readable", "clear" or "looks good", and when one check gives different verdicts on the same thing. Also on /rubric-numbers.
---

# Rubric numbers

You asked an AI judge "is it readable?" and got a yes, then a no, on the same thing. A word like "readable" leaves the line for the judge to draw, and it can draw it differently each time. This skill turns each check into a number with a pass/fail line, and hands the measuring to code where it can.

## The principles
1. A check is a number with a unit and a line: "every text is at least 40 px tall", not "easy to read on a phone".
2. A FAIL that names no element and no value is not a verdict.
3. A model's size estimate is a guess. Measure in code what code can measure.

## Steps
1. List every check the judge will run. Mark each one written as a word (readable, clear, clean, big enough).
2. Rewrite each marked check as a number with a unit (px, seconds, count) and a line, for example "FAIL if any text element is under 40 px tall." If no number fits, it is taste: write "the owner says yes to X".
3. Show the new checks and ask "Are these the right lines?" Start only after a yes.
4. Tell the judge: "For every FAIL, name the failing element and its measured or estimated value." A FAIL that names nothing goes back to the judge.
5. For anything code can measure (text height in an image, video length, word count), measure it with a short script. Use the judge only for the rest.
6. Where the judge can only estimate, leave a margin, and measure in code any estimate near the line.
7. Report each check as pass, fail or not run, with the element, the value, and whether it was measured or estimated.

## Rules
- Never give an AI judge a check written as an adjective.
- Never report an estimate as a measurement.
- Our run (scripts/RESULT.md): on one real video frame, Sonnet asked three times "is every piece of text easy to read on a phone?" said PASS, FAIL, FAIL. Asked "FAIL if any text element is under 40 px", it said FAIL three of three and named the title bar at about 22 px. On the other frame, code measured that title bar at 20 px (model: 22) and the command line at 47 px (model: 35 to 40).
- What it does not show (scripts/PROOF.md): how often a word check splits (the other frame did not split, so one split in six reads), that a number check is always right, or any general error rate for estimates.
