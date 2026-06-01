# modules/gap_analyzer.py

import pandas as pd


def get_required_skills(target_role):
    """
    Get required skills for a selected role.
    """

    roles_df = pd.read_csv("data/roles.csv")

    role_row = roles_df[
        roles_df["role"].str.lower() == target_role.lower()
    ]

    if role_row.empty:
        return []

    required_skills = role_row.iloc[0]["required_skills"]

    return [
        skill.strip().lower()
        for skill in required_skills.split(",")
    ]


def find_skill_gaps(user_skills, target_role):
    """
    Compare user skills against role requirements.
    """

    required_skills = get_required_skills(target_role)

    missing_skills = list(
        set(required_skills) - set(user_skills)
    )

    return {
        "required_skills": sorted(required_skills),
        "missing_skills": sorted(missing_skills)
    }