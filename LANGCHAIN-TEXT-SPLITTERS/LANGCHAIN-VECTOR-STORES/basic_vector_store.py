from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv

load_dotenv()

# =====================================================
# SAMPLE DOCUMENTS
# =====================================================

documents = [

    "Virat Kohli plays cricket",

    "Messi plays football",

    "NVIDIA builds GPUs"
]

# =====================================================
# EMBEDDING MODEL
# =====================================================

embedding_model = OpenAIEmbeddings()

# =====================================================
# VECTOR STORE
# =====================================================

vector_db = Chroma.from_texts(

    documents,

    embedding_model
)

print(vector_db)