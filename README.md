# 🐍 PyTutor – Your First LLM Application

A simple Python tutor chatbot built with **Streamlit** and **Groq**.
It only answers Python questions, streams replies word by word, and remembers your recent conversation.

## Features

- 💬 **Streamlit chat UI** – clean chat interface with a "Clear chat" button
- ⚡ **Streaming responses** – answers appear token by token
- ✍️ **Dynamic user prompt** – ask anything through the chat box
- 🧠 **Conversation history** – remembers the last 5 conversations (older ones are removed)
- 🛡️ **Python-only tutor** – politely refuses non-Python questions

## Project Structure

```
├── streamlit_app.py  # Streamlit UI + chat loop
├── llm.py            # Groq client, streaming call, history trimming
├── prompts.py        # System prompt (PyTutor rules)
├── requirements.txt  # Dependencies
└── .streamlit/
    └── secrets.toml  # Your GROQ_API_KEY (not committed)
```

## How It Works

```
User ──► streamlit_app.py ──► llm.py ──► Groq API (openai/gpt-oss-120b)
            ▲                                   │
            └──────── streamed response ◄───────┘
```

1. `messages` starts with the system prompt from `prompts.py`.
2. Each user question is appended to `messages`.
3. The full `messages` list is sent to Groq with `stream=True`.
4. Chunks are shown live and joined into `full_response`.
5. The reply is appended to `messages`.
6. `history()` keeps the system prompt + last 5 conversations and deletes older ones.

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/PracticAI-1/LLM_Application-python-tutor-.git
cd LLM_Application-python-tutor-
```

### 2. Create a virtual environment with uv

```bash
# install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### 3. Add your Groq API key

Get a free key from [console.groq.com](https://console.groq.com/keys) and create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

The app reads it with `st.secrets["GROQ_API_KEY"]`. This file is in `.gitignore`, so your key is never pushed.

### 4. Run the app

```bash
streamlit run streamlit_app.py
```

Open http://localhost:8501 in your browser.

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **Create app**.
3. Select this repo, branch `main`, and main file `streamlit_app.py`.
4. In **Advanced settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
   (same format as your local `secrets.toml`)
5. Click **Deploy** 🚀

## Tech Stack

- [Streamlit](https://streamlit.io) – UI
- [Groq](https://groq.com) – fast LLM inference
- [uv](https://github.com/astral-sh/uv) – Python package manager
