# project_coordinator_app.py
import streamlit as st
import pandas as pd
import datetime

# --- App Title ---
st.title("📊 Project Coordinator Role Profile (Entry Level)")
st.markdown("An overview of the role focused on supporting project teams and ensuring smooth project progression.")
st.divider()

# --- Role Overview & Suitability ---
st.header("🎯 Role Overview & Suitability")
st.markdown("""
Project Coordinators play a crucial support role within project teams, assisting Project Managers by handling administrative, organizational, and communication tasks. The goal is to ensure projects progress smoothly and meet objectives.

**Key Skills Leveraged:**
Directly leverages **organizational**, **time management**, **attention to detail**, and **communication** skills. Skills developed through mail handling (task management, schedules, organization) and an undergraduate degree are highly relevant.

**Career Path:**
Serves as a common and accessible entry point into the broader field of project management.
""")
st.divider()

# --- Day-to-Day Responsibilities ---
st.header("📅 Day-to-Day Responsibilities")
st.markdown("Typical duties involve:")
st.markdown("""
* Maintaining and organizing project documentation (plans, schedules, status reports, meeting minutes, risk logs).
* Tracking project progress against timelines, milestones, budgets, and resource allocation.
* Scheduling and coordinating project meetings, preparing agendas/materials, and distributing notes/action items.
* Facilitating communication among project team members, stakeholders, and potentially vendors or clients.
* Providing administrative support to the Project Manager and the team.
* Assisting with tracking resources, monitoring expenditures, and potentially processing project-related invoices.
* Using project management software (e.g., **Asana, Jira, Trello, MS Project**) and standard office productivity tools (**MS Office Suite**).
""")
st.divider()

# --- Qualifications & Entry Requirements ---
st.header("🎓 Qualifications & Entry Requirements")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Education")
    st.markdown("""
    * **Bachelor's Degree:** Frequently preferred or required. Provides foundational analytical and communication skills.
    * *(Your undergraduate degree is highly suitable.)*
    """)

with col2:
    st.subheader("Experience")
    st.markdown("""
    * **Typical Range:** Often genuinely entry-level (0-2 years).
    * **Prior Experience:** Administrative, coordination, or support roles are beneficial. Internships are a plus.
    * **Relevant Background:** Mail handling can highlight task management, adherence to schedules, and organization.
    """)

with col3:
    st.subheader("Skills")
    st.markdown("""
    * Exceptional Organization
    * Effective Time Management
    * Strong Written & Verbal Communication
    * Meticulous Attention to Detail
    * Practical Problem-Solving
    * Proficiency in MS Office Suite
    * Ability to Work Under Deadlines
    * Strong Teamwork Skills
    * *Familiarity with PM concepts/software is a plus*
    """)
st.divider()

# --- Salary Landscape (Atlanta/Remote Focus) ---
st.header("💰 Salary Landscape (Atlanta / Remote Focus)")
# Get current date - use the date provided in the thought process context if available
current_date_str = datetime.date.today().strftime('%B %d, %Y') # Fallback to system date if specific date wasn't captured
st.markdown(f"*(Salary data specific to **Atlanta** based on input, potentially from late 2023/early 2024. Current data as of {current_date_str} may vary. Verify with current listings for Atlanta or your specific location.)*")

st.subheader("Atlanta Market Estimates (Entry-Level):")
# Using st.metric for a more visual display
col_sal1, col_sal2 = st.columns(2)
# Escape the $ sign in the metric values
col_sal1.metric(label="Average Salary (Atlanta - Entry Level)", value="$46,862")
col_sal2.metric(label="75th Percentile (Atlanta - Entry Level)", value="$54,800")

st.markdown("""
* **Variations:** Data sources differ slightly (e.g., state averages vs. city, general vs. marketing roles). Entry points might start near \\$45k (or lower for specific fields like marketing entry). General Project *Manager* roles pay significantly more but require greater experience.
* **\\$50,000 Target:** Falls between the average and 75th percentile for entry-level Project Coordinators in Atlanta. **This is a realistic and achievable financial goal for this role in the Atlanta market, supported by an undergraduate degree.**
""") # Escaped $ signs here
st.divider()

# --- Schedule Flexibility ---
st.header("⏰ Schedule Flexibility")

flex_col1, flex_col2 = st.columns(2)

with flex_col1:
    st.subheader("Hybrid Work (🏡 + 🏢)")
    st.markdown("""
    * **Increasingly Common:** Aligns with distributed project teams trend.
    * **Job Postings:** Confirm availability of hybrid Project Coordinator roles.
    * **General Trends:** Significant portion of PM professionals work remotely at least part-time. Hybrid options remain strong for office roles.
    """)
    st.success("✅ Reasonably Attainable Option")

with flex_col2:
    st.subheader("Compressed Work Week (4x10 🗓️)")
    st.markdown("""
    * **Less Typical:** Often align with standard M-F business hours.
    * **Possibility:** Might be feasible depending on specific project demands, team structures, and company policy. Worth searching for in job postings.
    * **Not the Norm:** Less common than hybrid for this type of role.
    """)
    st.warning("⚠️ Possible, but Less Common than Hybrid")

st.divider()

# --- Work Environment Considerations ---
st.header("🏢 Work Environment Considerations")
st.markdown("""
* **Setting:** Typically office-based or hybrid.
* **Pace:** Can be fast-paced, especially nearing project deadlines. Requires significant collaboration.
* **Culture is Key:** Research company culture, team dynamics, and management practices (e.g., via reviews) to find a supportive environment.
""")
st.divider()

# --- References & Further Reading ---
st.header("🌐 References & Further Reading")
st.markdown(f"""
*Below are representative links based on the topics discussed. As web search isn't currently functional, these are examples. Please verify with current sources as of {current_date_str}.*

* **General Role Descriptions:**
    * [Project Management Institute (PMI): What is a Project Coordinator?](https://www.pmi.org/about/learn-about-pmi/what-is-project-management/project-coordinator)
    * [Indeed: Project Coordinator Job Description](https://www.indeed.com/hire/job-description/project-coordinator)
    * [LinkedIn: Project Coordinator Roles](https://www.linkedin.com/jobs/project-coordinator-jobs/)
* **Salary Data (Atlanta Focus):**
    * [Salary.com: Project Coordinator I Salary Atlanta, GA](https://www.salary.com/research/salary/benchmark/project-coordinator-i-salary/atlanta-ga) (Check for entry-level filters)
    * [Glassdoor: Project Coordinator Salaries Atlanta, GA](https://www.glassdoor.com/Salaries/atlanta-project-coordinator-salary-SRCH_IL.0,7_IM56_KO8,27.htm)
* **Skills & Software:**
    * [Asana: Project Management Skills](https://asana.com/resources/project-management-skills)
    * [List of Project Management Software (Wikipedia)](https://en.wikipedia.org/wiki/Comparison_of_project-management_software)
* **Work Schedules & Trends:**
    * [PMI Pulse of the Profession Report](https://www.pmi.org/learning/thought-leadership/pulse) (Look for reports discussing work trends)
    * [General Hybrid Work Statistics Search ({datetime.date.today().year})](https://www.google.com/search?q=hybrid+work+statistics+{datetime.date.today().year})
* **Company Research:**
    * [Glassdoor: Company Reviews](https://www.glassdoor.com/Reviews/index.htm)
    * [Built In: Best Places to Work (Filter by Location)](https://builtin.com/best-places-to-work)
""") # No $ signs in this section to escape

# --- Footer ---
st.caption(f"Information compiled based on provided text (Atlanta focus) and general knowledge. Current user location: Bethany, OR. Last updated conceptually: {current_date_str}")