from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

from langchain.schema.runnable import (

    RunnableSequence,

    RunnableParallel,

    RunnablePassthrough,

    RunnableBranch
)

load_dotenv()

# =====================================================
# REPORT PROMPT
# =====================================================

prompt1 = PromptTemplate(

    template='Write a detailed report on {topic}',

    input_variables=['topic']
)

# =====================================================
# SUMMARY PROMPT
# =====================================================

prompt2 = PromptTemplate(

    template='Summarize the following text \n {text}',

    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

# =====================================================
# REPORT GENERATION
# =====================================================

report_gen_chain = (

    prompt1
    | model
    | parser
)

# =====================================================
# CONDITIONAL ROUTING
# =====================================================

branch_chain = RunnableBranch(

    (
        lambda x: len(x.split()) > 300,

        prompt2
        | model
        | parser
    ),

    RunnablePassthrough()
)

# =====================================================
# FINAL CHAIN
# =====================================================

final_chain = RunnableSequence(

    report_gen_chain,

    branch_chain
)

print(

    final_chain.invoke({

        'topic':'Russia vs Ukraine'
    })
)