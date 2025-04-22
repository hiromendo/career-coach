import streamlit as st

# --- Page Configuration ---
#st.set_page_config(page_title="Visual Career Paths", layout="wide")

# --- Example Image URLs (Replace with actual URLs or remove if using only emojis) ---
# Check image licenses before using!
cpa_image_url = "https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/external-cpa-accounting-flaticons-lineal-color-flat-icons.png"
non_cpa_image_url = "https://img.icons8.com/external-flaticons-flat-flat-icons/64/external-calculator-accounting-flaticons-flat-flat-icons.png"

# --- Page Title and Introduction ---
st.title("✨ Career Path Evaluation: CPA vs. Non-CPA")
st.markdown("Compare the two main accounting career paths at a glance and see which aligns with your goals.")
st.caption("Use the interactive questions below the comparison to get personalized insights.")
st.divider()

# --- Side-by-Side Visual Comparison ---
st.header("Comparing the Paths")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📜 The CPA Path")
    # Conditionally display image if URL is valid
    # try:
    #     st.image(cpa_image_url, width=64)
    # except Exception:
    #     st.markdown("**(CPA Icon)**") # Fallback text

    st.markdown("**The Premier Accounting License**")
    st.markdown("---") # Separator line

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
     # Conditionally display image if URL is valid
    # try:
    #     st.image(non_cpa_image_url, width=64)
    # except Exception:
    #     st.markdown("**(Calculator Icon)**") # Fallback text

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

st.divider()

# --- Interactive Decision Helper (Same logic, potentially slightly different presentation)---
st.header("🤔 Which Path Aligns Best With You?")
st.markdown("Answer these questions to reflect on your priorities.")

# Use a dictionary to store answers
answers = {}
feedback_points = [] # List to collect feedback messages

with st.container(border=True):
    st.markdown("**1. Career Ambitions & Preferred Environment**")
    answers['ambition'] = st.radio(
        "**Ambition:** Primary long-term goal?",
        key="v_q_ambition", # Use unique keys for widgets on this page
        options=[
            "Top Executive (e.g., CFO/Partner in large org)",
            "Department/Team Lead (e.g., Controller/Manager)",
            "Skilled Specialist / Individual Contributor",
            "Own My Own Practice (Bookkeeping/Tax/Consulting)",
            "Stable role in Government / Non-Profit",
            "Still Exploring / Unsure"
        ], index=None, help="Where do you see yourself in 10-15 years?"
    )

    answers['environment'] = st.radio(
        "**Environment:** Preferred work setting?",
        key="v_q_environment",
        options=[
            "Large Public Accounting Firm", "Corporate (Medium-Large Company)",
            "Small-Medium Business (SMB)", "Government Agency",
            "Non-Profit Organization", "Flexible / Remote / Self-Employed"
        ], index=None, help="Think about company size, culture, and type of work."
    )

    # --- Feedback generation (same logic as before) ---
    if answers['ambition'] == "Top Executive (e.g., CFO/Partner in large org)": feedback_points.append("📈 High ambition -> CPA often needed.")
    elif answers['ambition'] == "Department/Team Lead (e.g., Controller/Manager)": feedback_points.append("🧑‍💼 Team Lead -> Both paths viable (CPA/CMA helpful).")
    elif answers['ambition'] == "Skilled Specialist / Individual Contributor": feedback_points.append("💡 Specialist -> Both paths viable (CPA for audit/tax, other certs for niches).")
    elif answers['ambition'] == "Own My Own Practice (Bookkeeping/Tax/Consulting)": feedback_points.append("🏠 Own Practice -> Non-CPA (Bookkeeping) or CPA/EA (Tax/Broader Services).")
    elif answers['ambition'] == "Stable role in Government / Non-Profit": feedback_points.append("🏛️ Gov/Non-Profit -> Many Non-CPA roles (CPA/CGFM for some audit/leadership).")

    if answers['environment'] == "Large Public Accounting Firm": feedback_points.append("🏢 Public Accounting -> CPA strongly preferred.")
    elif answers['environment'] == "Corporate (Medium-Large Company)": feedback_points.append("🏭 Corporate -> Both paths (CPA for top finance, Non-CPA/CMA common).")
    elif answers['environment'] in ["Small-Medium Business (SMB)", "Non-Profit Organization"]: feedback_points.append("🌱 SMB/Non-Profit -> Often rely on skilled Non-CPAs.")
    elif answers['environment'] == "Flexible / Remote / Self-Employed": feedback_points.append("💻 Flexible/Remote -> Possible for both (Non-CPA common for bookkeeping, CPA for consulting).")


with st.container(border=True):
    st.markdown("**2. Study, Exams, and Task Preferences**")
    answers['commitment'] = st.select_slider(
        "**Commitment:** Willingness/Ability for intense study (500+ hrs) *now*?",
        key="v_q_commitment",
        options=["Low", "Medium", "High"],
        help="Be honest about your current capacity."
    )

    answers['tasks'] = st.multiselect(
        "**Interest:** Most interesting accounting areas?",
        key="v_q_tasks",
        options=[
            "Auditing & Assurance", "Tax Preparation & Strategy", "Financial Reporting & Compliance",
            "Management Accounting (Budgets, Costs)", "Bookkeeping & Payroll Operations",
            "Financial Planning & Analysis (FP&A)", "Fraud Investigation / Forensics", "IT Audit / Systems"
        ],
        help="Select all that apply."
    )

    # --- Feedback generation (same logic as before) ---
    if answers['commitment'] == "Low": feedback_points.append("⏳ Low study commitment now -> Favors Non-CPA path.")
    elif answers['commitment'] == "Medium": feedback_points.append("⚖️ Medium commitment -> Weigh CPA effort vs. reward carefully.")
    elif answers['commitment'] == "High": feedback_points.append("✅ High commitment -> Makes CPA path feasible.")

    if "Auditing & Assurance" in answers['tasks']: feedback_points.append("🔍 Audit interest -> Strongly suggests CPA.")
    if "Tax Preparation & Strategy" in answers['tasks']: feedback_points.append("💵 Tax interest -> Fits CPA or EA.")
    if "Management Accounting (Budgets, Costs)" in answers['tasks'] or "Financial Planning & Analysis (FP&A)" in answers['tasks']: feedback_points.append("📊 Mgmt Acct/FP&A -> Aligns with corporate Non-CPA roles / CMA cert.")
    if "Bookkeeping & Payroll Operations" in answers['tasks']: feedback_points.append("🧾 Bookkeeping/Payroll -> Core Non-CPA roles (Consider ProAdvisor).")
    if "Fraud Investigation / Forensics" in answers['tasks']: feedback_points.append("🕵️ Forensics -> Often benefits from CPA + CFE.")
    if "IT Audit / Systems" in answers['tasks']: feedback_points.append("💻 IT Audit -> Often CPA/CISA + tech skills.")


# --- Display Combined Feedback ---
st.divider()
st.header("💡 Your Personalized Insights")

# Check if all questions impacting feedback have been answered
all_answered = answers.get('ambition') and answers.get('environment') and answers.get('commitment')

if not all_answered:
     st.warning("👈 Please answer all questions in sections 1 & 2 above to generate personalized insights.")
else:
    st.markdown("**Based on your selections:**")
    if not feedback_points:
        st.info("Consider the path details above and perhaps discuss with a mentor.")
    else:
        # Display feedback points concisely
        feedback_container = st.container(border=True)
        for point in feedback_points:
            feedback_container.markdown(f"- {point}")

        # --- Scoring Logic (same as before) ---
        cpa_leaning_score = 0
        if answers['ambition'] == "Top Executive (e.g., CFO/Partner in large org)": cpa_leaning_score += 2
        if answers['environment'] == "Large Public Accounting Firm": cpa_leaning_score += 2
        if "Auditing & Assurance" in answers['tasks']: cpa_leaning_score += 2
        if answers['commitment'] == "High": cpa_leaning_score += 1
        if answers['commitment'] == "Low": cpa_leaning_score -= 2
        if answers['ambition'] == "Own My Own Practice (Bookkeeping/Tax/Consulting)": cpa_leaning_score -= 1
        if answers['environment'] in ["Small-Medium Business (SMB)", "Non-Profit Organization"]: cpa_leaning_score -= 1
        if "Bookkeeping & Payroll Operations" in answers['tasks']: cpa_leaning_score -= 1
        # --- End Scoring Logic ---

        st.markdown("---")
        st.subheader("Overall Suggestion:")
        if cpa_leaning_score >= 3:
             st.success(f"✅ Your answers suggest the **CPA path** aligns strongly with your goals/commitment (Score: {cpa_leaning_score}). Deep dive into CPA requirements.")
        elif cpa_leaning_score <= -1:
             st.success(f"✅ Your answers lean towards the **Non-CPA path** for now (Score: {cpa_leaning_score}). Explore specific roles or alternative certifications (CMA, EA, etc.).")
        else:
             st.success(f"⚖️ Your preferences show elements of **both paths** (Score: {cpa_leaning_score}). Revisit your most critical factors (e.g., ambition vs. study time) and research specific roles that interest you.")

st.divider()
st.caption("This tool offers guidance based on common alignments. Your unique situation matters! Consider informational interviews for deeper insights.")