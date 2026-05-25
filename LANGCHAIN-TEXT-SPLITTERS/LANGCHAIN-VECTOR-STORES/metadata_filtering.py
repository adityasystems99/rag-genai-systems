from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv

load_dotenv()

# =====================================================
# DOCUMENTS
# =====================================================

documents = [

    "Inception is directed by Nolan",

    "3 Idiots stars Aamir Khan",

    "Interstellar is science fiction"
]

# =====================================================
# METADATA
# =====================================================

metadata = [

    {"genre":"sci-fi"},

    {"genre":"comedy"},

    {"genre":"sci-fi"}
]

# =====================================================
# VECTOR STORE
# =====================================================

vector_db = Chroma.from_texts(

    documents,

    OpenAIEmbeddings(),

    metadatas=metadata
)

# =====================================================
# FILTERED SEARCH
# =====================================================

results = vector_db.similarity_search(

    "space movie",

    k=2,

    filter={"genre":"sci-fi"}
)

# =====================================================
# OUTPUT
# =====================================================

for doc in results:

    print(doc.page_content)