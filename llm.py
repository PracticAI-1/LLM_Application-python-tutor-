import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL = "openai/gpt-oss-120b"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def history(messages):
    # 1 system prompt + 5 conversations (user + assistant) = 11 messages
    if len(messages) > 11:
        messages.pop(1)  # remove oldest user message
        messages.pop(1)  # remove oldest assistant message


def get_stream(messages):
    """Send the whole conversation to Groq and return the streaming response."""
    return client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        max_completion_tokens=1000,
        stream=True,
    )
