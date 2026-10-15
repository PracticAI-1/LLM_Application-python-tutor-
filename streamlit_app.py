import streamlit as st

from llm import get_stream, history
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="PyTutor", page_icon="🐍")
st.title("🐍 PyTutor")
st.caption("Your personal Python tutor. Ask anything about Python!")

# Conversation history starts with the system prompt and lives in the session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

messages = st.session_state.messages

with st.sidebar:
    st.header("Settings")
    if st.button("Clear chat"):
        del messages[1:]  # keep only the system prompt
        st.rerun()

# Show previous messages (skip the system prompt)
for message in messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Dynamic user prompt
user_input = st.chat_input("Ask a Python question...")

if user_input and user_input.strip():
    user_input = user_input.strip()

    messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    stream = get_stream(messages)

    full_response = ""

    # Stream the assistant's reply token by token
    with st.chat_message("assistant"):
        placeholder = st.empty()

        for chunk in stream:

            content = chunk.choices[0].delta.content

            if content:
                full_response += content
                placeholder.markdown(full_response + "▌")

        placeholder.markdown(full_response)

    messages.append({
        "role": "assistant",
        "content": full_response
    })

    # History: keep system prompt + last 5 conversations, delete older ones
    history(messages)
