import streamlit as st

# --- Page Configuration ---
#st.set_page_config(page_title="Credential Pathways", layout="wide")

# --- Page Title and Introduction ---
st.title("🎓 Address Education & Credential Gaps")
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
st.session_state.credential_path_choice = st.radio(
    "**Select Your Credential Situation:**",
    options=path_options,
    index=None, # No default selection
    key='path_radio', # Assign a key to the radio button
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