from langchain_core.messages import HumanMessage
from app.agent.graph import app
from .agent.plan_execute_graph import app_planner

config = {"configurable": {"thread_id": "1"}}

# result1 = app.invoke({"messages": [HumanMessage(content="what is 2 + 2")]}, config=config)

# result2 = app.invoke(
#     {"messages": [HumanMessage(content="what was my previous question?")]},
#     config=config
# )

# result = app.invoke(
#     {"messages": [HumanMessage(content="query the database for users")]},
#     config=config
# )

# print(app.checkpointer)


result = app_planner.invoke(
    {"input": "Research the impact of AI on software engineering jobs and summarize the findings", "past_steps": [], "plan": [], "response": ""},
    config=config
)


print(result['response'])