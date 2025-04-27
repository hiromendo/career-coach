import streamlit as st
import pandas as pd

# --- Main Title ---
st.title("🧐 II. Assessing Your Profile for a Marketing Analytics Manager Role")

st.markdown("""
Understanding how your personal background aligns with market demands is crucial for crafting a compelling narrative and identifying areas for development. This section helps map your experience to role requirements.
""")

st.divider()

# --- Section A: Leveraging Strengths ---
st.header("A. Leveraging Your Strengths: Connecting Experience to Analytics")
st.markdown("""
Your unique blend of quantitative education, digital marketing practice, and accounting rigor forms a strong foundation. Let's break down these assets:
""")

# Using subheaders and descriptive text for each strength area
st.subheader("🎓 Quantitative Foundation (Economics-Mathematics BA)")
st.markdown("""
* **Core Asset:** Demonstrates strong analytical reasoning, quantitative proficiency, and comfort with complex data – essential for analytics.[1]
* **Signals:** Ability to learn and apply sophisticated analytical techniques.
""")

st.subheader("💻 Digital Marketing Practical Skills")
st.markdown("""
* **Hands-On Experience:** Website development (WordPress), Google Analytics for traffic strategy, Excel for content organization.[1]
* **Differentiator:** Provides tangible application of marketing concepts and tools, moving beyond theory.
""")

st.subheader("💼 Accounting/Bookkeeping Analytical Overlap")
st.markdown("""
* **Highly Transferable:**
    * **Data Structuring:** Booking/classifying transactions parallels data organization.
    * **Reporting:** Preparing financial statements mirrors analytics reporting.
    * **Data Validation:** Account reconciliations align with ensuring data accuracy.
    * **Insight Generation:** Reporting to the CEO on budget/cash flow directly relates to translating data into executive insights.[1]
    * **Systems Thinking:** Managing the cash-to-accrual transition shows ability to handle complex data projects.
""")

st.subheader("🚀 Entrepreneurial Experience (Self-Employed Digital Marketer)")
st.markdown("""
* **Demonstrates:** Initiative, business acumen, project management, and multitasking – valuable leadership traits for a manager role.
""")

st.subheader("🛠️ Foundational Tool Proficiency")
st.markdown("""
* **Essential:** Proven advanced Excel expertise.[1]
* **Direct Advantage:** Practical Google Analytics experience.[9]
* **Adaptability:** Comfort with business software (QuickBooks).
""")

st.success(
    """
    **💡 Your Unique Narrative:** Weave these threads together!
    * **Accounting:** Data rigor, reporting discipline, financial literacy, business operations understanding.
    * **Digital Marketing:** Specific channel knowledge, hands-on Google Analytics use.
    * **Econ/Math Degree:** Proven quantitative aptitude.
    This combination allows understanding the *'what'* (marketing data) and the *'so what'* (business/financial impact) – highly valuable for an Analytics Manager.[1] Experience analyzing financial data for the CEO directly parallels the core analytics function.
    """
)

st.divider()

# --- Section B: Identifying & Addressing Potential Gaps ---
st.header("B. Identifying & Addressing Potential Gaps")
st.markdown("""
While your foundation is strong, certain areas common in Marketing Analytics Manager roles may need development:
""")

# Using subheaders and warning icons/boxes for gaps
st.subheader("🔧 Specific Marketing Analytics Tools")
st.warning("""
* **Limited Exposure:** Experience beyond Google Analytics and Excel (e.g., Tableau, Power BI, Looker, SQL, Python/R, Marketo, Salesforce, Amplitude) appears limited but frequently required.[1]
""")

st.subheader("🏢 Formal Corporate Analytics Experience")
st.warning("""
* **Potential Gap:** Self-employment may mean less experience with large corporate team structures, workflows, stakeholder dynamics, and large-scale datasets.
""")

st.subheader("📈 Advanced Analytical Techniques")
st.warning("""
* **Not Explicit:** Resume doesn't show specific experience with advanced methods like Multi-Touch Attribution (MTA), Marketing Mix Modeling (MMM), structured A/B testing (incrementality), or complex marketing-specific statistical modeling.[1]
""")

st.subheader("👨‍👩‍👧‍👦 Direct Management Experience")
st.warning("""
* **'Manager' Title Expectation:** While reporting to the CEO is significant, explicit experience managing direct reports or leading a dedicated team isn't evident.
""")

st.subheader("🏭 Industry-Specific Knowledge")
st.warning("""
* **Context Matters:** Deeper domain knowledge might be needed depending on the target industry (e.g., tech, healthcare, apparel nuances).
""")

st.info(
    """
    **🎯 Strategic Consideration:** The most significant gaps appear to be **broader tool proficiency** (beyond GA/Excel) and **formal corporate analytics environment experience**.
    * **Consider Starting Point:** **Senior Marketing Analyst** roles could be an excellent initial step. They leverage your analytical strengths while offering opportunities to master new tools/techniques and corporate processes, setting you up for a Manager role later.
    * **Bridge Management Gap:** Emphasize project leadership, strategic contributions, and CEO reporting from your background.
    """
)

st.divider()

# --- Section C: Resume Enhancement Strategy ---
st.header("C. Resume Enhancement Strategy for Marketing Analytics Roles")
st.markdown("""
Strategically refine and reframe your resume to highlight your suitability for analytics roles. Focus on translating your experience into the language of marketing analytics.
""")

st.subheader("📝 Objective/Summary Section")
st.markdown("""
* **Action:** Replace generic objectives with a targeted professional summary.
* **Content:** Immediately highlight your unique value: quantitatively adept (Econ/Math BA) + analytical skills from digital marketing (GA, traffic strategy) & financial analysis (reporting, modeling, systems). State your goal (Marketing Analytics Manager/Senior Analyst) and focus (using data for marketing effectiveness/business growth).
""")

st.subheader("✨ Experience Section - Digital Marketer (Self-Employed)")
st.markdown("""
* **Quantify Achievements:** Add metrics! *Example: "Increased client website traffic X% via SEO strategies derived from Google Analytics data."* or *"Improved on-time content delivery Y% by developing an Excel-based management system."*
* **Use Analytics Language:** Rephrase descriptions. *Instead of:* "Utilize analytics," *Use:* "Analyzed website performance metrics using Google Analytics to formulate data-backed traffic growth strategies."
* **Highlight Relevant Processes:** Frame Excel systems as "Designed data management systems using advanced Excel for content planning and performance tracking." Mention any A/B testing.
""")

st.subheader("✨ Experience Section - Full Charge Bookkeeper (AcademyX, Inc)")
st.markdown("""
* **Reframe Analytically:** Focus on analysis and impact. *Examples:* "Managed and analyzed financial datasets using QuickBooks, ensuring data integrity via reconciliations," "Developed and presented financial statements, variance analyses, and cash flow forecasts to the CEO, informing business decisions," "Led strategic cash-to-accrual accounting transition, redesigning data workflows."
* **Showcase Transferable Skills:** Highlight documentation/training creation as evidence of communication and process skills.
* **De-emphasize Routine Tasks:** Minimize basic transaction processing; frame analytically if possible (e.g., "Analyzed AR aging reports to improve collections").
""")

st.subheader("📋 Skills Section")
st.markdown("""
* **Action:** Create a dedicated, prominent, categorized skills section.
* **Categories & Content:**
    * **Marketing Analytics & Data Viz:** Google Analytics, Excel (Advanced: Pivot Tables, Financial Modeling), *[Add Tableau/Power BI/Looker if learned]*
    * **Databases & Querying:** *[Add SQL if learned]*
    * **Business Software:** QuickBooks, WordPress
    * **Languages/Frameworks:** *[Add Python/R if learned]*
    * **Quantitative & Analytical:** Statistical Analysis, Financial Analysis & Modeling, Data Interpretation, BI Reporting, Process Improvement, Budgeting & Forecasting.
""")

st.subheader("🎓 Education Section")
st.markdown("""
* **Action:** Ensure your BA in Economics-Mathematics (UC Santa Barbara) is clearly listed and prominent.
""")

st.markdown("---") # Simple separator before the table
st.markdown("This table maps requirements to your experience and suggests specific resume actions:")

# --- Data Table 2 (Improved Display) ---
# Data for Table 2 (same as provided)
data_table2 = {
    'Key Marketing Analytics Requirement (Skill/Tool/Experience)': [
        'Quantitative & Statistical Analysis',
        'Marketing Channel Knowledge (Digital)',
        'Data Visualization & Reporting',
        'SQL / Database Querying',
        'Advanced Excel',
        'Google Analytics',
        'Tableau / Power BI / Looker',
        'Cross-Functional Communication',
        'Business Acumen',
        '5+ Years Relevant Experience'
    ],
    'Your Relevant Experience/Skill (Mapped from Resume)': [
        'BA Econ-Math; Financial analysis (Bookkeeping); GA analysis (Marketing)',
        'Self-employed Digital Marketer role (GA, Websites)',
        'Financial statement prep (Bookkeeping); Excel systems (Marketing)',
        'None explicitly listed',
        'Excel systems (Marketing); All bookkeeping functions',
        'Utilized in Digital Marketer role',
        'None explicitly listed',
        'Reporting to CEO (Bookkeeping); Client work (Marketing); Training creation (Bookkeeping)',
        'Reporting to CEO on budget/cash flow; Running own business',
        '~10 yrs Self-Employed Marketing + ~2 yrs Bookkeeping'
    ],
    'Resume Enhancement Action (How to rephrase/highlight)': [
        'Prominently feature degree; Use terms like "statistical analysis," "quantitative modeling," "data interpretation" in experience descriptions.',
        'Specify channels worked with (SEO, Content); Quantify results achieved using GA data.',
        'Reframe financial reporting as "developing dashboards/reports for executive review." Highlight Excel system complexity. Add any new visualization tools learned to Skills.',
        'Add to Skills section if learning/learned. Cannot be claimed from current resume.',
        'Explicitly list "Advanced Excel" with specifics (Pivot Tables, Modeling) in Skills. Quantify complexity of systems built.',
        'Detail specific GA analyses performed (traffic sources, user behavior, goal tracking). Quantify impact of insights. List certification if obtained.',
        'Add to Skills section if learning/learned. Consider creating a sample dashboard for a portfolio.',
        'Emphasize communication with leadership ("Presented findings to CEO"). Frame client work as stakeholder management. Highlight training development.',
        'Explicitly state contribution to business decisions based on financial analysis. Highlight P&L responsibility/understanding from self-employment.',
        'Combine timelines strategically in summary. Focus experience bullets on the most relevant analytical tasks from both roles, emphasizing transferable skills from accounting.'
    ]
}
df_table2 = pd.DataFrame(data_table2)

st.subheader("Table 2: Resume Mapping - Experience vs. Requirements")
# Use container width makes the table stretch horizontally, often improving readability
st.dataframe(df_table2, hide_index=True, use_container_width=True)

st.divider()