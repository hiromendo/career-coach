import streamlit as st

# --- Data for the Plan ---
plan_data = [
    {
        "phase_title": "Phase 1: Foundational Research & Decision-Making",
        "phase_duration": "Est. 1-3 Weeks",
        "projects": [
            "Project 1.1: Deep Dive Verification & Pathway Clarification (AT Focus)",
            "Project 1.2: Career Path Finalization",
            "Project 1.3: Financial Impact Analysis & Funding Strategy",
        ],
    },
    {
        "phase_title": "Phase 2: Educational Preparation & Application",
        "phase_duration": "Est. 6-18 Weeks (depending on prerequisites and chosen pathway)",
        "projects": [
            "Project 2.1: Prerequisite Coursework Completion (If Necessary)",
            "Project 2.2: Standardized Test Preparation (e.g., GRE)",
            "Project 2.3: Program Selection & Application Submission",
            "Project 2.4: Gaining Observational/Volunteer Experience",
        ],
    },
    {
        "phase_title": "Phase 3: Academic Pursuit",
        "phase_duration": "Est. 2-3+ Years (depending on the chosen program)",
        "projects": [
            "Project 3.1: Excel in Academic & Clinical Program",
            "Project 3.2: Actively Seek Mentorship & Networking",
        ],
    },
    {
        "phase_title": "Phase 4: Licensure & Certification",
        "phase_duration": "Est. 3-6 Weeks post-graduation",
        "projects": [
            "Project 4.1: National Exam Preparation & Success",
            "Project 4.2: Oklahoma State Licensure Application",
            "Project 4.3: (Optional for PT, Recommended for Sports Focus) Pursue SCS or other relevant certifications",
        ],
    },
    {
        "phase_title": "Phase 5: Targeted Job Search & Career Launch in/near Claremore",
        "phase_duration": "Est. 3-6 Weeks",
        "projects": [
            "Project 5.1: Develop Claremore/Tulsa-focused Job Search Strategy",
            "Project 5.2: Resume & Interview Preparation",
            "Project 5.3: Salary Negotiation Strategy",
        ],
    },
]

# --- App Layout ---

# Main Title
st.title("Your Actionable Transition Plan to a Sports Therapy Career in Claremore")
st.markdown("---")

# Introduction
st.info("This plan outlines the key phases and projects to guide your transition. Each project is designed to be actionable and is estimated to take approximately **one week** to complete, though this can vary based on individual circumstances and the complexity of the task.")
st.markdown("---")

# Display Phases and Projects
for i, phase in enumerate(plan_data):
    with st.expander(f"{phase['phase_title']} ({phase['phase_duration']})", expanded=i==0): # Expand the first phase by default
        st.subheader("Projects for this Phase:")
        for project in phase['projects']:
            st.markdown(f"- **{project}**")
        st.markdown(f"*Estimated duration for this phase: {phase['phase_duration']}*")
        st.markdown("*Each project within this phase is approximately one week.*")
        st.markdown("---")


# Footer or additional notes (optional)
st.sidebar.header("About this Plan")
st.sidebar.info(
    "This interactive plan helps you track your progress towards a sports therapy career. "
    "Use the expanders to view details for each phase."
)
st.sidebar.markdown("---")
st.sidebar.markdown("Remember to adjust timelines based on your personal progress and external factors.")

# To run this Streamlit app:
# 1. Save this code as a Python file (e.g., `sports_therapy_plan_app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: streamlit run sports_therapy_plan_app.py
