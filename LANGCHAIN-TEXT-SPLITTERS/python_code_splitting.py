from langchain.text_splitter import (

    RecursiveCharacterTextSplitter,

    Language
)

text = """
class Student:

    def __init__(self,name):

        self.name = name

    def get_name(self):

        return self.name
"""


# PYTHON SPLITTER

splitter = RecursiveCharacterTextSplitter.from_language(

    language=Language.PYTHON,

    chunk_size=300,

    chunk_overlap=0
)

# SPLIT CODE

chunks = splitter.split_text(text)

# OUTPUT

print(len(chunks))

print(chunks[0])