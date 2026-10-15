import streamlit as st
from groq import Groq

MODEL = "openai/gpt-oss-120b"

# API key comes from .streamlit/secrets.toml locally, or the Secrets settings on Streamlit Cloud
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


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
