from rag.ingenstion import ingest
from rag.retriver import retrieve


def main():


    documents = retrieve("Posso pagar em 12 vezes?")

    for doc in documents:
        print(f"Página: {doc.metadata.get('page', 0) + 1}")
        print(f"Conteúdo: {doc.page_content}")
        print("---")


if __name__ == "__main__":
    main()
