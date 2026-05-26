# =====================================================
# IMPORTS
# =====================================================

from langchain_community.vectorstores import FAISS

from langchain_openai import (

    OpenAIEmbeddings,

    ChatOpenAI
)

from langchain.retrievers.contextual_compression import (

    ContextualCompressionRetriever
)

from langchain.retrievers.document_compressors import (

    LLMChainExtractor
)

from langchain_core.documents import Document

# =====================================================
# DOCUMENTS
# =====================================================

docs = [

    Document(page_content="""
    The Grand Canyon is one of the most visited natural wonders.
    Photosynthesis converts sunlight into energy.
    Millions visit every year.
    """),

    Document(page_content="""
    Chlorophyll captures sunlight during photosynthesis.
    Medieval castles were defensive structures.
    """)
]

# =====================================================
# VECTOR STORE
# =====================================================

embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(

    docs,

    embedding_model
)

# =====================================================
# BASE RETRIEVER
# =====================================================

base_retriever = vectorstore.as_retriever(

    search_kwargs={"k":5}
)

# =====================================================
# LLM COMPRESSOR
# =====================================================

llm = ChatOpenAI(

    model="gpt-3.5-turbo"
)

compressor = LLMChainExtractor.from_llm(llm)

# =====================================================
# COMPRESSION RETRIEVER
# =====================================================

compression_retriever = ContextualCompressionRetriever(

    base_retriever=base_retriever,

    base_compressor=compressor
)

# =====================================================
# USER QUERY
# =====================================================

query = "What is photosynthesis?"

# =====================================================
# RETRIEVE COMPRESSED RESULTS
# =====================================================

compressed_results = compression_retriever.invoke(query)

# =====================================================
# OUTPUT
# =====================================================

for i, doc in enumerate(compressed_results):

    print(f"\n--- Result {i+1} ---")

    print(doc.page_content)