import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Job Search Launch", layout="wide")

# --- Page Title and Introduction ---
st.title("🚀 Launch Your Targeted Job Search")
st.markdown("""
You've refreshed your skills, updated your resume, and started networking! Now it's time to actively
search and apply for roles in a focused, strategic way.

Follow these steps to manage your job search effectively. Click on each step to see detailed actions.
""")
st.info("✨ **Goal:** Systematically find and apply for suitable roles, leveraging your preparation.", icon="🎯")
st.divider()

# --- Step-by-Step Action Plan ---

# === Step 1 ===
st.subheader("Step 1: 🎯 Define Your Target & Strategy")
st.markdown("Focus your search for maximum efficiency.")
with st.expander("Click for Actionable Steps..."):
    st.markdown("##### Reconfirm Your Goals:")
    st.markdown("""
    * ✅ Review decisions from the 'Career Goal Evaluation' page (CPA/Non-CPA, industry interest).
    * 🎯 Set realistic target role levels (e.g., Staff Accountant if previously Senior) for re-entry.
    * 📍 Define location needs: Portland On-site, Hybrid, or Remote (OR-based or wider?).
    """)
    st.markdown("##### Research Companies:")
    st.markdown("""
    * 🏭 Identify specific Portland companies in your target industries/sizes.
    * 🌐 Research their culture, values, and recent news via their website & LinkedIn.
    * 📝 Keep a running list of target employers.
    """)
    st.markdown("##### Prepare Your Pitch:")
    st.markdown("""
    * 🗣️ Refine your 30-second "elevator pitch" explaining your background and return.
    * 🔑 Identify 3-5 key strengths/experiences relevant to your target roles.
    * 📖 Practice articulating your value proposition concisely.
    """)

# === Step 2 ===
st.subheader("Step 2: 🔍 Identify Opportunities")
st.markdown("Actively search using multiple channels.")
with st.expander("Click for Actionable Steps..."):
    st.markdown("##### Use Key Job Boards:")
    st.markdown("""
    * 🔔 Set up daily/weekly email alerts with specific keywords (e.g., "Staff Accountant Portland", "Remote Accountant Oregon", "Bookkeeper Hybrid") on major sites (LinkedIn, Indeed).
    * 📌 Regularly check niche/local boards: **Mac's List** & **OSCPA Career Center** are crucial for Portland.
    * ☁️ Use remote-specific boards if applicable (FlexJobs, We Work Remotely).
    """)
    st.link_button("Mac's List", "https://www.macslist.org/")
    st.link_button("OSCPA Career Center", "https://www.orcpa.org/career-center") # Membership may be required
    st.markdown("##### Activate Your Network:")
    st.markdown("""
    * 🤝 Inform key contacts you're *actively searching* and specify the types of roles/companies.
    * ❓ Ask politely if they know of openings or relevant people you should talk to.
    * 🔗 Request introductions or permission to name-drop if appropriate.
    """)
    st.page_link("pages/9_🤝_Networking_Strategy.py", label="Review Networking Strategies", icon="🤝")
    st.markdown("##### Engage Staffing Agencies:")
    st.markdown("""
    * 📞 Check in with recruiters you've registered with.
    * 📋 Reiterate your search criteria and availability (temp, contract, perm?).
    * 🆕 Ask about newly listed contract or temp-to-hire roles.
    """)
    st.page_link("pages/8_💼_Gain_Experience.py", label="See Staffing Agency List", icon="💼")


# === Step 3 ===
st.subheader("Step 3: ✍️ Apply Strategically")
st.markdown("Submit high-quality, targeted applications.")
with st.expander("Click for Actionable Steps..."):
    st.markdown("##### Tailor Each Application:")
    st.markdown("""
    * 🔑 Analyze the job description; customize your resume with relevant keywords (skills, software).
    * ✍️ Write a targeted cover letter connecting your unique background & skills to *their* specific needs. (Use your narrative!).
    * 📄 Proofread carefully! Avoid generic submissions.
    """)
    st.page_link("pages/10_📄_Resume_Narrative.py", label="Review Resume/Narrative Guide", icon="📄")
    st.markdown("##### Prioritize & Leverage Referrals:")
    st.markdown("""
    * ⭐ Give priority to roles where you have an internal contact or referral.
    * 🗣️ Mention your referral source clearly in your cover letter or application (with permission).
    * ⏳ Apply promptly, especially for roles with referrals.
    """)
    st.markdown("##### Track Your Applications:")
    st.markdown("""
    * 📊 Use a spreadsheet or tool to log: Company, Role, Date Applied, Link, Contact Person, Status.
    * 🗓️ Set reminders for follow-up if needed.
    * 📈 Stay organized to manage multiple applications effectively.
    """)
    # Optional: Link to a simple template or article about tracking
    # st.link_button("Job Application Tracker Tips", "...")


# === Step 4 ===
st.subheader("Step 4: 🤝 Prepare for Interviews")
st.markdown("Showcase your skills, enthusiasm, and fit.")
with st.expander("Click for Actionable Steps..."):
    st.markdown("##### Practice Your Story & Answers:")
    st.markdown("""
    * 🗣️ Rehearse your return-to-work narrative confidently.
    * ❓ Prepare answers for common questions (Why this role? Why now? Strengths? Gap? How are skills current?).
    * ⭐ Use the STAR method (Situation, Task, Action, Result) for behavioral questions.
    """)
    st.link_button("STAR Method Explained (The Muse)", "https://www.themuse.com/advice/star-interview-method")
    st.markdown("##### Research the Company & Role:")
    st.markdown("""
    * 🌐 Go beyond the homepage: Understand their mission, values, recent news, competitors.
    * 👥 Research your interviewers on LinkedIn if possible.
    * 🤔 Prepare questions that show genuine interest and insight.
    """)
    st.markdown("##### Logistics & Mindset:")
    st.markdown("""
    * 💻 Test technology beforehand for virtual interviews. Plan your attire.
    * 🧘 Manage nerves: Practice relaxation techniques, get good sleep.
    * 👍 Project positivity, enthusiasm, and professionalism.
    """)


# === Step 5 ===
st.subheader("Step 5: ✨ Follow Up & Stay Positive")
st.markdown("Maintain momentum and manage the process professionally.")
with st.expander("Click for Actionable Steps..."):
    st.markdown("##### Post-Interview Follow-Up:")
    st.markdown("""
    * 📧 Send personalized thank-you emails to each interviewer within 24 hours.
    * ✍️ Briefly reference a specific point from the conversation and reiterate your interest.
    * ✅ Proofread carefully before sending.
    """)
    # st.link_button("Interview Follow-Up Email Guide", "...") # Optional link
    st.markdown("##### Manage Waiting & Communication:")
    st.markdown("""
    * ⏳ Respect stated hiring timelines. Follow up politely via email if you haven't heard back after a reasonable period (e.g., 1-2 weeks past expected date).
    * 📞 Respond promptly to any communication from the employer.
    * 📝 Keep your application tracker updated with interview stages and follow-up dates.
    """)
    st.markdown("##### Maintain Momentum & Mindset:")
    st.markdown("""
    * ➡️ **Don't stop!** Continue networking, searching, and applying even while interviewing.
    * 💪 Stay positive! Job searching takes time. Celebrate small wins (getting an interview, positive feedback).
    * 🌱 Keep building experience (volunteer/contract work) if applicable; mention updates in later interview stages.
    """)


st.divider()
st.success("🚀 Launching your search is a big step! Stay organized, focused, and persistent.", icon="✅")