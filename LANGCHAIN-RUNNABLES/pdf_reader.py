# =====================================================
# IMPORTS
# =====================================================

from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv()

# =====================================================
# LOAD PDF
# =====================================================

loader = PyPDFLoader(

    "sample.pdf"
)

# =====================================================
# READ PDF PAGES
# =====================================================

documents = loader.load()

# =====================================================
# PRINT BASIC INFO
# =====================================================

print("\nTOTAL PAGES:\n")

print(len(documents))

print("\nFIRST PAGE CONTENT:\n")

print(documents[0].page_content)

# =====================================================
# TEXT SPLITTER
# =====================================================

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
)

# =====================================================
# CREATE CHUNKS
# =====================================================

chunks = text_splitter.split_documents(
    documents
)

# =====================================================
# PRINT CHUNK INFO
# =====================================================

print("\nTOTAL CHUNKS:\n")

print(len(chunks))

print("\nFIRST CHUNK:\n")

print(chunks[0].page_content)