from typing import Annotated
from typing_extensions import TypedDict
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

class PlanExecuteState(TypedDict):
    input: str
    plan: list[str]
    past_steps: list[str]
    response: str