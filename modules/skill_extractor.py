# modules/skill_extractor.py

SKILLS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "pandas",
    "numpy",
    "machine learning",
    "deep learning",
    "statistics",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "java",
    "c++",
    "c",
    "javascript",
    "html",
    "css",
    "react",
    "nodejs",
    "docker",
    "aws",
    "git",
    "github",
    "mongodb",
    "mysql",
    "sqlite",
    "flask",
    "streamlit"
]


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))