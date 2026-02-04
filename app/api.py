from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.agent.dual_agent import run_dual_agent

app = FastAPI(title="Agentic SQL API")


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    plan: str
    rows: Optional[str]
    summary: Optional[str]


@app.post("/query", response_model=QueryResponse)
def query_db(req: QueryRequest):
    return run_dual_agent(req.question)
