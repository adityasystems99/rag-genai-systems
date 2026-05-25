from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv

load_dotenv()

documents = [

    "Virat Kohli plays cricket",

    "Messi plays football",

    "NVIDIA builds GPUs"
]

vector_db = Chroma.from_texts(

    documents,

    OpenAIEmbeddings()
)

# =====================================================
# CREATE RETRIEVER
# =====================================================

retriever = vector_db.as_retriever(

    search_kwargs={"k":2}
)

# =====================================================
# RETRIEVE DOCUMENTS
# =====================================================

results = retriever.invoke(

    "Tell me about sports"
)

for doc in results:

    print(doc.page_content)