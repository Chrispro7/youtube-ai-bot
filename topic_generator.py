import anthropic
import os

def get_topic(niche: str) -> str:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""Generate ONE punchy, clickable YouTube Shorts topic about: {niche}
Rules:
- Under 60 characters
- Creates curiosity or surprise
- No hashtags, no emojis
- Just the title, nothing else
Examples: "Why Your Phone Battery Degrades So Fast"
          "The Hidden Trick in Every ATM" """

    msg = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=80,
        messages=[{"role": "user", "content": prompt}]
    )
    return msg.content[0].text.strip
