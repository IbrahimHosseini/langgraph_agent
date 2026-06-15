
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode

from app.agent.state import AgentState

tools = [search_tool, calculator_tool, db_query_tool]

def agent_node(state: AgentState):
    llm = ChatOpenAI(temperature=0)
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

@tool
def search_tool(input: str) -> str:
    """Search the web for information about a given topic."""
    return f"nothing to see here {input}"

@tool
def calculator_tool(expression: str) -> int:
    """Calculate the result of a given mathematical expression."""
    return f"nothing to see here {expression}"

@tool
def db_query_tool(query: str) -> str:
    """Query the database for information about a given topic."""
    return f"nothing to see here {query}"