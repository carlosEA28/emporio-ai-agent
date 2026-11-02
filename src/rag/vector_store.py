from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def get_vector_store(
    collection_name: str = "store_policies",
    persist_directory: str = "./data/vector_store"
) -> Chroma:

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory=persist_directory
    )

    return vector_store
