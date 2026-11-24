from fastapi import FastAPI
from pydantic import BaseModel

from chatBot import chatbot_response

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": chatbot_response(request.message)}
