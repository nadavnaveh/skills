---
name: step-cache
description: Splits a slow pipeline into steps, stores each step's output under a key made from its inputs (file bytes, settings, code version), and reuses that output when the key matches, so only the steps whose inputs changed run again. Fixes "every small fix re-runs my whole pipeline." Use when a build, render, report or data job takes minutes and you change one small part of it, or when a rebuild with no change still runs every step. Also on /step-cache.
---

# Step cache

You fixed one paragraph, and the whole pipeline ran again. It runs as one block, so it cannot see what your change touched. This skill splits it into steps and runs again only the steps whose inputs changed.

## The principles
1. The step is what runs again. A pipeline with no steps runs in full every time.
2. A step's key is made from everything it reads: file bytes, settings and code version.
3. Same key, same output. If the key matches, reuse the stored output. If not, run the step.
4. A key that misses an input gives stale output with no error. When in doubt, put it in the key.

## Steps
1. Time one full run and write the number down.
2. List the pipeline as steps in order, with what each one reads and writes. Ask "Are these the right steps?" and start only after a yes.
3. Build each step's key: a hash of the bytes of every file it reads, its settings and the version of its code and tools. Leave out paths, file dates and the time of the run.
4. Before a step runs, look in a cache folder for output stored under its key. If it is there, reuse it. If not, run the step and store the output under the key.
5. Have every run print each step as "ran" or "reused", and the total time.
6. Test twice. With no change, every step should say reused. After one small change, only the steps that read it, and the steps after them, should run.
7. Report the full, no-change and small-fix times, with what changed and how many steps ran or were reused. Name any step that still runs in full, and why.

## Rules
- Key on a file's bytes, never its name, path or date.
- Deleting the cache must be safe: a full run gives the same result, only slower. Ask before deleting it.
- Report only times measured on your own pipeline. Ours (scripts/PROOF.md, scripts/me-294.txt) come from one 13-scene, 81 s video: full render 122 s, no-change rebuild 11 s, one-paragraph fix 30 s with 1 scene drawn and 12 reused. They do not predict other pipelines.
- What our proof does not show: that the voice is cached (a voice change still re-takes the whole voice), or that a fully cached build never drew anything (the 8-of-8 rebuild in 7.1 s came after an earlier run had drawn and stored every scene).
