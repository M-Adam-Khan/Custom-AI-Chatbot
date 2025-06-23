from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name : str
    model_provider : str
    system_prompt: str
    messages : List[str]
    allow_search : bool

from fastapi import FastAPI, HTTPException
import traceback
from ai_agent import get_response

allowed_models = ["llama-3.3-70b-versatile","llama3-70b-8192", "gpt-4o-mini"]
app = FastAPI()

@app.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        if request.model_name not in allowed_models:
            return {"error": "Please select a valid AI Model!"}

        llm_id = request.model_name
        query = request.messages
        allow_search = request.allow_search
        system_prompt = request.system_prompt
        provider = request.model_provider

        response = get_response(llm_id, query, allow_search, system_prompt, provider)
        return {"response": response}

    except Exception as e:
        print("==== ERROR OCCURRED ====")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", port=5000, log_level="debug", reload=True)
