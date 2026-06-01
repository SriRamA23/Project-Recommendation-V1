from modules.pdf_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.gap_analyzer import find_skill_gaps
from modules.recommender import recommend_projects

with open("resume.pdf", "rb") as file:

    text = extract_text_from_pdf(file)

user_skills = extract_skills(text)

result = find_skill_gaps(
    user_skills,
    "Data Analyst"
)

recommendations = recommend_projects(
    user_skills,
    result["missing_skills"]
)

print("\nTOP RECOMMENDATIONS\n")

for project in recommendations:

    print("-" * 50)

    print("Project:", project["project_name"])

    print("Difficulty:", project["difficulty"])

    print("Impact Score:", project["impact_score"])

    print("Matching Skills:",
          project["matching_skills"])

    print("Gap Skills Covered:",
          project["gap_skills_covered"])

    print("Recommendation Score:",
          project["recommendation_score"])