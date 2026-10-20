---
name: long-videos
description: Works through an hour of video cheaply. It turns the video into a timed transcript first, searches the words for the minute that matters, looks at one frame every 10 seconds, cuts a short clip for a close look, and puts a timestamp on every claim. Fixes "I gave it an hour of video, and it cost a fortune and still missed the part I needed." Use when you hand the agent a recording, a meeting, a call, a talk, a demo or any video longer than a few minutes, when you need to find one moment in a long video, or when you want notes or a summary of one. Also on /long-videos.
---

# Long videos

You gave the agent an hour of video. It cost a fortune and still missed the part you needed. An hour holds about 100,000 frames, and looking at frames is the most expensive way to read a video. This skill reads the words first, finds the minute that matters and looks closely only there.

## The principles
1. Read words before frames. Words are cheap to read and easy to search.
2. Look closely only where the words point.
3. Every claim gets its minute, so anyone can check it.

## Steps
1. Turn the video into a timed transcript first. If the video has a captions file, use it. If not, take out the audio and run a speech-to-text tool that writes a timestamp on every line, such as Whisper. Save the transcript as a text file next to the video.
2. Ask the owner what they are looking for, in one line, such as "where we agreed the deal". Turn that line into a few search words.
3. Search the transcript for those words and list every hit with its time, such as "deal" at 12:41. Read the lines around each hit to pick the minutes that matter. If nothing matches, try other words before you look at any frames.
4. When you need to see the screen and not just hear it, take one frame every 10 seconds (ffmpeg can do this). At 30 frames a second, that is one frame in 300. Name each frame by its time.
5. Cut a short clip around the minute that matters, such as 12:30 to 14:30, and look at it closely: a frame every second or two, plus the transcript lines for those two minutes. Never do this for the whole hour.
6. Write the notes. Every claim carries the time it came from, such as "price agreed at 40,000 @12:41". If a claim has no time, check it or cut it.
7. Before you hand over the notes, pick two cited times at random and check that the video says what the note says. Report each one as holds or does not hold.

## Rules
- Never look at every frame of a long video. Start from the transcript.
- A claim without a timestamp is not a finding yet.
- Say which minutes you never sampled or clipped. They are not covered.
- If the audio is unclear or missing, say so before you rely on frames alone.
