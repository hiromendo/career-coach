import streamlit as st
import pandas as pd

# --- Main Title ---
st.title("📊 I. Understanding the Marketing Analytics Manager Landscape in Portland, OR")

st.markdown("""
Successfully navigating the job market requires a clear understanding of the target role, the specific demands of the local market, and the qualifications employers seek. This section breaks down these components for the Portland area.
""")

st.divider() # Visual separator

# --- Section A: Defining the Role ---
st.header("A. Defining the Role: Core Responsibilities and Variations")

st.markdown("""
The fundamental purpose of a **Marketing Analytics Manager** is to transform raw marketing data into actionable intelligence that shapes strategy and drives business growth. This involves synthesizing information from various sources (channel performance, customer behavior, market trends) to provide clear insights and recommendations to leadership and stakeholders.[1]
""")

st.subheader("🔑 Core Responsibilities")
st.markdown("""
Common responsibilities associated with this function include:

* 📊 **Performance Analysis:** Evaluating data from diverse marketing channels (PPC, SEO, Social Media, Email, CTV, Audio, etc.) to identify drivers and improvement areas.
* 📈 **Reporting & Visualization:** Developing and refining dashboards and reports (using tools like Looker, Tableau, Power BI) to track metrics and communicate findings.
* 🗣️ **Stakeholder Communication:** Preparing and presenting analytical findings for business reviews, ensuring clarity for all audiences.
* 🎯 **KPI Development:** Collaborating on defining and tracking Key Performance Indicators (KPIs) for campaigns and initiatives.
* 🔍 **Campaign Monitoring & Optimization:** Continuously monitoring campaigns and providing data-driven insights for ongoing improvement.
* 🔮 **Forecasting & Modeling:** Using statistical analysis to predict trends, forecast behavior, and inform planning.
* 🤝 **Cross-Functional Collaboration:** Working with Marketing, Sales, Product, and Finance teams to align analytics with business goals.
* 🧑‍🔬 **Market & Customer Research:** Conducting research to understand the audience, segment the market, and analyze competitors.
* 💡 **Strategy & Messaging Input:** Contributing data-driven insights to Go-To-Market (GTM) strategies and product messaging (sometimes overlapping with Product Marketing).
""")

st.subheader("🎭 Variations and Similar Titles")
st.markdown("""
Job titles can vary significantly even when core responsibilities overlap. Look beyond the exact title!
""")

# Use columns to compare examples or highlight key points
col1, col2 = st.columns(2)
with col1:
    st.info("""
    **Related Titles May Include:**
    * Marketing Data Analyst
    * Digital Marketing Analyst
    * Growth Analytics Manager
    * Senior Product Marketing Manager (w/ analytical focus)
    """)
with col2:
    st.warning("""
    **Key Distinction Example:**
    * **Allbirds (Marketing Analytics Mgr):** Focused on channel performance & reporting.[1]
    * **Morningstar (Sr. Product Marketing Mgr):** Emphasized GTM strategy & messaging, requiring analytics + storytelling.[2]
    """)

st.success(
    "**Takeaway:** Use a flexible search strategy! Focus on responsibilities described, not just the title. Manager roles often blend analysis with strategy and communication.[1]"
)


st.divider() # Visual separator

# --- Section B: Portland's Job Market ---
st.header("B. Portland's Job Market: Key Industries & Major Employers")

st.markdown("""
The Greater Portland region boasts a diverse economy with significant concentrations in several key sectors that frequently require marketing analytics expertise.
""")

st.subheader("🏭 Key Industries")
# Using markdown with emojis for a simple visual list
st.markdown("""
* 👟 **Apparel & Outdoor:** Nike, Columbia, Adidas, Allbirds, Hanna Andersson, Leatherman, Rejuvenation 
* 💻 **Computers & Electronics ("Silicon Forest"):** Intel, Lam Research, Tektronix, HP (Vancouver), Siemens EDA, ON Semi, Qorvo 
* ⚕️ **Healthcare:** Providence, OHSU, Kaiser, Cambia, Moda Health 
* 🏦 **Financial Services:** Umpqua Bank, The Standard, OnPoint CU, (also remote options like Affirm) 
* 📈 **Agencies & Consulting:** Tinuiti, SocialSellinator, Theo Agency, Aquent, Point B 
* 🛒 **Retail & E-commerce (Broader):** Fred Meyer, Williams-Sonoma, Amazon, Tillamook, Home Depot (Vancouver) 
* 🚚 **Other Notable Employers:** Daimler Trucks, PGE, Portland Trail Blazers 
""")

st.success(
    "**Opportunity Hotspots:** The concentration of major HQs in **Apparel/Outdoor** and **Tech/Electronics** suggests these sectors likely offer the most abundant opportunities. ([https://www.greaterportlandinc.com/](https://www.greaterportlandinc.com/research-center/major-employers))"
)

st.subheader("🏠 Remote & Hybrid Work Impact")
st.info("""
**Flexibility Matters:** While some employers prefer onsite (e.g., Rejuvenation [9]), many offer hybrid (e.g., Morningstar [2]) or fully remote options (e.g., Affirm [6]). This expands your search pool to include companies hiring remotely in OR/WA and roles in nearby Vancouver, WA.[7] A local presence is often advantageous, but don't discount remote opportunities.
""")


st.divider() # Visual separator

# --- Section C: Essential Skills, Tools & Qualifications ---
st.header("C. Essential Skills, Tools & Qualifications")

st.markdown("""
Employers seek a blend of analytical prowess, marketing knowledge, communication skills, and technical tool proficiency.
""")

# Using subheaders for different skill categories
st.subheader("🧠 Core Analytical & Business Skills")
st.markdown("""
* **Quantitative Foundation:** Strong ability to interpret complex data, apply statistics/modeling, problem-solve logically.[1]
* **Marketing Acumen:** Understanding channels (PPC, SEO, etc.), KPIs, campaign evaluation, customer behavior, GTM strategy.[1, 2]
""")

st.subheader("🗣️ Communication & Collaboration Skills")
st.markdown("""
* **Translating Data:** Clearly communicating complex findings to non-technical audiences via reports, visualizations, and presentations.[1]
* **Teamwork:** Collaborating effectively with cross-functional teams.[1] Strong storytelling is a plus.[2]
""")

st.subheader("🛠️ Technical Tool Proficiency")
st.markdown("""
* **Web Analytics:** Google Analytics (Standard), Amplitude [1, 9]
* **Data Visualization:** Tableau, Power BI, Looker [1]
* **Spreadsheets:** Advanced Microsoft Excel [1]
* **Databases/Querying:** SQL (Highly common/expected), Data Warehouses (Snowflake) [1, 3]
* **Marketing Automation/CRM:** Marketo, Pardot, HubSpot, Salesforce [2]
* **Statistical Software (Advantageous):** R or Python [4]
* **Attribution/Testing:** MTA/MMM systems, A/B testing [1]
""")

st.subheader("🎓 Experience & Education")
st.markdown("""
* **Experience:** Typically 5+ years relevant experience for Manager roles [1]; 8-10+ for Director [5]. Less for Analyst roles [3].
* **Education:** Bachelor's degree usually required (quantitative fields preferred: Stats, Math, Econ, CS, Business Analytics) [1]. MBA sometimes preferred for senior roles [5].
""")

st.markdown("""
---
The following table summarizes these key skills and tools, assessing alignment with a profile having an Economics-Mathematics degree, Digital Marketing, and Accounting experience.
""")

# --- Data Table 1 (Improved Display) ---
# Data for Table 1 (same as provided)
data_table1 = {
    'Skill/Tool Category': ['Analytical Skills', 'Analytical Skills', 'Marketing Knowledge', 'Marketing Knowledge', 'Communication', 'Communication', 'Technical Tools', 'Technical Tools', 'Technical Tools', 'Technical Tools', 'Technical Tools', 'Technical Tools', 'Technical Tools', 'Experience', 'Education'],
    'Specific Skill/Tool': ['Quantitative Analysis, Statistics, Forecasting', 'Data Interpretation, Problem Solving', 'Marketing Channels (PPC, SEO, Social, Email, etc.)', 'KPIs, Campaign Evaluation, Customer Behavior', 'Reporting, Data Visualization', 'Cross-functional Collaboration, Presentation', 'Web Analytics (Google Analytics, Amplitude)', 'Data Visualization (Tableau, Power BI, Looker)', 'Spreadsheets (Advanced Excel)', 'Databases/Querying (SQL)', 'Statistical Packages (Python, R)', 'CRM/Marketing Automation (Salesforce, Marketo, etc.)', 'Attribution/Testing (MTA/MMM, A/B Testing)', 'Years in Relevant Field (Marketing/Analytics)', "Bachelor's Degree (Quantitative Field Preferred)"],
    'Relevance/Examples from Listings (Snippet IDs)': ['Core requirement across roles [1]', 'Essential for deriving insights [1]', 'Understanding needed to analyze performance [1]', 'Needed for measurement and insight [1]', 'Crucial for sharing findings [1]', 'Required for working with teams/stakeholders [1]', 'GA is standard; Amplitude mentioned [1]', 'Frequently required for dashboards [1]', 'Fundamental tool [1]; User has direct experience', 'Highly probable requirement, common for analysts [3]; Snowflake mentioned [1]', 'Mentioned for some data roles, potential advantage [4]', 'Valuable for lifecycle analysis [2]', 'Mentioned in some roles for advanced analysis [1]', 'Typically 5+ years for Manager [1]', 'Often required/preferred [1]'],
    "User's Current Alignment (From Resume & Background)": ['Strong: BA in Economics-Mathematics provides theoretical foundation. Accounting role involved budgeting/forecasting.', 'Strong: Demonstrated through Econ/Math degree, formulating traffic strategies, financial analysis for CEO.', 'Developing: Practical experience with website traffic/content via self-employment. Lacks broad corporate channel exposure.', 'Developing: Experience with GA for traffic growth implies KPI use. Less formal experience with campaign evaluation frameworks or deep customer behavior modeling.', 'Developing: Experience creating financial statements. Lacks specific experience with tools like Tableau/Looker/Power BI.', 'Developing: Reported directly to CEO (high-level communication). Created training. Lacks experience collaborating within a large corporate marketing structure.', 'Good: Direct experience with Google Analytics. No mention of Amplitude.', 'Gap: No demonstrated experience.', 'Strong: Explicitly used Excel for systems/bookkeeping. Advanced skills likely from accounting/math background.', 'Gap: No demonstrated experience.', 'Potential: Econ/Math background suggests aptitude but no specific experience listed.', 'Gap: No demonstrated experience.', 'Gap: No demonstrated experience.', 'Partial: ~10 years self-employed digital marketing (part-time focus unclear) + ~2 years bookkeeping. Needs framing to highlight relevance.', 'Strong: BA in Economics-Mathematics is an excellent fit.']
}
df_table1 = pd.DataFrame(data_table1)

st.subheader("Table 1: Key Skills & Tools Assessment")
st.dataframe(df_table1, hide_index=True, use_container_width=True) # Make table wider

st.divider() # Visual separator

# --- Section D: Compensation Expectations ---
st.header("D. Compensation Expectations Overview")

st.markdown("""
Salary expectations vary significantly based on title, company, experience, and role scope. Here's an overview based on available data points:
""")

# Use columns and metrics for key salary figures
col_sal1, col_sal2 = st.columns(2)
with col_sal1:
    st.metric(label="Est. Manager Base Salary (PDX)", value="$100k - $150k+")
    st.caption("e.g., Allbirds: $120k-$130k [1]; Morningstar (Sr. PMM): $90k-$153k + bonus [2]")
with col_sal2:
    st.metric(label="Est. Analyst Base Salary (PDX)", value="$60k - $100k+")
    st.caption("e.g., Jr. Analyst: $55k-$65k [3]; Sr. Analyst: $86k-$141k (Cambia) [7]")

st.info("""
**Summary:** Marketing Manager roles likely target **~$100,000 - $150,000+** base salary in Portland, while Analyst roles range from **~$60,000 - $100,000+**. Large tech/apparel firms may offer higher ranges. Always research specific roles.
""")

st.subheader("💰 Beyond Salary: Benefits")
st.markdown("""
Comprehensive benefits packages are standard and typically include:
* Health Insurance (Medical, Dental, Vision)
* Retirement Savings (401k + Match)
* Paid Time Off (PTO) & Sick Leave
* Paid Parental Leave
* Potential Extras: Equity, Bonuses, Discounts, Wellness Programs, Professional Development Support [1]
""")

st.divider()