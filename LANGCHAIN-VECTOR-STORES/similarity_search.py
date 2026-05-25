from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv

load_dotenv()

# =====================================================
# DOCUMENTS
# =====================================================

documents = [

    "Virat Kohli plays cricket",

    "Messi plays football",

    "NVIDIA builds GPUs"
]

# =====================================================
# VECTOR STORE
# =====================================================

vector_db = Chroma.from_texts(

    documents,

    OpenAIEmbeddings()
)

# =====================================================
# SIMILARITY SEARCH
# =====================================================

results = vector_db.similarity_search(

    "Tell me about cricket",

    k=2
)

# =====================================================
# OUTPUT
# =====================================================

for doc in results:

    print(doc.page_content)