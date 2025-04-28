# logistics_coordinator_app.py
import streamlit as st
import pandas as pd
import datetime

# --- App Title ---
st.title("🚚 Logistics Coordinator Role Profile")
st.markdown("An overview of the role, responsibilities, qualifications, salary, and work environment.")
st.divider()

# --- Role Overview & Suitability ---
st.header("🎯 Role Overview & Suitability")
st.markdown("""
This position centers on managing and coordinating various aspects of the supply chain, including transportation, warehousing, inventory management, and order fulfillment.

**Relevance to Mail Handling:**
The direct relevance to mail handling experience is clear – skills like sorting, distribution planning, understanding timelines, and attention to detail are **foundational**.

**Key Skills:**
Organizational skills honed in previous roles and education are **paramount**.

**Career Path:**
This role often serves as an accessible entry point into the broader field of supply chain management, offering significant growth potential.
""")
st.divider()


# --- Day-to-Day Responsibilities ---
st.header("📅 Day-to-Day Responsibilities")
st.markdown("Common tasks include:")
st.markdown("""
* Monitoring and tracking shipments, providing status updates to relevant parties.
* Communicating and coordinating with carriers, suppliers, warehouse personnel, and customers to ensure smooth operations.
* Preparing, reviewing, and processing shipping documentation such as purchase orders, bills of lading, and invoices for accuracy.
* Maintaining inventory records, potentially assisting with warehouse organization or scheduling.
* Addressing and resolving shipping delays, errors, or other logistical problems.
* Utilizing logistics software systems (like Enterprise Resource Planning - **ERP**, or Transportation Management Systems - **TMS**) and standard office software, particularly **Microsoft Excel**.
* Potentially negotiating freight rates with carriers (may be more common in advanced roles).
""")
st.divider()

# --- Qualifications & Entry Requirements ---
st.header("🎓 Qualifications & Entry Requirements")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Education")
    st.markdown("""
    * **High School Diploma:** May suffice for some entry points.
    * **Bachelor's Degree:** Increasingly preferred or required, especially for advancement. Provides a distinct advantage.
    * *(Source: Bureau of Labor Statistics notes a Bachelor's is typical for Logisticians)*
    """)

with col2:
    st.subheader("Experience")
    st.markdown("""
    * **Typical Range:** 1-3 years in logistics, transportation, customer service, or related administrative fields.
    * **Relevant Background:** Mail handling experience, framed correctly, provides exposure to logistics principles.
    """)

with col3:
    st.subheader("Skills")
    st.markdown("""
    * Strong Organization
    * Clear Communication (Written & Verbal)
    * Meticulous Attention to Detail
    * Effective Problem-Solving
    * Robust Time Management
    * Proficiency in MS Office (especially Excel)
    * Familiarity with Logistics Software (ERP/TMS) - *Ideal*
    """)
st.divider()


# --- Salary Landscape (Atlanta/Remote) ---
st.header("💰 Salary Landscape (Atlanta / Remote Focus)")
st.markdown(f"*(Salary data estimates as of early 2024/late 2023, current data ({datetime.date.today().year}) may vary slightly. You should check current listings.)*")

st.subheader("Atlanta Market Estimates:")
# Using st.metric for a more visual display
col_sal1, col_sal2, col_sal3 = st.columns(3)
col_sal1.metric(label="Average Salary (Atlanta)", value="$45,100")
col_sal2.metric(label="Typical Range (25th-75th percentile)", value="$37.5k - $50k")
col_sal3.metric(label="Top Earners (Approx.)", value=">$59,000")

st.markdown("""
* **Entry-Level Average (Atlanta):** Approx. **\$40,265** (75th percentile around \$44,700).
* **Achieving \$50,000 Target:** This aligns with the 75th percentile for general coordinators. An undergraduate degree and relevant experience strengthen candidacy for higher-end salaries.
""")
st.divider()


# --- Schedule Flexibility ---
st.header("⏰ Schedule Flexibility")

flex_col1, flex_col2 = st.columns(2)

with flex_col1:
    st.subheader("Hybrid Work (🏡 + 🏢)")
    st.markdown("""
    * **Increasingly Common:** Many tasks (tracking, communication, documentation) are remote-friendly.
    * **Job Postings:** Confirm existence of hybrid Logistics Specialist/Coordinator roles.
    * **Broader Trends:** A significant portion (around 55%) of remote-capable employees work hybrid schedules.
    """)

with flex_col2:
    st.subheader("Compressed Work Week (4x10 🗓️)")
    st.markdown("""
    * **Less Common:** Compared to hybrid, finding standard office-based 4x10 schedules is harder.
    * **Possibility:** May exist in specific operational roles (shift work, 24/7 operations) but not typical for standard coordinator positions.
    * **Availability:** Some job boards allow filtering, but many companies may require standard or on-site schedules.
    """)

st.info("✅ **Realistic Expectation:** A hybrid schedule is more commonly available for a Logistics Coordinator role than a guaranteed 4x10 arrangement.")
st.divider()


# --- Work Environment Considerations ---
st.header("🏢 Work Environment Considerations")
st.markdown("""
* **Variety:** Can range from fast-paced distribution centers/warehouses to traditional corporate offices.
* **Pressure:** May fluctuate based on shipment deadlines and unforeseen issues (delays, errors).
* **Research is Key:** Investigate specific company cultures using employee reviews (e.g., Glassdoor, Indeed) and 'Best Places to Work' lists to find supportive environments.
""")
st.divider()


# --- References & Further Reading ---
st.header("🌐 References & Further Reading")
st.markdown("""
*Below are representative links based on the topics discussed. Actual search results would provide more specific and current data.*

* **General Role Descriptions:**
    * [Indeed: Logistics Coordinator Job Description](https://www.indeed.com/hire/job-description/logistics-coordinator)
    * [LinkedIn: Logistics Coordinator Roles](https://www.linkedin.com/jobs/logistics-coordinator-jobs/)
* **Salary Data:**
    * [Salary.com: Logistics Coordinator Salary Atlanta, GA](https://www.salary.com/research/salary/benchmark/logistics-coordinator-salary/atlanta-ga)
    * [Glassdoor: Logistics Coordinator Salaries](https://www.glassdoor.com/Salaries/logistics-coordinator-salary-SRCH_KO0,21.htm)
* **Bureau of Labor Statistics:**
    * [BLS: Logisticians Occupational Outlook Handbook](https://www.bls.gov/ooh/business-and-financial/logisticians.htm)
* **Work Schedules & Trends:**
    * [SHRM: Managing Flexible Work Arrangements](https://www.shrm.org/resourcesandtools/tools-and-samples/hr-qa/pages/managingflexibleworkarrangements.aspx) (General HR perspective)
* **Logistics Software:**
    * [Oracle NetSuite: What is ERP?](https://www.netsuite.com/portal/resource/articles/erp/what-is-erp.shtml)
    * [SAP: What is a Transportation Management System (TMS)?](https://www.sap.com/insights/what-is-a-tms-transportation-management-system.html)
* **Company Research:**
    * [Atlanta Business Chronicle: Best Places to Work](https://www.bizjournals.com/atlanta/feature/best-places-to-work) (Check for annual lists)
    * [Glassdoor: Best Places to Work](https://www.glassdoor.com/Award/Best-Places-to-Work-LST_KQ0,19.htm)
""")

# --- Footer ---
st.caption(f"Information compiled based on provided text and general knowledge. Last updated conceptually: {datetime.date.today()}")