# =========================================================
# IMPORTS
# =========================================================

import json

from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage

from tools.currency_tools import (

    get_conversion_factor,

    convert
)

# =========================================================
# MODEL
# =========================================================

llm = ChatOpenAI()

# =========================================================
# BIND TOOLS
# =========================================================

llm_with_tools = llm.bind_tools([

    get_conversion_factor,

    convert
])

# =========================================================
# USER QUERY
# =========================================================

messages = [

    HumanMessage(

        "Convert 10 INR to USD"
    )
]

# =========================================================
# INVOKE MODEL
# =========================================================

ai_message = llm_with_tools.invoke(messages)

# =========================================================
# MANUAL TOOL EXECUTION
# =========================================================

for tool_call in ai_message.tool_calls:

    if tool_call["name"] == "get_conversion_factor":

        tool_message1 = get_conversion_factor.invoke(tool_call)

        conversion_rate = json.loads(

            tool_message1.content

        )["conversion_rate"]

        messages.append(tool_message1)

    if tool_call["name"] == "convert":

        tool_call["args"]["conversion_rate"] = conversion_rate

        tool_message2 = convert.invoke(tool_call)

        messages.append(tool_message2)

print(messages)