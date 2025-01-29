import PyPDF2
from docx import Document

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

# Example usage:
# pdf_text = extract_text_from_pdf("your_document.pdf")
# docx_text = extract_text_from_docx("your_document.docx")
