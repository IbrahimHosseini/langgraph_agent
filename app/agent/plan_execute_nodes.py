from .state import PlanExecuteState
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from config import settings
from .state import PlanExecuteState
from pydantic import BaseModel

def should_continue_plan(plan_state: PlanExecuteState):
    plan_count = len(plan_state["plan"]) 

    if plan_count > 0:
        return "continue"
    return "end"

class Plan(BaseModel):
    steps: list[str]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=settings.OPENAI_API_KEY)

def planner_node(state: PlanExecuteState):
    llm_with_output = llm.with_structured_output(Plan, method="function_calling")
    result = llm_with_output.invoke([
        HumanMessage(content=f"Break down this task into small steps: {state['input']}")
    ])

    return {"plan": result.steps}

def executor_node(state: PlanExecuteState):
    current_step = state['plan'][0]
    
    result = llm.invoke([
        HumanMessage(content=f"Execute this step: {current_step}")
    ])

    return {
        "plan": state['plan'][1:],
        "past_steps": state['past_steps'] + [f"{current_step}: {result.content}"]
    }

def responder_node(state: PlanExecuteState):
    past_steps = state["past_steps"]

    result = llm.invoke([
        HumanMessage(content=f"""You are a research assistant. Based on the following completed research steps and their findings, write a comprehensive summary. 
        Completed steps:{past_steps}
        Write a clear, well-structured summary of the key findings.""")
    ])

    return {
        "response": result.content
    }
