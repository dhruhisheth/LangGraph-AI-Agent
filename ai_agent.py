# Setup API Keys for Groq and Tavily 
import os 
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPEN_API_KEY = os.environ.get("OPENAI_API_KEY")

# Setup LLM and Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 

def get_response_from_ai_agent (llm_id, query, allow_search, provider ):
    """
    Function to get response from AI agent with specified model and search capability
    Args:
        llm_id (str): Model name/ID
        query (str): User's question
        allow_search (bool): Whether to enable web search
        provider (str): "Groq" or "OpenAI"
    
    Returns:
        list: List of AI response messages
    """  
    if provider =="Groq" or "GROQ":
        llm=ChatGroq(model=llm_id)
    elif provider == "OpenAI" or "OPENAI":
        llm=ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Error")

    tools=[TavilySearch(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model = llm,
        tools = tools
    )

    state_messages = {
        "messages": [
            SystemMessage(content="Act as an AI chatbot who is smart and friendly"),
            HumanMessage(content=query)
        ]
    }
        
    response = agent.invoke(state_messages)
    messages=response.get("messages")
    ai_messages = [message.content for message in messages if isinstance (message, AIMessage)]
    
    return ai_messages
