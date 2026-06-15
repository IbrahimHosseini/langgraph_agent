
from config import settings
from .tools import tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode

from app.agent.state import AgentState

def agent_node(state: AgentState):
    llm = ChatOpenAI(temperature=0, api_key=settings.OPENAI_API_KEY)
    bind = llm.bind_tools(tools=tools)
    result = bind.invoke(state["messages"])

    return {"messages": [result]}
    
def tool_node(state: AgentState):
    return ToolNode(tools=tools).invoke(state)

def should_continue(state: AgentState):
    last_message = state["messages"][-1]
    
    if last_message.tool_calls:
        return "continue"
    return "end"