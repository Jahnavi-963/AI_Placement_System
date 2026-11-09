import streamlit as st


def eligibility_page():

    st.header("🏢 Company Eligibility Checker")

    st.write("Check your eligibility for top IT companies.")

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    tenth = st.number_input(
        "10th Percentage",
        min_value=0,
        max_value=100
    )

    twelfth = st.number_input(
        "12th Percentage",
        min_value=0,
        max_value=100
    )

    backlogs = st.number_input(
        "Active Backlogs",
        min_value=0,
        max_value=20,
        step=1
    )

    if st.button("Check Eligibility"):

        companies = {
            "TCS": {"cgpa": 6.0, "backlogs": 1},
            "Infosys": {"cgpa": 6.5, "backlogs": 0},
            "Wipro": {"cgpa": 6.0, "backlogs": 0},
            "Accenture": {"cgpa": 7.0, "backlogs": 0},
            "Capgemini": {"cgpa": 6.0, "backlogs": 0},
            "Cognizant": {"cgpa": 6.5, "backlogs": 0},
            "IBM": {"cgpa": 6.5, "backlogs": 0},
            "HCL": {"cgpa": 6.0, "backlogs": 1},
            "Tech Mahindra": {"cgpa": 6.0, "backlogs": 1},
            "LTIMindtree": {"cgpa": 7.0, "backlogs": 0}
        }

        eligible = 0

        st.subheader("Eligibility Result")
        for company, criteria in companies.items():

            reasons = []

            if cgpa < criteria["cgpa"]:
                reasons.append(f"Minimum CGPA {criteria['cgpa']} required")

            if backlogs > criteria["backlogs"]:
                reasons.append(f"Maximum {criteria['backlogs']} backlog(s) allowed")

            if tenth < 60:
                reasons.append("10th percentage should be at least 60%")

            if twelfth < 60:
                reasons.append("12th percentage should be at least 60%")

            if len(reasons) == 0:
                st.success(f"✅ {company} - Eligible")
                eligible += 1

            else:
                st.error(f"❌ {company} - Not Eligible")

                for reason in reasons:
                    st.write("•", reason)

        st.divider()

        total = len(companies)

        percentage = (eligible / total) * 100

        st.subheader("📊 Overall Result")

        col1, col2 = st.columns(2)

        col1.metric("Eligible Companies", f"{eligible}/{total}")

        col2.metric("Eligibility Percentage", f"{percentage:.1f}%")

        if percentage >= 80:
            st.success("🔥 Excellent! You are eligible for most companies.")

        elif percentage >= 50:
            st.warning("🙂 Good! Improve a few areas to become eligible for more companies.")

        else:
            st.error("⚠ Improve your profile (CGPA, backlogs, academics) to increase eligibility.")