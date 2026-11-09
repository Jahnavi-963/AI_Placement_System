import streamlit as st

def recommend_career(skills):

    skills = [s.strip().lower() for s in skills]

    careers = []

    if "python" in skills:
        careers.append("🐍 Python Developer")

    if "machine learning" in skills or "ai" in skills:
        careers.append("🤖 AI Engineer")

    if "machine learning" in skills:
        careers.append("🧠 ML Engineer")

    if "sql" in skills:
        careers.append("📊 Data Analyst")

    if "data science" in skills:
        careers.append("📈 Data Scientist")

    if "git" in skills:
        careers.append("💻 Software Engineer")

    if len(careers) == 0:
        careers.append("🎯 Learn Python to unlock career recommendations")

    return careers


def career_page():

    st.header("🎯 AI Career Recommendation")

    skills = st.text_area(
        "Enter Your Skills",
        placeholder="Python, SQL, Machine Learning"
    )

    if st.button("Recommend Career"):

        if skills.strip() == "":
            st.warning("⚠ Please enter your skills first.")
            return

        user_skills = skills.split(",")

        careers = recommend_career(user_skills)
        st.session_state.careers = careers

        st.subheader("💼 Recommended Careers")

        for career in careers:
            st.success(career)