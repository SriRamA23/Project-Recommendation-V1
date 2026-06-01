# modules/profile_builder.py

from modules.skill_extractor import extract_skills


def build_profile(resume_text):
    """
    Build a structured user profile from resume text.
    """

    profile = {
        "skills": extract_skills(resume_text),
        "education": [],
        "projects": [],
        "certifications": [],
        "experience": []
    }

    return profile