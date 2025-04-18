import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="OR CPA Requirements", layout="wide")

# --- Page Title and Introduction ---
st.title("🎓 Oregon CPA License Requirements (New Applicants)")
st.markdown("""
Planning to pursue a **new** CPA license in Oregon? Understanding the requirements is the first step.
This page breaks down the key components: **Education, Exam, Experience, and Ethics/Application**.

Review the requirements, then test your knowledge with the quick quiz at the bottom!
""")
st.info("ℹ️ This page focuses on **NEW** licenses. If reactivating, see the 'Credentials Pathway' page.", icon="❗")
st.divider()

# --- Requirements Overview using Columns and Containers ---
st.header("Key Requirements Overview")

col1, col2 = st.columns(2, gap="large")

# === Education ===
with col1:
    with st.container(border=True):
        st.subheader("1. 🎓 Education")
        st.markdown("""
        * **Total Hours:** Complete **150 semester hours** of college education (including a Bachelor's degree).
        * **Specific Courses:** Within the 150 hours, include ≥ **24 upper-division Accounting** hours and ≥ **24 general Business** hours.
        * **Need Credits?:** Consider Post-Baccalaureate certificates (e.g., PSU, Linfield) or Master's programs if needed.
        """)
        st.link_button("OR Board Education Rules", "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=3680", help="See Division 10 rules")


# === Exam ===
with col2:
    with st.container(border=True):
        st.subheader("2. ✍️ Uniform CPA Exam")
        st.markdown("""
        * **Requirement:** Pass all **4 sections** of the Uniform CPA Exam (score 75+ each). *(Note: 3 Core + 1 Discipline format as of 2024)*.
        * **Sitting Eligibility (OR):** Can *sit* for the exam with **120 semester hours** (incl. degree & required courses), but 150 needed for *license*.
        * **Preparation:** Significant study (300-400+ hrs) is typical; review courses (Becker, etc.) highly recommended.
        """)
        st.link_button("AICPA Exam Info", "https://www.aicpa-cima.com/resources/landing/cpa-exam")

# === Experience ===
with col1:
    with st.container(border=True):
        st.subheader("3. 💼 Experience")
        st.markdown("""
        * **Duration:** Complete **1 year** (~2000 hours) of relevant accounting experience.
        * **Supervision:** Experience must be **verified by an active, licensed CPA**.
        * **Type:** Can be in public accounting, industry, government, or academia (must meet relevancy criteria).
        """)
        st.link_button("OR Board Experience Rules", "https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=3680", help="See Division 10 rules")


# === Application & Ethics ===
with col2:
    with st.container(border=True):
        st.subheader("4. 📜 Application & Ethics")
        st.markdown("""
        * **Final Steps:** Apply to the OR Board *after* meeting Edu/Exam/Exp requirements (forms, fees, docs).
        * **State Ethics:** Pass a separate **Ethics exam** (often AICPA's course) *and* complete **4 hours of Oregon-specific** ethics CPE.
        * **Maintenance:** Renew license biennially with **80 hours of CPE**.
        """)
        st.link_button("OR Board Licensing Info", "https://www.oregon.gov/boa/Pages/Licensing.aspx")
        st.link_button("OR Board CPE Info", "https://www.oregon.gov/boa/pages/cpe.aspx")


st.divider()

# --- Interactive Quiz Section ---
st.header("🧠 Knowledge Check!")
st.markdown("Test your understanding of the key Oregon CPA requirements.")

# Use a form for the quiz
with st.form("cpa_req_quiz"):
    st.write("**Question 1:** How many total semester hours of education are required for CPA *licensure* in Oregon?")
    q1_answer = st.radio(
        "Q1 Options",
        options=["120 hours", "140 hours", "150 hours", "160 hours"],
        index=None, label_visibility="collapsed"
    )

    st.write("**Question 2:** What is the minimum number of semester hours required to *sit* for the CPA Exam in Oregon (assuming degree & course requirements met)?")
    q2_answer = st.radio(
        "Q2 Options",
        options=["100 hours", "120 hours", "150 hours", "Not specified"],
        index=None, label_visibility="collapsed"
    )

    st.write("**Question 3:** How much supervised work experience is generally required for an Oregon CPA license?")
    q3_answer = st.radio(
        "Q3 Options",
        options=["6 months", "1 year (~2000 hours)", "2 years (~4000 hours)", "No experience required"],
        index=None, label_visibility="collapsed"
    )

    st.write("**Question 4:** Besides passing the 4-part Uniform CPA Exam, what other *exam* must be passed for Oregon licensure?")
    q4_answer = st.radio(
        "Q4 Options",
        options=["Oregon Law Exam", "Ethics Exam", "CMA Exam", "No other exam"],
        index=None, label_visibility="collapsed"
    )

    # Submit button for the form
    submitted = st.form_submit_button("Check My Answers!")

    if submitted:
        score = 0
        correct_answers = {
            "Q1": "150 hours",
            "Q2": "120 hours",
            "Q3": "1 year (~2000 hours)",
            "Q4": "Ethics Exam"
        }
        user_answers = {"Q1": q1_answer, "Q2": q2_answer, "Q3": q3_answer, "Q4": q4_answer}
        results_messages = []

        for i in range(1, 5):
            q_key = f"Q{i}"
            if user_answers[q_key] == correct_answers[q_key]:
                score += 1
                results_messages.append(f"✅ **Question {i}: Correct!** ({correct_answers[q_key]})")
            elif user_answers[q_key] is None:
                 results_messages.append(f"⚠️ **Question {i}: Not Answered.** Correct answer: {correct_answers[q_key]}")
            else:
                results_messages.append(f"❌ **Question {i}: Incorrect.** You chose: {user_answers[q_key]}. Correct answer: {correct_answers[q_key]}")

        st.subheader("Quiz Results:")
        st.markdown(f"**You scored {score} out of 4.**")
        for msg in results_messages:
            st.markdown(msg)

        if score == 4:
            st.balloons()
            st.success("Great job! You've got a good handle on the key requirements.")
        else:
            st.warning("Review the sections above and check the official Oregon Board resources for clarification!")


st.divider()
st.info("Always refer to the official [Oregon Board of Accountancy website](https://www.oregon.gov/boa) for the most current and detailed requirements.", icon="❗")