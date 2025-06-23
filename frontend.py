import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="AI Agent", page_icon="🤖", layout="centered")

# Title and intro
st.title("🤖 Agentic AI Chatbot")
st.markdown("Create your own intelligent agent and chat with it in real-time. Designed for clarity, simplicity, and flexibility.")

# Sidebar for provider & model
with st.sidebar:
    st.header("⚙️ Configuration")
    provider = st.radio("Select Provider", ("Groq", "OpenAI"), index=0)

    GROQ_MODELS = ["llama3-70b-8192", "llama-3.3-70b-versatile"]
    OPENAI_MODELS = ["gpt-4o-mini"]

    if provider == "Groq":
        selected_model = st.selectbox("Groq Models", GROQ_MODELS)
    else:
        selected_model = st.selectbox("OpenAI Models", OPENAI_MODELS)

    allow_web_search = st.checkbox("🌐 Allow Web Search", value=False)

# Chat input section
st.markdown("### 🧠 System Prompt")
system_prompt = st.text_area("Define your agent's personality or behavior:", height=80, placeholder="E.g., You are a helpful assistant...")

st.markdown("### 💬 Ask a Question")
user_query = st.text_area("What would you like to ask?", height=150, placeholder="Ask anything...")

# Send button
submit_col, _ = st.columns([1, 5])
with submit_col:
    if st.button("🚀 Send Query", use_container_width=True):
        if not user_query.strip():
            st.warning("Please enter a query first.")
        else:
            # Prepare and send payload
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }

            try:
                response = requests.post("http://127.0.0.1:5000/chat", json=payload)
                if response.status_code == 200:
                    data = response.json()
                    if "response" in data:
                        st.markdown("### 🤖 AI Response")
                        st.success(data["response"])
                    else:
                        st.error(data.get("error", "Unknown error occurred."))
                else:
                    st.error(f"❌ Backend error {response.status_code}: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"🚫 Error connecting to backend: {e}")
