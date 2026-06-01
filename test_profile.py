from modules.pdf_parser import extract_text_from_pdf
from modules.profile_builder import build_profile

with open("resume.pdf", "rb") as file:

    text = extract_text_from_pdf(file)

profile = build_profile(text)

print(profile)