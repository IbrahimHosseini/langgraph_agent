
from config import settings
from .tools import tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode

from app.agent.state import AgentState

llm = ChatOpenAI(temperature=0, api_key=settings.OPENAI_API_KEY).bind_tools(tools=tools)
tool_node = ToolNode(tools=tools, handle_tool_errors=True)

def agent_node(state: AgentState):
    result = llm.invoke(state["messages"])
    
    return {"messages": [result]}

def should_continue(state: AgentState):
    last_message = state["messages"][-1]
    
    if last_message.tool_calls:
        return "continue"
    return "end"