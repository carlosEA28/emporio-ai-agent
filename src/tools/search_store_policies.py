from langchain.tools import tool

from rag.retriver import retrieve

@tool
def search_store_policies(query: str) -> str:
    """Search store policies about returns, exchanges, payments,
    warranties, opening hours, shipping and customer service.
    """

    documents = retrieve(query)

    if not documents:
        return "No relevant store policies were found."

    context = []

    for doc in documents:
        page = doc.metadata.get("page", 0) + 1
        content = doc.page_content

        context.append(
            f"Source: Store Policies - Page {page}\n"
            f"Content: {content}"
        )

    return "\n\n".join(context)
