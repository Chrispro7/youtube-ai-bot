import os
import requests

def get_topic(niche: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    prompt = f"""Generate ONE punchy, clickable YouTube Shorts topic about: {niche}
Rules:
- Under 60 characters
- Creates curiosity or surprise
- No hashtags, no emojis
- Just the title, nothing else
Examples: "Why Your Phone Battery Degrades So Fast"
          "The Hidden Trick in Every ATM" """

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    r = requests.post(url, json=body)
    data = r.json()
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()
