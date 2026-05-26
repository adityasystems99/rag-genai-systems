# =====================================================
# IMPORTS
# =====================================================

from langchain_openai import ChatOpenAI

# =====================================================
# LLM
# =====================================================

llm = ChatOpenAI(

    model="gpt-4o-mini",

    temperature=0.2
)

# =====================================================
# USER QUESTION
# =====================================================

question = """

Is nuclear fusion discussed in this video?
"""

# =====================================================
# RETRIEVE DOCUMENTS
# =====================================================

retrieved_docs = retriever.invoke(question)

# =====================================================
# FORMAT CONTEXT
# =====================================================

context_text = "\n\n".join(

    doc.page_content

    for doc in retrieved_docs
)

# =====================================================
# CREATE FINAL PROMPT
# =====================================================

final_prompt = prompt.invoke({

    "context": context_text,

    "question": question
})

# =====================================================
# GENERATE ANSWER
# =====================================================

answer = llm.invoke(final_prompt)

print(answer.content)