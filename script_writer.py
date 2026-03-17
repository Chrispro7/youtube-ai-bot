import os
import requests

def write_script(topic):
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": "Write a YouTube Shorts voiceover script for: " + topic + ". Plain spoken text only. 90-120 words. Conversational and engaging. Start directly with a hook."
            }
        ],
        "max_tokens": 400
    }

    r = requests.post(url, json=body, headers=headers)
    data = r.json()
    print("Groq script response: " + str(data))

    if "choices" not in data:
        error = data.get("error", {}).get("message", "Unknown error")
        raise Exception("Groq API error: " + error)

    return data["choices"][0]["message"]["content"].strip()
