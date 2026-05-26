# =====================================================
# IMPORTS
# =====================================================

from langchain.text_splitter import (

    RecursiveCharacterTextSplitter
)

# =====================================================
# SAMPLE TRANSCRIPT
# =====================================================

transcript = """

Nuclear fusion is the process where
two atomic nuclei combine to release energy.

"""

# =====================================================
# SPLITTER
# =====================================================

splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=200
)

# =====================================================
# CREATE CHUNKS
# =====================================================

chunks = splitter.create_documents(

    [transcript]
)

# =====================================================
# OUTPUT
# =====================================================

print(chunks[0].page_content)