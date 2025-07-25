from dotenv import load_dotenv
load_dotenv()
# Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel

class RequestState(BaseModel):
    model_name:str
    model_provider: str
    system_prompt: str
    user_query: str
    allow_search: bool

# Setup AI Agent from FrontEnd Request 
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from ai_agent import get_response_from_ai_agent 
ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title = "LangGraph AI Agent")
@app.post("/chat")

def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise HTTPException(
            status_code=400, 
            detail="Invalid model name. Kindly select a valid AI model."
        )
       
    try:
       
        llm_id = request.model_name
        query = request.user_query
        allow_search = request.allow_search
        provider = request.model_provider  
        
        # Create AI Agent and get response from it
        response = get_response_from_ai_agent(llm_id, query, allow_search, provider)
        
        return {
            "status": "success",
            "model_used": llm_id,
            "provider": provider,
            "search_enabled": allow_search,
            "response": response
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, 
        detail=f"Error processing request: {str(e)}"
        )

@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "LangGraph AI Agent API is running!"}

@app.get("/models")
def get_allowed_models():
    """Get list of allowed models"""
    return {"allowed_models": ALLOWED_MODEL_NAMES}

# Run app and Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)