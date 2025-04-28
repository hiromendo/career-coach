# conclusion_app.py
import streamlit as st
import pandas as pd
import datetime

# --- App Title ---
st.title("🏁 Career Transition Summary & Next Steps")
st.markdown("From Mail Handler to Logistics, Operations, or Project Coordination")
st.divider()

# --- Summary of Recommendations ---
st.header("A. Summary of Recommendations")

st.markdown("""
The analysis indicates that transitioning from a Mail Handler role into the positions below represents viable and promising career paths. Each leverages the valuable combination of practical skills from mail handling (organization, detail-orientation, process adherence) and analytical/communication skills from an undergraduate degree.
""")

st.subheader("Viable Target Roles:")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    **1. 🚚 Logistics Coordinator:**
    * **Fit:** Most direct transition, builds on familiarity with sorting, distribution, and timelines.
    """)
with col2:
    st.markdown("""
    **2. ⚙️ Operations Specialist (Entry/Associate):**
    * **Fit:** Broader scope, strongly leverages analytical skills to improve business processes.
    """)
with col3:
    st.markdown("""
    **3. 📊 Project Coordinator (Entry Level):**
    * **Fit:** Utilizes organizational/communication skills; common entry to project management.
    """)

st.subheader("Key Takeaways:")
st.success(f"""
**💰 Salary Target Achievable:** All three roles present realistic opportunities to achieve the target salary of \$50,000+ in the **Atlanta market**, especially with a bachelor's degree advantage. *(Verify salary ranges for your specific location, Bethany, OR, as needed)*.
""") # Escaped $ sign

st.info("""
**⏰ Schedule Flexibility:** Hybrid work schedules are increasingly common and attainable across these functions. A 4x10 compressed work week is less standard but possible depending on the company.
""")

st.subheader("✅ Strategic Steps for Success:")
st.markdown("""
Successfully navigating this transition relies heavily on:
* **Skill Assessment & Development:** Diligently identify and address skill gaps through targeted learning (see Resources below).
* **Tailored Application Materials:** Meticulously craft resumes and cover letters to highlight relevant skills and experiences for each target role.
* **Focused Job Search:** Prioritize companies with positive cultures that value employee appreciation and offer desired flexibility.
* **Thorough Interview Preparation:** Prepare to articulate how your unique background fits the role and company.
""")
st.divider()


# --- Final Encouragement ---
st.header("B. ✨ Final Encouragement")
st.markdown("""
Embarking on a career change requires dedication and persistence, but **it is an achievable goal.**

Your unique blend of hands-on operational experience and formal academic training provides a **strong and adaptable foundation.**

By strategically developing specific skills, effectively communicating your value, and targeting opportunities that align with your professional aspirations and personal values (including better management, appreciation, and schedule flexibility), securing a more fulfilling and rewarding career is **well within reach.**

This structured approach, combined with proactive effort, can lead to a successful transition into a role that better meets your long-term professional and personal objectives.
""")
st.divider()


# --- Resources for Your Transition ---
st.header("💡 Resources for Your Transition")
current_date_str = datetime.date.today().strftime('%B %d, %Y') # Using system date
st.markdown(f"*Below are representative links based on common transition needs. As web search isn't currently functional, please verify these or find alternatives as of {current_date_str}.*")

st.markdown("""
* **Career Change Strategies:**
    * [Indeed Career Guide: How To Make a Career Change](https://www.indeed.com/career-advice/finding-a-job/how-to-make-a-career-change)
    * [The Muse: Ultimate Guide to Career Change](https://www.themuse.com/advice/the-ultimate-guide-to-making-a-career-change)
* **Resume & Cover Letter Tailoring:**
    * [Indeed Career Guide: Tailoring Your Resume](https://www.indeed.com/career-advice/resumes-cover-letters/tailoring-resume-to-job-description)
    * [Harvard Business Review: Resume Tips for Career Changers](https://hbr.org/2021/10/writing-a-resume-when-youre-changing-careers)
* **Interview Preparation:**
    * [LinkedIn Careers Blog: Common Interview Questions](https://www.linkedin.com/pulse/how-answer-common-interview-questions-linkedin-news-asia/)
    * [Big Interview: Career Change Interview Questions](https://biginterview.com/blog/career-change-interview-questions)
* **Company Culture Research:**
    * [Glassdoor Company Reviews](https://www.glassdoor.com/Reviews/index.htm)
    * [LinkedIn Company Pages](https://www.linkedin.com/companies/) (Check employees, posts, 'Life' tab)
    * [Built In (Various Cities): Best Places to Work Lists](https://builtin.com/best-places-to-work)
* **Online Learning Platforms (Skill Development):**
    * [Coursera](https://www.coursera.org/) (Courses in Logistics, Operations, Project Management, Excel, etc.)
    * [edX](https://www.edx.org/) (Similar university-backed courses)
    * [LinkedIn Learning](https://www.linkedin.com/learning/) (Wide range of business and software skills)
    * [Project Management Institute (PMI)](https://www.pmi.org/certifications/become-a-project-manager) (For project management specific learning)
""")


# --- Footer ---
st.caption(f"Summary based on provided analysis. User location: Bethany, OR. Date: {current_date_str}")