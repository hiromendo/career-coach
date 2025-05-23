import streamlit as st
import pandas as pd # For the date in the sidebar

# --- Main Title for this project idea page ---
st.title("🤝 Project Idea 4: Crafting a Mock Landowner Outreach Strategy and Option Agreement Outline")
st.subheader("For a Solar Development Project")
st.markdown("---")

# --- Rationale ---
st.subheader("🎯 Rationale")
st.markdown("""
This project focuses on:
* *"solar siting and land acquisition documentation,"*
* The ability to *"Interface directly with land owners,"*
* And *"Familiarity with landowner negotiations."*

Securing land is one of the earliest and most critical steps in development.
""")
st.success( # Using st.success to highlight the direct alignment with JD requirements
    "**Key Alignment:** Addresses fundamental skills in land acquisition and stakeholder engagement."
)
st.markdown("---")

# --- Actionable Steps ---
st.subheader("🛠️ Actionable Steps")

st.markdown("""
1.  **Define Target Area:**
    Select a hypothetical rural area in a state with solar development potential.
    * *Example:* A county in Mississippi or Alabama (referencing states where Origis has projects).
    * *Tip: Focus on areas with potentially large, flat, and open parcels.*

2.  **Landowner Identification Research (Methodology):**
    Outline methods for identifying potential landowners of suitable parcels.
    * *Describe the process:* This could involve discussing the use of county tax assessor records (often publicly searchable online by address or parcel ID), plat maps, and online land databases (like those used by real estate professionals, though you'd describe their function, not access private data).
    * *Focus: Explain *how* one would typically find this information, not on retrieving actual private data.*

3.  **Develop Outreach Strategy:**
    Create a mock outreach plan. This should include:
    * **Initial Contact Methods:**
        * Introductory letters (professional, clear, concise).
        * Working with local land consultants or agents who have existing relationships.
        * Potentially, carefully planned direct outreach (phone calls, if appropriate for the mock scenario).
    * **Key Talking Points:** Emphasize project benefits such as:
        * Guaranteed long-term lease revenue for the landowner.
        * Diversification of income for agricultural landowners.
        * Local economic investment and job creation during construction.
        * Contribution to clean energy generation.
        * Minimal impact on day-to-day farming operations on non-leased land.
    * **Approach for Addressing Common Landowner Concerns:**
        * Impact on land use and future options.
        * Visual impact of the solar farm.
        * Decommissioning process and site restoration at end of life.
        * Potential for crop damage or interference during surveys or construction (and how it's mitigated/compensated).
        * Noise or glare (typically minimal for solar PV).
        * Property values.
    * *Tip: Role-play or think through potential conversations and objections.*

4.  **Option Agreement Key Terms Outline:**
    Research and list the typical key terms found in a solar land option agreement. This could include:
    * **Option Period:** The duration the developer has the exclusive right to evaluate the property (e.g., 1-3 years, with potential extensions).
    * **Option Payment(s):** Compensation to the landowner for granting the option (e.g., per acre, lump sum, annual payments).
    * **Extension Rights & Payments:** Terms for extending the option period if needed.
    * **Exercise Price / Lease Rate:** The agreed-upon payment if the developer exercises the option and leases the land (e.g., $/acre/year, $/MW/year, often with an escalator).
    * **Term of Lease:** Duration of the land lease if the option is exercised (e.g., 20-30 years, plus developer extension options, often totaling 30-50 years).
    * **Permitted Uses by Developer:** Rights granted to the developer during the option and lease periods (e.g., conducting surveys, geotechnical studies, environmental assessments, construction, operation, maintenance, decommissioning).
    * **Landowner Obligations:** Responsibilities of the landowner (e.g., cooperation with permitting, maintaining title, exclusivity – not leasing to other solar developers).
    * **Developer Obligations:** Responsibilities of the developer (e.g., payments, site restoration).
    * **Decommissioning and Site Restoration:** Developer's responsibility to remove equipment and restore the site at the end of the lease term.
    * **Assignment:** Developer's right to assign the agreement to another entity (e.g., a project financing entity or buyer of the project).
    * **Confidentiality.**
    * *Resource: Search for "solar land lease agreement key terms" or "solar option agreement checklist" from legal or industry resources.*

5.  **Prepare Summary Document:**
    Compile the outreach strategy and option agreement term outline into a concise document, as if preparing for an initial landowner engagement campaign or an internal strategy discussion.
    * *Structure: Target Area Profile, Landowner ID Methodology, Outreach Plan (Contact, Talking Points, Concerns), Key Option Agreement Terms, Conclusion.*
""")
st.markdown("---")

# --- Strategic Importance & Alignment ---
st.subheader("🌟 Value Proposition for Candidacy")
st.info( # Using st.info to emphasize the project's impact
    "**Demonstrates Foundational Skills:** This project demonstrates practical thinking about the foundational step of land acquisition and community engagement."
)

st.markdown("""
Origis Energy's ability to develop its extensive pipeline relies on successful landowner negotiations and securing site control.
Showing an understanding of this process, including the importance of *"Collaborative Community Outcomes"* which often begins with positive landowner relations, is highly valuable.

By completing this project, you show:
* An appreciation for the 'people' side of project development.
* Strategic thinking in approaching landowners.
* Familiarity with the critical legal and commercial terms for securing land.
""")

# --- Sidebar for navigation or extra info ---
st.sidebar.header("Project Detail")
st.sidebar.markdown("This page details the **Landowner Outreach & Option Agreement** project idea for a PDM role.")
st.sidebar.markdown("---")
# Example link back if part of a multi-page app structure
# st.sidebar.page_link("your_main_app_file.py", label="Back to PDM Projects Overview", icon="↩️")
st.sidebar.success(f"Content current as of: {pd.Timestamp.now(tz='America/Los_Angeles').strftime('%B %d, %Y')}")

# To run this app:
# 1. Save the code as a Python file (e.g., `pdm_landowner_outreach_app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: `streamlit run pdm_landowner_outreach_app.py`
#
# For a multi-page app structure, you would typically save this in a 'pages'
# directory and Streamlit would handle the navigation.
