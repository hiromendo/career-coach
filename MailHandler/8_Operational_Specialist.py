# operations_specialist_app.py
import streamlit as st
import pandas as pd
import datetime


# --- App Title ---
st.title("⚙️ Operations Specialist Role Profile (Entry/Associate Level)")
st.markdown("An overview of the role focused on analyzing, improving, and managing internal business processes.")
st.divider()

# --- Role Overview & Suitability ---
st.header("🎯 Role Overview & Suitability")
st.markdown("""
Operations Specialists focus on analyzing, improving, and managing internal business processes to enhance efficiency, reduce costs, and ensure smooth functioning.

**Scope:**
Generally broader than logistics, touching various aspects of how a business operates.

**Key Skills Leveraged:**
Strongly leverages **analytical**, **problem-solving**, and **organizational** skills. An undergraduate degree is particularly relevant.

**Relevance to Mail Handling:**
The process-oriented nature connects with the procedural aspects of mail handling (e.g., following steps, identifying bottlenecks).
""")
st.divider()

# --- Day-to-Day Responsibilities ---
st.header("📅 Day-to-Day Responsibilities")
st.markdown("Tasks can be diverse but often include:")
st.markdown("""
* Collecting and analyzing operational data to identify performance trends, bottlenecks, and improvement opportunities.
* Developing, documenting, and implementing new or refined operational procedures, protocols, and workflows.
* Monitoring day-to-day operational activities and performance metrics.
* Supporting operations managers in planning, coordinating activities, and reporting.
* Managing operational resources (e.g., inventory, supplies, personnel schedules).
* Ensuring operations comply with relevant industry regulations, legal standards, and internal policies.
* Preparing regular reports on operational performance, project status, or compliance assessments.
* Utilizing software tools, especially **Microsoft Excel** for data analysis, and potentially CRM systems, project management tools (e.g., Asana, Jira), or industry-specific platforms.
""")
st.divider()

# --- Qualifications & Entry Requirements ---
st.header("🎓 Qualifications & Entry Requirements")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Education")
    st.markdown("""
    * **Bachelor's Degree:** Often standard or strongly preferred.
    * **Typical Fields:** Business Administration, Operations Management, Finance, or related analytical disciplines.
    * *(Your undergraduate degree aligns well.)*
    """)

with col2:
    st.subheader("Experience")
    st.markdown("""
    * **Typical Range:** 1-2 years in operational, administrative, analytical, or related roles.
    * **Relevant Background:** Mail handling (process execution) combined with analytical skills from degree can be positioned effectively.
    """)

with col3:
    st.subheader("Skills")
    st.markdown("""
    * Strong Analytical & Problem-Solving
    * Excellent Organizational Skills
    * Clear Communication (Written & Verbal)
    * Proficiency in Microsoft Excel (Data analysis is key!)
    * Attention to Detail
    * Ability to Work Independently
    * Basic Project Management Understanding
    """)
st.divider()

# --- Salary Landscape (Atlanta/Remote) ---
st.header("💰 Salary Landscape (Atlanta / Remote Focus)")
st.markdown(f"*(Salary data estimates based on input, potentially from late 2023/early 2024. Current data as of {datetime.date.today().strftime('%B %d, %Y')} may vary. Verify with current listings.)*")

st.subheader("Atlanta Market Estimates:")
# Using st.metric for a more visual display
col_sal1, col_sal2, col_sal3 = st.columns(3)
col_sal1.metric(label="Average Salary (Atlanta - General Ops Specialist)", value="$65,803")
col_sal2.metric(label="Typical Range (25th-75th percentile)", value="$46.2k - $78.4k")
col_sal3.metric(label="Related Role Avg (Ops Support Spec.)", value="$59,961")

st.markdown("""
* **Remote Roles:** National averages can appear higher (e.g., $111k mentioned in source) but often include more senior or specialized positions. Entry-level remote may differ.
* **\$50,000 Target:** Falls comfortably within the typical Atlanta range, near or slightly above the 25th percentile (\$46.2k). **This is a realistic financial goal for an entry/associate level position.**
""")
st.divider()

# --- Schedule Flexibility ---
st.header("⏰ Schedule Flexibility")

flex_col1, flex_col2 = st.columns(2)

with flex_col1:
    st.subheader("Hybrid Work (🏡 + 🏢)")
    st.markdown("""
    * **Very Common:** Much of the work (analysis, reporting, documentation, coordination) suits remote execution.
    * **Job Postings:** Numerous postings explicitly list hybrid options.
    * **General Trends:** Hybrid remains a popular model for office/analytical roles.
    """)
    st.success("✅ High Likelihood of Finding Hybrid Roles")

with flex_col2:
    st.subheader("Compressed Work Week (4x10 🗓️)")
    st.markdown("""
    * **Less Standard:** Compared to hybrid, less common for typical office-based Operations Specialists.
    * **Possibility:** Might exist in industries with specific operational needs (e.g., healthcare, manufacturing, logistics shifts) but not the norm for general business operations roles.
    * **Depends on Employer:** Flexibility policies vary significantly.
    """)
    st.warning("⚠️ Possible, but Less Probable than Hybrid")

st.divider()

# --- Work Environment Considerations ---
st.header("🏢 Work Environment Considerations")
st.markdown("""
* **Setting:** Typically office environments or hybrid settings.
* **Culture/Pace:** Varies significantly by company and industry sector (e.g., tech startup vs. established manufacturer).
* **Research Recommended:** Look into company reviews and 'Best Places to Work' lists to find environments that align with your preferences for culture, pace, and team dynamics.
""")
st.divider()

# --- References & Further Reading ---
st.header("🌐 References & Further Reading")
st.markdown(f"""
*Below are representative links based on the topics discussed. As web search isn't currently functional, these are examples. Please verify with current sources as of {datetime.date.today().strftime('%B %d, %Y')}.*

* **General Role Descriptions:**
    * [Indeed: Operations Specialist Job Description](https://www.indeed.com/hire/job-description/operations-specialist)
    * [LinkedIn: Operations Specialist Roles](https://www.linkedin.com/jobs/operations-specialist-jobs/)
* **Salary Data:**
    * [Salary.com: Operations Specialist Salary Atlanta, GA](https://www.salary.com/research/salary/benchmark/operations-specialist-salary/atlanta-ga)
    * [Glassdoor: Operations Specialist Salaries](https://www.glassdoor.com/Salaries/operations-specialist-salary-SRCH_KO0,21.htm)
* **Skills & Software:**
    * [Coursera: Business Analysis Skills](https://www.coursera.org/articles/business-analyst-skills) (Related analytical skills)
    * [Microsoft Excel Official Site](https://www.microsoft.com/en-us/microsoft-365/excel)
* **Work Schedules & Trends:**
    * [Forbes Advisor: Hybrid Work Statistics {datetime.date.today().year}](https://www.forbes.com/advisor/business/hybrid-work-statistics/) *(Example - search for current stats)*
    * [SHRM: Flexible Work Resource Page](https://www.shrm.org/topics-tools/topics/flexible-work)
* **Company Research:**
    * [Built In Atlanta: Best Places to Work](https://builtin.com/atlanta/best-places-to-work-atlanta)
    * [Glassdoor: Company Reviews](https://www.glassdoor.com/Reviews/index.htm)
""")

# --- Footer ---
st.caption(f"Information compiled based on provided text and general knowledge. Last updated conceptually: {datetime.date.today().strftime('%B %d, %Y')}")