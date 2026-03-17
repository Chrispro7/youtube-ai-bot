import os
from topic_generator import get_topic
from script_writer import write_script
from tts_engine import generate_voiceover
from video_builder import build_video
from uploader import upload_to_youtube

def main():
    print("Starting YouTube AI Pipeline...")
    niche = os.getenv("CHANNEL_NICHE", "tech facts")
    topic = get_topic(niche)
    print(f"Topic: {topic}")
    script = write_script(topic)
    print(f"Script written ({len(script)} chars)")
    audio_path = generate_voiceover(script, voice="en-US-GuyNeural")
    print(f"Audio: {audio_path}")
    video_path = build_video(topic, script, audio_path)
    print(f"Video: {video_path}")
    result = upload_to_youtube(
        video_path=video_path,
        title=topic,
        description=script[:400] + "\n\n#Shorts #AI",
        tags=["shorts", "ai", niche],
        category="22"
    )
    print(f"Uploaded! ID: {result['id']}")

if __name__ == "__main__":
    main()
