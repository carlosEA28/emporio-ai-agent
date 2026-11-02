import os

from chromadb.api import ClientAPI
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv()

openai_key = os.environ.get("OPENAI_API_KEY", "")
parsedKey = SecretStr(openai_key)

def get_vector_store(
    collection_name: str = "store_policies",
    persist_directory: str = "./data/vector_store"
) -> Chroma:

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=parsedKey
    )

    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory=persist_directory
    )

    return vector_store
