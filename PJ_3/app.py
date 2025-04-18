# filename: app.py
import streamlit as st

# --- Page Functions (Content copied and adapted from original files) ---

def page_roadmap():
    st.title("📖 Roadmap to Re-Entering Accounting")
    st.markdown("""
    Welcome! This guide helps you navigate returning to the accounting field, particularly in the Portland, OR area.
    Work through the sections sequentially using the navigation on the left.
    **You must mark a page as reviewed using the checkbox at the bottom to unlock the next page.**
    """)
    st.divider()
    st.header("Guide Overview")
    st.markdown("""
    This application guides you through the key steps:

    1.  **Evaluate Career Goals:** Decide between CPA and Non-CPA paths.
    2.  **Understand Credentials:** Explore requirements for new CPAs, reactivation, or alternatives.
    3.  **Refresh Skills:** Identify areas to update (standards, tech) and find resources.
    4.  **Gain Experience:** Strategies to bridge the experience gap.
    5.  **Network:** Rebuild connections in the Portland area.
    6.  **Update Resume:** Craft your story and optimize your resume.
    7.  **Job Search:** Launch a targeted search.

    Use the navigation menu to move through each topic. Remember to mark each page as reviewed to proceed.
    """)
    st.success("Start by navigating to '1. Career Goal Evaluation'.")


def page_career_goals():
    # --- Content from PJ/pages/1_🎯_Career_Goal_Evaluation.py ---
    st.title("🎯 1. Evaluate Your Career Goals (CPA vs. Non-CPA)")
    st.markdown("""
    Choosing whether to pursue the Certified Public Accountant (CPA) license is a crucial first step
    in re-entering the accounting field after a break. This decision significantly impacts your required education,
    potential job roles, study commitment, and long-term career trajectory.

    This page will help you:
    1.  Understand the details of the CPA and Non-CPA paths.
    2.  Reflect on your own priorities and preferences through interactive questions.
    3.  See which path might align better with *your* specific goals.
    """)
    st.divider()

    # --- Detailed Path Information ---
    st.header("Understanding the Paths")

    col1, col2 = st.columns(2, gap="large") # Add gap between columns

    with col1:
        st.subheader("📜 The CPA Path")
        st.markdown("""
        The CPA is the **premier license** in the accounting profession, highly respected and often required for certain roles and advancement.

        * **Key Benefits:**
            * Access to higher-level leadership roles (Controller, Director, VP Finance, CFO).
            * Required to sign audit reports, essential for public accounting careers (Audit/Assurance).
            * Enhanced professional credibility and recognition.
            * Often leads to higher earning potential over a career.
            * Strong professional network access (AICPA, State Societies).
        * **Requirements & Challenges:**
            * **Rigorous Exam:** Must pass the 4-part Uniform CPA Examination.
            * **Education:** Specific requirements, typically 150 semester hours including defined accounting/business courses (check your state's rules - e.g., Oregon).
            * **Experience:** Usually 1-2 years of relevant, supervised accounting experience.
            * **Time/Cost:** Significant investment needed for exam prep courses, fees, and study time (often 300-500+ hours).
            * **Maintenance:** Ongoing Continuing Professional Education (CPE) required annually/biennially.
        * **Typical Roles:**
            * Public Accounting: Auditor, Tax Accountant, Consultant/Advisor (all levels up to Partner).
            * Industry: SEC Reporting Manager, Technical Accounting Manager, Corporate Controller, Internal Audit Director, CFO.
            * Specialized: Forensic Accountant, Governmental Auditor (some roles).
        """)

    with col2:
        st.subheader("💼 The Non-CPA Path")
        st.markdown("""
        A vast number of valuable and rewarding accounting roles exist that do not require CPA licensure.

        * **Key Benefits:**
            * Potentially faster entry into certain roles (e.g., Staff Accountant, Bookkeeper) without the immediate CPA hurdles.
            * Focus can be on specific industry knowledge or practical skills.
            * Flexibility to pursue **alternative certifications** tailored to interests (e.g., CMA for management accounting, EA for tax, CIA for internal audit, CFE for fraud, QuickBooks ProAdvisor).
            * Essential roles in small/medium businesses (SMBs), non-profits, government, and specific corporate functions.
        * **Potential Limitations:**
            * May encounter barriers to the very highest leadership positions (e.g., CFO in large public companies) or partnership in CPA firms.
            * Cannot sign audit reports or perform certain regulated attest functions.
            * Title restrictions (cannot use "CPA").
        * **Typical Roles:**
            * Core Accounting: Bookkeeper (Full-Charge), Accounts Payable/Receivable Specialist/Manager, Payroll Specialist/Manager, Staff Accountant, Senior Accountant, Accounting Manager (especially SMBs/non-profits).
            * Analysis/Corporate: Financial Analyst, Cost Accountant, Budget Analyst.
            * Specialized: Internal Auditor (CIA helpful), Tax Preparer (EA credential helpful), Fund Accountant, Grant Accountant (Non-Profit), Government Accountant/Auditor (CGFM/CDFM helpful).
        """)
    st.divider()

    # --- Interactive Decision Helper ---
    st.header("🤔 Which Path Aligns Best With You?")
    st.markdown("Answer the questions below to get personalized insights based on your preferences. There are no right or wrong answers!")

    # Use a dictionary to store answers if needed, or process directly
    answers = {}
    feedback_points = [] # List to collect feedback messages

    with st.container(border=True): # Add a border around the questionnaire
        st.subheader("Your Career Ambitions & Preferred Environment")

        answers['ambition'] = st.radio(
            "**Ambition:** What level of leadership or type of role is your *primary* long-term goal?",
            options=[
                "Top Executive (e.g., CFO/Partner in large org)",
                "Department/Team Lead (e.g., Controller/Manager)",
                "Skilled Specialist / Individual Contributor",
                "Own My Own Practice (Bookkeeping/Tax/Consulting)",
                "Stable role in Government / Non-Profit",
                "Still Exploring / Unsure"
            ],
            index=None, # Start with no selection
            key="pg1_q_ambition", # Unique key prefix
            help="Consider where you see yourself in 10-15 years."
        )

        answers['environment'] = st.radio(
            "**Environment:** Which work setting most appeals to you?",
            options=[
                "Large Public Accounting Firm",
                "Corporate (Medium-Large Company)",
                "Small-Medium Business (SMB)",
                "Government Agency",
                "Non-Profit Organization",
                "Flexible / Remote / Self-Employed"
            ],
            index=None,
            key="pg1_q_environment", # Unique key prefix
            help="Think about company size, culture, and type of work."
        )

        # --- Feedback generation (simple examples) ---
        if answers['ambition'] == "Top Executive (e.g., CFO/Partner in large org)":
            feedback_points.append("📈 High ambition often aligns with the CPA path.")
        if answers['environment'] == "Large Public Accounting Firm":
            feedback_points.append("🏢 Public accounting strongly favors the CPA license.")
        if answers['environment'] in ["Small-Medium Business (SMB)", "Non-Profit Organization"]:
             feedback_points.append("🌱 SMBs/Non-Profits frequently utilize skilled Non-CPAs.")

    with st.container(border=True):
        st.subheader("Study, Exams, and Task Preferences")

        answers['commitment'] = st.select_slider(
            "**Commitment:** Realistically, how willing *and* able are you to dedicate significant time (500+ hrs over 1-2 yrs) and resources to intense study and exams *right now*?",
            options=["Low", "Medium", "High"],
            key="pg1_q_commitment", # Unique key prefix
            help="Be honest about your current capacity and motivation for this level of effort."
        )

        answers['tasks'] = st.multiselect(
            "**Interest:** Which specific accounting areas genuinely interest you the most?",
            options=[
                "Auditing & Assurance", "Tax Preparation & Strategy", "Financial Reporting & Compliance",
                "Management Accounting (Budgets, Costs)", "Bookkeeping & Payroll Operations",
                "Financial Planning & Analysis (FP&A)", "Fraud Investigation / Forensics", "IT Audit / Systems"
            ],
            key="pg1_q_tasks", # Unique key prefix
            help="Select all that apply. What kind of work do you enjoy?"
        )

        # --- Feedback generation ---
        if answers['commitment'] == "Low":
            feedback_points.append("⏳ Lower study commitment points towards the Non-CPA path initially.")
        elif answers['commitment'] == "High":
            feedback_points.append("✅ High commitment makes the CPA path feasible.")
        if "Auditing & Assurance" in answers['tasks']:
            feedback_points.append("🔍 Audit interest strongly suggests the CPA path.")
        if "Bookkeeping & Payroll Operations" in answers['tasks']:
            feedback_points.append("🧾 Bookkeeping/Payroll are core Non-CPA activities.")

    # --- Display Combined Feedback ---
    st.divider()
    st.header("💡 Your Personalized Insights")

    if not answers.get('ambition') or not answers.get('environment') or not answers.get('commitment'):
         st.warning("👈 Please answer all the questions above to generate your personalized insights.")
    else:
        st.markdown("Based on your selections, here are some points to consider:")
        if not feedback_points:
            st.info("Explore the detailed descriptions above and consider discussing with a mentor.")
        else:
            for point in feedback_points:
                st.info(point) # Display feedback

        # Simple leaning indicator
        cpa_score = 0
        if answers['ambition'] == "Top Executive (e.g., CFO/Partner in large org)": cpa_score +=1
        if answers['environment'] == "Large Public Accounting Firm": cpa_score += 1
        if answers['commitment'] == "High": cpa_score += 1
        if "Auditing & Assurance" in answers['tasks']: cpa_score +=1
        if answers['commitment'] == "Low": cpa_score -= 1
        if answers['environment'] in ["Small-Medium Business (SMB)", "Non-Profit Organization"]: cpa_score -= 1
        if "Bookkeeping & Payroll Operations" in answers['tasks']: cpa_score -= 1

        st.markdown("---")
        if cpa_score > 0:
             st.success("**Overall Leaning:** Your answers suggest leaning towards the **CPA path**.")
        elif cpa_score < 0:
             st.success("**Overall Leaning:** Your answers suggest leaning towards the **Non-CPA path**.")
        else:
             st.success("**Overall Leaning:** Your preferences show balance. Consider your most critical factors.")


def page_visual_career_paths():
    # --- Content from PJ/pages/5_✨_Career_Paths.py ---
    st.title("✨ Visual Career Path Evaluation: CPA vs. Non-CPA")
    st.markdown("Compare the two main accounting career paths at a glance and see which aligns with your goals.")
    st.caption("This provides a visual summary of the information on the previous page.")
    st.divider()

    # --- Side-by-Side Visual Comparison ---
    st.header("Comparing the Paths")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("📜 The CPA Path")
        st.markdown("**The Premier Accounting License**")
        st.markdown("---")
        st.markdown("##### ✅ Key Benefits:")
        st.markdown("""
        * 📈 Access Higher Leadership (Controller, CFO)
        * 🏢 Essential for Public Accounting Firms (Audit)
        * ⭐ Enhanced Credibility & Recognition
        * 💰 Often Higher Long-Term Earning Potential
        * 🌐 Strong Professional Network (AICPA, etc.)
        """)
        st.markdown("##### ⚠️ Requirements & Challenges:")
        st.markdown("""
        * 📚 Rigorous 4-Part Uniform Exam
        * 🎓 150-Hour Education Rule (State Specific)
        * ⏳ 1-2 Years Supervised Experience
        * ⏰ Significant Study Time (300-500+ hrs) & Cost
        * 🔄 Ongoing CPE (Continuing Education) Needed
        """)
        st.markdown("##### 👨‍💼 Typical Roles:")
        st.markdown("""
        * **Public Accounting:** Auditor, Tax Pro, Consultant
        * **Industry:** Controller, SEC Reporting, CFO, Internal Audit Lead
        * **Specialized:** Forensic Accountant, Gov Auditor
        """)

    with col2:
        st.subheader("💼 The Non-CPA Path")
        st.markdown("**Diverse & Essential Accounting Roles**")
        st.markdown("---") # Separator line
        st.markdown("##### ✅ Key Benefits:")
        st.markdown("""
        * 🚀 Potentially Faster Entry to Some Roles
        * 🎯 Focus on Specific Skills / Industry Niche
        * 📜 Option for Other Certs (CMA, EA, CIA, CFE...)
        * 🏢 Vital in SMBs, Non-Profits, Government
        * 🛠️ Less Intensive Initial Requirements (No CPA Exam/150hr)
        """)
        st.markdown("##### ⚠️ Potential Limitations:")
        st.markdown("""
        * ⛔ Barriers to Top Exec Roles (Large Co.) / Partner
        * 🚫 Cannot Sign Audit Reports (Attest Functions)
        * 🏷️ Title Restriction (Cannot use "CPA")
        """)
        st.markdown("##### 👨‍💼 Typical Roles:")
        st.markdown("""
        * **Core:** Bookkeeper, AP/AR, Payroll, Staff/Senior Acct.
        * **Mgmt/Analysis:** Acct. Manager (SMB), Fin. Analyst, Cost Acct.
        * **Specialized:** Internal Auditor (CIA), Tax Preparer (EA), Grant Acct.
        """)


def page_credentials_pathway():
    # --- Content from PJ/pages/7_🎓_Credentials_Pathway.py ---
    st.title("🎓 2. Address Education & Credential Gaps")
    st.markdown("""
    Choosing the right credential path is key after a career break. Are you aiming for a **New CPA License**,
    **Reactivating an Old One**, or focusing on a **Non-CPA Role** (perhaps with alternative certifications)?

    Select your situation below to explore the specific requirements and recommended next steps.
    """)
    st.divider()

    # --- Interactive Choice ---
    path_options = [
        "I want to become a **New CPA**.",
        "I need to **Reactivate a Lapsed/Inactive CPA License**.",
        "I'm pursuing a **Non-CPA Path** (maybe with alternative certifications)."
    ]

    # Use session state to remember the choice
    if 'credential_path_choice' not in st.session_state:
        st.session_state.credential_path_choice = None

    # Store the choice from radio button directly into session state
    # Make key unique
    st.session_state.credential_path_choice = st.radio(
        "**Select Your Credential Situation:**",
        options=path_options,
        index=None, # No default selection
        key='pg2_path_radio', # Assign a unique key
        horizontal=True, # Display options horizontally
    )

    st.divider()

    # --- Display Content Based on Choice ---

    # === Path 1: New CPA License ===
    if st.session_state.credential_path_choice == path_options[0]:
        st.header("📜 Pathway: Becoming a New CPA in Oregon")
        st.markdown("Here's a breakdown of the primary requirements:")

        col1, col2, col3 = st.columns(3, gap="medium")

        with col1:
            with st.container(border=True):
                st.subheader("🎓 Education (150 Hours)")
                st.markdown("""
                * **Requirement:** Bachelor's degree + total of 150 semester hours.
                * **Coursework:** Must include specific upper-level Accounting (≥24hrs) & Business (≥24hrs) credits.
                * **Gap Filling:** If <150hrs, consider Post-Bacc Certificates or Master's.
                """)
                st.link_button("Oregon Exam/License Requirements", "https://www.oregon.gov/boa/Pages/Exam-Requirement.aspx", type="secondary")
                st.link_button("PSU Post-Bacc Cert Example", "https://www.pdx.edu/academics/programs/undergraduate/accounting-postbaccalaureate-certificate", type="secondary")

        with col2:
            with st.container(border=True):
                st.subheader("✍️ Uniform CPA Exam")
                st.markdown("""
                * **Requirement:** Pass all 4 sections (3 Core + 1 Discipline as of 2024 CPA Evolution).
                * **Prep:** Most use review courses (Becker, Wiley, Roger, Gleim). Significant time commitment (300-500+ hrs).
                * **Oregon:** Can sit for exam with 120 credits (incl. degree/courses), but need 150 for license.
                 """)
                st.link_button("AICPA Exam Information", "https://www.aicpa-cima.com/resources/landing/cpa-exam", type="secondary")
                st.link_button("Review Course Info (PSU List)", "https://sites.google.com/pdx.edu/actg-resources/career-resources/public-accounting-resources/cpa-exam-eligibility/cpa-review-programs", type="secondary")

        with col3:
            with st.container(border=True):
                st.subheader("💼 Experience")
                st.markdown("""
                * **Requirement:** Generally 1 year (~2000 hrs) of qualifying accounting experience.
                * **Supervision:** Must be verified by an actively licensed CPA.
                * **Timing:** Can often be gained before, during, or after the exam (check OR Board rules).
                """)
                st.link_button("Oregon Board Main Page", "https://www.oregon.gov/boa", type="secondary")
                # Add link to experience verification form if easily found

    # === Path 2: Reactivating CPA License ===
    elif st.session_state.credential_path_choice == path_options[1]:
        st.header("🔄 Pathway: Reactivating Your Oregon CPA License")
        st.warning("**Action:** Your first step should be contacting the Oregon Board of Accountancy directly to confirm your specific status and requirements!", icon="📞")
        st.link_button("Oregon Board Contact Info", "https://www.oregon.gov/boa/Pages/Contact_Us.aspx")
        st.markdown("General guidelines based on status:")

        col1, col2 = st.columns(2, gap="medium")

        with col1:
            with st.container(border=True):
                st.subheader("🟢 Inactive Status")
                st.markdown("""
                * **Situation:** You voluntarily placed your license on inactive status and kept renewing it as inactive.
                * **Requirement:** Catch up on CPE (approx. **32 hours**, incl. 4 ethics, within 12 months prior), apply for reactivation, pay fee.
                """)
                st.link_button("OR Board CPE Requirements", "https://www.oregon.gov/boa/pages/cpe.aspx", type="secondary")

        with col2:
            with st.container(border=True):
                st.subheader("🟡 Lapsed Status (Not Renewed)")
                st.markdown("""
                * **Requirement:** CPE requirements *increase* based on how long the license was lapsed (can be 80+ or even 160+ hours). Potential penalties apply. Must apply for reinstatement & pay back fees/penalties.
                * **Critical:** If lapsed > **6 years**, license may be expired, potentially requiring re-application as a *new* candidate (retake exam!).
                """)
                st.link_button("OR Board Reinstatement Rule (OAR)", "https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791", type="secondary")


    # === Path 3: Non-CPA Path / Alternative Certs ===
    elif st.session_state.credential_path_choice == path_options[2]:
        st.header("💼 Pathway: Non-CPA Roles & Alternative Certifications")
        st.markdown("""
        A CPA isn't required for many accounting roles. However, alternative certifications can boost your credibility and demonstrate updated knowledge, especially after a break. These are optional but valuable for specific career tracks.
        """)

        col1, col2, col3 = st.columns(3, gap="medium")

        with col1:
            with st.container(border=True):
                st.subheader("📜 CMA (Management Acct.)")
                st.markdown("""
                * **Focus:** Corporate finance, management accounting, strategy, analysis, decision support.
                * **Issuer:** IMA (Institute of Management Accountants).
                * **Good For:** Industry roles (Cost Acct., Fin. Analyst, Controller in some orgs).
                """)
                st.link_button("IMA CMA Certification Info", "https://www.imanet.org/cma-certification", type="secondary")

        with col2:
            with st.container(border=True):
                st.subheader("📜 CIA (Internal Audit)")
                st.markdown("""
                * **Focus:** Internal controls, risk management, governance, operational audits.
                * **Issuer:** IIA (Institute of Internal Auditors).
                * **Good For:** Internal Audit roles in various organizations.
                """)
                st.link_button("IIA CIA Certification Info", "https://www.theiia.org/en/certifications/cia/", type="secondary")

        with col3:
            with st.container(border=True):
                st.subheader("📜 EA (Tax Expert)")
                st.markdown("""
                * **Focus:** Tax preparation, representation before the IRS. Federal tax expertise.
                * **Issuer:** IRS (Internal Revenue Service).
                * **Good For:** Tax-focused roles (public practice or industry), tax preparation businesses.
                """)
                st.link_button("IRS Enrolled Agent Info", "https://www.irs.gov/tax-professionals/enrolled-agents", type="secondary")

        st.info("**Also Consider:** CFE (Fraud Examiner), CGFM (Government Financial Manager), QuickBooks ProAdvisor, etc., depending on your specific interests.", icon="💡")


    # --- Placeholder if no choice made ---
    elif st.session_state.credential_path_choice is None:
        st.info("👆 Select one of the options above to see the relevant requirements and resources.", icon="👆")

    st.divider()
    st.markdown("This information provides a starting point. Always verify specific requirements with the official governing bodies (Oregon Board of Accountancy, AICPA, IMA, IIA, IRS).")


def page_cpa_quiz():
    # --- Content from PJ/pages/12_🎓_Oregon_CPA_Reqs_Quiz.py ---
    st.title("🎓 Oregon CPA License Requirements Quiz")
    st.markdown("Test your knowledge of the key requirements for obtaining a **new** CPA license in Oregon.")
    st.info("ℹ️ Based on information from the 'Credentials Pathway' page.")
    st.divider()

    # --- Interactive Quiz Section ---
    st.header("🧠 Knowledge Check!")

    # Use a form for the quiz
    with st.form("pg_cpa_req_quiz"): # Unique form key
        st.write("**Question 1:** How many total semester hours of education are required for CPA *licensure* in Oregon?")
        q1_answer = st.radio(
            "Q1 Options",
            options=["120 hours", "140 hours", "150 hours", "160 hours"],
            index=None, label_visibility="collapsed", key="q1_quiz"
        )

        st.write("**Question 2:** What is the minimum number of semester hours required to *sit* for the CPA Exam in Oregon (assuming degree & course requirements met)?")
        q2_answer = st.radio(
            "Q2 Options",
            options=["100 hours", "120 hours", "150 hours", "Not specified"],
            index=None, label_visibility="collapsed", key="q2_quiz"
        )

        st.write("**Question 3:** How much supervised work experience is generally required for an Oregon CPA license?")
        q3_answer = st.radio(
            "Q3 Options",
            options=["6 months", "1 year (~2000 hours)", "2 years (~4000 hours)", "No experience required"],
            index=None, label_visibility="collapsed", key="q3_quiz"
        )

        st.write("**Question 4:** Besides passing the 4-part Uniform CPA Exam, what other *exam* must be passed for Oregon licensure?")
        q4_answer = st.radio(
            "Q4 Options",
            options=["Oregon Law Exam", "Ethics Exam", "CMA Exam", "No other exam"],
            index=None, label_visibility="collapsed", key="q4_quiz"
        )

        # Submit button for the form
        submitted = st.form_submit_button("Check My Answers!")

        if submitted:
            score = 0
            correct_answers = {
                "Q1": "150 hours",
                "Q2": "120 hours",
                "Q3": "1 year (~2000 hours)",
                "Q4": "Ethics Exam"
            }
            # Ensure keys match the radio button keys
            user_answers = {"Q1": q1_answer, "Q2": q2_answer, "Q3": q3_answer, "Q4": q4_answer}
            results_messages = []

            for i in range(1, 5):
                q_key = f"Q{i}"
                if user_answers[q_key] == correct_answers[q_key]:
                    score += 1
                    results_messages.append(f"✅ **Question {i}: Correct!** ({correct_answers[q_key]})")
                elif user_answers[q_key] is None:
                     results_messages.append(f"⚠️ **Question {i}: Not Answered.** Correct answer: {correct_answers[q_key]}")
                else:
                    results_messages.append(f"❌ **Question {i}: Incorrect.** You chose: {user_answers[q_key]}. Correct answer: {correct_answers[q_key]}")

            st.subheader("Quiz Results:")
            st.markdown(f"**You scored {score} out of 4.**")
            for msg in results_messages:
                st.markdown(msg)

            if score == 4:
                st.balloons()
                st.success("Great job! You've got a good handle on the key requirements.")
            else:
                st.warning("Review the 'Credentials Pathway' page and check the official Oregon Board resources for clarification!")

    st.divider()
    st.info("Always refer to the official [Oregon Board of Accountancy website](https://www.oregon.gov/boa) for the most current and detailed requirements.", icon="❗")


def page_refresh_skills():
    # --- Content from PJ/pages/2_📚_Refresh_Skills_Resources.py ---
    st.title("📚 3. Refresh Your Accounting Knowledge and Skills")
    st.markdown("""
    After time away from the accounting field, proactively updating your knowledge and technical skills is essential.
    The profession evolves with new standards, regulations, and technologies. This page provides resources
    to help you get current in key areas. Explore the tabs below for curated links and information.
    """)
    st.divider()

    # --- Create Tabs for Different Skill Areas ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "📜 Principles & Standards",
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
        * **[AICPA & CIMA A&A Focus Newsletter](https://www.journalofaccountancy.com/newsletters/a-a-focus.html)**: Often includes summaries and discussions of recent accounting standard updates.
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
        """)


def page_visual_skills_refresh():
    # --- Content from PJ/pages/6_💡_Visual_Skills_Refresh.py ---
    st.title("💡 Visual Guide: Refreshing Your Skills")
    st.markdown("""
    Stay current! The accounting world changes fast. Use these resources to update your knowledge
    in key areas like standards, tech, and continuous learning. Click the buttons to explore resources.
    This page visually summarizes the resources from the 'Refresh Skills' page.
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
            st.link_button("FASB Codification", "https://fasb.org/page/PageContent?pageId=/staticpages/codification-access.html&isStaticPage=true", help="Basic view free", key="vsr_fasb")
            st.link_button("AICPA Standards Overview", "https://www.aicpa-cima.com/resources/landing/standards-and-statements", key="vsr_aicpa_std")
            st.caption("*Tip: Search major CPA firm websites for free summaries.*")

    with col2:
        with st.container(border=True):
            st.subheader("🏛️ Tax Law Updates")
            st.markdown("""
            * **Key Areas:** TCJA impacts, Inflation Reduction Act credits/changes.
            * **Goal:** Understand current business & individual tax landscape.
            """)
            st.link_button("IRS IRA Hub", "https://www.irs.gov/inflation-reduction-act-of-2022", key="vsr_irs_ira")
            st.link_button("IRS Business News", "https://www.irs.gov/newsroom/businesses", key="vsr_irs_biz")
            st.caption("*Tip: Tax-specific CPE is highly recommended.*")

    st.divider()

    # --- Section 2: Technology & Software ---
    st.header("💻 Technology & Software Skills")
    st.markdown("Master the tools employers expect you to know.")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        with st.container(border=True):
            st.subheader("📊 Excel (Advanced)")
            st.markdown("""
            * **Focus:** PivotTables, XLOOKUP, Power Query, Key Formulas.
            * **Goal:** Efficient data manipulation & analysis.
            """)
            st.link_button("Microsoft Learn (Excel)", "https://learn.microsoft.com/en-us/training/excel", key="vsr_excel")

        with st.container(border=True):
            st.subheader("📈 Data Analytics Tools")
            st.markdown("""
            * **Examples:** Tableau, Microsoft Power BI.
            * **Goal:** Visualize & interpret financial data trends.
            """)
            st.link_button("MS Learn (Power BI)", "https://learn.microsoft.com/en-us/training/powerplatform/power-bi", key="vsr_pbi")
            st.link_button("Tableau Learning", "https://www.tableau.com/learn", key="vsr_tableau")


    with col2:
        with st.container(border=True):
            st.subheader("🧾 QuickBooks (Desktop/Online)")
            st.markdown("""
            * **Focus:** Core features for SMB accounting. Free ProAdvisor training.
            * **Goal:** Manage books efficiently for small/medium businesses.
            """)
            st.link_button("QB Training & Cert", "https://quickbooks.intuit.com/accountants/training-certification/", key="vsr_qb")

        with st.container(border=True):
            st.subheader("⚙️ ERP Systems (Awareness)")
            st.markdown("""
            * **Examples:** NetSuite, SAP, Dynamics 365.
            * **Goal:** Understand integrated systems (often learned on-the-job).
            """)
            # Example links - Add more if needed
            st.link_button("SAP Training", "https://training.sap.com/", key="vsr_sap")
            st.link_button("MS Dynamics 365 Learn", "https://learn.microsoft.com/en-us/training/dynamics365", key="vsr_d365")


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
            st.link_button("OSCPA CPE Catalog", "https://www.orcpa.org/cpe", key="vsr_oscpa")
            st.link_button("PCC Accounting", "https://www.pcc.edu/programs/accounting/", key="vsr_pcc")
            st.link_button("PSU Post-Bacc Acct Cert", "https://www.pdx.edu/academics/programs/undergraduate/accounting-postbaccalaureate-certificate", key="vsr_psu")

        with st.container(border=True):
            st.subheader("🌐 National CPE & Certs")
            st.markdown("""
            * **AICPA:** Official CPE, Webcast Pass, Certificates.
            * **CPAacademy:** Often has free webinars.
            * **Others:** Surgent, Becker, Gleim, CPE Store.
            """)
            st.link_button("AICPA CPE & Learning", "https://www.aicpa-cima.com/cpe-learning", key="vsr_aicpa_cpe")
            st.link_button("CPAacademy.org", "https://www.cpaacademy.org/", key="vsr_cpaacademy")

    with col2:
        with st.container(border=True):
            st.subheader("📰 Publications & News")
            st.markdown("""
            * **Journals:** JoA, FM Mag, Tax Adviser (AICPA).
            * **News Sites:** Accounting Today.
            * **Firm Insights:** Check Big 4/Large firm websites.
            """)
            st.link_button("Journal of Accountancy", "https://www.journalofaccountancy.com/", key="vsr_joa")
            st.link_button("Accounting Today", "https://www.accountingtoday.com/", key="vsr_at")

        with st.container(border=True):
            st.subheader("🖥️ Online Courses / Other")
            st.markdown("""
            * **Platforms:** Coursera, edX, LinkedIn Learning, Udemy.
            * **Networks:** OSCPA/IMA forums, LinkedIn Groups.
            * **Media:** Accounting podcasts/blogs.
            """)
            st.link_button("Coursera", "https://www.coursera.org/", key="vsr_coursera")
            st.link_button("LinkedIn Learning", "https://www.linkedin.com/learning/", key="vsr_linkedin_learn")


def page_gain_experience():
    # --- Content from PJ/pages/8_💼_Gain_Experience.py ---
    st.title("💼 4. Gaining Recent Experience After a Break")
    st.markdown("""
    Bridging the experience gap on your resume is crucial when returning to accounting. Potential employers want to see
    that your skills are current and that you're actively re-engaging with the profession.

    This page outlines three key strategies with actionable steps and resources to help you gain that valuable recent experience.
    """)
    st.divider()

    # --- Use Columns for the Three Strategies ---
    col1, col2, col3 = st.columns(3, gap="large")

    # === Column 1: Volunteer & Freelance ===
    with col1:
        st.subheader("🤝 Volunteer & Freelance")
        st.markdown("Offer your skills part-time to refresh knowledge, build confidence, and get recent references.")

        with st.container(border=True):
            st.markdown("**🎯 Strategy:** Find opportunities where organizations need basic accounting, bookkeeping, or tax help.")
            st.markdown("**✅ Benefits:** Flexible, builds resume, demonstrates initiative, valuable community contribution.")

        st.markdown("---")
        st.markdown("##### 🚀 Actionable Steps:")
        st.markdown("""
        1.  **Identify Targets:** Think local non-profits, community groups, schools, religious organizations, or even professional association chapters.
        2.  **Search Volunteer Sites:** Use platforms like Hands On Greater Portland, Idealist, or Catchafire (skills-based).
        3.  **Offer Specific Skills:** Inquire about roles like Treasurer, Finance Committee member, or bookkeeping assistance. Prepare a brief pitch.
        4.  **Consider Tax Season:** Sign up for IRS VITA/TCE to prepare returns (excellent refresher & resume builder).
        5.  **Tap Personal Network:** Offer bookkeeping help to friends/family with small businesses (even short projects count).
        6.  **(Optional) Explore Freelance Platforms:** Check Upwork/Fiverr for small, remote bookkeeping/data entry gigs (be mindful of competition/rates).
        """)

        st.markdown("##### 🌐 Key Resources:")
        st.link_button("Hands On Greater Portland", "https://www.handsonportland.org/", key="ge_ho")
        st.link_button("Idealist (Volunteer)", "https://www.idealist.org/en/jobs?job_type=VOLOP", key="ge_ideal")
        st.link_button("Catchafire", "https://www.catchafire.org/", key="ge_catch")
        st.link_button("IRS VITA/TCE Volunteer", "https://www.irs.gov/individuals/irs-tax-volunteers", key="ge_vita")
        st.link_button("Upwork", "https://www.upwork.com/", key="ge_uw")


    # === Column 2: Returnships & Projects ===
    with col2:
        st.subheader("🏢 Returnships & Projects")
        st.markdown("Look for structured re-entry programs or propose your own project work.")

        with st.container(border=True):
            st.markdown("**🎯 Strategy:** Target formal 'returnship' programs or create opportunities via networking.")
            st.markdown("**✅ Benefits:** Structured re-entry, potential mentorship, often leads to full-time offers, bridges gap directly.")

        st.markdown("---")
        st.markdown("##### 🚀 Actionable Steps:")
        st.markdown("""
        1.  **Research Formal Programs:** Use platforms like iRelaunch, Path Forward, Apres Group to find companies offering returnships.
        2.  **Check Target Companies:** Visit career pages of larger firms (Big 4, national firms) and major local companies (Nike, Intel, etc.) - search "returnship" or "career re-entry".
        3.  **Network for Leads:** Ask your professional contacts if their companies have or would consider such programs.
        4.  **Propose a Project:** Reach out to former managers/colleagues or contacts at target companies. Offer to help with a specific, short-term need (e.g., busy season support, system cleanup project, specific analysis). Frame it as a way to demonstrate your current value.
        5.  **Explore Re-Entry Support Orgs:** Look into programs specifically designed to help professionals (especially women) return after a break.
        """)

        st.markdown("##### 🌐 Key Resources:")
        st.link_button("iRelaunch", "https://www.irelaunch.com/", key="ge_ir")
        st.link_button("Path Forward", "https://www.pathforward.org/", key="ge_pf")
        st.markdown("*Also check specific career pages of target companies & large CPA firms.*")


    # === Column 3: Temp Agencies & Contract Roles ===
    with col3:
        st.subheader("⏳ Temp Agencies & Contract")
        st.markdown("Get paid work experience quickly through specialized staffing firms.")

        with st.container(border=True):
            st.markdown("**🎯 Strategy:** Register with reputable accounting/finance staffing agencies for temporary or contract assignments.")
            st.markdown("**✅ Benefits:** Fast way to get recent experience, exposure to different companies/systems, can lead to permanent offers, builds network.")

        st.markdown("---")
        st.markdown("##### 🚀 Actionable Steps:")
        st.markdown("""
        1.  **Identify Agencies:** Research firms specializing in accounting/finance placements in Portland (see list below).
        2.  **Update Resume:** Tailor your resume to highlight core accounting skills, transferable skills, and any recent upskilling (courses, volunteering).
        3.  **Register:** Sign up online via agency websites. Upload your resume.
        4.  **Connect with Recruiters:** Follow up via phone or LinkedIn. Clearly state your goals (returning professional, seeking temp/contract/temp-to-hire) and skills.
        5.  **Be Prepared:** Expect skills assessments (Excel, accounting basics).
        6.  **Be Flexible:** Be open to roles like AP, AR, Staff Accountant, Bookkeeper initially to gain current experience.
        """)

        st.markdown("##### 🌐 Key Resources (Portland Area):")
        st.link_button("Robert Half / Accountemps", "https://www.roberthalf.com/us/en/locations/or/portland", key="ge_rh")
        st.link_button("Ledgent Finance", "https://ledgent.com/locations/portland-finance-and-accounting-staffing-agencies/", key="ge_lg")
        st.link_button("Aston Carter", "https://www.astoncarter.com/en/locations/north-america/united-states/oregon/portland", key="ge_ac")
        st.link_button("VanderHouwen", "https://www.vanderhouwen.com/", key="ge_vh")
        st.link_button("Boly:Welch", "https://bolywelch.com/", key="ge_bw")
        st.markdown("*Also search Indeed/LinkedIn for 'Contract' or 'Temporary' Accounting roles.*")


    st.divider()
    st.info("**Key Takeaway:** Combining one or more of these strategies can effectively build recent, relevant experience for your resume and demonstrate your commitment to re-entering the accounting field.", icon="💡")


def page_networking():
    # --- Content from PJ/pages/9_🤝_Networking_Strategy.py ---
    st.title("🤝 5. Rebuild Your Professional Network in Portland")
    st.markdown("""
    Networking is **essential** when returning to accounting, especially after a break. Many opportunities aren't advertised!
    It helps you learn about the current market, get advice, find support, and uncover job leads.

    This page provides actionable strategies tailored for the Portland area.
    """)
    st.success("💡 **Key Goal:** Re-establish yourself as an active member of the Portland accounting community.", icon="🎯")
    st.divider()

    # --- Use Columns for Different Networking Avenues ---
    col1, col2 = st.columns(2, gap="large")

    # === Column 1: Reconnect & Engage Associations ===
    with col1:
        # --- Reconnecting with Existing Network ---
        with st.container(border=True):
            st.subheader("🔗 Reconnect with Past Contacts")
            st.markdown("**Why:** Warm contacts are often most willing to help (advice, referrals).")
            st.markdown("##### 🚀 Actionable Steps:")
            st.markdown("""
            1.  **List:** Brainstorm former colleagues, managers, clients, classmates (Portland focus).
            2.  **Prioritize:** Start with positive relationships & well-connected individuals.
            3.  **Reach Out:** Use LinkedIn/Email. Keep it brief & positive: "Returning to accounting, would value catching up & getting your perspective..." (Don't ask for a job directly).
            4.  **Prepare for Chats:** Ask about industry changes, advice for re-entry, their company culture. Share your update concisely.
            5.  **Follow Up:** Send a thank-you note promptly.
            """)
            st.info("☕ Aim for 2-3 'coffee chats' (virtual or in-person) per month initially.", icon="ℹ️")

        st.markdown("<br/>", unsafe_allow_html=True) # Add space

        # --- Professional Associations ---
        with st.container(border=True):
            st.subheader("🧑‍🤝‍🧑 Join Professional Associations")
            st.markdown("**Why:** Access events, CPE, member directories, hidden job boards, stay current.")
            st.markdown("##### 🚀 Actionable Steps:")
            st.markdown("""
            1.  **Identify & Join:** Prioritize **OSCPA** (State CPA Society) and **IMA Portland** (Management Acct.). Consider others based on interest (IIA, OSTC, AFWA). *Check for affiliate/candidate rates!*
            2.  **Check Calendars Often:** Add relevant CPE & networking events to *your* calendar.
            3.  **Attend Actively:** Go to mixers, webinars, lunches. Prepare your 30-sec intro. Aim to meet 2-3 new people each time.
            4.  **Engage:** Ask questions during sessions, participate in discussions.
            5.  **Volunteer (Optional):** Join a committee for deeper connections.
            """)
            st.markdown("##### 🌐 Key Portland Resources:")
            st.link_button("OSCPA Website", "https://www.orcpa.org/", key="nw_oscpa")
            st.link_button("IMA Portland Chapter", "https://portland.imanet.org/", key="nw_ima")
            st.link_button("IIA Portland Chapter", "https://chapters.theiia.org/portland/Pages/default.aspx", key="nw_iia")
            st.link_button("OSTC (Tax Consultants)", "https://www.ostc-oregon.com/", key="nw_ostc") # Check for local chapter info


    # === Column 2: Online Presence & Events/Informal ===
    with col2:
        # --- Online Networking (LinkedIn) ---
        with st.container(border=True):
            st.subheader("💻 Leverage LinkedIn")
            st.markdown("**Why:** Build visibility, research companies/people, connect with recruiters.")
            st.markdown("##### 🚀 Actionable Steps:")
            st.markdown("""
            1.  **Optimize Profile:** Professional photo, clear headline ("Accounting Professional Returning | Seeking...") summary explaining your goal, add recent skills/courses.
            2.  **Connect:** Find & connect with Portland CPAs, Acct. Managers, Recruiters. *Personalize requests!* ("Returning to accounting in PDX...")
            3.  **Join Groups:** Search for "OSCPA Members," "Portland Finance Professionals," "Oregon Accountants," etc.
            4.  **Engage:** Like/comment thoughtfully on posts. Share occasional relevant articles.
            5.  **Set to 'Open to Work':** Let recruiters know you're looking (can be private to recruiters only).
            """)
            st.link_button("Go to LinkedIn", "https://www.linkedin.com/", key="nw_li")

        st.markdown("<br/>", unsafe_allow_html=True) # Add space

        # --- Events & Informal Networking ---
        with st.container(border=True):
            st.subheader("🗓️ Attend Events & Seek Info")
            st.markdown("**Why:** Face-to-face (or direct virtual) interaction builds rapport quickly.")
            st.markdown("##### 🚀 Actionable Steps:")
            st.markdown("""
            1.  **Prioritize Association Events:** Combine CPE/learning with networking (see Associations).
            2.  **Attend Career Fairs:** Check PSU/UO/OSU/OSCPA events (even if student-focused) to meet recruiters directly.
            3.  **Request Informational Interviews:** Use LinkedIn/Network to ask professionals for brief chats (~20 min) about their role/company/industry. *Focus on learning, not job hunting.*
            4.  **Monitor Event Sites:** Check Eventbrite, Meetup.com for local finance/business networking events.
            5.  **Follow Local Business News:** Check Portland Business Journal for events.
            6.  **Alumni Groups:** Participate in relevant university alumni events.
            """)
            st.markdown("##### 🌐 Key Resources:")
            st.link_button("Eventbrite (Portland)", "https://www.eventbrite.com/d/or--portland/business--professional-networking/", key="nw_eb")
            st.link_button("Portland Biz Journal Events", "https://www.bizjournals.com/portland/events", key="nw_pbj")


    st.divider()

    # --- Networking Mindset ---
    st.header("💡 Networking Mindset & Tips")
    col_a, col_b = st.columns(2) # Avoid conflict with earlier cols
    with col_a:
        st.info("""
        * **Be Prepared:** Have a concise (30-sec) intro ready.
        * **Be Curious:** Ask questions, listen more than you talk.
        * **Be Helpful:** Offer connections or info if you can.
        * **Be Patient:** Building relationships takes time.
        """, icon="🧠")
    with col_b:
        st.success("""
        * **Be Specific:** Know what roles/industries interest you.
        * **Be Professional:** Online and in person.
        * **Follow Up:** Send thank yous & connect on LinkedIn.
        * **Be Yourself:** Authenticity builds trust.
        """, icon="✅")


    st.divider()
    st.caption("Networking is a continuous activity, not just for job searching. Maintain connections throughout your career.")


def page_resume():
    # --- Content from PJ/pages/10_📄_Resume_Narrative.py ---
    st.title("📄 6. Update Your Resume & Craft Your Narrative")
    st.markdown("""
    Your resume and cover letter tell your professional story. After a career break, it's important
    to update them strategically, highlighting both past experience and recent activities, while positively
    framing your return to accounting.

    Explore the tabs below for concise tips and actionable advice.
    """)
    st.info("✨ **Goal:** Create compelling documents that showcase your value and address your career journey confidently.", icon="🎯")
    st.divider()

    # --- Use Tabs for Key Areas ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Resume Refresh",
        "💡 Highlighting Skills",
        "🌉 Addressing the Gap",
        "✍️ Cover Letter Story"
    ])

    # === Tab 1: Resume Refresh ===
    with tab1:
        st.header("📄 Resume Refresh: Modern & Optimized")
        st.markdown("Ensure your resume format is current and passes Applicant Tracking Systems (ATS).")

        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("##### 1. Update Format & Style")
                st.markdown("""
                * 📄 Use a clean, modern template (Chronological or Combination format often work well).
                * 🔍 Ensure readability: Clear font, good spacing, consistent formatting.
                * 🔗 **Action:** Explore templates from reputable sources.
                """)
                st.link_button("MS Word Templates", "https://create.microsoft.com/en-us/templates/resumes-and-cover-letters", key="res_word")
                st.link_button("Canva Templates", "https://www.canva.com/resumes/templates/", key="res_canva")

        with col2:
            with st.container(border=True):
                st.markdown("##### 2. Optimize for ATS")
                st.markdown("""
                * ⚙️ Include keywords relevant to target jobs (e.g., GAAP, Reconciliation, Excel, QuickBooks).
                * 📄 Avoid complex formatting like tables or images that confuse ATS bots.
                * 📊 **Action:** Review job descriptions for keywords; use simple ATS checkers for formatting tips.
                """)
                st.link_button("ATS Resume Guide (Example)", "https://www.jobscan.co/blog/ats-resume/", help="Explains ATS - use free advice", key="res_ats")

        with st.container(border=True):
            st.markdown("##### 3. Feature Recent Activity")
            st.markdown("""
            * ⭐ Place recent courses, certs, volunteer work, or projects prominently.
            * ✨ Add a 'Recent Professional Development' or 'Skills Summary' section near the top.
            * 📅 **Action:** Clearly date recent activities (e.g., "QuickBooks Online Certification - 2025") to show current engagement.
            """)


    # === Tab 2: Highlighting Skills ===
    with tab2:
        st.header("💡 Highlighting Skills: Past, Present & Transferable")
        st.markdown("Showcase the full range of your abilities.")

        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.markdown("##### 1. Quantify Past Accomplishments")
                st.markdown("""
                * 🎯 Use numbers to show impact from previous accounting roles.
                * ❓ Ask: How much ($/%) saved? How many managed? What process improved?
                * 📝 **Action:** Revisit old performance reviews or project notes to find quantifiable results.
                """)

        with col2:
            with st.container(border=True):
                st.markdown("##### 2. Identify Transferable Skills")
                st.markdown("""
                * 🔗 Skills from your break often apply! Think: Analysis, Communication, Project Mgmt, Tech Use.
                * 🤝 Connect these skills directly to accounting needs in your summary or descriptions.
                * 📋 **Action:** Brainstorm skills gained during your break.
                """)

        with st.container(border=True):
            st.markdown("##### 3. Combine Old & New")
            st.markdown("""
            * 🔗 Weave together your foundational accounting experience with newly refreshed knowledge and transferable skills.
            * ⭐ Your summary/objective should reflect this unique blend.
            * 📄 **Action:** Craft a powerful summary statement highlighting this combination.
            """)


    # === Tab 3: Addressing the Gap ===
    with tab3:
        st.header("🌉 Addressing the Career Gap Positively")
        st.markdown("Be transparent but frame your time away constructively.")

        col1, col2 = st.columns(2)

        with col1:
             with st.container(border=True):
                st.markdown("##### 1. Note Briefly on Resume")
                st.markdown("""
                * ⏳ Include a short entry for the break period in your Experience section.
                * ✨ Frame positively: e.g., "Career Sabbatical focused on [Industry/Activity] and Skill Development".
                * 🚫 Avoid lengthy explanations or apologies on the resume itself.
                """)
                st.markdown("---")
                st.markdown("**Example Resume Entry:**")
                st.code("2014 – 2024    Career Break / Industry Exploration\n- Engaged in [Your Activity], developing skills in [e.g., analysis].\n- Undertook professional development focused on returning to Accounting.", language=None)

        with col2:
            with st.container(border=True):
                st.markdown("##### 2. Focus on Now & Future")
                st.markdown("""
                * 🚀 Emphasize your *current* readiness and enthusiasm for returning to accounting.
                * 💡 Highlight recent learning and activities that demonstrate your commitment.
                * ➡️ **Action:** Shift the focus from *why you left* to *why you're a great fit now*.
                """)

            with st.container(border=True):
                st.markdown("##### 3. Highlight Productivity")
                st.markdown("""
                * ⭐ Mention valuable skills gained or key projects completed during the break.
                * 🌐 Even non-traditional work (volunteering, freelance) shows initiative.
                * 📈 **Action:** Connect these experiences back to skills relevant for accounting roles.
                """)


    # === Tab 4: Cover Letter Story ===
    with tab4:
        st.header("✍️ Crafting Your Cover Letter Narrative")
        st.markdown("Use the cover letter to tell your unique story concisely and compellingly.")

        with st.container(border=True):
            st.markdown("##### 1. Tell Your Concise Story")
            st.markdown("""
            * 🔗 Connect the dots: Past Accounting -> Break Activities/Skills -> Motivated Return.
            * ⏳ Briefly acknowledge the transition, focusing on skills gained.
            * ➡️ **Action:** Draft a 1-2 sentence transition statement.
            """)
            st.markdown("---")
            st.markdown("**Example Narrative Snippets:**")
            st.info('_"Following a foundational career in accounting, I spent time honing analytical skills... I am now eager to bring this enhanced skillset back to accounting."_')
            st.info('_"After a period focused on [Activity], developing strong [Skill], I have refreshed my accounting knowledge through [Course] and am excited to re-enter the field."_')


        with st.container(border=True):
            st.markdown("##### 2. Show Enthusiasm & Fit")
            st.markdown("""
            * 🔥 Clearly state your excitement for the specific role and company.
            * 🎯 Explain *why* you want *this* job and how your unique background benefits *them*.
            * 🤝 **Action:** Research the company and tailor your letter.
            """)

        with st.container(border=True):
            st.markdown("##### 3. Focus on Value, Not Apology")
            st.markdown("""
            * ⭐ Highlight the *value* you bring NOW (combined experience + new skills).
            * 🚫 Avoid apologizing for the gap or over-explaining.
            * 🚀 **Action:** Project confidence in your abilities and your decision to return.
            """)
            st.link_button("More Tips on Explaining Gaps", "https://www.themuse.com/advice/how-to-explain-gap-in-resume-cover-letter-interview", key="res_muse")


    st.divider()
    st.success("✅ A well-crafted resume and narrative turn your career break into a unique strength!")


def page_job_search():
    # --- Content from PJ/pages/11_🚀_Job_Search_Launch.py ---
    st.title("🚀 7. Launch Your Targeted Job Search")
    st.markdown("""
    You've refreshed your skills, updated your resume, and started networking! Now it's time to actively
    search and apply for roles in a focused, strategic way.

    Follow these steps to manage your job search effectively. Click on each step to see detailed actions.
    """)
    st.info("✨ **Goal:** Systematically find and apply for suitable roles, leveraging your preparation.", icon="🎯")
    st.divider()

    # --- Step-by-Step Action Plan ---

    st.subheader("Step 1: 🎯 Define Your Target & Strategy")
    with st.expander("Click for Actionable Steps..."):
        st.markdown("##### Reconfirm Your Goals:")
        st.markdown("""
        * ✅ Review decisions from 'Career Goal Evaluation'.
        * 🎯 Set realistic target role levels for re-entry.
        * 📍 Define location needs: Portland On-site, Hybrid, or Remote?
        """)
        st.markdown("##### Research Companies:")
        st.markdown("""
        * 🏭 Identify specific Portland companies in your target industries/sizes.
        * 🌐 Research their culture, values, and recent news.
        * 📝 Keep a running list of target employers.
        """)
        st.markdown("##### Prepare Your Pitch:")
        st.markdown("""
        * 🗣️ Refine your 30-second "elevator pitch".
        * 🔑 Identify 3-5 key strengths/experiences.
        * 📖 Practice articulating your value proposition.
        """)

    st.subheader("Step 2: 🔍 Identify Opportunities")
    with st.expander("Click for Actionable Steps..."):
        st.markdown("##### Use Key Job Boards:")
        st.markdown("""
        * 🔔 Set up daily/weekly email alerts (LinkedIn, Indeed).
        * 📌 Regularly check niche/local boards: **Mac's List** & **OSCPA Career Center**.
        * ☁️ Use remote-specific boards if applicable.
        """)
        st.link_button("Mac's List", "https://www.macslist.org/", key="js_mac")
        st.link_button("OSCPA Career Center", "https://www.orcpa.org/career-center", key="js_oscpa") # Membership may be required
        st.markdown("##### Activate Your Network:")
        st.markdown("""
        * 🤝 Inform key contacts you're *actively searching*.
        * ❓ Ask politely for leads or introductions.
        """)
        # st.page_link("app.py", page="page_networking", label="Review Networking Strategies", icon="🤝") # Need st.navigation structure first
        st.markdown("##### Engage Staffing Agencies:")
        st.markdown("""
        * 📞 Check in with recruiters you've registered with.
        * 📋 Reiterate your search criteria and availability.
        """)
        # st.page_link("app.py", page="page_gain_experience", label="See Staffing Agency List", icon="💼") # Need st.navigation structure first


    st.subheader("Step 3: ✍️ Apply Strategically")
    with st.expander("Click for Actionable Steps..."):
        st.markdown("##### Tailor Each Application:")
        st.markdown("""
        * 🔑 Analyze job description; customize resume with keywords.
        * ✍️ Write a targeted cover letter.
        * 📄 Proofread carefully!
        """)
        # st.page_link("app.py", page="page_resume", label="Review Resume/Narrative Guide", icon="📄") # Need st.navigation structure first
        st.markdown("##### Prioritize & Leverage Referrals:")
        st.markdown("""
        * ⭐ Give priority to roles with referrals.
        * 🗣️ Mention your referral source clearly (with permission).
        """)
        st.markdown("##### Track Your Applications:")
        st.markdown("""
        * 📊 Use a spreadsheet or tool to log applications & status.
        * 🗓️ Set reminders for follow-up.
        """)


    st.subheader("Step 4: 🤝 Prepare for Interviews")
    with st.expander("Click for Actionable Steps..."):
        st.markdown("##### Practice Your Story & Answers:")
        st.markdown("""
        * 🗣️ Rehearse your return-to-work narrative confidently.
        * ❓ Prepare answers for common questions (STAR method).
        """)
        st.link_button("STAR Method Explained", "https://www.themuse.com/advice/star-interview-method", key="js_star")
        st.markdown("##### Research the Company & Role:")
        st.markdown("""
        * 🌐 Understand their mission, values, news.
        * 👥 Research interviewers on LinkedIn.
        * 🤔 Prepare insightful questions.
        """)
        st.markdown("##### Logistics & Mindset:")
        st.markdown("""
        * 💻 Test technology. Plan attire.
        * 🧘 Manage nerves. Project positivity.
        """)


    st.subheader("Step 5: ✨ Follow Up & Stay Positive")
    with st.expander("Click for Actionable Steps..."):
        st.markdown("##### Post-Interview Follow-Up:")
        st.markdown("""
        * 📧 Send personalized thank-you emails within 24 hours.
        * ✍️ Reference conversation specifics. Reiterate interest.
        """)
        st.markdown("##### Manage Waiting & Communication:")
        st.markdown("""
        * ⏳ Respect hiring timelines. Follow up politely if needed.
        * 📞 Respond promptly to employer communication.
        """)
        st.markdown("##### Maintain Momentum & Mindset:")
        st.markdown("""
        * ➡️ **Don't stop!** Continue networking & applying.
        * 💪 Stay positive! Celebrate small wins.
        * 🌱 Keep building experience/skills.
        """)

    st.divider()
    st.success("🚀 Launching your search is a big step! Stay organized, focused, and persistent.", icon="✅")


# --- Main App Logic ---

# --- Page Configuration (Global) ---
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Define Pages and their order ---
# Map page names (for display) to their functions and a unique key
PAGES = {
    "Start Here: Roadmap": (page_roadmap, "roadmap"),
    "1. Career Goal Evaluation": (page_career_goals, "goals"),
    "   - Visual Career Paths": (page_visual_career_paths, "viz_goals"), # Indented for visual grouping
    "2. Credentials Pathway": (page_credentials_pathway, "creds"),
    "   - OR CPA Reqs Quiz": (page_cpa_quiz, "quiz"), # Indented
    "3. Refresh Skills": (page_refresh_skills, "skills"),
    "   - Visual Skills Refresh": (page_visual_skills_refresh, "viz_skills"), # Indented
    "4. Gain Experience": (page_gain_experience, "exp"),
    "5. Networking Strategy": (page_networking, "network"),
    "6. Resume & Narrative": (page_resume, "resume"),
    "7. Job Search Launch": (page_job_search, "job_search")
}

# Extract ordered keys and functions for easier access
page_names = list(PAGES.keys())
page_functions = [PAGES[name][0] for name in page_names]
page_keys = [PAGES[name][1] for name in page_names]
total_pages = len(PAGES)

# --- Initialize Session State for Completion ---
# Use page keys for state
for key in page_keys:
    if f"completed_{key}" not in st.session_state:
        st.session_state[f"completed_{key}"] = False

# --- Sidebar ---
with st.sidebar:
    st.header("Navigation")

    # --- Calculate Progress ---
    completed_count = sum(st.session_state[f"completed_{key}"] for key in page_keys)
    progress_value = completed_count / total_pages if total_pages > 0 else 0

    # --- Display Progress ---
    st.progress(progress_value)
    st.caption(f"Progress: {completed_count} / {total_pages} pages reviewed")
    st.divider()


    # --- Navigation Menu ---
    # `st.navigation` returns the *function* of the selected page
    selected_page_func = st.navigation(page_functions, pages=page_names) # Use st.navigation

# --- Determine Index of Selected Page ---
current_page_index = page_functions.index(selected_page_func)
current_page_key = page_keys[current_page_index]

# --- Locking Logic ---
unlocked = True
if current_page_index > 0: # Skip check for the first page (Roadmap)
    previous_page_key = page_keys[current_page_index - 1]
    if not st.session_state[f"completed_{previous_page_key}"]:
        unlocked = False

# --- Display Selected Page or Locked Message ---
if unlocked:
    selected_page_func() # Call the function to render the page

    # --- Completion Checkbox (Show only if page is unlocked) ---
    st.divider()
    # Use the page key for the checkbox state
    st.checkbox("Mark this page as reviewed to unlock the next page", key=f"completed_{current_page_key}")
    st.caption(f"*Reviewing '{page_names[current_page_index]}' unlocks '{page_names[current_page_index + 1]}'*") if current_page_index < total_pages - 1 else st.caption("*This is the last page.*")


else:
    st.warning(f"🔒 Please complete the previous page ('**{page_names[current_page_index - 1]}**') to unlock this section.", icon="👈")
    st.info("Navigate back using the sidebar and check the 'Mark as reviewed' box at the bottom of the previous page.")

# --- Optional: Footer or additional global elements ---
st.sidebar.divider()
st.sidebar.info("App demonstrating `st.navigation` with locking.")