import pdfplumber
def extract_text_from_pdf(pdf_file):
    """
    Extract text from uploaded PDF file.

    Parameters:
        pdf_file : Uploaded PDF file object

    Returns:
        str : Extracted text
    """

    extracted_text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

        return extracted_text
    except Exception as e:

        print(f"PDF Extraction Error: {e}")

        return ""