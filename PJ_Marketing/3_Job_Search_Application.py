import streamlit as st
import pandas as pd

# --- Main Title ---
st.title("🗺️ III. Strategic Job Search & Application Plan for Portland")

st.markdown("""
A targeted and proactive approach is necessary to identify and secure the right Marketing Analytics Manager opportunity in the competitive Portland market.
""")

st.divider()

# --- Section A: Targeting Your Search ---
st.header("A. Targeting Your Search: Identifying Relevant Companies and Roles")
st.markdown("Effectively focusing your job search increases efficiency and improves the chances of finding a suitable match.")

# Using subheaders for different targeting strategies
st.subheader("🏭 Leverage Industry Clusters")
st.markdown("""
* Concentrate search efforts on Portland's prominent sectors: **Apparel & Outdoor, Computers & Electronics (Silicon Forest), Healthcare, Financial Services, Marketing Agencies**.
* Use resources like the Greater Portland Inc Major Employers list.[16]
""")

st.subheader("🏢 Consider Company Size and Type")
st.markdown("""
* **Large Corps (Nike, Intel):** Structured roles, defined paths, potentially rigid processes.[16]
* **Mid-size/Growth:** Broader scope, faster pace, potential for high impact.
* **Agencies:** Diverse clients and industries.[26]
* **Startups:** High impact, less structure, potentially higher risk.[19]
""")

st.subheader("🏷️ Broaden Role Title Search")
st.markdown("""
* Don't limit to "Marketing Analytics Manager." Include: **Marketing Data Analyst, Digital Marketing Analyst, Senior Marketing Analyst, BI Analyst Marketing, Growth Analyst, Customer Insights Analyst, Product Marketing Analyst**.[1]
""")

st.subheader("📍 Apply Appropriate Location Filters")
st.markdown("""
* Search: **Portland, Beaverton, Hillsboro, Lake Oswego, Vancouver (WA)**.
* **Crucially, include "Remote"** and check job descriptions for OR/WA residency eligibility.[1]
""")

st.subheader("🔍 Conduct Company Research")
st.markdown("""
* Before applying, investigate target companies: business model, marketing, values (sustainability [31], remote work [6], DEI [31]), culture.
* Use company websites, news, Glassdoor reviews for context.[1]
""")

st.markdown("---") # Separator before table
st.markdown("The following table provides an illustrative list of potential target companies:")

# --- Data Table 3 (Improved Display) ---
# Data for Table 3 (same as provided)
data_table3 = {
    'Company Name': ['Nike, Inc.', 'Intel Corporation', 'Columbia Sportswear', 'Lam Research', 'Adidas America', 'Providence Health & Services', 'Oregon Health & Science University (OHSU)', 'Daimler Trucks North America', 'Tektronix', 'Rejuvenation (Williams-Sonoma)', 'Allbirds', 'Tillamook County Creamery Assoc.', 'Cambia Health Solutions', 'Umpqua Bank', 'The Standard', 'Agencies (e.g., Tinuiti, Wieden+Kennedy, local shops)', 'Remote Roles (e.g., Affirm)'],
    'Industry': ['Apparel & Outdoor', 'Computers & Electronics', 'Apparel & Outdoor', 'Computers & Electronics', 'Apparel & Outdoor', 'Healthcare & Sciences', 'Healthcare & Sciences', 'Manufacturing - Transportation', 'Computers & Electronics', 'Retail / Home Goods', 'Apparel & Outdoor / E-Commerce', 'Food & Beverage', 'Financial Services (Insurance) / Healthcare', 'Financial Services', 'Financial Services (Insurance)', 'Agency / Marketing Services', 'Various (e.g., Fintech)'],
    'HQ/Major Office Location': ['Beaverton (HQ)', 'Hillsboro', 'Beaverton (HQ)', 'Tualatin', 'Portland (North America HQ)', 'Portland (Regional HQ)', 'Portland (HQ)', 'Portland (HQ)', 'Beaverton (HQ)', 'Portland (HQ)', 'Portland / SF', 'Tillamook/Portland', 'Portland (HQ)', 'Portland (HQ)', 'Portland (HQ)', 'Portland', 'Remote'],
    'Potential Role Titles': ['Marketing Analyst, Digital Analyst, Consumer Insights', 'Marketing Analyst, Business Analyst, Data Scientist', 'Marketing Analyst, Ecomm Analyst, Data Analyst', 'Product Marketing Analyst, Business Ops Analyst', 'Digital Analytics, Brand Analyst, Consumer Insights', 'Marketing Analyst, BI Analyst, Data Analyst', 'BI Analyst, Research Data Analyst', 'Marketing Analyst, Business Analyst', 'Marketing Analyst, Business Analyst', 'Digital Marketing Manager/Analyst', 'Marketing Analytics Manager', 'Consumer Market Insights Mgr, Marketing Analytics', 'Data Reporting Analyst, BI Analyst', 'Marketing Analyst, Data Analyst', 'BI Analyst, Data Analyst', 'Marketing Analyst, Digital Strategist, Media Analyst', 'Analytics Manager, Growth Analyst'],
    'Notes': ['Global leader, large marketing/analytics function [16]', 'Major tech employer, "Silicon Forest" anchor [16]', 'Strong outdoor brand family [16]', 'Semiconductor equipment, B2B focus [11]', 'Major competitor to Nike [16]', 'Large healthcare system [16]', 'Major academic medical center [7]', 'B2B focus, large manufacturer [16]', 'Test & measurement equipment, tech pioneer [16]', 'Requires hybrid presence [9]', 'Previously hired for this role in Portland [1]', 'Strong regional brand [8]', 'Health solutions focus [7]', 'Regional bank [16]', 'Insurance and financial products [7]', 'Serve diverse clients [19]', 'Check eligibility for OR residents [6]']
}
df_table3 = pd.DataFrame(data_table3)

st.subheader("Table 3: Illustrative Target Company List - Portland Area")
# Use container width for better table layout
st.dataframe(df_table3, hide_index=True, use_container_width=True)

st.divider()

# --- Section B: Job Boards & Networking ---
st.header("B. Effective Use of Job Boards & Networking in Portland")
st.markdown("A dual strategy using online boards and active networking is most effective.")

# Use columns to separate Job Boards and Networking
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌐 Online Job Boards")
    st.markdown("""
    * **Primary:** LinkedIn, Indeed [7], ZipRecruiter [3], Glassdoor [35].
    * **Industry-Specific:** Built In Portland (Tech/Startup) [24].
    * **Niche:** IIMRA (Market Research/Analytics) [35].
    * **Direct:** **Always check target company career pages directly!** [2]
    """)

with col2:
    st.subheader("🤝 Networking Strategy")
    st.markdown("""
    * **LinkedIn:** Connect with recruiters & professionals in target roles/companies. Engage with content.
    * **Local Events/Orgs:** AMA Portland, SEMpdx, TAO events. Check Built In Portland, Meetup.com.
    * **Informational Interviews:** Request brief (15-20 min) chats with people in the field. Use alumni networks (UCSB).
    * **Recruiters:** Engage with staffing agencies (Aquent [28], Robert Half, etc.).
    """)

st.success(
    """
    **💡 Key Insight:** Networking is crucial for accessing the "hidden job market," especially in Portland's strong industry clusters (Apparel, Tech). Informational interviews offer invaluable insider perspectives.
    """
)

st.divider()

# --- Section C: Crafting Compelling Application Materials ---
st.header("C. Crafting Compelling Application Materials (Beyond the Resume)")
st.markdown("Tailored materials are essential to stand out, especially when transitioning fields.")

st.subheader("📝 Cover Letter")
st.markdown("""
* **Customize Each One:** Generic letters fail. Target the specific role/company.
* **Connect the Dots:** Reference job description requirements and link them directly to your skills/experience.
* **Articulate Your Unique Background:** Explain how Econ/Math rigor + accounting discipline + digital marketing practice = strong analytics candidate.
* **Address Gaps Proactively (Briefly):** *Example: "While focused on financial analysis, I applied similar data principles using Google Analytics and am actively learning SQL/Tableau."*
* **Show Genuine Interest:** Mention specific company work, values, or initiatives.
""")

st.subheader("🔗 LinkedIn Profile")
st.markdown("""
* **Optimize & Align:** Ensure consistency with your enhanced resume.
* **Keywords:** Use "Marketing Analytics," "Data Analysis," "Google Analytics," etc., in headline/summary.
* **Elaborate:** Detail key projects/accomplishments in experience sections.
* **Recommendations:** Request recommendations highlighting analytical skills, problem-solving, and work ethic.
""")

st.subheader("💼 Portfolio (Optional but Highly Recommended)")
st.markdown("""
* **Provides Tangible Proof:** Especially valuable for showing self-employment work or new skills. Host on a personal site (WordPress) or platforms like Tableau Public/GitHub.
* **Potential Content Ideas:**
    * **GA Case Study:** Anonymized analysis of website traffic (insights & actions).
    * **Excel System:** Description/visual of content system (data organization benefits).
    * **Sample Dashboard:** Visualize public marketing data using Tableau Public/Data Studio.
    * **Accounting Project:** Frame cash-to-accrual transition as a data systems/analysis project.
""")

st.info(
    """
    **✨ Purpose:** A tailored **Cover Letter** crafts your narrative and addresses communication skills.[1] A **Portfolio** provides concrete proof of analytical capabilities, addressing potential gaps (II.B) and demonstrating initiative.
    """
)


st.divider()

# --- Section D: Interview Preparation ---
st.header("D. Interview Preparation: Demonstrating Analytical & Strategic Value")
st.markdown("Interviews assess technical skills, analytical thinking, communication, and business acumen. Prepare thoroughly.")

# Using subheaders for different interview components
st.subheader("⭐ Behavioral Questions (STAR Method)")
st.markdown("""
* **Prepare Specific Examples:** Use **S**ituation, **T**ask, **A**ction, **R**esult.
* **Focus Scenarios:** Where data was used to solve problems, influence decisions, improve outcomes, identify opportunities.
* **Draw from Both Backgrounds:** *Example 1:* Analyzing GA data to pivot marketing strategy (STAR). *Example 2:* Analyzing financial data for CEO budget recommendations (STAR).
""")

st.subheader("💻 Technical Questions")
st.markdown("""
* **Discuss Concepts/Tools:**
    * Google Analytics metrics & interpretation.
    * Statistical concepts (significance, A/B testing, correlation vs. causation).
    * Analytical approaches for channels (SEO success measurement, PPC analysis).[1]
    * *Potential:* Logic problems, simple Excel/SQL tasks.
""")

st.subheader("📊 Case Studies")
st.markdown("""
* **Anticipate Scenarios:** (e.g., declining retention, new product launch).
* **Practice Structuring Responses:**
    1. Clarify objective.
    2. Identify KPIs.
    3. Determine data needed.
    4. Outline analysis steps (segmentation, trends, etc.).
    5. Suggest data-driven recommendations/next steps.
""")

st.subheader("📈 Connecting to Business Impact")
st.markdown("""
* **Emphasize Outcomes:** Link analysis to tangible business goals (revenue, LTV, cost reduction, ROI).
* **Leverage CEO Reporting Experience:** Show understanding of how data informs high-level strategy.
""")

st.subheader("❓ Questions for the Employer")
st.markdown("""
* **Prepare Thoughtful Questions:** Go beyond basics. Ask about:
    * Data infrastructure & toolset.
    * Team structure (marketing/analytics).
    * Current analytical challenges.
    * How success is measured (role/team).
    * Professional development opportunities.
* **Demonstrates:** Engagement, critical thinking, genuine interest.
""")

st.success(
    """
    **🎯 Interview Goal:** Showcase not just technical skills, but *how* you think analytically and strategically connect data to the bigger picture.[1] Articulate the value of your unique accounting + marketing background.
    """
)

st.divider()