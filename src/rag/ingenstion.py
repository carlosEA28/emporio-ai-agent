import logging
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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

def split_documents(documents, chunks_size = 1000, chunks_overlap=200):
    """Split the documents into chuncks"""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunks_size,
        chunk_overlap=chunks_overlap,
        length_function=len,
        separators=["\n\n","\n", " ", ""]

    )

    splitted_docs =splitter.split_documents(documents)

    return splitted_docs
