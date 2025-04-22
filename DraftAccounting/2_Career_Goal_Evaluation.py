import streamlit as st

# Set page configuration for better layout
#st.set_page_config(page_title="Career Goal Evaluation", layout="wide")

# --- Page Title and Introduction ---
st.title("🎯 Evaluate Your Career Goals (CPA vs. Non-CPA)")
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
    st.subheader("1. Your Career Ambitions & Preferred Environment")

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
        key="q_ambition",
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
        key="q_environment",
        help="Think about company size, culture, and type of work."
    )

    # --- Feedback for Section 1 ---
    if answers['ambition'] == "Top Executive (e.g., CFO/Partner in large org)":
        feedback_points.append("📈 High ambition for top roles often necessitates the **CPA license** for credibility and access, especially in large organizations.")
    elif answers['ambition'] == "Department/Team Lead (e.g., Controller/Manager)":
        feedback_points.append("🧑‍💼 Leading teams fits **both paths**. CPA adds weight, but strong experience and potentially other certs (like CMA) work well on the Non-CPA path too, especially outside large public companies.")
    elif answers['ambition'] == "Skilled Specialist / Individual Contributor":
         feedback_points.append("💡 Deep specialization can thrive on **both paths**. CPA is key for audit/tax specialization in firms, while Non-CPAs often specialize in industry areas, systems, or with certs like EA/CFE.")
    elif answers['ambition'] == "Own My Own Practice (Bookkeeping/Tax/Consulting)":
         feedback_points.append("🏠 Owning a practice often follows the **Non-CPA path** (bookkeeping focus) or requires specific licenses like **EA** (tax) or **CPA** (broader services, attest).")
    elif answers['ambition'] == "Stable role in Government / Non-Profit":
         feedback_points.append("🏛️ Gov/Non-Profit roles are widely available for **Non-CPAs**. While CPA is beneficial for some audit/leadership roles (consider CGFM too), it's often not required for many staff/analyst positions.")

    if answers['environment'] == "Large Public Accounting Firm":
        feedback_points.append("🏢 Public accounting firms heavily favor the **CPA license** for career progression beyond entry levels.")
    elif answers['environment'] == "Corporate (Medium-Large Company)":
        feedback_points.append("🏭 Corporate roles exist for **both**. **CPA** is often preferred for higher finance leadership/reporting roles. **Non-CPA** roles are abundant in operational accounting, FP&A (consider CMA).")
    elif answers['environment'] in ["Small-Medium Business (SMB)", "Non-Profit Organization"]:
        feedback_points.append("🌱 SMBs and Non-Profits often rely on skilled **Non-CPAs** for full-charge bookkeeping, accounting management, and grant accounting.")
    elif answers['environment'] == "Flexible / Remote / Self-Employed":
        feedback_points.append("💻 Flexibility is possible on **both paths**. Non-CPA roles (bookkeeping, payroll) are common for remote/freelance. CPA offers higher-value remote consulting/tax services.")


with st.container(border=True):
    st.subheader("2. Study, Exams, and Task Preferences")

    answers['commitment'] = st.select_slider(
        "**Commitment:** Realistically, how willing *and* able are you to dedicate significant time (500+ hrs over 1-2 yrs) and resources to intense study and exams *right now*?",
        options=["Low", "Medium", "High"],
        key="q_commitment",
        help="Be honest about your current capacity and motivation for this level of effort."
    )

    answers['tasks'] = st.multiselect(
        "**Interest:** Which specific accounting areas genuinely interest you the most?",
        options=[
            "Auditing & Assurance", "Tax Preparation & Strategy", "Financial Reporting & Compliance",
            "Management Accounting (Budgets, Costs)", "Bookkeeping & Payroll Operations",
            "Financial Planning & Analysis (FP&A)", "Fraud Investigation / Forensics", "IT Audit / Systems"
        ],
        key="q_tasks",
        help="Select all that apply. What kind of work do you enjoy?"
    )

    # --- Feedback for Section 2 ---
    if answers['commitment'] == "Low":
        feedback_points.append("⏳ A lower current capacity for intense study points towards exploring the **Non-CPA path** first. You can always pursue certifications later if desired.")
    elif answers['commitment'] == "Medium":
        feedback_points.append("⚖️ Medium commitment means carefully weighing the **CPA path's** significant effort against its benefits for your specific goals. Success requires dedication.")
    elif answers['commitment'] == "High":
        feedback_points.append("✅ High commitment makes the **CPA path** achievable. If your goals align, this willingness is a key asset.")

    if "Auditing & Assurance" in answers['tasks']:
        feedback_points.append("🔍 Interest in Audit strongly points to the **CPA path**, as it's legally required for signing audit reports.")
    if "Tax Preparation & Strategy" in answers['tasks']:
        feedback_points.append("💵 Tax interest fits **both CPA and EA** paths. EA is solely tax-focused, while CPA offers broader accounting/business context.")
    if "Management Accounting (Budgets, Costs)" in answers['tasks'] or "Financial Planning & Analysis (FP&A)" in answers['tasks']:
        feedback_points.append("📊 Management Accounting / FP&A interests align well with corporate roles (often **Non-CPA** path) and the **CMA certification**.")
    if "Bookkeeping & Payroll Operations" in answers['tasks']:
        feedback_points.append("🧾 Bookkeeping/Payroll are core **Non-CPA path** activities. Consider practical certs like QuickBooks ProAdvisor.")
    if "Fraud Investigation / Forensics" in answers['tasks']:
        feedback_points.append("🕵️ Forensic Accounting often combines **CPA** knowledge with the specialized **CFE (Certified Fraud Examiner)** credential.")
    if "IT Audit / Systems" in answers['tasks']:
         feedback_points.append("💻 IT Audit often blends accounting knowledge (**CPA** can be helpful) with tech skills and the **CISA (Certified Information Systems Auditor)** credential.")


# --- Display Combined Feedback ---
st.divider()
st.header("💡 Your Personalized Insights")

if not answers.get('ambition') or not answers.get('environment') or not answers.get('commitment'):
     st.warning("👈 Please answer all the questions above in sections 1 & 2 to generate your personalized insights.")
else:
    st.markdown("Based on your selections, here are some points to consider:")
    if not feedback_points:
        st.info("Explore the detailed descriptions above and consider discussing with a mentor.")
    else:
        for point in feedback_points:
            # Using st.info for neutral tone, could use success/warning if desired
            st.info(point)

        # Attempt a simple summary based on weighted factors
        cpa_leaning_score = 0
        if answers['ambition'] == "Top Executive (e.g., CFO/Partner in large org)": cpa_leaning_score += 2
        if answers['environment'] == "Large Public Accounting Firm": cpa_leaning_score += 2
        if "Auditing & Assurance" in answers['tasks']: cpa_leaning_score += 2
        if answers['commitment'] == "High": cpa_leaning_score += 1
        if answers['commitment'] == "Low": cpa_leaning_score -= 2 # Strong counter-indicator
        if answers['ambition'] == "Own My Own Practice (Bookkeeping/Tax/Consulting)": cpa_leaning_score -= 1 # Can go either way, slight non-cpa lean initially
        if answers['environment'] in ["Small-Medium Business (SMB)", "Non-Profit Organization"]: cpa_leaning_score -= 1
        if "Bookkeeping & Payroll Operations" in answers['tasks']: cpa_leaning_score -= 1

        st.markdown("---")
        if cpa_leaning_score >= 3:
             st.success(f"**Overall Leaning:** Your answers suggest the **CPA path** might be a strong fit for your stated goals and commitment level ({cpa_leaning_score} points towards CPA).")
        elif cpa_leaning_score <= -1:
             st.success(f"**Overall Leaning:** Your answers suggest the **Non-CPA path** seems more aligned with your preferences right now ({abs(cpa_leaning_score)} points towards Non-CPA). Consider roles in this area or alternative certifications.")
        else: # Neutral score
             st.success("**Overall Leaning:** Your preferences show alignment with **both paths**, or key factors are balanced. Focus on which aspect (e.g., long-term ambition vs. immediate study commitment) is the *most critical deciding factor* for you. Further research into specific roles is recommended.")

st.divider()
st.markdown("This tool provides guidance, but it's not definitive. Your unique background, local job market, and personal circumstances are also important. Consider conducting informational interviews with professionals on both paths to gain deeper insights before making your decision.")
st.caption(f"Information current as of {st.session_state.get('TODAYS_DATE', 'today')}.") # Placeholder for date if needed elsewhere