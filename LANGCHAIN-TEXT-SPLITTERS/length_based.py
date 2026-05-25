from langchain.text_splitter import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

# LOAD PDF

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

# CHARACTER SPLITTER

splitter = CharacterTextSplitter(

    chunk_size=200,

    chunk_overlap=0,

    separator=''
)

# SPLIT DOCUMENTS

result = splitter.split_documents(docs)

# OUTPUT

print(result[1].page_content)