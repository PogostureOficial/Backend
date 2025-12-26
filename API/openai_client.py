from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

WORKFLOW_ID = os.getenv("OPENAI_WORKFLOW_ID")

def run_workflow(messages):
    """
    messages: lista de mensajes estilo:
    [
      { "role": "user", "content": "Hola" }
    ]
    """

    response = client.responses.create(
        workflow=WORKFLOW_ID,
        input=messages
    )

    return response.output_text
