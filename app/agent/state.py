from typing import Annotated
from typing_extensions import TypedDict
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]