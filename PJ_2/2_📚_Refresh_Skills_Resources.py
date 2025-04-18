import streamlit as st

# Set page configuration
#st.set_page_config(page_title="Refresh Skills & Knowledge", layout="wide")

# --- Page Title and Introduction ---
st.title("📚 Refresh Your Accounting Knowledge and Skills")
st.markdown("""
After time away from the accounting field, proactively updating your knowledge and technical skills is essential.
The profession evolves with new standards, regulations, and technologies. This page provides resources
to help you get current in key areas. Explore the tabs below for curated links and information.
""")
st.divider()

# --- Create Tabs for Different Skill Areas ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Principles & Standards",
    "💻 Technology & Software",
    "🎓 CPE & Courses",
    "📖 Self-Study Resources"
])

# --- Tab 1: Principles & Standards ---
with tab1:
    st.header("Accounting Principles & Standards (GAAP & Tax)")
    st.markdown("""
    Accounting standards (like U.S. GAAP) and tax laws change over time. Familiarizing yourself with major updates from the last decade is crucial. Key areas include:

    * **Revenue Recognition (ASC 606):** A major overhaul affecting how companies recognize revenue from contracts with customers.
    * **Lease Accounting (ASC 842):** Significantly changed how leases are recorded on the balance sheet for most companies.
    * **Tax Law Changes:** Various acts (like the Tax Cuts and Jobs Act, Inflation Reduction Act) have impacted corporate and individual taxes, credits, and deductions.

    **Key Resources:**
    * **[FASB Accounting Standards Codification®](https://fasb.org/page/PageContent?pageId=/staticpages/codification-access.html&isStaticPage=true)**: The official source of U.S. GAAP. Basic view is free, Professional View requires a subscription (or may be available via [AAA Academic Access](https://aaahq.org/Research/FASB-Codification-and-GARS-Online-Q-A) if affiliated with a university).
    * **[AICPA Standards & Statements](https://www.aicpa-cima.com/resources/landing/standards-and-statements)**: Provides access to AICPA professional standards (Auditing, Attestation, Code of Conduct, etc.). Summaries of recent FASB ASUs may be found in AICPA publications or CPE.
    * **[AICPA & CIMA A&A Focus Newsletter](https://www.journalofaccountancy.com/newsletters/a-a-focus.html)**: Often includes summaries and discussions of recent accounting standard updates (like the [2024 ASU rundown example](https://www.journalofaccountancy.com/newsletters/a-a-focus/a-a-focus-recap-quality-management-faqs-and-a-2024-asu-rundown.html)).
    * **Major Accounting Firm Resources:** Firms like Deloitte, PwC, EY, KPMG often publish free summaries and insights on recent standards updates on their websites (search for "[Firm Name] accounting technical library" or "technical updates").
    * **[IRS Inflation Reduction Act of 2022 Page](https://www.irs.gov/inflation-reduction-act-of-2022)**: Official IRS resource detailing tax law changes and resources related to this significant act.
    * **[IRS Newsroom - Businesses](https://www.irs.gov/newsroom/businesses)**: General resource for recent tax law updates affecting businesses.
    * **Continuing Professional Education (CPE):** Taking update courses on GAAP or Tax is a highly effective way to learn (see CPE & Courses tab).
    """)

# --- Tab 2: Technology & Software ---
with tab2:
    st.header("Technology & Software Skills")
    st.markdown("""
    Proficiency in current accounting software and related technology is expected in most roles. Key areas include:

    * **Spreadsheet Software (Excel):** Advanced skills are often required beyond basic data entry. Focus on:
        * Formulas: `XLOOKUP`/`VLOOKUP`, `SUMIFS`/`COUNTIFS`, `INDEX`/`MATCH`, logical functions (`IF`, `AND`, `OR`).
        * Data Analysis: PivotTables, Pivot Charts, Sorting/Filtering, Conditional Formatting.
        * Data Management: Power Query (for data cleaning/transformation), basic Macros (optional but helpful).
        * **Resource:** [Microsoft Learn - Training](https://learn.microsoft.com/en-us/training/) (Search for Excel courses).
        * **Certification:** [Microsoft Office Specialist (MOS) Expert for Excel](https://learn.microsoft.com/en-us/credentials/certifications/mos-excel-expert-2019/) (demonstrates advanced competency).
    * **Accounting Software (Small/Medium Business Focus):**
        * **QuickBooks (Desktop & Online):** Extremely common for SMBs. Understand the differences.
        * **Resource:** [QuickBooks Training & Certification (Official Intuit Site)](https://quickbooks.intuit.com/accountants/training-certification/) - Offers free training and certification for accountants (ProAdvisor Program).
    * **Enterprise Resource Planning (ERP) Systems:** Used by larger organizations to integrate various business functions. Knowledge is often specific to the employer, but familiarity is a plus.
        * Examples: Oracle NetSuite, SAP S/4HANA, Microsoft Dynamics 365 Business Central/Finance.
        * **Resources:** Training is usually extensive and often provided by employers or specialized consultants. Official vendor sites offer learning paths (often paid): [Oracle University](https://education.oracle.com/), [SAP Training](https://training.sap.com/), [Microsoft Learn (for Dynamics)](https://learn.microsoft.com/en-us/training/).
    * **Data Analytics & Visualization Tools:** Increasingly important for analyzing financial data.
        * Examples: Tableau, Microsoft Power BI.
        * **Resources:** Vendor websites (Tableau Learning, Microsoft Power BI Learning Paths on Microsoft Learn), online course platforms.
    """)

# --- Tab 3: Continuing Education (CPE) & Courses ---
with tab3:
    st.header("Continuing Education (CPE) & Formal Courses")
    st.markdown("""
    Structured courses are an excellent way to refresh knowledge, learn new standards/technologies, and potentially earn CPE credits (required for active CPAs, but courses are open to all).

    **Local Portland, Oregon Resources:**
    * **[Oregon Society of CPAs (OSCPA) CPE Catalog](https://www.orcpa.org/cpe)**: Offers a wide variety of courses (live, webcast, self-study) on accounting, tax, ethics, technology, etc., relevant to Oregon professionals.
    * **[Portland Community College (PCC) Accounting Programs](https://www.pcc.edu/programs/accounting/)**: Offers degrees and certificates, including an **Accelerated Accounting Certificate** (less than 1 year) good for refreshing fundamentals and learning relevant tech (Excel, payroll). Also offers prerequisites if needed for university programs.
    * **[Portland State University (PSU) Post-Baccalaureate Accounting Certificate](https://www.pdx.edu/academics/programs/undergraduate/accounting-postbaccalaureate-certificate)**: Designed for those with a non-accounting bachelor's degree needing credits for the CPA exam or seeking a career change. Strong local reputation.
    * **Linfield University Online Accounting Certificate**: Another post-baccalaureate option available online ([Check Linfield OCE website for details](https://www.linfield.edu/)).

    **National CPE Providers & Platforms:**
    * **[AICPA & CIMA CPE & Learning](https://www.aicpa-cima.com/cpe-learning)**: Official store for AICPA CPE, including self-study, webcasts (Webcast Pass), and certificate programs (Data Analytics, Cybersecurity, PFP, etc.). Check out **CPExpress** for short, targeted courses.
    * **[The CPE Store](https://www.cpestore.com/)**: NASBA-approved provider with courses accepted in many states.
    * **[CPAacademy.org](https://www.cpaacademy.org/)**: Popular platform often featuring free CPE webinars sponsored by various providers (quality varies, but great for specific topic updates).
    * **Other Major Providers:** Surgent CPE, Becker CPE, Gleim CPE often offer extensive catalogs (check their websites).
    * **Online Course Platforms (MOOCs):**
        * **Coursera / edX:** Offer university-level courses in accounting and finance, often from reputable institutions. Search for topics like "Intermediate Accounting," "Financial Statement Analysis," etc.
        * **LinkedIn Learning / Udemy:** Provide practical, skill-based courses on software (Excel, QuickBooks), specific accounting topics, and business skills.
    """)

# --- Tab 4: Self-Study Resources ---
with tab4:
    st.header("Self-Study Resources")
    st.markdown("""
    Supplement formal learning with ongoing self-study to stay current.

    **Professional Publications & News:**
    * **[Journal of Accountancy](https://www.journalofaccountancy.com/)**: AICPA's flagship publication covering accounting, auditing, tax, finance, and technology news (Online access generally included with AICPA membership).
    * **[FM Magazine](https://www.fm-magazine.com/)**: Focuses on management accounting topics, published by AICPA & CIMA (access often requires membership).
    * **[The Tax Adviser](https://www.thetaxadviser.com/)**: AICPA publication focused on tax planning and strategy (access often requires AICPA Tax Section membership).
    * **[Accounting Today](https://www.accountingtoday.com/)**: Leading trade publication and website covering news impacting the accounting profession. Offers newsletters.
    * **Major Firm Websites:** Again, check the "Insights," "Library," or "Technical Resources" sections of firms like Deloitte, PwC, EY, KPMG for articles and analysis.

    **Networking & Communities:**
    * **Professional Associations:** Engaging with OSCPA, IMA, AFWA, IIA (see Networking page/section) provides access to discussions, newsletters, and insights from peers.
    * **LinkedIn Groups:** Join groups focused on accounting, finance, specific software (QuickBooks), or Oregon professionals.

    **Other Resources:**
    * **Accounting Podcasts/Blogs:** Search for podcasts covering accounting news, career advice, or specific niches (e.g., cloud accounting, tax updates).
    * **Books:** Review classic accounting textbooks or find recent books on specific topics of interest.

    **Simple Checklist for Self-Study Exploration:**
    """)
    # Simple interactive checklist
    if 'explore_joa' not in st.session_state: st.session_state.explore_joa = False
    if 'explore_at' not in st.session_state: st.session_state.explore_at = False
    if 'explore_firm' not in st.session_state: st.session_state.explore_firm = False
    if 'explore_podcast' not in st.session_state: st.session_state.explore_podcast = False
    if 'explore_linkedin' not in st.session_state: st.session_state.explore_linkedin = False

    st.checkbox("Browse Journal of Accountancy / FM Magazine articles", key="explore_joa")
    st.checkbox("Sign up for Accounting Today newsletter", key="explore_at")
    st.checkbox("Check a major accounting firm's 'Insights' section", key="explore_firm")
    st.checkbox("Find & listen to an accounting-related podcast episode", key="explore_podcast")
    st.checkbox("Join a relevant LinkedIn Group", key="explore_linkedin")

st.divider()
st.markdown("Refreshing your skills is an ongoing process. Start with the areas most relevant to your target roles and gradually expand your knowledge.")