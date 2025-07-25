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

def get_response_from_ai_agent(llm_id, query, allow_search, provider, system_prompt=""):
    """
    Function to get response from AI agent with specified model and search capability
    Args:
        llm_id (str): Model name/ID
        query (str): User's question
        allow_search (bool): Whether to enable web search
        provider (str): "Groq" or "OpenAI"
        system_prompt (str): Custom system prompt from user
    
    Returns:
        list: List of AI response messages
    """  
    # Build the full system prompt
    full_system_prompt = f"""
    You are a helpful fashion AI assistant. 
    
    IMPORTANT: If the user has provided specific instructions about your personality, expertise, or tone below, follow them exactly:
    
    {system_prompt if system_prompt.strip() else "Be a friendly, knowledgeable fashion advisor."}
    
    Now respond to the user's fashion question with the personality and expertise specified above.
    """
    
    # Fix provider logic
    if provider.lower() == "groq":
        llm = ChatGroq(model=llm_id)
    elif provider.lower() == "openai":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    tools = [TavilySearch(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model=llm,
        tools=tools
    )
    
    # Use the full_system_prompt here!
    state_messages = {
        "messages": [
            SystemMessage(content=full_system_prompt),  # ← Use the custom prompt!
            HumanMessage(content=query)
        ]
    }
        
    response = agent.invoke(state_messages)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    
    return ai_messages
