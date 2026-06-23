from langgraph.graph import END, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from app.agent.state import PlanExecuteState
from .plan_execute_nodes import should_continue_plan, planner_node, executor_node, responder_node

graph = StateGraph(PlanExecuteState)

graph.add_node("planner", planner_node)
graph.add_node("executor", executor_node)
graph.add_node("responder", responder_node)


graph.set_entry_point("planner")

graph.add_edge("planner", "executor")

graph.add_conditional_edges(
    "executor",
    should_continue_plan,
    {"continue": "executor", "end": "responder"}
)

checkpointer = MemorySaver()

app_planner = graph.compile(checkpointer=checkpointer)