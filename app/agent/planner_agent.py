# from langchain_ollama import ChatOllama
from app.db.schema import load_schema
from app.agent.prompts import PLANNER_RULES
import os

from langchain_nvidia_ai_endpoints import ChatNVIDIA   

def create_planner_agent():
    # llm = ChatOllama(
    #     model="llama3",
    #     base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    #     temperature=0,
    # )
    llm = ChatNVIDIA(
            model="meta/llama-3.1-8b-instruct",
            api_key=None,          # reads from NVIDIA_API_KEY
            temperature=0,
            max_tokens=512,
        )
    schema = load_schema()

    system_prompt = f"""
{PLANNER_RULES}

Database schema:
{schema}
"""

    # IMPORTANT: return the raw model + prompt
    def planner_invoke(user_input: str):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ]
        response = llm.invoke(messages)
        return response.content

    return planner_invoke
