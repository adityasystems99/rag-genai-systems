from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

# LOAD PDF

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()


# DOCUMENT SPLITTER

splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
)

# SPLIT DOCUMENT


chunks = splitter.split_documents(docs)

# OUTPUT

print(len(chunks))

print(chunks[0].page_content)