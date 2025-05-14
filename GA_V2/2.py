import streamlit as st
import pandas as pd

# --- Main Title for this section ---
st.header("3. Actionable Projects to Build Relevant Experience for a Project Development Manager Role")
st.markdown("""
To bridge the gap between your current resume and the specific requirements of the Project Development Manager role at Origis Energy, undertaking targeted personal projects can be highly effective.
The following projects are designed to build and demonstrate experience in key areas such as solar siting, permitting, interconnection, financial modeling, and landowner relations – all critical for *"driving additional pipeline growth and project successes in both utility scale solar and energy storage."*
""")
st.markdown("---") # Visual separator

# --- Table: Summary of Actionable Projects ---
st.subheader("Table: Summary of Actionable Projects and Their Alignment with Project Development Manager Role")

# Data for the table - Manually extracted from the provided Markdown table
data = {
    "Project Title": [
        "Developing a Site Suitability Analysis and Preliminary Permitting Pathway for a Utility-Scale Solar Project",
        "Simulating an Interconnection Request and Desktop Feasibility Assessment for a Solar + Storage Project",
        "Building a Pro-Forma Financial Model and Analyzing Key PPA Terms for a Utility-Scale Solar Project",
        "Crafting a Mock Landowner Outreach Strategy and Option Agreement Outline for a Solar Development Project"
    ],
    "Brief Description": [
        "Researching land suitability (GIS data, zoning, environmental screens, transmission proximity) and outlining the key federal, state, and local permits for a hypothetical 100MW solar project.",
        "Outlining the initial steps of an interconnection request process in a chosen RTO/ISO, identifying key data inputs, and performing a high-level desktop analysis of potential interconnection challenges for a 100MW solar + 50MWh storage project.",
        "Developing a simplified pro-forma financial model (inputs: capex, opex, degradation, PPA price, financing assumptions) for a hypothetical solar project and analyzing common terms and risk allocation in a sample Power Purchase Agreement (PPA).",
        "Developing a strategy for identifying and approaching landowners for a utility-scale solar project, and outlining key terms for a land option agreement."
    ],
    "Key Skills/Experience Gained (aligns with JD Requirements)": [
        "Solar siting, land constraint analysis, preliminary environmental/permitting assessment, research of Federal, State & Local solar project permitting.",
        "Interconnection study process understanding, technical considerations for solar + storage, wholesale market/RTO operations awareness, grid evaluation.",
        "Clean energy financial modeling, understanding of PPA structures, project finance concepts, risk analysis.",
        "Land acquisition strategy, landowner negotiation preparation, understanding of land-related legal documentation."
    ],
    "Relevance to Origis Energy's Focus": [
        "Aligns with Origis's need to \"Evaluate transmission grids and land constraints\" and \"Assist in the management of all aspects of solar and storage project permitting.\" Origis has projects in states like FL and TX.",
        "Reflects Origis's work with \"transmission or customer connected\" solutions and the need to \"Support early stage interconnection team with applications, following interconnection process management.\" Origis operates across various RTO/ISO territories.",
        "Supports Origis's activities in \"project finance negotiations support\" and \"PPA negotiations support.\" Financial viability is key to \"insuring solar project bankability\".",
        "Directly addresses the need to \"Interface directly with land owners, land consultants to secure selected sites\" and \"Familiarity with landowner negotiations.\" Origis emphasizes \"Collaborative Community Outcomes\"."
    ],
    "Potential Impact on Candidacy": [
        "Demonstrates analytical skills in site selection, understanding of permitting complexities, and proactive learning in core development tasks.",
        "Showcases understanding of grid integration, a critical step in project development, and familiarity with RTO/ISO procedures.",
        "Demonstrates financial acumen relevant to project development, ability to assess project economics, and understanding of PPA dynamics.",
        "Highlights skills in a crucial early-stage development activity, demonstrating an understanding of securing land rights and initiating community relations."
    ]
}

df_projects_pdm = pd.DataFrame(data)

# Convert DataFrame to HTML and apply custom CSS for styling and text wrapping.
# CSS ensures no specific background color, allowing it to adapt to Streamlit's theme.
html_table_pdm = f"""
<style>
    .pdm-custom-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9rem; /* Adjust font size as needed */
        margin-bottom: 1rem; /* Add some space below the table */
    }}
    .pdm-custom-table th, .pdm-custom-table td {{
        border: 1px solid #555; /* Darker border for better visibility on light/dark themes */
        padding: 10px 12px; /* Increased padding for better readability */
        text-align: left;
        white-space: normal; /* Crucial for text wrapping */
        word-wrap: break-word; /* Helps break long words */
        overflow-wrap: break-word; /* Ensures wrapping for very long unbreakable strings */
        vertical-align: top; /* Align text to the top of the cell */
        background-color: transparent; /* Ensure cells have transparent background */
        color: inherit; /* Ensure text color adapts to the Streamlit theme (light/dark) */
    }}
    .pdm-custom-table th {{
        font-weight: bold;
        background-color: rgba(128, 128, 128, 0.1); /* Subtle grey background for headers, slightly transparent */
    }}
</style>
{df_projects_pdm.to_html(escape=False, index=False, classes='pdm-custom-table')}
"""

# Displaying the HTML table
# unsafe_allow_html is True because we are injecting custom HTML and CSS
st.markdown(html_table_pdm, unsafe_allow_html=True)

# --- Sidebar for navigation or extra info ---
st.sidebar.header("PDM Project Focus")
st.sidebar.info(
    "This page outlines actionable projects tailored for aspiring Project Development Managers "
    "in the renewable energy sector, aligning with Origis Energy's typical role requirements."
)
st.sidebar.markdown("---")
st.sidebar.success(f"Content current as of: {pd.Timestamp.now(tz='America/Los_Angeles').strftime('%B %d, %Y')}")


# To run this app:
# 1. Save the code as a Python file (e.g., `pdm_projects_app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: `streamlit run pdm_projects_app.py`
