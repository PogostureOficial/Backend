from fastapi import FastAPI
from pydantic import BaseModel
from openai_client import run_agent

app = FastAPI()

class MessageRequest(BaseModel):
    messages: list

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask_agent(req: MessageRequest):
    answer = run_agent(req.messages)
    return {"response": answer}
