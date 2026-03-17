import os
import requests

def get_topic(niche):
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "user",
                "content": "Generate ONE punchy YouTube Shorts topic about: " + niche + ". Under 60 characters. No hashtags. No emojis. Just the title only."
            }
        ],
        "max_tokens": 80
    }

    r = requests.post(url, json=body, headers=headers)
    data = r.json()
    print("Groq response: " + str(data))

    if "choices" not in data:
        error = data.get("error", {}).get("message", "Unknown error")
        raise Exception("Groq API error: " + error)

    return data["choices"][0]["message"]["content"].strip()
