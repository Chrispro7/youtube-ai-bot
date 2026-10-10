# I Automated YouTube with 7 Python Files

Status: script final, not recorded.

## Package

- **Title:** I Automated YouTube with 7 Python Files (39 chars, `title.py` score 100)
- **Thumbnail text:** BOT MADE THIS
- **Thumbnail brief:** finished bot-made frame on the right two-thirds, a sliver of terminal running
  `main.py` on the left. White text, heavy black stroke, top left over the dark terminal. Keep the
  video frame bright and saturated so the text holds contrast at feed size.

## Hooks (hookscore.py)

1. **You should stop editing Shorts by hand before you see what 254 lines of Python do with one
   command.** 72 STRONG, The Warning. Weakest: curiosity.
2. Seven Python files, 254 lines, one command, and you never open an editor before the video is on
   YouTube. 57 WORKABLE, The Impossible Claim. Use only if literally true.

## Script (~250 words, ~1:40 at 150 wpm)

**[0:00 HOOK]** You should stop editing Shorts by hand before you see what 254 lines of Python do
with one command.
`[ON SCREEN: the 7 filenames with their line counts, then the total, 254]`

**[0:08 TURN]** I'm going to run it once, right now, and walk through every file it touches on the
way to YouTube.
`[ON SCREEN: terminal, typing python main.py]`

**Beat 1, the topic.** `topic_generator.py` picks a topic. The niche comes from one setting, and by
default it's tech facts.
`[ON SCREEN: the "Topic:" line printing in the terminal]`

**Beat 2, the script.** `script_writer.py` turns that topic into a script. Here's what it wrote this
time.
`[ON SCREEN: the script text scrolling, next to the "Script written" line]`

**Beat 3, the voice.** `tts_engine.py` reads it out loud with one neural voice. Here are ten seconds
of it.
`[ON SCREEN: waveform with captions, 10 seconds of audio]`

**Beat 4, the video.** `video_builder.py` is the biggest file, at 89 lines. It puts the voice and the
visuals together.
`[ON SCREEN: the file scrolling, then the finished frame]`

**Beat 5, the upload.** `uploader.py` sends it to YouTube with a title, a description and tags.
`oauth_setup.py` is the smallest file, 13 lines, and nothing uploads without it.
`[ON SCREEN: the "Uploaded! ID:" line, then YouTube Studio]`

**PAYOFF.** That's the whole thing: seven files and one command, from topic to upload. The code is
linked in the description.
`[ON SCREEN: the Short live in Studio, and the repo link]`

**CLOSE.** Comment the topic you want the bot to make next.
`[ON SCREEN: end card]`

## Before recording

- [ ] Test-run `python main.py` end to end (the pipeline has not been run yet).
- [ ] Decide whether the repo is public; if not, cut the "code is linked" line.
- [ ] Re-check the line counts (254 total, 89 in `video_builder.py`, 13 in `oauth_setup.py`) if the
      code changes before filming.
- [ ] Fill in `voice.md` so future scripts are in your voice.
