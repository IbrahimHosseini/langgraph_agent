from langchain_core.messages import HumanMessage
from app.agent.graph import app

result = app.invoke({"messages": [HumanMessage(content="what is 2 + 2")]})
print(result)

