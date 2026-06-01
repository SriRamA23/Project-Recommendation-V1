# test_pdf.py

from modules.pdf_parser import extract_text_from_pdf

with open("resume.pdf", "rb") as file:

    text = extract_text_from_pdf(file)

    print(text)