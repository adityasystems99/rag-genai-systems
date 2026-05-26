# =====================================================
# IMPORTS
# =====================================================

from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_openai import ChatOpenAI

from langchain.chains import RetrievalQA

from dotenv import load_dotenv

# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv()

# =====================================================
# LOAD PDF
# =====================================================

loader = PyPDFLoader(

    "sample.pdf"
)

documents = loader.load()

# =====================================================
# SPLIT DOCUMENTS
# =====================================================

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
)

chunks = text_splitter.split_documents(
    documents
)

# =====================================================
# EMBEDDING MODEL
# =====================================================

embedding_model = OpenAIEmbeddings(

    model="text-embedding-3-small"
)

# =====================================================
# CREATE VECTOR STORE
# =====================================================

vectorstore = FAISS.from_documents(

    chunks,

    embedding_model
)

# =====================================================
# CREATE RETRIEVER
# =====================================================

retriever = vectorstore.as_retriever(

    search_kwargs={
        "k":3
    }
)

# =====================================================
# LLM
# =====================================================

llm = ChatOpenAI(

    model="gpt-3.5-turbo",

    temperature=0
)

# =====================================================
# RETRIEVAL QA CHAIN
# =====================================================

qa_chain = RetrievalQA.from_chain_type(

    llm=llm,

    retriever=retriever,

    chain_type="stuff"
)

# =====================================================
# USER QUERY
# =====================================================

query = input("Ask Question From PDF: ")

# =====================================================
# EXECUTE RAG PIPELINE
# =====================================================

result = qa_chain.invoke({

    "query":query
})

# =====================================================
# PRINT RESULT
# =====================================================

print("\nANSWER:\n")

print(result["result"])