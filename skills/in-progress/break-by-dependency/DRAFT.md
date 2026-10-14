---
name: break-by-dependency
description: DRAFT, not ready. Splits one big job into steps by what depends on what, so each step says what it hands to the next and independent steps can run in parallel. Fixes "I gave it one big job and it came back a mess." Use when a task is bigger than one prompt.
disable-model-invocation: true
---

# Break by dependency (DRAFT)

Status: stub. Not ready to use.

Pain: one big ask, one big mess.

Planned shape:
- Outcome, then the parts, then what each part needs from another.
- Each step names its input, what it hands on, and how you check it.
- An open question stays open. Never invent a value to finish the plan.
