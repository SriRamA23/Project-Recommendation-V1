# modules/roadmap_generator.py

def generate_roadmap(
    missing_skills,
    recommended_projects,
    target_role
):
    """
    Generate learning roadmap.
    """

    roadmap = []

    # Learn missing skills first
    for skill in missing_skills:
        roadmap.append(
            f"Learn {skill.title()}"
        )

    # Build recommended projects
    for project in recommended_projects:
        roadmap.append(
            f"Build Project: {project['project_name']}"
        )

    # Final career step
    roadmap.append(
        f"Apply for {target_role} Internships/Jobs"
    )

    return roadmap