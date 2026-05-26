# =========================================================
# IMPORTS
# =========================================================

from langchain.agents import (

    initialize_agent,

    AgentType
)

from langchain_openai import ChatOpenAI

from tools.currency_tools import (

    get_conversion_factor,

    convert
)

# =========================================================
# MODEL
# =========================================================

llm = ChatOpenAI()

# =========================================================
# AGENT INITIALIZATION
# =========================================================

agent_executor = initialize_agent(

    tools=[

        get_conversion_factor,

        convert
    ],

    llm=llm,

    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,

    verbose=True
)

# =========================================================
# USER QUERY
# =========================================================

user_query = """

Convert 10 INR to USD
"""

# =========================================================
# AGENT EXECUTION
# =========================================================

response = agent_executor.invoke({

    "input": user_query
})

print(response)