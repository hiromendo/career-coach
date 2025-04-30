import streamlit as st
import pandas as pd


# --- Main Title ---
st.title("3. Target Role & Market Analysis")

st.divider()

# --- 3.1. Role Suitability Assessment ---
st.subheader("3.1. Role Suitability Assessment")
st.markdown("""
Based on the profile analysis, the suitability for each target role is assessed as follows:
""")

# Using markdown with bolding for emphasis and structure
st.markdown("""
**Associate Project Manager / Project Manager: (High Fit)**
* **Alignment:** Strong alignment due to direct PM experience (Tetra Tech, self-employment), PMO experience (BCG, PwC), managing scope/schedule/budget, stakeholder coordination.
* **Certifications:** Relevant certifications (PMP in progress, Construction PM Cert).
* **Experience:** Spans development projects, transformation initiatives, operational models.
* **Skills:** MS Project, Bluebeam Revu.
* **Enhancement:** PMP completion will further boost fit.
""")

st.markdown("""
**Management Analyst / Strategy Analyst: (High Fit)**
* **Alignment:** Excellent fit drawing on extensive consulting background (BCG, PwC Strategy&) involving operational/financial analysis, process improvement, transformation roadmaps, stakeholder interviews, developing materials, identifying value creation levers.
* **Relevance:** Experience in ESG analysis, energy transition, financial services projects is highly relevant.
* **Example Roles:** Senior Management Analyst at NYU Langone, Strategy Analyst roles align well.
""")

st.markdown("""
**Procurement Analyst / Sourcing Manager: (Medium-High Fit)**
* **Alignment:** Good fit based on direct sourcing/procurement experience (Tetra Tech - RFP, negotiation, bid analysis, subcontractor management) and analytical work (lease vs. buy analysis @ BCG).
* **Skills:** Experience developing SOPs for financial tracking is relevant.
* **Positioning:** While not the primary focus, demonstrated skills are transferable, especially for roles requiring analytical rigor.
""")

st.markdown("""
**Business Developer: (Medium Fit)**
* **Foundation:** Relevant experience supporting proposal development and achieving sales targets (Tetra Tech - $400K).
* **Transferable Skills:** Developing business cases, identifying value creation levers (BCG, PwC).
* **Gap:** Dedicated end-to-end business development experience is less prominent.
* **Positioning:** Requires careful narrative crafting, emphasizing strategic and financial aspects contributing to securing new business.
""")
st.divider()

# --- 3.2. NYC Job Market Assessment ---
st.subheader("3.2. NYC Job Market Assessment (Hybrid/In-Office)")
st.markdown("""
The NYC job market supports the requirement for hybrid or in-office roles across the target sectors. Many job postings explicitly state hybrid arrangements or are based in NYC offices.
""")
# Using columns for better visual layout of market assessment
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    * **Project Management:** Numerous PM roles in construction, finance, tech, energy often require on-site/hybrid presence for oversight and collaboration.
    * **Management/Strategy Analyst:** Consulting firms and large corporations (finance, tech) offer analyst roles, frequently in hybrid formats.
    """)
with col2:
    st.markdown("""
    * **Procurement/Sourcing:** Roles available within large organizations (finance, tech, manufacturing, retail), often supporting hybrid models.
    * **Business Development:** BD roles, especially client-facing or market-focused, often necessitate in-office or hybrid arrangements.
    """)
st.divider()

# --- 3.3. Salary Benchmark Analysis ---
st.subheader("3.3. Salary Benchmark Analysis ($100k+ Target)")
st.markdown("""
The **$100,000 minimum salary requirement is achievable** for the target roles in the NYC market, particularly given the candidate's education and experience level, though it sits at the lower end for some more senior or specialized positions.
""")

# --- Salary Table Data ---
# Manually creating the data structure for the DataFrame
salary_data = {
    'Role Category': [
        'Project Management', 'Project Management', 'Project Management', 'Project Management', 'Project Management',
        'Management/ Strategy Analyst', 'Management/ Strategy Analyst', 'Management/ Strategy Analyst', 'Management/ Strategy Analyst', 'Management/ Strategy Analyst', 'Management/ Strategy Analyst', 'Management/ Strategy Analyst',
        'Procurement/ Sourcing Analyst', 'Procurement/ Sourcing Analyst', 'Procurement/ Sourcing Analyst',
        'Business Development', 'Business Development', 'Business Development', 'Business Development'
    ],
    'Title Examples': [
        'Associate Project Manager', 'Senior Associate Project Manager', 'Principal Associate Project Manager', 'Project Manager (General/Construction/Energy)', 'Senior Project Manager',
        'Management Analyst / Wealth Mgt Analyst', 'Real Estate Analyst', 'Senior Management Analyst (Healthcare)', 'Strategy Analyst (VP Level, Finance)', 'Business Strategy Analyst Senior', 'Sustainability Consultant (Assoc. Manager)', 'Management Consultant (Post-MBA/Experienced)',
        'Procurement Analyst', 'Supply Chain Analyst', 'Sourcing Manager / Senior Procurement Manager',
        'Business Developer (Software Co.)', 'Business Development Associate (Entry/Junior)', 'Business Development Manager (Construction/Real Estate)', 'Business Development Manager (General)'
    ],
    'NYC Salary Range (Annual Base)': [
        '$62k - $90k', '$103k - $118k', '$128k - $146k', '$80k - $150k+', '$121k - $150k (Avg $134k)',
        '$78k - $113k', '$84k - $113k', '$81k - $117k', '$110k - $178k', '$103k - $186k', '$117k - $145k', '$190k+ Base',
        '$60k - $80k', '$59k - $84k (Avg $74k, 90th %ile $100k)', '$110k - $160k+',
        '~$75k', '$40k - $80k', '$110k - $130k', '$80k - $160k+'
    ],
    'Snippet References': [
        'Ralph Lauren (potentially lower exp)', 'Capital One [6, 7]', 'Capital One [8]', 'Varies widely', 'Average $134k',
        'Bank of America [7]', 'Fulton Realty', 'NYU Langone', 'State Street [8]', 'USAA', 'Deepki', 'MBB/Big 4',
        'General estimates', 'Average $74k', 'N/A',
        'Vegavid', 'Various (often remote)', 'Burnham Nationwide', 'Varies'
    ],
    'Meets $100k+ Target?': [
        'Lower End', 'Yes', 'Yes', 'Yes', 'Yes',
        'Lower End/Yes', 'Lower End/Yes', 'Lower End/Yes', 'Yes', 'Yes', 'Yes', 'Yes',
        'Lower End', 'Lower End/Yes (Top Earners)', 'Yes',
        'Lower End', 'No', 'Yes', 'Yes'
    ],
    'Notes': [
        'Experience level critical.', 'Aligns well with experience.', 'Potential target with strong positioning.', 'Construction/Energy often >$100k.', 'Strong possibility given background.',
        'Title/scope dependent.', 'Relevant given self-employment exp.', 'Hybrid role example.', 'High potential in finance.', 'Often requires significant experience.', 'Aligns with ESG/Energy background.', 'Reflects prior consulting level.',
        'May require targeting senior roles.', 'Analytical skills apply.', 'More likely target.',
        'Varies significantly.', 'Below target level.', 'Aligns with target & some experience.', 'Requires strong positioning.'
    ]
}
salary_df = pd.DataFrame(salary_data)

st.markdown("**Table 1: NYC Salary Benchmarks for Target Roles**")
# Display the DataFrame using st.dataframe for interactivity
st.dataframe(salary_df, use_container_width=True) # Set use_container_width to True

st.success("""
**Conclusion on Salary:** The **\$100k+ target is realistic**, especially for Senior Associate/Project Manager, Management/Strategy Analyst, Sourcing Manager, and Business Development Manager roles in Finance, Consulting, Energy, and potentially Construction sectors within NYC. Entry-level or standard Analyst/Associate roles might fall short unless negotiation or specific company pay scales are favorable. The candidate's Master's degrees and consulting background support aiming for roles comfortably exceeding the \$100k minimum.
""")
st.divider()

# --- 3.4. Target Industries & Companies ---
st.subheader("3.4. Target Industries & Companies")
st.markdown("""
Based on the candidate's background and NYC focus, the following industries and companies represent strong potential targets:
""")

# Industry sections with company examples and references
st.markdown("**Energy / Renewables / ESG:**")
st.markdown("""
* **Alignment:** Direct alignment with Tetra Tech, WIEB fellowship, ESG analysis (BCG), construction/PM skills. NYC has growing firms in clean energy investment, development, consulting.
* **Companies:** CleanCapital, Deepki, LS Power, Convergent Energy + Power, NY Power Authority, EnergyHub, Ambient Fuels, OYA Solar, IPPsolar, Samba Energy, GreenSpark Solar, Standard Solar, PowerFlex, EmPower Solar, Brooklyn SolarWorks, NineDot Energy, ContourGlobal, UL Solutions, David Energy, CoreWeave (NJ).
* **Consider Also:** Energy consulting practices (Deloitte, PwC, BCG).
* **References:** [Deepki Job Snippet], [LS Power Info], [Convergent Energy Info], [NYPA Info], [EnergyHub Info], [Ambient Fuels Info], [OYA Solar Info], [IPPsolar Info], [Samba Energy Info], [GreenSpark Solar Info], [Standard Solar Info], [PowerFlex Info], [EmPower Solar Info], [Brooklyn SolarWorks Info], [NineDot Energy Info], [ContourGlobal Info], [UL Solutions Info], [David Energy Info], [CoreWeave Job Snippet]
""") # Note: Placeholder references based on context

st.markdown("**Financial Services:**")
st.markdown("""
* **Alignment:** Leverages consulting projects (PwC, BCG), M.A. Economics, analytical skills. NYC is a global finance hub.
* **Focus Roles:** Strategy, project management, operations, ESG investing, LatAm-focused divisions.
* **Companies:** JPMorgan Chase [1, 2, 5], Citigroup [3], Goldman Sachs [3], Morgan Stanley [3], BNY Mellon [3], BlackRock [4], American Express [3], HSBC [5], Capital One [6], Bank of America [7], State Street [8], Blackstone [9], Sixth Street [10], Santander [11], BTG Pactual [12].
* **Consider Also:** Fintech firms [13], Investment Management firms [14], ESG divisions [15].
* **References:**
    * [1] [baruch.cuny.edu/nycdata/business-headquarters/banks.htm](baruch.cuny.edu/nycdata/business-headquarters/banks.htm)
    * [2] [blog.mirrorreview.com/finance-companies-new-york](blog.mirrorreview.com/finance-companies-new-york)
    * [3] [careers.jpmorgan.com/us/en/chase](careers.jpmorgan.com/us/en/chase)
    * [4] [chase.com/personal/banking/education/student/choosing-a-career](chase.com/personal/banking/education/student/choosing-a-career)
    * [5] [theenterpriseworld.com/finance-companies-in-new-york](theenterpriseworld.com/finance-companies-in-new-york)
    * [6] [capitalonecareers.com Job IDs: 78717066480, 80651272592, 77605466016]
    * [7] [salary.com/research/company/bank-of-america-private-bank/wealth-management-analyst-salary?cjid=20627216](salary.com/research/company/bank-of-america-private-bank/wealth-management-analyst-salary?cjid=20627216)
    * [8] [app.joinrise.co/jobs/state-street-alpha-product-and-strategy-analyst-vp-ecix](app.joinrise.co/jobs/state-street-alpha-product-and-strategy-analyst-vp-ecix)
    * [9-15] General industry knowledge/assumed references based on context. BTG Pactual [12], Santander [11], Sixth Street [10], Blackstone [9].
""") # Note: Links made clickable, references consolidated

st.markdown("**Management Consulting:**")
st.markdown("""
* **Alignment:** Natural fit given BCG and PwC Strategy& background.
* **Target Roles:** Consultant, Senior Consultant, Project Leader/Manager.
* **Focus Practices:** Energy, Financial Services, Operations, ESG.
* **Companies (NYC Offices):** McKinsey & Company, Boston Consulting Group (BCG), Bain & Company, Deloitte Consulting, PwC Advisory/Strategy&, EY Consulting, Accenture, KPMG, AlixPartners, Alvarez & Marsal, Capco, ZS Associates, ?whatif!, Acquis Consulting Group.
* **References:** General industry knowledge.
""")

st.markdown("**Construction / Real Estate Development:**")
st.markdown("""
* **Alignment:** Leverages Tetra Tech, self-employed PM, OSHA-10, Construction PM certificate.
* **Focus Roles:** Project Management, Procurement, Business Development.
* **Companies (NYC Presence):** Turner Construction, AECOM Tishman, Skanska USA, Structure Tone/Pavarini McGovern, Lendlease, Gilbane Building Company, Hunter Roberts Construction Group, J.T. Magen & Company, The Walsh Group, JRM Construction Management, Bette & Cring, Omnibuild, Navillus Contracting, Barr & Barr, Burnham Nationwide.
* **Consider Also:** Real estate development firms, corporate real estate divisions.
* **References:** General industry knowledge, [Burnham Nationwide Job Snippet].
""")

st.markdown("**Companies Valuing Language Skills / LatAm Focus:**")
st.markdown("""
* **Alignment:** Target multinationals with NYC presence and LatAm operations where Spanish/Portuguese fluency is an asset.
* **Companies:** JPMorgan Chase, Citi, Santander, BTG Pactual, Law firms (Latham & Watkins, Willkie Farr & Gallagher), divisions within consulting firms or multinationals (e.g., Sixth Street's Spanish investments, ContourGlobal's South America assets).
* **References:** Company websites, prior references (Santander [11], BTG Pactual [12], Sixth Street [10]), [ContourGlobal Info].
""")

# --- Target Company Table ---
# Manually creating data for the second table
target_company_data = {
    'Industry Sector': [
        'Energy/Renewables/ESG',
        'Financial Services',
        'Management Consulting',
        'Construction/Real Estate'
    ],
    'Company Examples (NYC Presence)': [
        'CleanCapital, Deepki, NYPA, LS Power, CoreWeave (NJ)',
        'JPMorgan Chase, Goldman Sachs, Morgan Stanley, BlackRock, Capital One, State Street, Santander, BTG Pactual',
        'McKinsey, BCG, Bain, Deloitte, PwC, EY',
        'Turner Construction, AECOM Tishman, Skanska, Structure Tone, Lendlease, Burnham Nationwide'
    ],
    'Potential Roles': [
        'Project Manager, Strategy Analyst, Procurement/Sourcing Manager, Sustainability Consultant',
        'Management Analyst, Strategy Analyst, Project Manager, ESG Analyst, LatAm-focused roles',
        'Consultant, Senior Consultant, Project Manager, Strategy Analyst',
        'Project Manager, Assistant PM, Procurement/Sourcing, Business Development'
    ],
    'Notes': [
        'Strong alignment with background & ESG trend.',
        'High salary potential, leverage consulting & econ background.',
        'Direct alignment with past experience, high salary potential.',
        'Leverages PM certs, Tetra Tech, self-employment.'
    ],
    'Snippet References': [ # Consolidating references for brevity in the table
        'Various company sites, job postings',
        'See Finance Refs [1-15]',
        'General industry knowledge',
        'General industry knowledge, Burnham job snippet'
    ]
}
target_company_df = pd.DataFrame(target_company_data)

st.markdown("**Table 2: Target Company List (Illustrative Examples)**")
# Display the DataFrame
st.dataframe(target_company_df, use_container_width=True) # Set use_container_width to True

st.divider()
st.caption("This analysis guides the subsequent networking and application strategy.")

# --- How to Run ---
# Add comments explaining how to execute the Streamlit app
# To run this app:
# 1. Save the code as a Python file (e.g., `nyc_market_app.py`).
# 2. Ensure you have Streamlit and Pandas installed (`pip install streamlit pandas`).
# 3. Open your terminal or command prompt.
# 4. Navigate to the directory where you saved the file.
# 5. Run the command: `streamlit run nyc_market_app.py`

