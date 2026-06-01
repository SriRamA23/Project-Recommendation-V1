# modules/scorer.py

def calculate_resume_score(
    user_skills,
    required_skills
):
    """
    Calculate resume readiness score.
    """

    if len(required_skills) == 0:
        return 0

    matched = len(
        set(user_skills).intersection(required_skills)
    )

    score = (
        matched / len(required_skills)
    ) * 100

    return round(score, 2)


def projected_score(
    current_score,
    recommended_projects
):
    """
    Estimate score after completing projects.
    """

    improvement = 0

    for project in recommended_projects:

        improvement += (
            project["gap_skills_covered"] * 4
        )

    future_score = min(
        current_score + improvement,
        100
    )

    return round(future_score, 2)