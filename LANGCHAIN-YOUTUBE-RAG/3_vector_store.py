# =====================================================
# IMPORTS
# =====================================================

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

# =====================================================
# EMBEDDING MODEL
# =====================================================

embedding_model = OpenAIEmbeddings()

# =====================================================
# VECTOR STORE
# =====================================================

vector_store = FAISS.from_documents(

    chunks,

    embedding_model
)

print(vector_store)