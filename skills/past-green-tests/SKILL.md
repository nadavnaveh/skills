---
name: past-green-tests
description: Checks the design of the code after the tests pass. It looks at which layer imports which, how big each file is, where the same logic is copied and which names say nothing, then gives a person a short list to check the shape. Fixes "the tests were green, and the code was still a mess." Use after the tests pass and before you merge, when a file keeps growing, when the agent added a feature by copying code, when you see names like data2, temp or final_v3, or before you approve a change from an agent. Also on /past-green-tests.
---

# Past green tests

The tests were green, and the code was still a mess. Tests check what the code does, not how it is built, so a screen that reads the database directly passes just as well as one that goes through the API. This skill runs four design checks the tests never make, then hands the shape to a person.

## The principles
1. Green tests prove behavior, not design. Check the design on its own.
2. A design rule that is only written down will be broken. Turn it into a check that fails.
3. A warning asks for a look, not a fix on the spot. A big file or a copy gets looked at, then the person decides.
4. A person checks the shape. The agent brings the evidence.

## Steps
1. **Imports.** Write the layer rule in one line, for example "the UI may call the API, never the database." Add a check that fails when a file in the UI folder imports from the database folder. It can be a test, a lint rule or a short script that runs with the tests. Show it fail once on a bad import, then pass once the import is gone.
2. **File size.** List the biggest files with their line counts, and the files that grew most in this change (`git diff --stat`). A file near 3,000 lines is a warning. For each one, say what it does in one line and where it could be split.
3. **Copies.** Search for logic that shows up in more than one place, like the same tax() in three files. For each one, name every file and line. Keep one version and make the others call it.
4. **Naming.** List names that say nothing: data2, temp, tmp, final_v3, new, old. For each one, suggest a name that says what it holds, like invoices. Rename one at a time.
5. **Design check.** Give the person a short list to tick, one line at a time: layers (does every import follow the rule?), names (does every name say what it holds?), size (is any file doing too much?). Put the evidence next to each line.
6. Report each check as pass, fail or not run, with the output or the list behind it.

## Rules
- Run the tests after every rename, merge or split. They must stay green the whole way.
- Do not change what the code does in the same change that fixes its design.
- Split a big file only after the person says yes.
- The design check is ticked by a person, never by the agent.
