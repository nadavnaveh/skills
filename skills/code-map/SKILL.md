---
name: code-map
description: Maps old code before anyone changes it. It finds where every request starts, follows the data step by step, counts who calls the function you want to change, marks the risky parts and checks what is tested. Fixes "I changed one small thing in old code, and something far away broke." Use it before you change, fix or refactor code you did not write or have not opened in months, when you join a new project, when a change touches billing, login or anything that moves money or data, and before you plan a big change. Also on /code-map.
---

# Code map

You changed one small thing in old code, and something far away broke.
Nobody knew what called it, where its data went or that it had no tests.
This skill draws a five-part map of the code first, so the change starts from what is known.

## The principles
1. Find where work starts, then follow the data. That shows you the path a change will travel.
2. Every line on the map points to a file. "I think" is not a map.
3. Count the callers before you change a function. The count tells you how far a break can spread.
4. Red means it moves money, logs people in, deletes or sends data, or has many callers and no tests. Red parts get the smallest steps.

## Steps
1. Find the entry points. Use plan mode (Shift+Tab) while you read, so nothing gets edited. Read the folders where work starts (for example api/, jobs/, cli/). List each route, job or command and the file it lives in. In a large project, give the reading to a subagent and take back only the list.
2. Trace the data flow for the part you will change, one hop at a time. Start where the data comes in (a form, a request, a file). Follow it to where it is stored and where it goes out (a report, an email, a reply). Write each hop as "from → to", with the file.
3. List who calls what. Search for every place that calls the function you plan to change. Also search for its name as plain text, since routes, job names and settings can call it too. If there is no search tool, run grep -rn "name" . in the terminal. Write the number of callers and each caller with its file.
4. Mark the risky parts. Use the red test from principle 4. Mark green what you checked and found safe to change. Run git log on each part to see which files keep getting fixes.
5. Check what is covered. If the project has a test coverage command, run it. If not, list which files have tests and which have none. Write the result for each part, for example "billing 20%, ui 80%".
6. Show the map in chat with its five parts and the red parts first. Ask "Change it with this map?" After a yes, leave plan mode, save the map to one file (for example docs/code-map.md) and add one line to CLAUDE.md that points to it.

## Rules
- Before you change a red part with few tests, write a test for it, or get the owner's yes to go without one.
- Mark anything you could not trace as unknown, never as safe.
- Keep the map to one page that a person can read before they touch the code.
