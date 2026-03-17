import anthropic
import os

def write_script(topic: str) -> str:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    msg = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=400,
        messages=[{
            "role": "user",
            "content": f"""Write a YouTube Shorts voiceover script for: "{topic}"
Format: Plain spoken text only, no stage directions.
Length: 90-120 words (fits in ~45 seconds).
Style: Conversational, engaging, ends with a surprising fact.
No intro like "Hey guys", start directly with the hook."""
        }]
    )
    return msg.content[0].text.strip
