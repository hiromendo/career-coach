import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Resume & Narrative", layout="wide")

# --- Page Title and Introduction ---
st.title("📄 Update Your Resume & Craft Your Narrative")
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
            * 🔗 **Action:** Explore templates from reputable sources (check links below).
            """)
            st.link_button("MS Word Templates", "https://create.microsoft.com/en-us/templates/resumes-and-cover-letters")
            st.link_button("Canva Templates", "https://www.canva.com/resumes/templates/")

    with col2:
        with st.container(border=True):
            st.markdown("##### 2. Optimize for ATS")
            st.markdown("""
            * ⚙️ Include keywords relevant to target jobs (e.g., GAAP, Reconciliation, Excel, QuickBooks).
            * 📄 Avoid complex formatting like tables or images that confuse ATS bots.
            * 📊 **Action:** Review job descriptions for keywords; consider using simple online ATS checkers/guides for formatting tips.
            """)
            # Example link to an article explaining ATS - replace if a better one is found
            st.link_button("ATS Resume Guide (Jobscan Example)", "https://www.jobscan.co/blog/ats-resume/", help="Explains how ATS works - use free advice, paid checker optional.")

    with st.container(border=True):
        st.markdown("##### 3. Feature Recent Activity")
        st.markdown("""
        * ⭐ Place recent courses, certs, volunteer work, or projects prominently.
        * sección Add a 'Recent Professional Development' or 'Skills Summary' section near the top.
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
            # Simple interactive example
            past_ach = st.text_input("Example Past Duty:", "Managed month-end close process")
            quant_ach = st.text_input("Quantified Version:", "Managed month-end close process, reducing close time by 15% over 6 months.")
            st.caption("*(Example of adding impact)*")


    with col2:
        with st.container(border=True):
            st.markdown("##### 2. Identify Transferable Skills")
            st.markdown("""
            * 🔗 Skills from your break (e.g., marketing) often apply! Think: Analysis, Communication, Project Mgmt, Tech Use.
            * 🤝 Connect these skills directly to accounting needs in your summary or descriptions.
            * 📋 **Action:** Brainstorm skills gained during your break. Check common ones below.
            """)
            st.multiselect("Common Transferable Skills:",
                           ["Project Management", "Data Analysis", "Client Communication / Service",
                            "Problem Solving", "Technology Adaptation", "Written Communication",
                            "Teamwork / Collaboration", "Time Management"],
                           key="transferable_skills_checklist", help="Select skills you developed during your break.")

    with st.container(border=True):
        st.markdown("##### 3. Combine Old & New")
        st.markdown("""
        * 🔗 Weave together your foundational accounting experience with newly refreshed knowledge and transferable skills.
        * ⭐ Your summary/objective should reflect this unique blend.
        * 📄 **Action:** Craft a powerful summary statement highlighting this combination (see Cover Letter tab for narrative).
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
            st.code("2014 – 2024    Career Break / Industry Exploration\n- Engaged in [Your Activity, e.g., Digital Marketing roles], developing skills in [e.g., data analysis, client management].\n- Undertook professional development focused on returning to Accounting (see Certifications/Courses).", language=None)

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
            * 🌐 Even non-traditional work (volunteering, freelance, personal projects) shows initiative.
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
        * ➡️ **Action:** Draft a 1-2 sentence transition statement (see examples below).
        """)
        st.markdown("---")
        st.markdown("**Example Narrative Snippets:**")
        st.info('_"Following a foundational career in accounting, I spent the last decade honing analytical and client-service skills in the marketing sector. I am now eager to bring this enhanced skillset back to my core strength in accounting."_')
        st.info('_"After a period focused on [Your Activity], during which I developed strong [Skill 1] and [Skill 2], I have refreshed my accounting knowledge through [Course/Cert] and am excited to re-enter the field."_')


    with st.container(border=True):
        st.markdown("##### 2. Show Enthusiasm & Fit")
        st.markdown("""
        * 🔥 Clearly state your excitement for the specific role and company.
        * 🎯 Explain *why* you want *this* job and how your unique background benefits *them*.
        * 🤝 **Action:** Research the company and tailor your letter to their needs/culture.
        """)

    with st.container(border=True):
        st.markdown("##### 3. Focus on Value, Not Apology")
        st.markdown("""
        * ⭐ Highlight the *value* you bring NOW (combined experience + new skills).
        * 🚫 Avoid apologizing for the gap or over-explaining personal reasons.
        * 🚀 **Action:** Project confidence in your abilities and your decision to return.
        """)
        st.link_button("More Tips on Explaining Gaps (The Muse)", "https://www.themuse.com/advice/how-to-explain-gap-in-resume-cover-letter-interview")


st.divider()
st.success("✅ A well-crafted resume and narrative turn your career break into a unique strength!")