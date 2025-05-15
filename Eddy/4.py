import streamlit as st
import pandas as pd # For the date in the sidebar

# --- Main Title for this project idea page ---
st.title("🔗 Project Idea 2: Simulating an Interconnection Request and Desktop Feasibility Assessment")
st.subheader("For a Solar + Storage Project")
st.markdown("---")

# --- Rationale ---
st.subheader("🎯 Rationale")
st.markdown("""
This project targets the job description's requirements for:
* *"interconnection study process experience,"*
* *"technical understanding of solar + storage projects,"*
* *"wholesale market/RTO market operations knowledge."*

Understanding grid interconnection is vital for project viability.
""")
st.success( # Using st.success to highlight the direct alignment with JD requirements
    "**Key Alignment:** Directly addresses crucial knowledge areas for managing grid-tied renewable projects."
)
st.markdown("---")

# --- Actionable Steps ---
st.subheader("🛠️ Actionable Steps")

st.markdown("""
1.  **Select RTO/ISO and Project:**
    Choose an RTO/ISO (e.g., MISO, PJM, ERCOT, CAISO – referencing where Origis operates) and define a hypothetical solar (e.g., **100 MW**) plus battery storage (e.g., **50 MW / 200 MWh**) project.
    * *Tip: Pick an RTO/ISO whose documentation is readily accessible online.*

2.  **Research Interconnection Process:**
    Study the selected RTO/ISO’s generation interconnection procedures, typically available on their website. Focus on:
    * The initial application requirements.
    * The queue process.
    * The sequence of studies (e.g., Feasibility Study, System Impact Study, Facilities Study).
    * *Resource: RTO/ISO websites are the primary source. Look for "Generator Interconnection" or "Planning" sections.*

3.  **Identify Key Data for Application:**
    List the typical technical and commercial information required for an initial interconnection request. Examples include:
    * Project location (latitude/longitude or address)
    * Project size (MWac for solar, MW/MWh for storage)
    * Technology type (e.g., inverter-based resources)
    * Preliminary single-line diagram or site layout (conceptual)
    * Proposed Point of Interconnection (POI)
    * Desired commercial in-service date.
    * *Focus: Understand the *level of detail* needed at the initial application stage.*

4.  **Desktop Feasibility Analysis:**
    Using publicly available transmission maps (often found on RTO/ISO sites or EIA) and RTO/ISO planning documents, identify potential POIs near a hypothetical site. Analyze potential constraints such as:
    * Voltage level and capacity of nearby transmission/distribution lines.
    * Proximity to existing substations.
    * Known congestion areas or transmission limitations (from planning reports).
    * *Consider: What makes a POI more or less favorable from a high-level perspective?*

5.  **Outline Potential Challenges:**
    Based on your research, list common challenges or risks associated with interconnection in that RTO/ISO for a project of your defined type. Examples:
    * High network upgrade costs.
    * Long queue wait times.
    * Potential for curtailment risk.
    * Complex study processes or data requirements.
    * *Think about what could delay a project or make it uneconomical from an interconnection standpoint.*

6.  **Prepare Summary:**
    Create a brief report or presentation summarizing the initial interconnection steps for your chosen RTO/ISO and your desktop feasibility assessment. Highlight key considerations that would be relevant for an *"early stage interconnection team"* at a company like Origis.
    * *Structure: Introduction (Project & RTO), Interconnection Process Overview, Data Requirements, Desktop Feasibility (Potential POIs & Constraints), Key Challenges, Conclusion.*
""")
st.markdown("---")

# --- Strategic Importance & Alignment ---
st.subheader("🌟 Value Proposition for Candidacy")
st.info( # Using st.info to emphasize the project's impact
    "**Demonstrates Critical Insight:** This project showcases your initiative in understanding a complex and critical aspect of project development – getting power to the grid."
)

st.markdown("""
Origis Energy needs to *"Overcome Transmission Challenges"* and effectively manage the interconnection process to ensure *"project certainty"*.
Demonstrating familiarity with these processes, even at a simulated level, is a significant plus.

By completing this project, you show:
* An understanding of how projects connect to the larger energy system.
* The ability to research and synthesize complex technical and regulatory information.
* Proactive engagement with a key risk factor in renewable energy development.
""")

# --- Sidebar for navigation or extra info ---
st.sidebar.header("Project Detail")
st.sidebar.markdown("This page details the **Interconnection Simulation** project idea for a PDM role.")
st.sidebar.markdown("---")
# Example link back if part of a multi-page app structure
# st.sidebar.page_link("your_main_app_file.py", label="Back to PDM Projects Overview", icon="↩️")
st.sidebar.success(f"Content current as of: {pd.Timestamp.now(tz='America/Los_Angeles').strftime('%B %d, %Y')}")

# To run this app:
# 1. Save the code as a Python file (e.g., `pdm_interconnection_app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: `streamlit run pdm_interconnection_app.py`
#
# For a multi-page app structure, you would typically save this in a 'pages'
# directory and Streamlit would handle the navigation.
