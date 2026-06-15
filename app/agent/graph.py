from langgraph.graph import END, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from app.agent.nodes import agent_node, should_continue, tool_node
from app.agent.state import AgentState

graph = StateGraph(AgentState)

graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)

graph.set_entry_point("agent")
graph.add_edge("tools", "agent")

graph.add_conditional_edges(
    "agent",
    should_continue,
    {"continue": "tools", "end": END}
)

checkpointer = MemorySaver()

app = graph.compile(checkpointer=checkpointer)