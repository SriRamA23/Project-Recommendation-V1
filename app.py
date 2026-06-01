import streamlit as st

from modules.pdf_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.gap_analyzer import find_skill_gaps
from modules.recommender import recommend_projects
from modules.scorer import (
    calculate_resume_score,
    projected_score
)
from modules.roadmap_generator import generate_roadmap


st.set_page_config(
    page_title="CareerIQ",
    page_icon="🎯",
    layout="wide"
)

st.title("CareerIQ")
st.subheader("Resume-to-Project Recommendation Engine")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

target_role = st.selectbox(
    "Select Target Role",
    [
        "Data Analyst",
        "Data Scientist",
        "ML Engineer",
        "Software Engineer",
        "Full Stack Developer"
    ]
)

if uploaded_file is not None:

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            # Extract text
            resume_text = extract_text_from_pdf(
                uploaded_file
            )

            # Extract skills
            user_skills = extract_skills(
                resume_text
            )

            # Gap Analysis
            gap_result = find_skill_gaps(
                user_skills,
                target_role
            )

            # Recommendations
            recommendations = recommend_projects(
                user_skills,
                gap_result["missing_skills"]
            )

            # Scores
            current_score = calculate_resume_score(
                user_skills,
                gap_result["required_skills"]
            )

            future_score = projected_score(
                current_score,
                recommendations
            )

            # Roadmap
            roadmap = generate_roadmap(
                gap_result["missing_skills"],
                recommendations,
                target_role
            )

        st.success("Analysis Complete")

        # Skills
        st.header("Detected Skills")

        if user_skills:
            for skill in user_skills:
                st.write("✅", skill.title())
        else:
            st.warning("No skills detected")

        # Missing Skills
        st.header("Missing Skills")

        if gap_result["missing_skills"]:
            for skill in gap_result["missing_skills"]:
                st.write("❌", skill.title())
        else:
            st.success("No skill gaps found")

        # Scores
        st.header("Resume Score")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Current Score",
                f"{current_score}%"
            )

        with col2:
            st.metric(
                "Projected Score",
                f"{future_score}%"
            )

        # Recommendations
        st.header("Recommended Projects")

        for project in recommendations:

            with st.expander(
                project["project_name"]
            ):

                st.write(
                    f"Difficulty: {project['difficulty']}"
                )

                st.write(
                    f"Impact Score: {project['impact_score']}"
                )

                st.write(
                    f"Skills Used: {project['skills_used']}"
                )

                st.write(
                    f"Recommendation Score: {project['recommendation_score']}"
                )

        # Roadmap
        st.header("Learning Roadmap")

        for index, step in enumerate(
            roadmap,
            start=1
        ):
            st.write(
                f"{index}. {step}"
            )