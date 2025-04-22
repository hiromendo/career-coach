import streamlit as st
import pandas as pd


# ─── Title & intro ─────────────────────────────────────────────────────────────
st.title("5. Top Recommendations & Strategic Fit")
st.markdown("""
Based on the analysis of the professional profile, career preferences, local market data, and accessibility considerations,  
the following roles are recommended as strong potential fits:
""")

# ─── Salary comparison ──────────────────────────────────────────────────────────
st.subheader("📊 Salary Comparison Across Roles")
salary_data = {
    "Role": [
        "IT Support Technician (Tier 1/2)",
        "Junior Salesforce Administrator",
        "Data Analyst (Entry/Junior)"
    ],
    "Average Salary ($k)": [50.6, 75, 60]
}
df = pd.DataFrame(salary_data)
col_table, col_chart = st.columns((2, 3))

with col_table:
    st.table(df.set_index("Role"))

with col_chart:
    st.bar_chart(df.set_index("Role"))

# ─── Recommendations ────────────────────────────────────────────────────────────
with st.expander("Recommendation 1: IT Support Technician (Tier 1/2)", expanded=True):
    st.markdown("""
* **Rationale:** This role directly aligns with the A.A.S in Applied Computer Technology and leverages the problem‑solving skills demonstrated in previous roles.  
  The local market shows demand in the Beaverton/Hillsboro area [18], and average salaries ($50.6k in Beaverton [18]) fit squarely within the $50k‑$60k target range.  
  The work involves varied troubleshooting tasks, addressing the desire for non‑repetitive work. Communication can often be managed effectively through ticketing systems, email, and chat, with planned accommodations (interpreters via VR/Bridges) for team meetings or complex user interactions.  
  This path provides a solid foundation for a long‑term IT career.
    """)
    st.metric(label="Target Salary Range", value="$50k–60k")
    st.markdown("[Market data source][18]")

with st.expander("Recommendation 2: Junior Salesforce Administrator"):
    st.markdown("""
* **Rationale:** This path directly capitalizes on the valuable Salesforce Certified Administrator credential and the practical internship experience.  
  The Salesforce ecosystem has high demand and offers significant career growth potential. While typical starting salaries in the Portland/Beaverton area may begin closer to $70k or $80k [22, 23], this meets the "or more" aspect of the salary goal and reflects the value of the certification.  
  The role utilizes technical configuration, process improvement, and problem‑solving skills. Communication often involves structured requests, documentation, and system configuration, lending itself well to accessibility, with accommodations planned for meetings.  
  Success requires targeting companies open to junior talent and potentially leveraging VR/Bridges for placement support and initial salary negotiation guidance.
    """)
    st.metric(label="Typical Entry Salary", value="$70k–80k")
    st.markdown("[Salary benchmarks][22] · [Salary benchmarks][23]")

with st.expander("Recommendation 3: Data Analyst (Entry/Junior Level)"):
    st.markdown("""
* **Rationale:** This role connects the data handling experience from the R&D Technician role, the analytical thinking potentially used in optimizing Amazon processes, and general technical aptitude.  
  The field is growing, with local demand evident [2, 9, 10]. While average salaries are high, entry‑level positions can potentially align with the $50k–$60k target range [12].  
  The work focuses on deriving insights and solving problems, offering engaging and non‑repetitive tasks. Communication heavily relies on data visualization and written reports [5], which can be highly accessible.  
  This path may require the most immediate upskilling or portfolio development to demonstrate specific proficiency in tools like Power BI and SQL.
    """)
    st.metric(label="Entry‑Level Salary Range", value="$50k–60k")
    st.markdown("[Market demand][2] · [Market demand][9] · [Market demand][10]")

# ─── Summary box ───────────────────────────────────────────────────────────────
st.info("""
**Comparing these options:**  
- **IT Support Technician** offers the most direct alignment with existing education and the target salary baseline.  
- **Salesforce Administrator** provides the highest growth and salary potential but may require aiming slightly above the initial salary floor.  
- **Data Analyst** offers strong engagement and accessibility but necessitates demonstrating specific, current tool expertise.
""")

# ─── Footer with link placeholders ───────────────────────────────────────────────
st.markdown("""
[18]: https://example.com/local-it-support-data  
[22]: https://example.com/salesforce-salary-1  
[23]: https://example.com/salesforce-salary-2  
[2]: https://example.com/data-analyst-demand  
[5]: https://example.com/data-viz-accessibility  
[9]: https://example.com/local-data-9  
[10]: https://example.com/local-data-10  
[12]: https://example.com/data-analyst-salary-12
""", unsafe_allow_html=True)
