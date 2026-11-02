from langchain_core.documents import Document

from rag.vector_store import get_vector_store


from langchain_core.documents import Document



def retrieve(query: str, top_k: int = 3) -> list[Document]:
    """Retrieve relevant policy documents from ChromaDB."""

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    if top_k < 1:
        raise ValueError("top_k must be greater than zero.")

    vector_store = get_vector_store()

    documents = vector_store.similarity_search(
        query=query.strip(),
        k=top_k
    )

    return [
        document
        for document in documents
        if document.page_content.strip()
    ]
