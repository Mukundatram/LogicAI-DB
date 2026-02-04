from app.agent.planner_agent import create_planner_agent
from app.agent.executor_agent import create_executor_agent


def run_dual_agent(user_question: str):
    planner = create_planner_agent()
    executor = create_executor_agent()

    # 1. Planning
    plan_text = planner(user_question)

    # 2. Execution
    execution_prompt = f"""
Use the following SQL plan to generate and execute SQL.

{plan_text}
"""

    result_response = executor.invoke({
        "messages": [{"role": "user", "content": execution_prompt}]
    })

    rows = None
    summary = None

    for msg in result_response["messages"]:
        if msg.type == "tool":
            rows = msg.content          # STRING result from DB
        elif msg.type == "ai":
            summary = msg.content

    return {
        "plan": plan_text,
        "rows": rows,
        "summary": summary,
    }
