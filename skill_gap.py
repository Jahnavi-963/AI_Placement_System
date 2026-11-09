import streamlit as st

REQUIRED_SKILLS = [
    "Python",
    "C++",
    "SQL",
    "DSA",
    "Machine Learning",
    "Git",
    "Communication",
    "Problem Solving"
]


def analyze_skills(user_skills):

    user = [x.strip().lower() for x in user_skills]

    missing = []

    for skill in REQUIRED_SKILLS:
        if skill.lower() not in user:
            missing.append(skill)

    score = int(((len(REQUIRED_SKILLS) - len(missing)) / len(REQUIRED_SKILLS)) * 100)

    return missing, score


def skill_gap_page():

    st.header("🧠 Skill Gap Analysis")

    skills = st.text_area(
        "Enter your skills (comma separated)",
        placeholder="Python, SQL, Machine Learning"
    )

    if st.button("Analyze Skills"):

        if skills.strip() == "":
            st.warning("⚠ Please enter your skills first.")
            return

        user_skills = skills.split(",")

        missing, score = analyze_skills(user_skills)
        st.session_state.skill_score = score
        st.session_state.missing_skills = missing

        st.metric("Placement Readiness", f"{score}%")
        st.progress(score / 100)

        if len(missing) == 0:
            st.success("🎉 Excellent! You have all required skills.")
        else:
            st.subheader("❌ Missing Skills")

            courses = {
                "Python": "Complete Python Course",
                "C++": "C++ Programming",
                "SQL": "SQL Basics",
                "DSA": "Data Structures & Algorithms",
                "Machine Learning": "Machine Learning Fundamentals",
                "Git": "Git & GitHub",
                "Communication": "Communication Skills",
                "Problem Solving": "Competitive Programming"
            }

            for skill in missing:
                st.write(f"• {skill} → {courses.get(skill, 'Learn this skill')}")