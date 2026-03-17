import os
import requests

def write_script(topic):
    api_key = os.getenv("GEMINI_API_KEY")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + api_key

    prompt = "Write a YouTube Shorts voiceover script for: " + topic + ". Plain spoken text only. 90-120 words. Conversational and engaging. Start directly with a hook."

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
    print("Gemini script response: " + str(data))

    if "candidates" not in data:
        error = data.get("error", {}).get("message", "Unknown error")
        raise Exception("Gemini API error: " + error)

    result = data["candidates"][0]["content"]["parts"][0]["text"]
    return result.strip()
