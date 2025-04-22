import streamlit as st
import pandas as pd

st.title("Job Market Analysis: Beaverton & Surrounding Areas")
st.markdown("""
Visual overview of local job market for roles aligned with your profile and interests.
""")

# Section 1: Power BI & Data Analyst Roles
st.header("🔍 Focus Area: Power BI & Data Analyst Roles")
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    - **Market Demand & Employers**: Contract and full‑time Power BI / BI Developer and Data Analyst roles across consumer goods, manufacturing, finance, non‑profits, and staffing agencies.
    - **Required Skills**: Power BI, DAX, SQL, data modeling, visualization, critical thinking.
    - **Fit Assessment**: Leverage R&D data experience; build portfolio projects to showcase Power BI & SQL proficiency.
    """)
with col2:
    st.metric(label="Entry-Level Range", value="$60k–$80k")
    st.metric(label="Beaverton Avg Data Analyst", value="$86k–$99k")
    st.metric(label="Portland Avg Data Analyst", value="$77k")

# DataFrame for Role Comparison
df_analyst = pd.DataFrame([
    {
        "Job Title": "Power BI Developer (Entry/Mid)",
        "Salary Range": "$60k–$80k",
        "Core Skills": "Power BI, DAX, SQL, Data Modeling",
        "Communication": "Visual & Written Reports"
    },
    {
        "Job Title": "Data Analyst (Entry/Junior)",
        "Salary Range": "$50k–$65k+",
        "Core Skills": "SQL, Excel, Tableau, Power BI",
        "Communication": "Written & Visual"
    },
    {
        "Job Title": "Business Intelligence Analyst",
        "Salary Range": "$77k–$84k",
        "Core Skills": "BI Tools, Dashboards, Reporting",
        "Communication": "Written & Visual"
    }
])
st.subheader("Role Comparison")
st.dataframe(df_analyst)

# Section 2: Technician Roles
st.header("🛠️ Focus Area: Technician Roles")
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    - **Key Specialties**: IT Support, Lab Technician, Field Service, Maintenance.
    - **Skills**: Troubleshooting, equipment operation, protocols, data recording, customer support.
    - **Fit Assessment**: AAS in Applied Computer Technology aligns well with IT & Lab roles; R&D tech experience directly relevant.
    """)
with col2:
    st.metric(label="IT Technician Avg (OR)", value="$50.6k")
    st.metric(label="Lab Technician Avg (Beaverton)", value="$49k")
    st.metric(label="Field Service Range", value="$52k–$62k")

# DataFrame for Technician Spectrum
df_tech = pd.DataFrame([
    {"Type": "IT Support Technician", "Salary": "$40k–$58k", "Skills": "HW/SW, Networking, Ticketing", "Interaction": "User Support"},
    {"Type": "Lab Technician", "Salary": "$40k–$53k", "Skills": "Equipment, Protocols, QC", "Interaction": "Task-Focused"},
    {"Type": "Field Service Technician", "Salary": "$52k–$62k", "Skills": "Installation, Repair", "Interaction": "Customer"},
    {"Type": "Maintenance Technician", "Salary": "$52k–$58k", "Skills": "Repairs, Upkeep", "Interaction": "Task-Focused"}
])
st.subheader("Technician Job Spectrum")
st.dataframe(df_tech)

# Section 3: Salesforce Administrator
st.header("⚡ Focus Area: Salesforce Administrator")
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    - **Leverage Credentials**: Salesforce Certified Administrator + hands-on internship.
    - **Typical Duties**: User management, custom objects, Flows, reports, dashboards, data management.
    - **Fit Assessment**: Direct alignment; strong salary potential; aim for roles $70k+ and negotiate.
    """)
with col2:
    st.metric(label="Portland Avg Admin", value="$90.8k")
    st.metric(label="Beaverton Senior Admin", value="$103.6k")
    st.metric(label="Entry-Level Range", value="$70k–$80k")

# Section 4: Other Avenues
st.header("🚀 Other Potential Avenues")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Operations Analyst Avg", value="$73k")
    st.write("Leverage process improvement & data skills.")
with col2:
    st.metric(label="Business Analyst Avg", value="$88k")
    st.write("Workflows, system support, stakeholder analysis.")
with col3:
    st.metric(label="Marketing & Analytics Avg", value="$52k–$95k")
    st.write("Combine marketing degree with analytics.")

st.markdown("""
**Tip**: Explore portfolio projects and certifications to showcase skills visually—dashboards, sample reports, or interactive demos.
""")
