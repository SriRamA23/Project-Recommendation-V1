# modules/skill_extractor.py

import pandas as pd


def load_skills():
    """
    Load skills dynamically from skills.csv
    """

    skills_df = pd.read_csv(
        "data/skills.csv"
    )

    skills = (
        skills_df["skill"]
        .dropna()
        .str.lower()
        .tolist()
    )

    return skills


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    text = text.lower()

    skills = load_skills()

    found_skills = []

    for skill in skills:

        if skill in text:
            found_skills.append(skill)

    return sorted(
        list(set(found_skills))
    )