from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

from langchain.schema.runnable import (

    RunnableSequence,

    RunnableParallel,

    RunnablePassthrough
)

load_dotenv()

# JOKE PROMPT


prompt1 = PromptTemplate(

    template='Write a joke about {topic}',

    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

# EXPLANATION PROMPT

prompt2 = PromptTemplate(

    template='Explain the following joke - {text}',

    input_variables=['text']
)

# FIRST CHAIN

joke_gen_chain = RunnableSequence(

    prompt1,

    model,

    parser
)

# PARALLEL CONTEXT

parallel_chain = RunnableParallel({

    'joke': RunnablePassthrough(),

    'explanation': RunnableSequence(
        prompt2,
        model,
        parser
    )
})

# FINAL CHAIN

final_chain = RunnableSequence(

    joke_gen_chain,

    parallel_chain
)

print(

    final_chain.invoke({

        'topic':'cricket'
    })
)