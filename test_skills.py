from modules.pdf_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills

with open("resume.pdf", "rb") as file:

    text = extract_text_from_pdf(file)

skills = extract_skills(text)

print("\nDetected Skills:\n")

for skill in skills:
    print(skill)