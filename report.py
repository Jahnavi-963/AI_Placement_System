import streamlit as st
import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


def create_pdf():

    filename = "Placement_Report.pdf"

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER
    title.textColor = colors.darkblue

    heading = styles["Heading2"]
    heading.textColor = colors.darkblue

    story = []

    # ==========================================
    # TITLE
    # ==========================================

    story.append(
        Paragraph(
            "AI Placement Analysis Report",
            title
        )
    )

    story.append(Spacer(1,20))

    # ==========================================
    # STUDENT INFORMATION
    # ==========================================

    story.append(
        Paragraph(
            "Student Information",
            heading
        )
    )

    story.append(Spacer(1,10))

    username = st.session_state.get(
        "username",
        "Not Available"
    )

    info = [

        ["Student Name", username],

        [
            "Date",
            datetime.datetime.now().strftime("%d-%m-%Y")
        ],

        [
            "Time",
            datetime.datetime.now().strftime("%I:%M %p")
        ]

    ]

    info_table = Table(
        info,
        colWidths=[180,250]
    )

    info_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,0),(0,-1),colors.whitesmoke),

        ("BACKGROUND",(1,0),(1,-1),colors.beige),

        ("BOTTOMPADDING",(0,0),(-1,-1),8),

        ("FONTNAME",(0,0),(-1,-1),"Helvetica")

    ]))

    story.append(info_table)

    story.append(Spacer(1,20))
        # ==========================================
    # PLACEMENT PREDICTION
    # ==========================================

    story.append(
        Paragraph(
            "Placement Prediction",
            heading
        )
    )

    story.append(Spacer(1,10))

    prediction = st.session_state.get("prediction", 0)

    if prediction >= 80:
        status = "Excellent Placement Chance"
    elif prediction >= 60:
        status = "Good Placement Chance"
    elif prediction >= 40:
        status = "Average Placement Chance"
    else:
        status = "Needs Improvement"

    prediction_data = [

        ["Placement Chance", f"{prediction:.2f}%"],

        ["Status", status]

    ]

    prediction_table = Table(
        prediction_data,
        colWidths=[180,250]
    )

    prediction_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,0),(0,-1),colors.whitesmoke),

        ("BACKGROUND",(1,0),(1,-1),colors.beige),

        ("BOTTOMPADDING",(0,0),(-1,-1),8)

    ]))

    story.append(prediction_table)

    story.append(Spacer(1,20))

    # ==========================================
    # RESUME ANALYSIS
    # ==========================================

    story.append(
        Paragraph(
            "Resume Analysis",
            heading
        )
    )

    story.append(Spacer(1,10))

    ats = st.session_state.get("ats_score", 0)

    if ats >= 80:
        resume_status = "Excellent Resume"
    elif ats >= 60:
        resume_status = "Good Resume"
    elif ats >= 40:
        resume_status = "Average Resume"
    else:
        resume_status = "Needs Improvement"

    ats_data = [

        ["ATS Score", f"{ats}/100"],

        ["Resume Status", resume_status]

    ]

    ats_table = Table(
        ats_data,
        colWidths=[180,250]
    )

    ats_table.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,0),(0,-1),colors.whitesmoke),

        ("BACKGROUND",(1,0),(1,-1),colors.beige),

        ("BOTTOMPADDING",(0,0),(-1,-1),8)

    ]))

    story.append(ats_table)

    story.append(Spacer(1,20))
        # ==========================================
    # INTERVIEW PERFORMANCE
    # ==========================================

    story.append(Paragraph("Interview Performance", heading))
    story.append(Spacer(1,10))

    attempts = st.session_state.get("attempt", 0)
    total_score = st.session_state.get("score", 0)

    if attempts > 0:
        average = total_score / attempts
    else:
        average = 0

    interview_data = [
        ["Attempts", str(attempts)],
        ["Average Score", f"{average:.2f}%"]
    ]

    interview_table = Table(interview_data, colWidths=[180,250])

    interview_table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("BACKGROUND",(0,0),(0,-1),colors.whitesmoke),
        ("BACKGROUND",(1,0),(1,-1),colors.beige),
        ("BOTTOMPADDING",(0,0),(-1,-1),8)
    ]))

    story.append(interview_table)
    story.append(Spacer(1,20))


    # ==========================================
    # SKILL GAP ANALYSIS
    # ==========================================

    story.append(Paragraph("Skill Gap Analysis", heading))
    story.append(Spacer(1,10))

    skill_score = st.session_state.get("skill_score", 0)

    missing = st.session_state.get("missing_skills", [])

    if len(missing) == 0:
        missing_text = "None"
    else:
        missing_text = ", ".join(missing)

    skill_data = [
        ["Skill Readiness", f"{skill_score}%"],
        ["Missing Skills", missing_text]
    ]

    skill_table = Table(skill_data, colWidths=[180,250])

    skill_table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("BACKGROUND",(0,0),(0,-1),colors.whitesmoke),
        ("BACKGROUND",(1,0),(1,-1),colors.beige),
        ("BOTTOMPADDING",(0,0),(-1,-1),8)
    ]))

    story.append(skill_table)
    story.append(Spacer(1,20))


    # ==========================================
    # CAREER RECOMMENDATION
    # ==========================================

    story.append(Paragraph("Career Recommendation", heading))
    story.append(Spacer(1,10))

    careers = st.session_state.get("careers", [])

    if len(careers) == 0:
        career_text = "No Recommendation"
    else:
        career_text = "<br/>".join(careers)

    story.append(
        Paragraph(career_text, styles["BodyText"])
    )

    story.append(Spacer(1,20))


    # ==========================================
    # OVERALL PERFORMANCE
    # ==========================================

    story.append(Paragraph("Overall Performance", heading))
    story.append(Spacer(1,10))

    overall = (prediction + ats + average + skill_score) / 4

    if overall >= 80:
        stars = "★★★★★"
        result = "Excellent Candidate"
    elif overall >= 60:
        stars = "★★★★☆"
        result = "Good Candidate"
    elif overall >= 40:
        stars = "★★★☆☆"
        result = "Average Candidate"
    else:
        stars = "★★☆☆☆"
        result = "Needs Improvement"

    overall_data = [
        ["Overall Score", f"{overall:.2f}%"],
        ["Rating", stars],
        ["Result", result]
    ]

    overall_table = Table(overall_data, colWidths=[180,250])

    overall_table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("BACKGROUND",(0,0),(0,-1),colors.whitesmoke),
        ("BACKGROUND",(1,0),(1,-1),colors.beige),
        ("BOTTOMPADDING",(0,0),(-1,-1),8)
    ]))

    story.append(overall_table)

    story.append(Spacer(1,25))

    story.append(
        Paragraph(
            "<b>Generated by AI Placement Portal</b>",
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename


def report_page():

    st.header("📄 Placement Report")

    st.write("Generate a professional placement report in PDF format.")

    if st.button("📥 Generate Report"):

        pdf = create_pdf()

        with open(pdf, "rb") as file:

            st.success("Report Generated Successfully!")

            st.download_button(
                label="⬇ Download Placement Report",
                data=file,
                file_name="Placement_Report.pdf",
                mime="application/pdf"
            )