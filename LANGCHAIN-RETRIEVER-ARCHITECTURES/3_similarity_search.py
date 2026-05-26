# =====================================================
# IMPORTS
# =====================================================

from langchain_community.vectorstores import Chroma

from langchain_openai import OpenAIEmbeddings

from langchain_core.documents import Document

# =====================================================
# DOCUMENTS
# =====================================================

documents = [

    Document(
        page_content="LangChain simplifies LLM development."
    ),

    Document(
        page_content="FAISS is useful for similarity search."
    ),

    Document(
        page_content="Embeddings map text into vectors."
    )
]

# =====================================================
# VECTOR STORE
# =====================================================

vectorstore = Chroma.from_documents(

    documents,

    OpenAIEmbeddings()
)

# =====================================================
# QUERY
# =====================================================

query = "What are embeddings?"

# =====================================================
# SIMILARITY SEARCH
# =====================================================

results = vectorstore.similarity_search(

    query,

    k=2
)

# =====================================================
# OUTPUT
# =====================================================

for i, doc in enumerate(results):

    print(f"\n--- Result {i+1} ---")

    print(doc.page_content)