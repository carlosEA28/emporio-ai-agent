from rag.ingenstion import ingest, processPdf, split_documents


def main():


    res = ingest("./data/pdf")



    print(res)


if __name__ == "__main__":
    main()
