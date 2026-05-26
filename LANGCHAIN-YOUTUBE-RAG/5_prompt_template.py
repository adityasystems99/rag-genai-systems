# =====================================================
# IMPORTS
# =====================================================

from langchain_core.prompts import PromptTemplate

# =====================================================
# PROMPT TEMPLATE
# =====================================================

prompt = PromptTemplate(

    template="""
    You are a helpful assistant.

    Answer ONLY from the provided transcript context.

    If context is insufficient,
    say you don't know.

    Context:
    {context}

    Question:
    {question}
    """,

    input_variables=[

        "context",

        "question"
    ]
)

print(prompt)