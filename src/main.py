from rag.ingenstion import processPdf


def main():
    docs = processPdf("./data/pdf")

    print(docs)


if __name__ == "__main__":
    main()
