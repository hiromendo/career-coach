# pages/2_🎯_Introduction_-_Report_Objectives.py
import streamlit as st

# --- Header ---
st.title("🎯 Report Objectives & Structure")
st.markdown("This section outlines the purpose of the career transition analysis and how it's structured to help you navigate the information effectively.")

st.markdown("---") # Visual separator

# --- Main Purpose ---
st.header("Purpose of this Analysis")
st.info("""
The core goal is to provide you with:
1.  A **data-driven assessment** of suitable new career paths tailored to your situation.
2.  A structured, **actionable roadmap** outlining clear steps for a successful transition.
""", icon="🎯")

st.markdown("---") # Visual separator

# --- Report Structure/Flow ---
st.header("How This Report Guides You")
st.markdown("The analysis follows a logical progression:")

col1, col2 = st.columns(2)

with col1:
    # Step 1: Skills Inventory
    with st.container(border=True): # Add border for visual separation
        st.subheader("1. Identifying Your Assets 🛠️")
        st.markdown("Begins by identifying your valuable **transferable skills** derived from:")
        st.markdown("* Current Mail Handler Role")
        st.markdown("* Undergraduate Degree")

    # Step 2: Exploring Roles
    with st.container(border=True):
        st.subheader("2. Exploring Potential Roles 💼")
        st.markdown("Explores three specific roles chosen for their alignment with:")
        st.markdown("* Your Skills & Salary Goals (`$50k+`)")
        st.markdown("* Desired Flexibility (`Hybrid/4x10`)")
        st.markdown("* Location & Positive Environment Potential")
        st.markdown("**Roles Examined:**")
        st.markdown("  - Logistics Coordinator")
        st.markdown("  - Operations Specialist")
        st.markdown("  - Project Coordinator")


with col2:
    # Step 3: Role Details
    with st.container(border=True):
        st.subheader("3. Deep Dive into Each Role 🔍")
        st.markdown("Details provided for each recommended role include:")
        st.markdown("* Typical Responsibilities")
        st.markdown("* Common Qualifications")
        st.markdown("* Salary Expectations (Atlanta Market)")
        st.markdown("* Availability of Flexible Work")

    # Step 4: Strategy Outline
    with st.container(border=True):
        st.subheader("4. Your Actionable Roadmap 🗺️")
        st.markdown("Outlines a comprehensive **step-by-step strategy** covering:")
        st.markdown("* Skill Gap Analysis")
        st.markdown("* Learning & Resources")
        st.markdown("* Resume/Cover Letter Crafting")
        st.markdown("* Job Search Techniques")
        st.markdown("* Interview Preparation")

st.markdown("---") # Visual separator

# --- Foundation ---
st.header("Grounded in Data")
# Using st.success to highlight the reliable basis of the report
st.success("""
All recommendations and strategies are based on an analysis of your specific background weighed against current labor market trends and specific job opportunity data relevant to the Atlanta area and remote work.
""", icon="📈")

st.markdown("---")
st.caption("Use the sidebar to navigate to the different sections of this analysis.")