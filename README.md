# 🧠 LangGraph AI Fashion Agent

A smart and friendly fashion assistant built with **LangGraph**, powered by **Groq/OpenAI** models and real-time web search using **Tavily**. It lets you chat with a stylish AI persona, customize prompts, and get live fashion insights — all from an elegant frontend.

---

## 🌟 Features

- 🤖 **Multi-LLM Support**: Choose between Groq (LLaMA3, Mixtral) and OpenAI (GPT-4o-mini)
- 🧭 **Web Search Integration**: Enable Tavily to get real-time trends
- 🧵 **Customizable AI Persona**: Inject your own prompt to control the AI’s fashion tone
- 🧑‍💻 **FastAPI Backend**: For robust and scalable interaction handling
- 🧑‍🎨 **Streamlit UI**: A clean, simple frontend to ask anything — from outfit ideas to style dilemmas

---

## 🛠 Tech Stack

| Layer        | Tech                            |
|--------------|---------------------------------|
| LLM Backend  | Groq, OpenAI (via Langchain)    |
| Web Search   | Tavily                          |
| Agent Engine | LangGraph (ReAct agent)         |
| API Layer    | FastAPI                         |
| UI           | Streamlit                       |
| Env Mgmt     | Pipenv                          |

---

## 🚀 Setup Instructions

#### 1. Clone the Repo

```bash
git clone https://github.com/dhruhisheth/LangGraph-AI-Agent.git
cd LangGraph-AI-Agent
```

#### 2. Install Dependencies

```bash
pip install pipenv
pipenv install
pipenv shell
```

#### 3. Create Your `.env` File  
Never commit this file to GitHub. Use it locally only.
```bash
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```  
Make sure .env is listed in `.gitignore`.

---

## ▶️ Running the App  
#### Start FastAPI Backend
```bash
python backend.py
```
> Open `http://127.0.0.1:9999/docs` to view Swagger UI
### Run the Streamlit Frontend
```bash
streamlit run frontend.py
```
> App will launch in your browser at `http://localhost:8501`

---

## 💡 Sample Prompt Ideas    
_“Style me like a Tokyo streetwear rebel.”_  
_“Make me look like a 90s rom-com heroine.”_  
_“Suggest an outfit for a beach date in Malibu.”_  
_“What’s trending in Gen-Z streetwear this week?”_  

--

## 🧪 Example API Payload
```bash
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act like a Paris fashion week stylist.",
  "user_query": "What should I wear to a rooftop brunch?",
  "allow_search": true
}
```
