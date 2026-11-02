from rag.ingenstion import processPdf, split_documents


def main():
    docs = processPdf("./data/pdf")
    chunks = split_documents(docs)

    print(chunks)


if __name__ == "__main__":
    main()
