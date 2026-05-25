from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)

text = """
Space exploration has led to incredible scientific discoveries.

From landing on the Moon to exploring Mars,
humanity continues to push the boundaries.

These missions expanded our knowledge and
improved technologies like GPS and satellites.
"""

# RECURSIVE SPLITTER

splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=0
)

# SPLIT TEXT

chunks = splitter.split_text(text)

# OUTPUT

print(len(chunks))

print(chunks)