from fastapi import FastAPI
from pydantic import BaseModel
from openai_client import run_workflow

app = FastAPI()

class AskRequest(BaseModel):
    messages: list

@app.post("/ask")
def ask(req: AskRequest):
    answer = run_workflow(req.messages)
    return { "response": answer }
