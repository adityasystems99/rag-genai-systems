# =====================================================
# IMPORTS
# =====================================================

from langchain_core.runnables import (

    RunnableParallel,

    RunnablePassthrough,

    RunnableLambda
)

from langchain_core.output_parsers import (

    StrOutputParser
)

# =====================================================
# FORMAT FUNCTION
# =====================================================

def format_docs(retrieved_docs):

    context_text = "\n\n".join(

        doc.page_content

        for doc in retrieved_docs
    )

    return context_text

# =====================================================
# PARALLEL CHAIN
# =====================================================

parallel_chain = RunnableParallel({

    "context":

        retriever

        | RunnableLambda(format_docs),

    "question":

        RunnablePassthrough()
})

# =====================================================
# OUTPUT PARSER
# =====================================================

parser = StrOutputParser()

# =====================================================
# MAIN RAG CHAIN
# =====================================================

main_chain = (

    parallel_chain

    | prompt

    | llm

    | parser
)

# =====================================================
# RUN PIPELINE
# =====================================================

result = main_chain.invoke(

    "Can you summarize the video?"
)

print(result)