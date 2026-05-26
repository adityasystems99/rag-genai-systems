# =====================================================
# IMPORTS
# =====================================================

from langchain.retrievers.multi_query import MultiQueryRetriever

from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings

from langchain_openai import ChatOpenAI

from langchain_core.documents import Document

# =====================================================
# DOCUMENTS
# =====================================================

all_docs = [

    Document(
        page_content="Healthy food improves energy."
    ),

    Document(
        page_content="Exercise helps maintain balance."
    ),

    Document(
        page_content="Sleep helps recovery and health."
    )
]

# =====================================================
# VECTOR STORE
# =====================================================

vectorstore = FAISS.from_documents(

    documents=all_docs,

    embedding=OpenAIEmbeddings()
)

# =====================================================
# MULTIQUERY RETRIEVER
# =====================================================

multiquery_retriever = MultiQueryRetriever.from_llm(

    retriever=vectorstore.as_retriever(

        search_kwargs={"k":5}
    ),

    llm=ChatOpenAI(
        model="gpt-3.5-turbo"
    )
)

# =====================================================
# USER QUERY
# =====================================================

query = "How to improve energy levels and maintain balance?"

# =====================================================
# RETRIEVE
# =====================================================

results = multiquery_retriever.invoke(query)

# =====================================================
# OUTPUT
# =====================================================

for i, doc in enumerate(results):

    print(f"\n--- Result {i+1} ---")

    print(doc.page_content)