import streamlit as st

# --- Main Title ---
st.title("5. Actionable Job Search Plan (Phased Approach)")

st.divider()

st.markdown("""
This plan outlines a structured approach over several weeks, with later phases running concurrently. Consistency and organization are key.
""")

# --- Phase 1: Preparation ---
st.subheader("5.1. Phase 1: Preparation (Weeks 1-2) 🛠️")
with st.expander("Expand Preparation Details", expanded=True): # Start expanded
    st.markdown("""
    * **Resume & Cover Letter Masters:**
        * Create master versions tailored for each primary target role category (PM, Analyst, Procurement, BD).
        * Refine bullet points using action verbs and quantification.
        * Develop an adaptable standard cover letter template.
        * Incorporate keywords from relevant job descriptions.
        * Ensure layoff is addressed professionally: *"Role terminated due to Tetra Tech downsizing – supporting references listed below."*
    * **LinkedIn Profile Enhancement:**
        * Update headline, 'About' section, experience, skills per Section 4.3 strategy.
        * Ensure consistency with master resumes.
        * Obtain a professional headshot if needed.
        * Start engaging (liking/commenting) with relevant content.
    * **Narrative Crafting:**
        * Finalize the core "story" (Section 4.4). Practice articulating it concisely.
        * Prepare and practice answers to common interview questions (Tell me about yourself, Why this role?, Why NYC?, Tell me about the layoff). Leverage positive framing and mention reference availability.
    * **Target List Refinement:**
        * Build the initial detailed target company list (Section 3.4, Table 2).
        * Begin deeper research into top 10-15 priority companies using LinkedIn, company career pages (e.g., [Deloitte Careers](https://www2.deloitte.com/us/en/careers/careers.html), [JPMorgan Chase Careers](https://careers.jpmorgan.com/us/en/students/programs), [CleanCapital Careers](https://cleancapital.com/careers/), [Turner Construction Careers](https://www.turnerconstruction.com/careers)), and news searches.
        * Identify specific teams or potential contacts.
    """)
st.divider()

# --- Phase 2: Outreach & Networking ---
st.subheader("5.2. Phase 2: Outreach & Networking (Weeks 2-Ongoing) 🤝")
with st.expander("Expand Outreach & Networking Details"):
    st.markdown("""
    Networking is crucial, especially given the layoff context, as referrals often bypass initial screening hurdles.

    * **Leverage Existing Network:**
        * Systematically reach out to trusted former colleagues (Tetra Tech, BCG, PwC, WIEB fellowship), classmates (Stanford, UPenn, Minho), and personal contacts.
        * Use a concise message explaining the situation (downsizing), target roles/industries in NYC, and ask for advice, insights, or introductions.
    * **Alumni Networks:**
        * Actively use Stanford and UPenn alumni databases and LinkedIn groups.
        * Search for alumni at target companies or in desired roles in NYC.
        * Attend virtual or local alumni events if feasible.
    * **LinkedIn Networking:**
        * Identify 2nd/3rd-degree connections at priority companies.
        * Send personalized connection requests (mention shared connection, alma mater, specific interest).
        * Engage thoughtfully with posts by key contacts or company pages.
        * Join relevant LinkedIn groups (PMP holders, Energy Professionals, NYC Finance Network).
    * **Informational Interviews:**
        * Request brief (15-20 min) virtual/coffee meetings for learning and advice (not directly asking for a job).
        * Prepare specific questions about roles, culture, trends, and advice.
    * **Industry Events:**
        * Research and attend relevant virtual or NYC-based events (Energy/Renewables, Finance, Consulting, Construction).
        * Prepare a brief elevator pitch based on your narrative.
    """)
st.divider()

# --- Phase 3: Application & Targeting ---
st.subheader("5.3. Phase 3: Application & Targeting (Weeks 3-Ongoing) 📝")
with st.expander("Expand Application & Targeting Details"):
    st.markdown("""
    Apply strategically, prioritizing quality and fit over sheer volume.

    * **Strategic Application:**
        * Focus on roles strongly aligning with profile/goals, especially those from networking or priority companies.
        * **Tailor resume and cover letter for EVERY application**, using keywords.
    * **Utilize Multiple Channels:**
        * **Company Career Portals:** Apply directly (e.g., [Deloitte](https://www2.deloitte.com/us/en/careers/careers.html), [JPMorgan Chase](https://careers.jpmorgan.com/us/en/students/programs), [CleanCapital](https://cleancapital.com/careers/), [Turner Construction](https://www.turnerconstruction.com/careers)).
        * **Major Job Boards:** Use [LinkedIn](https://www.linkedin.com/jobs/), [Indeed](https://www.indeed.com/), [ZipRecruiter](https://www.ziprecruiter.com/).
        * **Niche Job Boards:** Explore industry-specific boards (e.g., [Climatebase](https://climatebase.org/) for energy/ESG, [eFinancialCareers](https://www.efinancialcareers.com/) for finance), construction sites, university boards.
        * **Premium Job Boards:** Consider [TheLadders](https://www.theladders.com/) for $100k+ roles.
    * **Referrals:** **Prioritize applying through referral links** obtained via networking.
    * **Targeting LatAm Roles:**
        * Use keywords ("Latin America," "LatAm," "Spanish," "Portuguese") in searches.
        * Reach out to contacts in LatAm-focused teams (e.g., Citi, Latham & Watkins, Willkie Farr, Santander, BTG Pactual) if appropriate.
    * **Follow Up:**
        * Send a brief follow-up note (email/LinkedIn) 1-2 weeks after applying, especially if referred or had prior contact. Reiterate interest and key qualifications.
    """)
st.divider()

# --- Phase 4: Interviewing & Negotiation ---
st.subheader("5.4. Phase 4: Interviewing & Negotiation (As opportunities arise) 💼")
with st.expander("Expand Interviewing & Negotiation Details"):
    st.markdown("""
    Preparation is key to converting interviews into offers.

    * **Interview Preparation:**
        * **Company Research:** Thoroughly research mission, values, news, projects, culture (website, LinkedIn, press releases). Understand market position.
        * **Role Alignment:** Re-read job description, identify key competencies, prepare specific examples.
        * **STAR Method:** Structure behavioral answers: Situation, Task, Action, Result (quantifiable). Prepare examples for PM, analysis, problem-solving, leadership, teamwork, challenges.
        * **Practice:** Conduct mock interviews. Practice narrative and answering common/challenging questions (including layoff).
        * **Case Studies (If Applicable):** Practice frameworks and quantitative analysis for consulting/strategy roles.
        * **Questions for Interviewer:** Prepare 3-5 thoughtful questions per interviewer (role, team, culture, challenges, opportunities).
    * **Leverage Differentiators:** Strategically weave in unique strengths: consulting + execution, energy/ESG expertise, PMP progress, construction knowledge, language skills (Spanish/Portuguese).
    * **Salary Negotiation:**
        * **Know Your Worth:** Use salary data (Table 1), factor in advanced degrees/experience.
        * **Timing:** Avoid discussing salary too early. If asked, provide a researched range (e.g., "$115k-$135k base," ensuring bottom >= $100k minimum).
        * **Justification:** Articulate value based on skills, experience, UVP.
        * **Total Compensation:** Evaluate the entire package (base, bonus potential, benefits, PTO, development). Negotiate on the total package if needed.
    """)
st.divider()

# --- 5.5. Tracking and Momentum Management ---
st.subheader("5.5. Tracking and Momentum Management 📈")
with st.expander("Expand Tracking & Momentum Details"):
    st.markdown("""
    A systematic approach is vital for managing complexity and maintaining motivation.

    * **Use a Tracking System:**
        * Employ a spreadsheet (Google Sheets, Excel) or job search tool (JibberJobber, Huntr, Teal).
        * Track: Target companies/roles, contacts (names, dates, follow-ups), applications (date, role, company, link, status), interviews (dates, interviewers, notes), follow-up reminders.
    * **Set Weekly Goals:**
        * Establish SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound).
        * Examples: "Reach out to 5 new contacts," "Submit 3 tailored applications," "Follow up on 5 applications," "Spend 2 hours on interview prep."
    * **Stay Positive & Persistent:**
        * Acknowledge the process can be taxing.
        * **Maintain Routine:** Stick to a regular schedule.
        * **Stay Organized:** Use the tracking system diligently.
        * **Celebrate Small Wins:** Acknowledge progress.
        * **Leverage Support Network:** Talk to friends, family, mentors.
        * **Manage Expectations:** Finding the right role takes time. Focus on process and improvement.
    """)

st.divider()
st.success("Implementing this structured, multi-faceted plan significantly increases the likelihood of success. Consistency and organization are paramount.")

# --- How to Run ---
# Add comments explaining how to execute the Streamlit app
# To run this app:
# 1. Save the code as a Python file (e.g., `nyc_action_plan_app.py`).
# 2. Ensure you have Streamlit installed (`pip install streamlit`).
# 3. Open your terminal or command prompt.
# 4. Navigate to the directory where you saved the file.
# 5. Run the command: `streamlit run nyc_action_plan_app.py`
