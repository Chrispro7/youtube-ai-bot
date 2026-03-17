import os
import requests

def write_script(topic: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    prompt = f"""Write a YouTube Shorts voiceover script for: "{topic}"
Format: Plain spoken text only, no stage directions.
Length: 90-120 words (fits in ~45 seconds).
Style: Conversational, engaging, ends with a surprising fact.
No intro like "Hey guys", start directly with the hook."""

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    r = requests.post(url, json=body)
    data = r.json()
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()
