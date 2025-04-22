# Import necessary libraries
import streamlit as st
import pandas as pd

# # --- Page Configuration ---
# st.set_page_config(
#     layout="wide",
#     page_title="Career Pathways: Accounting & Digital Marketing",
#     page_icon="🚀"
# )

# --- Report Data (Simulated from Text) ---

# Table 1 Data: Portland, OR Area Hybrid/In-Person Roles
portland_data = {
    'Job Title Category': [
        'Marketing Analytics',
        'Marketing Operations',
        'Financial/Business Analyst',
        'Revenue Operations',
        'Business Development',
        'Product Marketing',
        'Digital Strategy/Marketing'
    ],
    'Sample Specific Titles Found': [
        'Marketing Analytics Mgr, Lead Insights & Analytics Mgr, Sr Financial Analyst (Marketing Focus)',
        'Marketing Operations Mgr, Marketing Project Mgr',
        'Financial Analyst (FP&A, etc.), Business Analyst (Finance/Tech), Financial Reporting Mgr',
        'Revenue Operations Manager',
        'Business Development Manager, Sales Development Rep',
        'Product Marketing Manager, Sr. Marketing Product Mgr',
        'Digital Strategist (Agency roles), Marketing Manager (Strategy focus)'
    ],
    'Estimated Portland Area Salary Range (Annualized)': [
        '$90K - $155K+',
        '$45K - $117K+',
        '$70K - $118K+ (Salaried); $33 - $65/hr (Contract)',
        'Varies (Likely $100K+)',
        '$60K - $160K+',
        '$105K - $136K+',
        'Varies (Agency dependent)'
    ],
    'Key Skill Alignment (Accounting/Marketing Blend)': [
        'Strong Analytical (Acct), Data Viz, Marketing KPIs (Mktg), Communication',
        'Process Orientation (Acct), Project Mgmt (Mktg), MarTech (Mktg), Efficiency Focus (Acct/Mktg)',
        'Analytical/Quant (Acct), Problem Solving (Acct), Requirements Gathering (BA), Stakeholder Mgmt (BA), Excel/BI Tools',
        'Process Optimization (Acct/Mktg), CRM/Salesforce/CPQ (Mktg/Tech), Data Analysis (Acct), Cross-functional Collab',
        'Client Acquisition (Mktg - SE), Negotiation (Mktg), Financial Acumen for Deals (Acct), Relationship Building',
        'Market Strategy (Mktg), Messaging (Mktg), Competitive Analysis (Mktg/Acct), Pricing/ROI (Acct)',
        'Digital Channel Expertise (Mktg), Strategic Planning (Mktg), Analytics (Acct/Mktg), Client Mgmt (Mktg - SE)'
    ]
}
df_portland = pd.DataFrame(portland_data)

# --- Streamlit App Layout ---

st.title("🚀 Strategic Career Pathways Summary")
st.subheader("For Professionals with Combined Accounting & Digital Marketing Experience in an AI-Driven Market")
st.markdown("---")

st.info(
    """
    **Executive Summary Highlights:**
    * AI automates routine tasks but **increases the value** of strategic, analytical, creative, and human-centric skills.
    * The blend of **financial acumen (Accounting)** and **strategic, customer-focus (Digital Marketing)** offers a distinct advantage.
    * Recommended roles leverage this synergy, focusing on data interpretation, strategic planning, client management, and ethical judgment where **human insight remains critical**.
    """
)

# --- Main Content Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Profile Advantage",
    "💡 AI Impact",
    "🧭 Career Paths",
    "📈 Market Opportunities",
    "🎯 Recommendations"
])

# --- Tab 1: Profile Advantage ---
with tab1:
    st.header("Section 1: The Accountant-Marketer Advantage")
    st.markdown(
        """
        This unique background combines foundational analytical rigor with strategic growth capabilities.

        **Key Skill Pillars:**
        * **Accounting Foundation:** Financial literacy, analytical/quantitative skills, attention to detail, problem-solving, ethical grounding.
        * **Digital Marketing Engine:** Strategic planning, content/communication, SEO/SEM, marketing analytics, client acquisition/management (from self-employment), adaptability, MarTech proficiency.
        * **Synergistic Value:** Ability to bridge finance and marketing, develop financially sound *and* market-aware strategies, and communicate effectively across domains.
        """
    )

    with st.expander("See More Details on Skill Synergy"):
        st.write("""
        The fusion of rigorous financial understanding with strategic, creative, and growth-oriented marketing expertise creates a powerful professional synergy. This profile can:
        - **Holistic Decision-Making:** Ground marketing concepts in profitability and feasibility while ensuring financial plans consider market dynamics (CAC, CLV).
        - **Bridge Functional Gaps:** Translate financial data into marketing implications and marketing results into financial terms, vital for cross-functional roles.
        - **Quantify Value:** Not only conceive and execute growth strategies but also meticulously measure their financial impact and articulate ROI effectively.
        """)

# --- Tab 2: AI Impact ---
with tab2:
    st.header("Section 2: The Impact of Artificial Intelligence")
    st.markdown(
        """
        AI is transforming both accounting and marketing, automating tasks while creating demand for new skills.

        **Key Impacts & Trends:**
        * **Automation & Efficiency:** AI automates routine data entry, processing, reporting (Accounting) and content drafting, ad targeting, campaign tasks (Marketing), freeing up human capacity.
        * **Enhanced Capabilities:** AI augments analysis (predictive forecasting, fraud detection in Accounting; hyper-personalization, customer insights in Marketing).
        * **Shift to Strategic Focus:** Both fields see a shift towards higher-value work: strategic advisory, complex analysis, planning (Accounting) and strategy, creativity, brand building (Marketing).
        """
    )

    st.success(
        """
        **💡 AI-Resilient Human Skills:**
        * **Complex Strategy & Critical Thinking:** Navigating ambiguity, high-stakes decisions, foresight beyond algorithms.
        * **Creativity & Innovation:** Generating novel ideas, unique messaging, emotional resonance.
        * **High-Level Relationships & Ethics:** Building trust, nuanced negotiation, ethical judgment, responsible oversight.
        *(Also crucial: Nuanced Communication, Adaptability, Cross-Functional Collaboration)*
        """
    )

    with st.expander("Learn More About AI's Role as Augmentation"):
        st.write("""
        AI excels at processing data and executing procedures but struggles with ambiguity, context, genuine creativity, empathy, and ethical nuance. The future likely involves professionals working *alongside* AI, leveraging its power while providing uniquely human strategic direction, critical judgment, and interpretation. The ability to 'translate' between technical AI outputs and actionable business strategy is increasingly valuable, fitting the combined Accountant-Marketer profile well.
        """)

# --- Tab 3: Career Paths ---
with tab3:
    st.header("Section 3: Promising AI-Resilient Career Paths")
    st.markdown(
        """
        These roles leverage the combined skillset and emphasize human-centric capabilities resilient to automation.

        **Top Recommended Role Categories:**
        * **Analytics & Operations Focused:** Marketing Analytics Manager, Revenue Operations (RevOps) Manager/Strategist (Aligning Marketing, Sales, Service).
        * **Finance & Business Analysis Focused:** Financial Analyst (FP&A, Strategic/Marketing Finance), Business Analyst (Bridging Marketing/Finance/Tech).
        * **Growth & Strategy Focused:** Business Development Manager, Product Marketing Manager, Digital Strategy Consultant/Manager.
        """
    )
    st.warning(
        """
        **Why These Roles are Resilient:**
        * They require **interpreting complex data** within business context, not just reporting it.
        * They involve **strategic planning, critical thinking, and creative problem-solving**.
        * They rely heavily on **cross-functional communication, collaboration, and stakeholder management**.
        *(The self-employment experience adds value via initiative, adaptability, and client/business management skills)*
        """
    )

    with st.expander("Explore Specific Role Descriptions (Examples)"):
        st.markdown("""
        * **Marketing Analytics Mgr:** Measures marketing effectiveness/ROI, analyzes customer data, derives insights for optimization, requires analytics tools (SQL, Tableau) + communication.
        * **RevOps Mgr:** Aligns Marketing/Sales/Service processes, tech (CRM, Marketing Automation), and data for predictable revenue; needs process, tech, analytical, and cross-functional skills.
        * **Financial Analyst (Strategic/Marketing Focus):** Budgeting, forecasting, modeling, analyzing ROI (esp. for marketing spend), requires financial acumen + strategic thinking + business partnering.
        * **Business Analyst:** Bridges business needs (e.g., Marketing/Finance) and tech solutions, gathers requirements, analyzes processes; needs analytical + communication + problem-solving skills.
        * **Business Development Mgr:** Drives growth via new opportunities/partnerships; needs sales/negotiation (Mktg-SE), strategic thinking (Mktg), financial acumen for deals (Acct).
        * **Product Marketing Mgr:** Defines product positioning/messaging, GTM strategy, sales enablement; needs market strategy (Mktg), analytics (Acct/Mktg), communication.
        * **Digital Strategy Consultant:** Advises on leveraging digital channels/tech/data for business goals; needs broad digital expertise (Mktg), analytics (Acct/Mktg), strategic planning (Mktg).
        """)

# --- Tab 4: Market Opportunities ---
with tab4:
    st.header("Section 4: Market Opportunities & Landscape")
    st.markdown(
        """
        Demand exists both locally (Portland, OR - Hybrid/In-Person) and nationally (US - Remote). Compensation often reflects the blend of strategic and analytical responsibilities.
        """
    )

    st.subheader("Table 1: Sample Portland, OR Area Hybrid/In-Person Roles & Estimates")
    st.dataframe(df_portland, hide_index=True)
    st.caption("(Note: Salary ranges are estimates based on limited report data and vary widely.)")

    st.subheader("Key Market Observations")
    st.markdown(
        """
        * **Portland & US Remote Availability:** Opportunities for these roles exist in the Portland metro area (tech, apparel, healthcare, services) often with hybrid options, and are widely available as fully remote positions across the US.
        * **Compensation Trends:** Roles requiring a sophisticated blend of analysis, strategic oversight, cross-functional leadership, or direct revenue impact often command higher salaries, valuing the integrated skillset.
        * **Remote Work Impact:** Remote availability significantly expands opportunities but also increases competition, making a strong, unique value proposition crucial.
        """
    )
    with st.expander("See Sample US Remote Salary Estimates (from report)"):
        st.markdown("""
        * **Marketing Analytics Mgr (Remote):** $100K - $238K+
        * **Marketing Ops Mgr (Remote):** $100K - $170K+ (Mgr/Sr Mgr)
        * **Financial/Business Analyst (Remote):** $70K - $143K+ (Analyst); $120K - $200K (Sr BA)
        * **RevOps Mgr/Director (Remote):** $129K (Avg Mgr); $180K - $220K (Director)
        * **Business Development Mgr (Remote):** Base varies greatly ($50K - $143K+ examples), often plus commission.
        * **Product Marketing Mgr (Remote):** $119K - $208K+
        * **Digital Strategy (Mgr/Director - Remote):** $129K - $280K+ (Varies by level)
        """)
        st.caption("(Note: Salary ranges are estimates based on limited report data and vary widely.)")


# --- Tab 5: Recommendations ---
with tab5:
    st.header("Section 5: Strategic Recommendations for Career Pivot")
    st.markdown(
        """
        Leverage the unique background and target roles strategically for a successful transition.
        """
    )

    st.success(
        """
        **Top Strategic Actions:**
        1.  **Prioritize Intersectional Roles:** Focus on primary targets like Marketing Analytics, RevOps, Strategic Financial/Business Analyst roles that directly blend analytics and strategy. Consider strong secondary options like BDM, PMM, Digital Strategy based on interest.
        2.  **Craft Your Unique Narrative:** Frame your resume/interviews to highlight the *synergy* between accounting's analytical foundation and digital marketing's strategic/growth/adaptability drivers. Quantify achievements using metrics relevant to target roles.
        3.  **Consider Targeted Upskilling:** Boost competitiveness with skills in high demand for target roles (e.g., Advanced Excel, Tableau/Power BI, SQL, Salesforce/HubSpot).
        """
    )

    st.subheader("Actionable Next Steps")
    st.markdown(
        """
        * **Refine Target Roles:** Select 2-3 primary paths.
        * **Tailor Resume/LinkedIn:** Create distinct versions highlighting relevant skills/keywords for each target.
        * **Network Strategically:** Connect with people in target fields/companies (online/local).
        * **Focused Job Search:** Use specific keywords for hybrid/remote roles; analyze job descriptions for requirements.
        * **Prepare for Interviews:** Practice articulating value proposition with specific STAR examples blending both skill sets.
        """
    )

    st.warning(
        """
        **Ongoing Resilience:**
        Remember that AI resilience is continuous. Commit to ongoing learning, adapting to new technologies, and honing uniquely human skills like strategic insight, creativity, empathy, and complex problem-solving.
        """
    )

st.markdown("---")
st.caption("Summary based on the 'Strategic Career Pathways' report analysis.")
