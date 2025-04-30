import streamlit as st

# --- Main Title ---
# Display the main title prominently with an emoji
st.title("🗽 Strategic Career Transition & Job Search Plan: New York City")


st.divider() # Add another visual separator

# --- Introduction Section ---
st.header("1. Introduction")

# Use markdown for formatted text, including bolding key terms
st.markdown("""
This report outlines a tailored career transition and job search strategy for an individual seeking employment in **New York City (NYC)**.
The strategy considers the candidate's professional background, educational qualifications, skills, and specific job search parameters.
""")

st.subheader("Key Search Parameters 🎯")

# Use columns to arrange key information side-by-side for better visual structure
col1, col2, col3 = st.columns([2, 1.5, 2]) # Adjust column ratios as needed for balance

# Column 1: Target Roles
with col1:
    st.markdown("##### Target Roles 💼") # Use a slightly smaller header for subsections
    # Use bullet points for the list of roles
    st.markdown("""
    * Associate Project Manager
    * Management Analyst
    * Procurement Analyst
    * Business Developer
    """)

# Column 2: Location and Salary
with col2:
    st.markdown("##### Location Preference 🏢")
    st.markdown("NYC (Hybrid or In-office)")
    st.markdown("<br>", unsafe_allow_html=True) # Add some vertical space

    # Use st.metric to highlight the salary requirement visually
    st.metric(label="Minimum Salary Requirement", value="$100,000 USD 💰")

# Column 3: Background and Context
with col3:
    st.markdown("##### Candidate Background Highlights ✨")
    # Use bullet points for background areas
    st.markdown("""
    * Consulting
    * Energy Sector
    * Project Management
    * Real Estate Development
    """)
    # Use st.warning to subtly draw attention to the context
    st.warning("Context: Recent role termination due to organizational downsizing.")

st.divider() # Separate parameters from the objective

# --- Objective Section ---
st.subheader("Overall Objective")
# Use st.info to highlight the main goal of the plan
st.info("""
Provide a **structured, actionable roadmap** for securing a suitable position in the competitive NYC market, leveraging diverse experience while navigating the job search post-termination.
""")

# Add a concluding caption
st.caption("This introduction sets the stage for the detailed strategic plan that follows.")

# --- How to Run ---
# Add comments explaining how to execute the Streamlit app
# To run this app:
# 1. Save the code as a Python file (e.g., `nyc_career_app.py`).
# 2. Ensure you have Streamlit installed (`pip install streamlit`).
# 3. Open your terminal or command prompt.
# 4. Navigate to the directory where you saved the file.
# 5. Run the command: `streamlit run nyc_career_app.py`
