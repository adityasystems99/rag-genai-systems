from langchain_openai import ChatOpenAI

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma

from langchain.chains import RetrievalQA

from dotenv import load_dotenv

load_dotenv()

# =====================================================
# DOCUMENTS
# =====================================================

documents = [

    "Virat Kohli is an Indian cricketer",

    "Messi is a football player",

    "NVIDIA develops GPUs"
]

# =====================================================
# VECTOR DB
# =====================================================

vector_db = Chroma.from_texts(

    documents,

    OpenAIEmbeddings()
)

# =====================================================
# RETRIEVER
# =====================================================

retriever = vector_db.as_retriever()

# =====================================================
# LLM
# =====================================================

llm = ChatOpenAI()

# =====================================================
# RAG CHAIN
# =====================================================

qa_chain = RetrievalQA.from_chain_type(

    llm=llm,

    retriever=retriever
)

# =====================================================
# QUERY
# =====================================================

result = qa_chain.invoke({

    "query":"Who develops GPUs?"
})

print(result["result"])