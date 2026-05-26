from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

from langchain.schema.runnable import (

    RunnableSequence,

    RunnableLambda,

    RunnablePassthrough,

    RunnableParallel
)

load_dotenv()

# =====================================================
# CUSTOM FUNCTION
# =====================================================

def word_count(text):

    return len(text.split())

# =====================================================
# PROMPT
# =====================================================

prompt = PromptTemplate(

    template='Write a joke about {topic}',

    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

# =====================================================
# JOKE CHAIN
# =====================================================

joke_gen_chain = RunnableSequence(

    prompt,

    model,

    parser
)

# =====================================================
# PARALLEL CHAIN
# =====================================================

parallel_chain = RunnableParallel({

    'joke': RunnablePassthrough(),

    'word_count': RunnableLambda(
        word_count
    )
})

# =====================================================
# FINAL CHAIN
# =====================================================

final_chain = RunnableSequence(

    joke_gen_chain,

    parallel_chain
)

result = final_chain.invoke({

    'topic':'AI'
})

final_result = """

{}

word count - {}

""".format(

    result['joke'],

    result['word_count']
)

print(final_result)