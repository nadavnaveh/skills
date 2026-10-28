---
name: second-ear
description: Turns every AI-generated voice take back into text, compares it with the script word by word, regenerates any take with missing, extra or repeated words, and sends the spots the check cannot hear to a person. Fixes "the AI voice skipped a line, and nobody noticed until it was posted." Use whenever a voice or voice-over is generated from a script (text to speech, a cloned voice, a dub), before anyone else hears the take, and before you call a take done. Also on /second-ear.
---

# Second ear

The AI voice skipped a line, and nobody noticed until it was posted. A generated take sounds smooth even when it repeats or drops a sentence, so a quick listen misses it. This skill turns the take back into text, compares it with the script, and sends what the check cannot hear to a person.

## The principles
1. Check a take against the script, not by how it sounds. Turn the audio into text and compare word by word.
2. A flagged take is thrown out and regenerated whole, never patched.
3. The check has blind spots. Write them down and send them to a human ear.

## Steps
1. Save the script as plain text, one paragraph per line. Every take is checked against this copy.
2. Generate the take, then transcribe it with a transcriber that gives timestamps (ours is Whisper).
3. Run `python3 scripts/voice_check.py <copy.txt> <transcript.json>`. It flags runs of 3 or more copy words missing, runs of 3 or more extra words, and phrases heard more often than the copy has them, then ends with PASS or LISTEN.
4. Read every flag. A spelling difference (digits for number words, a foreign word in another alphabet) is not an error; say so. On a real flag, discard the take, regenerate it whole and check again.
5. List the blind spots in the take that passed, with timestamps: any phrase the transcriber may have written once though it was said more, and any single word that differs from the copy.
6. Have a person listen to those spots before anyone else hears the take.
7. Report each take: PASS or LISTEN, each flag and what you did, the blind spots, and who listened.

## Rules
- PASS means the transcript matches the copy. The take is not done until a person has heard the blind spots.
- A single word heard differently passes under the 3-word threshold. Only a person can tell whether the voice or the transcriber slipped.
- Our proof (scripts/PROOF.md, scripts/RESULT.md) is our own takes. Across 60 transcripts there was one real catch: restored01 take 1 repeated a line and skipped the next sentence (15 missing copy words plus repeat flags), and take 2 passed with 0 flags. In September a phrase said three times was written once and passed. Another take passed with one word heard differently.
- The proof does not show a catch rate, that the check catches everything, or which side slipped in the one-word case.
