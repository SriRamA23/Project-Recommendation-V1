from modules.pdf_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.gap_analyzer import find_skill_gaps
from modules.recommender import recommend_projects
from modules.roadmap_generator import generate_roadmap

with open("resume.pdf", "rb") as file:

    text = extract_text_from_pdf(file)

user_skills = extract_skills(text)

target_role = "Data Analyst"

gap_result = find_skill_gaps(
    user_skills,
    target_role
)

recommendations = recommend_projects(
    user_skills,
    gap_result["missing_skills"]
)

roadmap = generate_roadmap(
    gap_result["missing_skills"],
    recommendations,
    target_role
)

print("\nCAREER ROADMAP\n")

for i, step in enumerate(roadmap, start=1):
    print(f"{i}. {step}")