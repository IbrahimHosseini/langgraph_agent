from langchain_core.messages import HumanMessage
from app.agent.graph import app

config = {"configurable": {"thread_id": "1"}}

result1 = app.invoke({"messages": [HumanMessage(content="what is 2 + 2")]}, config=config)
print("First:", result1["messages"][-1].content)

result2 = app.invoke(
    {"messages": [HumanMessage(content="what was my previous question?")]},
    config=config
)
print("Second:", result2["messages"][-1].content)
print(app.checkpointer)