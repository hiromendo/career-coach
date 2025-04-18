import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Gain Recent Experience", layout="wide")

# --- Page Title and Introduction ---
st.title("💼 Gaining Recent Experience After a Break")
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
    st.link_button("Hands On Greater Portland", "https://www.handsonportland.org/")
    st.link_button("Idealist (Volunteer Filter)", "https://www.idealist.org/en/jobs?job_type=VOLOP")
    st.link_button("Catchafire", "https://www.catchafire.org/")
    st.link_button("IRS VITA/TCE Volunteer Info", "https://www.irs.gov/individuals/irs-tax-volunteers")
    st.link_button("Upwork", "https://www.upwork.com/")


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
    st.link_button("iRelaunch", "https://www.irelaunch.com/")
    st.link_button("Path Forward", "https://www.pathforward.org/")
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
    st.link_button("Robert Half / Accountemps", "https://www.roberthalf.com/us/en/locations/or/portland")
    st.link_button("Ledgent Finance & Accounting", "https://ledgent.com/locations/portland-finance-and-accounting-staffing-agencies/")
    st.link_button("Aston Carter", "https://www.astoncarter.com/en/locations/north-america/united-states/oregon/portland")
    st.link_button("VanderHouwen", "https://www.vanderhouwen.com/")
    st.link_button("Boly:Welch", "https://bolywelch.com/")
    st.markdown("*Also search Indeed/LinkedIn for 'Contract' or 'Temporary' Accounting roles.*")


st.divider()
st.info("**Key Takeaway:** Combining one or more of these strategies can effectively build recent, relevant experience for your resume and demonstrate your commitment to re-entering the accounting field.", icon="💡")