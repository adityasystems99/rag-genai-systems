from langchain_experimental.text_splitter import (
    SemanticChunker
)

from langchain_openai.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

#SEMANTIC SPLITTER

text_splitter = SemanticChunker(

    OpenAIEmbeddings(),

    breakpoint_threshold_type="standard_deviation",

    breakpoint_threshold_amount=3
)

sample = """
Farmers were working hard in the fields.

IPL is the biggest cricket league.

Terrorism is a danger to peace and safety.
"""

# CREATE DOCUMENTS

docs = text_splitter.create_documents([sample])

#OUTPUT

print(len(docs))

print(docs)