#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("A friendly, Fashion AI")
st.write("What’s on your style radar?")

system_prompt=st.text_area("Who’s your style spirit today?", height=70, placeholder=(
        "e.g. ‘Channel a Tokyo streetwear maverick’, "
        "‘Speak as a Paris haute-couture icon’, "
        "‘Be my sustainable fashion guru’, "
        "‘Style me like a 1920s flapper star’…"
    ))

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Provider", ("Groq", "OpenAI"))

if provider.lower() == "groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider.lower() == "openai":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("🔎 Tap into live trend radar", value=True)

user_query=st.text_area("What’s your fashion dilemma today?", height=150, placeholder="Ask Us Anything!")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Style Me!"):
    if user_query.strip():
        #Step2: Connect with backend via URL
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "user_query": user_query,
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                # Grab just the last non‐empty string in the “response” list
                ai_text = next((r for r in reversed(response_data["response"]) if r.strip()), "")
                st.subheader("Fashion AI Response")
                st.markdown(ai_text)
        else:
            st.error(f"Request failed ({response.status_code}):\n{response.text}")
    