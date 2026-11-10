import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import datetime
import os

from dotenv import load_dotenv

# ================= Modules =================
from auth import signup, login, forgot
from prediction import prediction_page
from dashboard import dashboard_page
from resume import extract_text, ats_score, suggestions
from interview import interview_page
from certificate import certificate_page
from eligibility import eligibility_page
from history import history_page
from feedback import feedback_page
from report import report_page
from profile import save_profile, load_profile
from skill_gap import skill_gap_page
from career import career_page

# ================= Page Config =================
st.set_page_config(
    page_title="AI Placement Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= Session State =================

if "login" not in st.session_state:
    st.session_state.login = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "attempt" not in st.session_state:
    st.session_state.attempt = 0

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "ats_score" not in st.session_state:
    st.session_state.ats_score = 0
    # =====================================================
# 🔐 AUTH SYSTEM
# =====================================================

if not st.session_state.login:

    st.title("🔐 AI Placement System Login")

    option = st.radio(
        "Choose Option",
        ["Login", "Signup", "Forgot Password"]
    )

    # ---------------- LOGIN ----------------
    if option == "Login":

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if login(username, password):

                st.session_state.login = True
                st.session_state.username = username

                st.success("Login Successful ✅")
                st.rerun()

            else:
                st.error("Invalid Username or Password ❌")

    # ---------------- SIGNUP ----------------
    elif option == "Signup":

        new_user = st.text_input("Create Username")
        new_pass = st.text_input("Create Password", type="password")

        if st.button("Create Account"):

            if signup(new_user, new_pass):
                st.success("Account Created Successfully ✅")

            else:
                st.error("Username Already Exists ❌")

    # ---------------- FORGOT PASSWORD ----------------
    elif option == "Forgot Password":

        user = st.text_input("Enter Username")

        if st.button("Get Password"):

            result = forgot(user)

            if result:
                st.info(f"Your Password is: {result}")

            else:
                st.error("User Not Found ❌")

    st.stop()
    # =====================================================
# 🤖 LOAD MODEL
# =====================================================

try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    st.error("❌ model.pkl file not found.")
    st.stop()

# =====================================================
# 📊 SAMPLE DATA
# =====================================================

df = pd.DataFrame({
    "Skills": [2, 4, 6, 8, 10],
    "Placement": [20, 35, 55, 80, 95],
    "CGPA": [5, 6, 7, 8, 9]
})

# =====================================================
# 💾 SAVE HISTORY FUNCTION
# =====================================================

def save_history(username, data, result):

    file = "history.csv"

    new_data = pd.DataFrame([[
        username,
        data[0],
        data[1],
        data[2],
        data[3],
        result,
        str(datetime.datetime.now())
    ]], columns=[
        "username",
        "cgpa",
        "skills",
        "aptitude",
        "projects",
        "result",
        "date"
    ])

    if os.path.exists(file):

        old = pd.read_csv(file)
        old = pd.concat([old, new_data], ignore_index=True)

    else:

        old = new_data

    old.to_csv(file, index=False)

# =====================================================
# 📌 SIDEBAR MENU
# =====================================================
st.sidebar.title("🎓  AI Placement Portal")

st.sidebar.success(
    f"👤 {st.session_state.username}"
)

st.sidebar.divider()
menu = st.sidebar.radio(
    "Navigation",
    [
    "🏠 Home",
    "👤 Student Profile",
    "📥 Student Input",
    "🎯 Prediction",
    "📊 Dashboard",
    "📄 Resume Analyzer",
    "🎤 Interview Bot",
    "💬 Interview Feedback",
    "📈 Skill Gap Analysis",
    "💼 Career Recommendation",
    "🏆 Certificate",
    "📜 Prediction History",
    "📑 Placement Report",
    "🏢 Company Eligibility"
]
)
# =====================================================
# 
# =====================================================

if menu == "🏠 Home":
    st.title("🎓 AI Placement Management System")

    st.caption("🚀 AI Powered Student Placement Portal")

    st.success(f"👋 Welcome, {st.session_state.username}")

    st.info(
    """
            This platform helps students prepare for placements using Artificial Intelligence.

             📌 Predict Placement Chances

            📌 Analyze Resume ATS Score

            📌 Practice AI Interviews

            📌 Improve Skills

              📌 Track Placement Readiness
                          """
)

    st.divider()
    # ===========================
    # Metrics
    # ===========================

    st.subheader("📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🎯 Placement Accuracy",
            value="85%",
            delta="+5%"
        )

    with col2:
        st.metric(
            label="🤖 ML Model",
            value="Random Forest"
        )

    with col3:
        st.metric(
            label="📄 ATS Score",
            value=st.session_state.get("ats_score", 0),
            delta="+2"
        )

    with col4:
        st.metric(
            label="🎤 Interviews",
            value=st.session_state.get("attempt", 0)
        )

    st.divider()

    # ===========================
    # Features
    # ===========================

    st.subheader("🚀 Platform Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info("🎯 Placement Prediction")

        st.info("📄 ATS Resume Analyzer")

        st.info("🎤 AI Interview Practice")

        st.info("📊 Performance Dashboard")

        st.info("📈 Skill Gap Analysis")

    with col2:

        st.info("💼 Career Recommendation")

        st.info("🏆 Certificate Generator")

        st.info("🏢 Company Eligibility Checker")

        st.info("📑 Placement Report")

        st.info("📜 Prediction History")

    st.divider()
            # =====================================
    # Placement Analytics
    # =====================================

    st.subheader("📊 Placement Analytics")

    left, right = st.columns([2, 1])

    with left:

        chart_data = pd.DataFrame({

            "Module": [
                "Prediction",
                "Resume",
                "Interview",
                "Skill Gap",
                "Report"
            ],

            "Completion": [
                90,
                st.session_state.get("ats_score", 0),
                st.session_state.get("score", 0),
                80,
                95
            ]

        })

        fig = px.bar(

            chart_data,

            x="Module",

            y="Completion",

            text="Completion",

            color="Completion",

            color_continuous_scale="blues"

        )

        fig.update_layout(

            height=420,

            xaxis_title="",

            yaxis_title="Completion (%)",

            title="Overall Performance"

        )

        st.plotly_chart(fig, width="stretch")

    with right:

        pie = pd.DataFrame({

            "Category": [
                "Ready",
                "Need Practice"
            ],

            "Value": [
                80,
                20
            ]

        })

        fig2 = px.pie(

            pie,

            values="Value",

            names="Category",

            hole=0.65,

            color_discrete_sequence=px.colors.qualitative.Set2

        )

        fig2.update_layout(

            height=420,

            title="Placement Readiness"

        )

        st.plotly_chart(fig2, width="stretch")

    st.divider()
            # =====================================
    # AI Tip of the Day
    # =====================================

    st.subheader("💡 AI Tip of the Day")

    st.info("""
📌 Improve one skill every day.

✔ Practice 2 DSA problems
✔ Improve your Resume
✔ Attend Mock Interviews
✔ Build one Project
✔ Update LinkedIn & GitHub regularly

Small daily improvements lead to big placement success.
""")

    st.divider()

    st.subheader("💡 Quote of the Day")

    st.info("""
                 Success doesn't come from what you do occasionally.

                It comes from what you do consistently.

                  🚀 Keep Learning • Keep Building • Keep Growing
                  """)

    st.caption(
        "© 2026 AI Placement Management System | Developed using Streamlit & Machine Learning"
    )
    
    # =====================================================
# 👤 STUDENT PROFILE
# =====================================================

elif menu == "👤 Student Profile":
    st.header("👤 Student Profile")

    profile = load_profile(st.session_state.username)

    if profile is not None:

        default_name = profile["name"]
        default_email = profile["email"]
        default_college = profile["college"]
        default_branch = profile["branch"]
        default_year = int(profile["year"])
        default_roll = profile["roll_no"]
        default_phone = profile["phone"]
        default_skills = profile["skills"]

    else:

        default_name = ""
        default_email = ""
        default_college = ""
        default_branch = ""
        default_year = 3
        default_roll = ""
        default_phone = ""
        default_skills = ""

    name = st.text_input("Full Name", default_name)
    email = st.text_input("Email", default_email)
    college = st.text_input("College", default_college)
    branch = st.text_input("Branch", default_branch)

    year = st.selectbox(
        "Year",
        [1, 2, 3, 4],
        index=max(0, default_year - 1)
    )

    roll = st.text_input("Roll Number", default_roll)
    phone = st.text_input("Phone Number", default_phone)

    skills = st.text_area(
        "Skills (comma separated)",
        default_skills
    )

    if st.button("💾 Save Profile"):

        save_profile(
            st.session_state.username,
            name,
            email,
            college,
            branch,
            year,
            roll,
            phone,
            skills
        )

        st.success("✅ Profile Saved Successfully")

# =====================================================
# 📥 STUDENT INPUT
# =====================================================

elif menu == "📥 Student Input":

    st.header("📥 Student Details")

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0
    )

    skills = st.slider(
        "Technical Skills",
        0,
        10,
        5
    )

    aptitude = st.slider(
        "Aptitude",
        0,
        10,
        5
    )

    projects = st.number_input(
        "Projects",
        min_value=0,
        max_value=10,
        value=2
    )

    internship = st.selectbox(
        "Internship",
        [0, 1, 2]
    )

    communication = st.slider(
        "Communication",
        0,
        10,
        5
    )

    backlogs = st.selectbox(
        "Backlogs",
        [0, 1, 2]
    )

    hackathon = st.selectbox(
        "Hackathon",
        [0, 1]
    )

    st.session_state.data = [
        cgpa,
        skills,
        aptitude,
        projects,
        internship,
        communication,
        backlogs,
        hackathon
    ]

    st.success("✅ Student data saved")

# =====================================================
# 🎯 PLACEMENT PREDICTION
# =====================================================

elif menu == "🎯 Prediction":

    prediction_page()
    # =====================================================
# 📊 DASHBOARD
# =====================================================

elif menu == "📊 Dashboard":


    dashboard_page()

# =====================================================
# 📄 RESUME ANALYZER
# =====================================================

elif menu == "📄 Resume Analyzer":

    st.header("📄 ATS Resume Analyzer")

    file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if file:

        text = extract_text(file)

        score = ats_score(text)

        st.session_state.ats_score = score

        st.subheader(f"ATS Score : {score}")

        st.write(suggestions(score))

# =====================================================
# 🎤 INTERVIEW BOT
# =====================================================

elif menu == "🎤 Interview Bot":

    interview_page()

# =====================================================
# 📈 SKILL GAP ANALYSIS
# =====================================================

elif menu == "📈 Skill Gap Analysis":

    skill_gap_page()

# =====================================================
# 💼 CAREER RECOMMENDATION
# =====================================================

elif menu == "💼 Career Recommendation":

    career_page()

# =====================================================
# 🏆 CERTIFICATE
# =====================================================

elif menu == "🏆 Certificate":

    if st.session_state.get("attempt", 0) == 0:

        st.warning("Please complete at least one interview.")

    else:

        avg = (
            st.session_state["score"]
            /
            st.session_state["attempt"]
        )

        certificate_page(avg)

# =====================================================
# 📜 PREDICTION HISTORY
# =====================================================

elif menu == "📜 Prediction History":

    history_page()

# =====================================================
# 📑 PLACEMENT REPORT
# =====================================================

elif menu == "📑 Placement Report":

    report_page()

# =====================================================
# 🏢 COMPANY ELIGIBILITY
# =====================================================

elif menu == "🏢 Company Eligibility":

    eligibility_page()

# =====================================================
# 💬 INTERVIEW FEEDBACK
# =====================================================

elif menu == "💬 Interview Feedback":

    feedback_page()

# =====================================================
# 🚪 LOGOUT
# =====================================================

st.sidebar.divider()

if st.sidebar.button("🚪 Logout"):

    st.session_state.login = False
    st.session_state.username = ""

    st.rerun()
    st.sidebar.divider()

    st.sidebar.caption("Version 1.0")

    st.sidebar.caption("Developed by Jahnavi Peetha")