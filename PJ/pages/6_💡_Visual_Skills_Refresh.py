import streamlit as st

# Set page configuration
st.set_page_config(page_title="Visual Skills Refresh", layout="wide")

# --- Page Title and Introduction ---
st.title("💡 Visual Guide: Refreshing Your Skills")
st.markdown("""
Stay current! The accounting world changes fast. Use these resources to update your knowledge
in key areas like standards, tech, and continuous learning. Click the buttons to explore resources.
""")
st.divider()

# --- Section 1: Principles & Standards ---
st.header("📜 Principles & Standards Updates")
st.markdown("Catch up on significant changes in GAAP and Tax Law.")

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("📊 U.S. GAAP Updates")
        st.markdown("""
        * **Key Areas:** Revenue Recognition (ASC 606), Leases (ASC 842).
        * **Goal:** Understand major shifts in financial reporting.
        """)
        st.link_button("FASB Codification (Official Source)", "https://fasb.org/page/PageContent?pageId=/staticpages/codification-access.html&isStaticPage=true", help="Basic view free; Pro view paid or via AAA Academic Access")
        st.link_button("AICPA Standards Overview", "https://www.aicpa-cima.com/resources/landing/standards-and-statements")
        st.markdown("*Tip: Search major CPA firm websites (Deloitte, PwC, etc.) for free technical update summaries.*")

with col2:
    with st.container(border=True):
        st.subheader("🏛️ Tax Law Updates")
        st.markdown("""
        * **Key Areas:** TCJA impacts, Inflation Reduction Act credits/changes.
        * **Goal:** Understand current business & individual tax landscape.
        """)
        st.link_button("IRS Inflation Reduction Act Hub", "https://www.irs.gov/inflation-reduction-act-of-2022")
        st.link_button("IRS Business Newsroom", "https://www.irs.gov/newsroom/businesses")
        st.markdown("*Tip: Tax-specific CPE courses are highly recommended for deep dives.*")

st.divider()

# --- Section 2: Technology & Software ---
st.header("💻 Technology & Software Skills")
st.markdown("Master the tools employers expect you to know.")

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("📊 Excel (Advanced)")
        st.markdown("""
        * **Focus:** PivotTables, XLOOKUP, Power Query, Key Formulas (`SUMIFS`, `INDEX/MATCH`).
        * **Goal:** Efficient data manipulation & analysis.
        """)
        st.link_button("Microsoft Learn (Excel)", "https://learn.microsoft.com/en-us/training/excel")
        # Placeholder link below, update if necessary for current exam version
        st.link_button("MOS Expert Cert Info", "https://learn.microsoft.com/en-us/credentials/certifications/mos-excel-expert-2019/", help="Demonstrates advanced competency")

    with st.container(border=True):
        st.subheader("📈 Data Analytics Tools")
        st.markdown("""
        * **Examples:** Tableau, Microsoft Power BI.
        * **Goal:** Visualize & interpret financial data trends.
        """)
        st.link_button("Microsoft Learn (Power BI)", "https://learn.microsoft.com/en-us/training/powerplatform/power-bi")
        st.link_button("Tableau Learning", "https://www.tableau.com/learn")


with col2:
    with st.container(border=True):
        st.subheader("🧾 QuickBooks (Desktop/Online)")
        st.markdown("""
        * **Focus:** Core features for SMB accounting. Free ProAdvisor training available.
        * **Goal:** Manage books efficiently for small/medium businesses.
        """)
        st.link_button("QB Training & Certification", "https://quickbooks.intuit.com/accountants/training-certification/")

    with st.container(border=True):
        st.subheader("⚙️ ERP Systems (Awareness)")
        st.markdown("""
        * **Examples:** NetSuite, SAP, Dynamics 365.
        * **Goal:** Understand integrated systems used by larger companies (often learned on-the-job).
        """)
        st.link_button("Oracle NetSuite Training", "https://education.oracle.com/netsuite-training") # Example link
        st.link_button("SAP Training", "https://training.sap.com/")
        st.link_button("MS Dynamics 365 Learn", "https://learn.microsoft.com/en-us/training/dynamics365")


st.divider()

# --- Section 3: Learning Resources ---
st.header("🎓 Courses, CPE & Self-Study")
st.markdown("Leverage structured learning and ongoing resources.")

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("🏛️ Local OR Resources")
        st.markdown("""
        * **OSCPA:** Courses tailored for Oregon CPAs.
        * **PCC:** Accelerated Cert for fundamentals & tech.
        * **PSU/Linfield:** Post-Bacc Certs for CPA path.
        """)
        st.link_button("OSCPA CPE Catalog", "https://www.orcpa.org/cpe")
        st.link_button("PCC Accounting Programs", "https://www.pcc.edu/programs/accounting/")
        st.link_button("PSU Post-Bacc Acct Cert", "https://www.pdx.edu/academics/programs/undergraduate/accounting-postbaccalaureate-certificate")

    with st.container(border=True):
        st.subheader("🌐 National CPE & Certs")
        st.markdown("""
        * **AICPA:** Official CPE, Webcast Pass, Certificates.
        * **CPAacademy:** Often has free webinars.
        * **Others:** Surgent, Becker, Gleim, CPE Store.
        """)
        st.link_button("AICPA CPE & Learning", "https://www.aicpa-cima.com/cpe-learning")
        st.link_button("CPAacademy.org", "https://www.cpaacademy.org/")
        # Add links to others if desired

with col2:
    with st.container(border=True):
        st.subheader("📰 Publications & News")
        st.markdown("""
        * **Journals:** JoA, FM Mag, Tax Adviser (AICPA).
        * **News Sites:** Accounting Today.
        * **Firm Insights:** Check Big 4/Large firm websites.
        """)
        st.link_button("Journal of Accountancy", "https://www.journalofaccountancy.com/")
        st.link_button("Accounting Today", "https://www.accountingtoday.com/")
        # Add links to others if desired

    with st.container(border=True):
        st.subheader("🖥️ Online Courses / Other")
        st.markdown("""
        * **Platforms:** Coursera, edX, LinkedIn Learning, Udemy.
        * **Networks:** OSCPA/IMA forums, LinkedIn Groups.
        * **Media:** Accounting podcasts/blogs.
        """)
        # Add direct links to platforms if useful
        st.link_button("Coursera", "https://www.coursera.org/")
        st.link_button("LinkedIn Learning", "https://www.linkedin.com/learning/")


# --- Self-Study Checklist ---
st.divider()
with st.container(border=True):
    st.subheader("🚀 Your Self-Study Action Checklist")
    st.markdown("Check off items as you explore these ongoing learning methods:")

    # Initialize state if not already present
    if 'v_explore_joa' not in st.session_state: st.session_state.v_explore_joa = False
    if 'v_explore_at' not in st.session_state: st.session_state.v_explore_at = False
    if 'v_explore_firm' not in st.session_state: st.session_state.v_explore_firm = False
    if 'v_explore_podcast' not in st.session_state: st.session_state.v_explore_podcast = False
    if 'v_explore_linkedin' not in st.session_state: st.session_state.v_explore_linkedin = False
    if 'v_explore_cpe' not in st.session_state: st.session_state.v_explore_cpe = False

    st.checkbox("Browse Journal of Accountancy / FM Magazine", key="v_explore_joa")
    st.checkbox("Check Accounting Today Website/Newsletter", key="v_explore_at")
    st.checkbox("Review a Major CPA Firm's 'Insights' Section", key="v_explore_firm")
    st.checkbox("Find/Listen to an Accounting Podcast", key="v_explore_podcast")
    st.checkbox("Join/Explore a Relevant LinkedIn Group", key="v_explore_linkedin")
    st.checkbox("Browse OSCPA or AICPA CPE Catalog for relevant courses", key="v_explore_cpe")


st.divider()
st.success("✅ Continuous learning is key! Focus on the areas most relevant to your target roles first.")