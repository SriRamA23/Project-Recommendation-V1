from modules.pdf_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.gap_analyzer import find_skill_gaps

with open("resume.pdf", "rb") as file:

    text = extract_text_from_pdf(file)

user_skills = extract_skills(text)

result = find_skill_gaps(
    user_skills,
    "Data Analyst"
)

print("\nUSER SKILLS:")
print(user_skills)

print("\nREQUIRED SKILLS:")
print(result["required_skills"])

print("\nMISSING SKILLS:")
print(result["missing_skills"])