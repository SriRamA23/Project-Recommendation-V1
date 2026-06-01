from modules.pdf_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.gap_analyzer import find_skill_gaps
from modules.recommender import recommend_projects
from modules.scorer import (
    calculate_resume_score,
    projected_score
)

with open("resume.pdf", "rb") as file:

    text = extract_text_from_pdf(file)

user_skills = extract_skills(text)

gap_result = find_skill_gaps(
    user_skills,
    "Data Analyst"
)

recommendations = recommend_projects(
    user_skills,
    gap_result["missing_skills"]
)

current_score = calculate_resume_score(
    user_skills,
    gap_result["required_skills"]
)

future_score = projected_score(
    current_score,
    recommendations
)

print("\nCurrent Score:", current_score)

print("Future Score:", future_score)