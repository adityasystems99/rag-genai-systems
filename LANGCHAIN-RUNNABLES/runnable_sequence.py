from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

from langchain.schema.runnable import RunnableSequence

load_dotenv()

#PROMPT 1

prompt1 = PromptTemplate(

    template='Write a joke about {topic}',

    input_variables=['topic']
)

#MODEL

model = ChatOpenAI()

#PARSERS

parser = StrOutputParser()

# PROMPT 2

prompt2 = PromptTemplate(

    template='Explain the following joke - {text}',

    input_variables=['text']
)

# SEQUENTIAL CHAIN

chain = RunnableSequence(

    prompt1,

    model,

    parser,

    prompt2,

    model,

    parser
)

#EXECUTION

print(

    chain.invoke({

        'topic':'AI'
    })
)