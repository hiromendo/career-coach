import streamlit as st

# --- Main Title ---
st.title("🧭 Strategic Career Transition & Job Search Plan: NYC")
st.header("4. Strategic Positioning")
st.divider()

st.markdown("""
To effectively compete in the NYC market, a clear and compelling strategic positioning is essential.
""")

# --- 4.1. Unique Value Proposition (UVP) ---
st.subheader("4.1. Unique Value Proposition (UVP) ✨")
# Use st.info to highlight the UVP
st.info("""
The candidate's UVP lies in the unique intersection of **top-tier management consulting rigor**, **hands-on project management execution** (including procurement and BD support), specialized knowledge in the **energy/ESG sector**, and valuable **international/language capabilities**.

This combination allows the candidate to:
* Bridge **strategy and execution** effectively.
* Bring **analytical depth** to operational and project management challenges.
* Navigate **complex stakeholder environments** (demonstrated in large PMO roles).
* Contribute immediately to **energy, sustainability, or internationally focused initiatives**.
* Offer a **global perspective** enhanced by language fluency (Spanish, Portuguese) and international education/experience.
""")
st.divider()

# --- 4.2. Resume & Cover Letter Tailoring ---
st.subheader("4.2. Resume & Cover Letter Tailoring 📄✍️")
# Use an expander for detailed tailoring advice
with st.expander("View Resume & Cover Letter Tailoring Strategy", expanded=False):
    st.markdown("""
    The resume is comprehensive but needs tailoring for each specific application to highlight the most relevant experiences and skills for the target role.

    **Key Tailoring Actions:**

    * **Headline/Summary:** Customize to match the target role (e.g., "Project Manager | Energy & Sustainability | PMP Candidate" or "Management Consultant | Strategy & Operations | Financial Services & ESG").
    * **Experience Bullets:**
        * Prioritize and rephrase bullet points under each past role to emphasize achievements directly related to the job description keywords.
        * **Quantify achievements** wherever possible (e.g., "$XM budget managed," "% cost savings," "# projects delivered").
        * **For PM roles:** Emphasize scope, schedule, budget management, risk mitigation, stakeholder coordination, PMP/OSHA/Construction certs, specific PM tools (MS Project, Bluebeam).
        * **For Analyst roles:** Highlight analytical work (financial modeling, data analysis, market research), strategy development, process improvement, ESG analysis, client presentations, playbook development.
        * **For Procurement roles:** Focus on RFP execution, negotiation, bid analysis, subcontractor management, cost savings analysis, vendor relations.
        * **For BD roles:** Emphasize proposal support, sales results, business case development, identifying value levers, client relationship building.
    * **Skills Section:** Ensure keywords from the job description are present (if accurate). List PMP as "In Progress".
    * **Addressing Layoff (Resume):** The statement "Role terminated due to Tetra Tech downsizing" is appropriate.
    * **Cover Letter:**
        * **Always submit a tailored cover letter.**
        * Briefly explain the career trajectory.
        * Express specific interest in **that company and role**.
        * Highlight **2-3 key qualifications** matching the job description.
        * Mention **language skills/PMP/ESG focus** if relevant.
        * Address the reason for seeking a new role (downsizing + seeking specific opportunity in NYC) professionally, framing it as an opportunity. Mention availability of references.
    """)
st.divider()

# --- 4.3. LinkedIn Profile Enhancement ---
st.subheader("4.3. LinkedIn Profile Enhancement ") # Using HTML for LI icon
# Use an expander for LinkedIn tips
with st.expander("View LinkedIn Enhancement Checklist", expanded=False):
    st.markdown("""
    LinkedIn is a critical tool for networking and visibility.

    **Enhancement Checklist:**

    * **Headline:** Align with the resume headline, incorporating keywords for target roles and industries.
    * **About Section:** Expand on the UVP, telling a concise story about the career path, key skills (PM, analysis, strategy, ESG, languages), and career goals (NYC focus, target industries).
    * **Experience Section:** Ensure consistency with tailored resumes. Add relevant media/links if available. Request recommendations.
    * **Skills & Endorsements:** Add relevant skills and seek endorsements.
    * **Activity:** Actively engage with content (like, comment, share) from target companies/individuals. Join relevant industry groups.
    * **Profile Picture/Banner:** Use a professional headshot and consider a relevant banner.
    * **Open to Work Feature:** Utilize strategically, specifying target roles, location (NYC), and availability.
    """)
st.divider()

# --- 4.4. Narrative Crafting ---
st.subheader("4.4. Narrative Crafting 🗣️")
# Use an expander for narrative elements
with st.expander("Develop Your Career Narrative", expanded=False):
    st.markdown("""
    Develop a clear, concise, and compelling narrative for networking, cover letters, and interviews.

    **Key Narrative Components:**

    * **The "Story":** Connect the dots between different roles.
        * *Example:* "My career started in consulting, developing analytical, strategic, and stakeholder skills across financial services and ESG. Seeking direct project execution experience, I moved into project management, first with family real estate developments and then managing complex renewable energy projects at Tetra Tech, including procurement and BD support. My background also includes energy policy work. Following a company downsizing, I'm eager to leverage this blend of strategic analysis and hands-on project/operations management in NYC, where my language skills can also be an asset..." *(Tailor further based on specific role)*
    * **Addressing the Layoff:** Be direct, professional, and brief.
        * *Example:* "My role at Tetra Tech was impacted by a company-wide downsizing. While unexpected, I'm grateful for the experience managing renewable energy projects and am now focused on finding my next opportunity in NYC, specifically targeting roles like [Target Role] where I can apply my skills in [Skill 1] and [Skill 2]." Emphasize positives and forward look. Mention strong references available.
    * **"Why NYC?":** Be specific.
        * *Example:* "NYC is the epicenter of [Target Industry/Field], offering unparalleled opportunities in [Specific Area]. I'm also drawn to the city's energy and diversity and have [personal/professional] connections here."
    * **"Why this Role/Company?":** Connect your skills/experience directly to the company's work/mission and role requirements.
        * *Example:* "I was particularly drawn to [Company Name]'s recent work in [Specific Project/Initiative mentioned on website] because it aligns perfectly with my experience in [Relevant Skill/Experience]. The [Role Name] position seems like an excellent opportunity to leverage my background in [Skill 1] and [Skill 2] to contribute to [Company Goal/Team Objective]."
    """)
st.divider()

# --- 4.5. Target List Refinement ---
st.subheader("4.5. Target List Refinement 🎯")
# Use an expander for refinement steps
with st.expander("Refine Your Target Company List", expanded=False):
    st.markdown("""
    Use the initial list (Table 2) as a foundation and refine it continuously.

    **Refinement Steps:**

    * **Deep Dives:** Research specific divisions, teams, and initiatives within target companies (e.g., Deloitte's Energy & Resources practice, JPMorgan Chase's LatAm divisions/ESG initiatives, CleanCapital's focus, Turner Construction's NYC projects). Use company websites (careers/about sections), LinkedIn, industry news.
    * **Identify Hiring Managers/Team Members:** Use LinkedIn to find individuals in relevant roles/teams at target companies for potential networking.
    * **Prioritization:** Rank companies based on:
        * Strength of role fit (multiple relevant openings?).
        * Alignment with skills and interests (Energy, ESG, LatAm focus?).
        * Company culture (website, reviews, network insights).
        * Presence of network connections (alumni, former colleagues).
        * Recent news (growth, new projects, hiring trends).
    """)

st.divider()
st.caption("Effective strategic positioning is key to standing out in the competitive NYC job market.")

# --- How to Run ---
# Add comments explaining how to execute the Streamlit app
# To run this app:
# 1. Save the code as a Python file (e.g., `nyc_positioning_app.py`).
# 2. Ensure you have Streamlit installed (`pip install streamlit`).
# 3. Open your terminal or command prompt.
# 4. Navigate to the directory where you saved the file.
# 5. Run the command: `streamlit run nyc_positioning_app.py`
