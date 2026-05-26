# =====================================================
# WIKIPEDIA RETRIEVER
# =====================================================

from langchain_community.retrievers import WikipediaRetriever

# =====================================================
# CREATE RETRIEVER
# =====================================================

retriever = WikipediaRetriever(

    top_k_results=2,

    lang="en"
)

# =====================================================
# USER QUERY
# =====================================================

query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# =====================================================
# RETRIEVE DOCUMENTS
# =====================================================

docs = retriever.invoke(query)

# =====================================================
# DISPLAY RESULTS
# =====================================================

for i, doc in enumerate(docs):

    print(f"\n--- Result {i+1} ---")

    print(doc.page_content[:1000])