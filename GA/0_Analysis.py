import streamlit as st

# --- Main Title ---
st.title("2. Profile Analysis (SWOT)")

st.divider()

# --- Introductory Text ---
st.markdown("""
A thorough analysis of the candidate's resume reveals a strong foundation but also areas requiring strategic positioning.
The following SWOT analysis breaks down these aspects:
""")

# --- SWOT Analysis using Expanders ---
# Using expanders helps manage the large amount of text and keeps the page clean.

# --- Strengths ---
with st.expander("💪 Strengths", expanded=True): # Keep strengths expanded by default
    st.markdown("""
    * **Diverse Industry Exposure:** Experience spans **management consulting** (BCG, PwC Strategy&), **energy** (Tetra Tech, WIEB fellowship), **real estate development** (Self-employed), and **financial services** (consulting projects). Demonstrates adaptability and broad knowledge.
    * **Project Management Expertise:** Direct experience in PM roles (Deputy PM @ Tetra Tech, PM for family projects) including **scope, schedule, budget management, task management, financial tracking, quality management, and PMO contributions**. Managed multiple projects (**$1MM total contract value** @ Tetra Tech) and coordinated large stakeholder groups (**80+** @ BCG, **100+** @ PwC).
    * **Consulting Skillset:** Proven ability in **analysis** (operational, financial, ESG), **process mapping/improvement**, **strategy development** (growth, go-to-market, transformation roadmaps), **stakeholder management**, and developing client-facing materials (playbooks, business cases) gained at top-tier firms (**BCG, PwC Strategy&**).
    * **Quantitative & Analytical Skills:** Experience building **financial models** (Excel underwriting for 30+ properties), conducting **due diligence**, analyzing data for cost savings (**30% savings identified**), identifying value creation opportunities (**$123-185MM net income growth identified**), and performing **bid analysis**. Professional proficiency in **Excel**.
    * **Sourcing & Procurement Experience:** Direct experience executing **RFP processes, negotiation, bid analysis, and subcontractor management** (@ Tetra Tech). Analysis of lease vs. buy models.
    * **Business Development Acumen:** Supported **proposal development** (~30 proposals) leading to significant project sales (~$400K @ Tetra Tech). Experience developing **business cases** and identifying **value creation levers**.
    * **Education & Certifications:** Strong academic background (Multiple Master's - **Stanford**, Law - **Minho**; BA - **UPenn**, Magna cum laude, Phi Beta Kappa). Relevant certifications: **OSHA-10**, Construction PM certificate, **PMP (in progress)**.
    * **Language Skills:** Fluency in **English, Spanish, and Portuguese** - a significant asset.
    * **Software Proficiency:** Professional proficiency in **Excel, PowerPoint, Microsoft Project**; relevant tools (**Bluebeam Revu, Google Earth**); basic **SQL, Visio**.
    """)

# --- Weaknesses ---
with st.expander("🤔 Weaknesses"):
    st.markdown("""
    * **Recent Layoff:** Termination from Tetra Tech (downsizing) requires careful explanation.
    * **Varied Career Path:** Diverse experience needs a clear narrative to avoid perception of lacking deep specialization.
    * **Shorter Tenures:** Some recent roles (Tetra Tech, PwC Strategy&) have relatively short durations requiring context.
    * **"Associate" Titles:** Recent consulting titles may need positioning for more senior roles or the **$100k+ salary target** outside consulting structures.
    """)

# --- Opportunities ---
with st.expander("✨ Opportunities"):
    st.markdown("""
    * **High-Demand Skills:** **Project management, data analysis, ESG knowledge, process improvement** are highly sought after.
    * **Target Industries Growth:** **Energy transition/renewables, Fintech, infrastructure/construction** sectors are growing.
    * **NYC Market:** Major hub for **Finance, Consulting, Tech, Energy/Sustainability**.
    * **Language Skills:** Spanish/Portuguese fluency valuable for roles with **Latin American focus** or multinational companies.
    * **PMP Certification:** Completion will significantly bolster **project management credentials**.
    * **ESG Focus:** Experience with **ESG analysis** (BCG) and **energy fellowship** (WIEB) aligns with growing demand.
    """)

# --- Threats ---
with st.expander("⚠️ Threats"):
    st.markdown("""
    * **Competitive NYC Market:** Attracts top talent, leading to high competition.
    * **Economic Uncertainty:** Potential for hiring freezes or downsizing (as experienced).
    * **Perception of "Job Hopping":** Sequence of roles could be misinterpreted without a strong narrative.
    * **Salary Expectations:** **\$100k+ minimum** requires targeting commensurate roles, potentially in higher-paying sectors (Finance, Consulting) or Senior PM roles.
    """)

st.divider()
st.caption("This SWOT analysis informs the strategic recommendations that follow.")

# --- How to Run ---
# Add comments explaining how to execute the Streamlit app
# To run this app:
# 1. Save the code as a Python file (e.g., `nyc_swot_app.py`).
# 2. Ensure you have Streamlit installed (`pip install streamlit`).
# 3. Open your terminal or command prompt.
# 4. Navigate to the directory where you saved the file.
# 5. Run the command: `streamlit run nyc_swot_app.py`
