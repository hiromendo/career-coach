import streamlit as st
import pandas as pd # For the date in the sidebar

# --- Main Title for this project idea page ---
st.title("🔎 Project Idea 1: Developing a Site Suitability Analysis and Preliminary Permitting Pathway")
# Using a slightly more specific title based on the content that follows.
st.subheader("For a Utility-Scale Solar Project")
st.markdown("---")

# --- Rationale ---
st.subheader("🎯 Rationale")
st.markdown("""
This project directly addresses the job description's requirements for:
* *"solar siting and land acquisition documentation,"*
* Understanding *"Federal, State & Local solar project permitting,"*
* The ability to *"Evaluate transmission grids and land constraints."*

It allows you to simulate the critical initial assessment phase of project development.
""")
st.success( # Using st.success to highlight the direct alignment with JD requirements
    "**Key Alignment:** Directly tackles core skills mentioned in Project Development Manager job descriptions."
)
st.markdown("---")

# --- Actionable Steps ---
st.subheader("🛠️ Actionable Steps")

# Using columns for a more engaging layout for steps if desired, or just markdown.
# For this number of steps, simple markdown should be clear.

st.markdown("""
1.  **Define Project Parameters:**
    Conceptualize a hypothetical utility-scale solar project (e.g., **100 MW**) in a specific county within a target state where Origis has a presence (e.g., Florida, Texas).
    * *Tip: Choose a county and state to make your research more focused and realistic.*

2.  **Site Screening:**
    Utilize publicly available GIS data (e.g., state environmental portals, FEMA flood maps, USGS data, transmission maps from EIA or RTOs) to identify potentially suitable parcels. Consider factors like:
    * Land slope
    * Proximity to transmission infrastructure (substations, high-voltage lines)
    * Avoidance of critical habitats, wetlands, and floodplains.
    * *Resource: Explore tools like Google Earth Pro for initial visual assessment and measurement.*

3.  **Constraint Mapping:**
    Document key land constraints (environmental, topographical, existing land use, zoning regulations) for the selected area.
    * *Consider creating a simple visual map or overlay highlighting these constraints.*

4.  **Preliminary Permitting Research:**
    Identify the primary federal (e.g., NEPA review if federal nexus, Clean Water Act Section 404), state (e.g., state environmental agency permits, siting board approvals), and local (county zoning, building permits) permits likely required for a solar project of this scale in the chosen jurisdiction.
    * *Focus: Understand the *types* of permits and the *agencies* involved.*

5.  **Develop Pathway Outline:**
    Create a high-level flowchart or checklist outlining the anticipated permitting steps, key agencies involved, and estimated timelines for major permits.
    * *Visuals like flowcharts can be very effective here.*

6.  **Summarize Findings:**
    Compile your analysis into a concise report or presentation, highlighting the site's potential and the primary permitting hurdles, similar to what might be presented to management.
    * *Structure: Executive Summary, Site Characteristics, Constraint Analysis, Permitting Overview, Conclusions.*
""")
st.markdown("---")

# --- Strategic Importance & Alignment ---
st.subheader("🌟 Value Proposition for Candidacy")
st.info( # Using st.info to emphasize the project's impact
    "**Demonstrates Core Competencies:** This project showcases your ability to perform due diligence on potential project locations, a fundamental skill for a Project Development Manager."
)

st.markdown("""
It shows an understanding of the multifaceted considerations that go into site selection, from technical feasibility (transmission access) to regulatory compliance (permitting).

Origis Energy develops projects across numerous states, each with unique regulatory landscapes, making this adaptability crucial. By completing this project, you demonstrate:
* Analytical rigor in site assessment.
* Proactive learning of complex permitting processes.
* Strategic thinking relevant to early-stage project development.
""")

# --- Sidebar for navigation or extra info ---
st.sidebar.header("Project Detail")
st.sidebar.markdown("This page details the **Site Suitability Analysis** project idea for a PDM role.")
st.sidebar.markdown("---")
# Example link back if part of a multi-page app structure
# st.sidebar.page_link("your_main_app_file.py", label="Back to PDM Projects Overview", icon="↩️")
st.sidebar.success(f"Content current as of: {pd.Timestamp.now(tz='America/Los_Angeles').strftime('%B %d, %Y')}")

# To run this app:
# 1. Save the code as a Python file (e.g., `pdm_site_suitability_app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: `streamlit run pdm_site_suitability_app.py`
#
# For a multi-page app structure, you would typically save this in a 'pages'
# directory and Streamlit would handle the navigation.
