# from langchain_ollama import ChatOllama
from deepagents import create_deep_agent
from app.agent.prompts import EXECUTOR_RULES
from app.tools.mysql_tool import run_sql
from app.db.schema import load_schema
import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
def create_executor_agent():
    # llm = ChatOllama(
    #     model="qwen2.5-coder:3b",
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
{EXECUTOR_RULES}

Database schema:
{schema}
"""

    return create_deep_agent(
        model=llm,
        tools=[run_sql],
        system_prompt=system_prompt,
    )
