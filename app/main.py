from langchain_core.messages import HumanMessage
from app.agent.graph import app

config = {"configurable": {"thread_id": "1"}}

# result1 = app.invoke({"messages": [HumanMessage(content="what is 2 + 2")]}, config=config)

# result2 = app.invoke(
#     {"messages": [HumanMessage(content="what was my previous question?")]},
#     config=config
# )

result = app.invoke(
    {"messages": [HumanMessage(content="query the database for users")]},
    config=config
)
print("Second:", result["messages"][-1].content)
print(app.checkpointer)