from langchain_text_splitters import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader

def get_content_and_chunks(pdf_docs):
    content = " "
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            content += page.extract_text()
    text_split = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100
        )
    chunks = text_split.split_text(content)
    return chunks
