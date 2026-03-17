import asyncio
import edge_tts

VOICES = [
    "en-US-GuyNeural",
    "en-US-JennyNeural",
    "en-GB-RyanNeural",
    "en-AU-WilliamNeural",
]

def generate_voiceover(text: str, voice: str = "en-US-GuyNeural") -> str:
    output = f"/tmp/voiceover_{hash(text) % 99999}.mp3"

    async def _generate():
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate="+8%",
            pitch="+0Hz"
        )
        await communicate.save(output)

    asyncio.run(_generate())
    return output
