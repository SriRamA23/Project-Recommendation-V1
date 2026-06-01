# modules/recommender.py

import pandas as pd


def recommend_projects(user_skills, missing_skills, top_n=5):

    projects_df = pd.read_csv("data/projects.csv")

    recommendations = []

    for _, row in projects_df.iterrows():

        project_skills = [
            skill.strip().lower()
            for skill in row["skills_used"].split(",")
        ]

        matching_skills = len(
            set(user_skills).intersection(project_skills)
        )

        gap_skills_covered = len(
            set(missing_skills).intersection(project_skills)
        )

        score = (
            matching_skills * 2
            +
            gap_skills_covered * 3
            +
            row["impact_score"]
        )

        recommendations.append({
            "project_name": row["project_name"],
            "skills_used": row["skills_used"],
            "difficulty": row["difficulty"],
            "impact_score": row["impact_score"],
            "matching_skills": matching_skills,
            "gap_skills_covered": gap_skills_covered,
            "recommendation_score": score
        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["recommendation_score"],
        reverse=True
    )

    return recommendations[:top_n]