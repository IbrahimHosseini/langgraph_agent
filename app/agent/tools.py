from langchain_core.tools import tool

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


tools = [search_tool, calculator_tool, db_query_tool]