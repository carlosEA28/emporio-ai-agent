import logging
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.vector_store import get_vector_store
import uuid


logger = logging.getLogger(__name__)

def processPdf(pdf_directory:str):
    """Processes all the PDF files in a directory"""

    all_docs = []
    pdf_dir = Path(pdf_directory)

    if not pdf_dir.is_dir():
        raise FileNotFoundError(f"Diretório de PDFs não encontrado: {pdf_dir}")

    pdf_files = list(pdf_dir.glob("**/*.pdf"))

    if not pdf_files:
        logger.warning("Nenhum PDF encontrado em: %s", pdf_dir)
        return []

    for pdf_file in pdf_files:

        try:
            loader = PyPDFLoader(str(pdf_file))
            documents = loader.load()


            for doc in documents:
                doc.page_content = " ".join(doc.page_content.split())

                doc.metadata['source'] = pdf_file.name
                doc.metadata['category'] = "Policy"
                doc.metadata['version'] = "2.1"
                doc.metadata['language'] = "PT-BR"
                doc.metadata["file_type"] = "pdf"
                doc.metadata["last_updated"] = "June-2025"


            all_docs.extend(documents)

        except Exception:
            logger.exception("Falha ao carregar o PDF: %s", pdf_file)
            raise

    return all_docs

def split_documents(documents):
    """Split the documents into chuncks"""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n","\n", " ", ""]

    )

    splitted_docs =splitter.split_documents(documents)

    return splitted_docs



def ingest(pdf_directory: str) -> int:
    """Load, split and index PDF documents into ChromaDB."""

    documents = processPdf(pdf_directory)

    if not documents:
        raise ValueError(
            f"No PDF documents were loaded from: {pdf_directory}"
        )

    chunks = split_documents(documents)

    if not chunks:
        raise ValueError("No chunks were generated from the PDF documents.")

    ids = [
        uuid.uuid5(
            uuid.NAMESPACE_URL,
            f"{doc.metadata.get('source')}:{doc.metadata.get('page')}:{i}:{doc.page_content}"
        ).hex
        for i, doc in enumerate(chunks)
    ]

    vector_store = get_vector_store()

    vector_store.add_documents(
        documents=chunks,
        ids=ids
    )

    print(f"Successfully indexed {len(chunks)} chunks.")
    print(vector_store._collection.count())

    return len(chunks)
