import os
import requests

def get_topic(niche):
    api_key = os.getenv("GEMINI_API_KEY")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + api_key

    prompt = "Generate ONE punchy YouTube Shorts topic about: " + niche + ". Under 60 characters. No hashtags. No emojis. Just the title only."

    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    r = requests.post(url, json=body)
    data = r.json()
    print("Gemini response: " + str(data))

    if "candidates" not in data:
        error = data.get("error", {}).get("message", "Unknown error")
        raise Exception("Gemini API error: " + error)

    result = data["candidates"][0]["content"]["parts"][0]["text"]
    return result.strip()
