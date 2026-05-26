# =========================================================
# IMPORTS
# =========================================================

from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage

from langchain_core.tools import tool

# =========================================================
# TOOL
# =========================================================

@tool
def multiply(a: int, b: int) -> int:
    """
    Multiplies two numbers
    """

    return a * b

# =========================================================
# MODEL
# =========================================================

llm = ChatOpenAI()

# =========================================================
# BIND TOOLS
# =========================================================

llm_with_tools = llm.bind_tools([multiply])

# =========================================================
# USER QUERY
# =========================================================

messages = [

    HumanMessage(

        "Can you multiply 3 with 1000?"
    )
]

# =========================================================
# MODEL INVOCATION
# =========================================================

result = llm_with_tools.invoke(messages)

print(result.tool_calls)