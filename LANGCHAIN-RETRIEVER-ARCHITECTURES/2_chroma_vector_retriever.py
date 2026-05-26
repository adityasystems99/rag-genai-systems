# =====================================================
# IMPORTS
# =====================================================

from langchain_community.vectorstores import Chroma

from langchain_openai import OpenAIEmbeddings

from langchain_core.documents import Document

# =====================================================
# SOURCE DOCUMENTS
# =====================================================

documents = [

    Document(
        page_content="LangChain helps developers build LLM applications easily."
    ),

    Document(
        page_content="Chroma is a vector database optimized for LLM-based search."
    ),

    Document(
        page_content="Embeddings convert text into high-dimensional vectors."
    ),

    Document(
        page_content="OpenAI provides powerful embedding models."
    ),
]

# =====================================================
# EMBEDDING MODEL
# =====================================================

embedding_model = OpenAIEmbeddings()

# =====================================================
# CREATE CHROMA VECTOR STORE
# =====================================================

vectorstore = Chroma.from_documents(

    documents=documents,

    embedding=embedding_model,

    collection_name="my_collection"
)

# =====================================================
# CREATE RETRIEVER
# =====================================================

retriever = vectorstore.as_retriever(

    search_kwargs={"k": 2}
)

# =====================================================
# USER QUERY
# =====================================================

query = "What is Chroma used for?"

# =====================================================
# RETRIEVE DOCUMENTS
# =====================================================

results = retriever.invoke(query)

# =====================================================
# OUTPUT
# =====================================================

for i, doc in enumerate(results):

    print(f"\n--- Result {i+1} ---")

    print(doc.page_content)