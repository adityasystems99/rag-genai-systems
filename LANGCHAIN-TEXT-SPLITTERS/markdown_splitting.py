from langchain.text_splitter import (

    RecursiveCharacterTextSplitter,

    Language
)

text = """
# Project Name: Smart Student Tracker

## Features

- Add students
- View details

## Tech Stack

- Python
- No dependencies
"""

# MARKDOWN SPLITTER

splitter = RecursiveCharacterTextSplitter.from_language(

    language=Language.MARKDOWN,

    chunk_size=200,

    chunk_overlap=0
)

# SPLIT TEXT

chunks = splitter.split_text(text)

# OUTPUT


print(len(chunks))

print(chunks[0])