#How text becomes vectors

# IMPORTS

from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

# EMBEDDING MODEL

embedding_model = OpenAIEmbeddings(

    model="text-embedding-3-small"
)

# TEXT

text = "Virat Kohli is a famous Indian cricketer"

# CREATE VECTOR

vector = embedding_model.embed_query(text)

# OUTPUT

print(type(vector))

print(len(vector))

print(vector[:10])