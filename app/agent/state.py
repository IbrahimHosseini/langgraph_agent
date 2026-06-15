from typing import Annotated
from typing_extensions import TypedDict
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]