import os
import requests
import textwrap
from moviepy.editor import (
    AudioFileClip,
    VideoFileClip,
    ColorClip,
    CompositeVideoClip,
    ImageSequenceClip,
    concatenate_videoclips
)
from PIL import Image, ImageDraw, ImageFont
import numpy as np

PEXELS_KEY = os.getenv("PEXELS_API_KEY")

def get_background_clips(query: str, count: int = 3) -> list:
    try:
        url = "https://api.pexels.com/videos/search"
        headers = {"Authorization": PEXELS_KEY}
        params = {"query": query, "per_page": count, "size": "medium"}
        r = requests.get(url, headers=headers, params=params)
        data = r.json()
        paths = []
        for video in data.get("videos", [])[:count]:
            file_url = video["video_files"][0]["link"]
            path = f"/tmp/clip_{video['id']}.mp4"
            if not os.path.exists(path):
                with open(path, "wb") as f:
                    f.write(requests.get(file_url).content)
            paths.append(path)
        return paths
    except Exception as e:
        print(f"Pexels error: {e}")
        return []

def make_text_overlay(text: str, size=(1080, 1920)):
    img = Image.new("RGBA", size, (0, 0, 0, 160))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52
        )
    except:
        font = ImageFont.load_default()
    wrapped = textwrap.fill(text, 22)
    draw.multiline_text(
        (540, 960), wrapped, font=font, fill="white",
        anchor="mm", align="center",
        stroke_width=3, stroke_fill="black"
    )
    return np.array(img.convert("RGB"))

def build_video(topic: str, script: str, audio_path: str) -> str:
    print("Building video...")
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    output = f"/tmp/final_{abs(hash(topic)) % 99999}.mp4"

    clips = []
    try:
        clip_paths = get_background_clips(topic.split()[-1], count=3)
        for cp in clip_paths:
            vc = VideoFileClip(cp).resize((1080, 1920))
            clips.append(
                vc.subclip(0, min(vc.duration, duration / max(len(clip_paths), 1)))
            )
    except Exception as e:
        print(f"Clip error: {e}")

    if clips:
        bg = concatenate_videoclips(clips).subclip(0, duration)
    else:
        bg = ColorClip((1080, 1920), color=(10, 10, 30), duration=duration)

    txt_frames = [make_text_overlay(topic, (1080, 1920))] * int(duration * 30)
    txt_clip = (
        ImageSequenceClip(txt_frames, fps=30)
        .set_duration(duration)
        .set_opacity(0.85)
    )

    final = CompositeVideoClip([bg, txt_clip]).set_audio(audio)
    final.write_videofile(
        output, fps=30, codec="libx264",
        audio_codec="aac", logger=None
    )
    print(f"Video saved: {output}")
    return output
