from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_AGENT_ID

client = OpenAI(api_key=OPENAI_API_KEY)

def run_agent(messages):
    response = client.responses.create(
        model="gpt-5",
        agent_id=OPENAI_AGENT_ID,
        input=messages
    )
    return response.output_text
