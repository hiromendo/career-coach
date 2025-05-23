# To run this app, save it as app.py and run: streamlit run app.py
import streamlit as st
import pandas as pd

# --- Helper function to generate anchor IDs for navigation ---
def generate_anchor(text):
    """Generates a URL-friendly anchor ID from text."""
    return text.lower().replace(" ", "-").replace(":", "").replace("’", "").replace("'", "").replace("/", "-").replace("(", "").replace(")", "").replace("&", "-and-")

# --- Custom CSS for cards and layout ---
st.markdown("""
<style>
    /* General body and heading styles */
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #1E3A5F; /* Dark blue for headings */
    }
    h1 {
        border-bottom: 2px solid #4A90E2; /* Accent color for main title */
        padding-bottom: 0.3em;
    }
    h2 { /* Section headers */
        color: #2E61A1;
        margin-top: 2em;
        border-bottom: 1px solid #ddd;
        padding-bottom: 0.2em;
    }
    h3 { /* Subsection headers */
        color: #367BC3;
        margin-top: 1.5em;
    }

    /* Card style for key insights */
    .card {
        border: 1px solid #E0E0E0; /* Light grey border */
        border-left: 5px solid #4A90E2; /* Accent color left border */
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05); /* Subtle shadow */
        background-color: #F8F9FA; /* Very light grey background */
    }
    .card-title {
        font-size: 1.15em;
        font-weight: bold;
        color: #1E3A5F; /* Dark blue title */
        margin-bottom: 10px;
    }
    .card p {
        font-size: 0.95em;
        line-height: 1.6;
    }

    /* Link container style */
    .link-container {
        margin-top: 15px;
        padding: 15px;
        background-color: #E9F2FC; /* Light blue background */
        border-radius: 6px;
        border: 1px dashed #4A90E2; /* Dashed accent border */
    }
    .link-container h5 {
        margin-bottom: 8px;
        font-size: 1.05em;
        color: #1E3A5F;
    }
    .link-container p {
        font-size: 0.9em;
        color: #333;
        margin-bottom: 5px;
    }
    .link-container a {
        color: #0056b3; /* Standard link blue */
        text-decoration: none;
    }
    .link-container a:hover {
        text-decoration: underline;
    }
    .link-container small {
        color: #555; /* Darker grey for snippet */
        display: block; /* Ensure snippet is on a new line */
        margin-top: 2px;
    }

    /* Styling for dataframes */
    .stDataFrame {
        width: 100%;
        margin-top: 1em;
        margin-bottom: 1em;
    }
    /* Ensure tables are not overly wide by default if Streamlit theme makes them so */
    div[data-testid="stDataFrame"] > div > div > table {
        width: auto !important; /* Or specify a max-width if preferred */
        min-width: 600px; /* Ensure readable width */
    }


    /* Sidebar styling */
    .st-emotion-cache-16txtl3 { /* Specific to Streamlit's sidebar class, might change with versions */
        background-color: #F0F4F8; /* Light grey-blue sidebar */
    }
    .st-emotion-cache-16txtl3 h2 { /* Sidebar header */
        color: #1E3A5F;
    }
    .st-emotion-cache-16txtl3 a { /* Sidebar links */
        color: #2E61A1;
        text-decoration: none;
        padding: 5px 0px;
        display: block;
    }
    .st-emotion-cache-16txtl3 a:hover {
        color: #4A90E2; /* Accent color on hover */
        text-decoration: none;
    }

    /* General content padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Bullet point styling */
    ul {
        list-style-type: disc; /* Or 'circle', 'square' */
        padding-left: 20px; /* Indent list */
    }
    li {
        margin-bottom: 0.5em; /* Space between list items */
        line-height: 1.6;
    }

</style>
""", unsafe_allow_html=True)

# --- Page Configuration ---
st.set_page_config(layout="wide", page_title="Strategic Blueprint: NYC Energy Finance Re-entry")

# --- Main Title ---
st.markdown("<h1>Navigating Your Next Chapter: A Strategic Blueprint for Re-entry into NYC's Energy Finance Landscape</h1>", unsafe_allow_html=True)

# --- Placeholder for search results (will be populated by the tool) ---
# This dictionary will store search results fetched by the Google Search tool.
# Keys are the search queries, values are lists of {title, link, snippet}.
search_results_store = {}

# --- Function to display links ---
def display_links(query, search_results_store):
    """Displays formatted links from the search_results_store."""
    results = search_results_store.get(query)
    if results:
        st.markdown("<div class='link-container'>", unsafe_allow_html=True)
        st.markdown("<h5>🔗 Further Reading & Resources:</h5>", unsafe_allow_html=True)
        for link_info in results:
            title = link_info.get("title", "No Title")
            link = link_info.get("link", "#")
            snippet = link_info.get("snippet", "No snippet available.")
            st.markdown(f"""
            <p><a href='{link}' target='_blank'>{title}</a><br>
            <small>{snippet}</small></p>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='link-container'>", unsafe_allow_html=True)
        st.markdown("<h5>🔗 Further Reading & Resources:</h5>", unsafe_allow_html=True)
        st.markdown("<p><small>No specific links found or search pending for this section.</small></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# --- Data for Tables ---
# Table 1: Summary of High-Demand Adjacent Roles in NYC for Your Profile
table1_data = {
    'Role Category': ['Energy PM & Hedge Fund Analyst', 'Energy Transition & Sustainable Finance', 'Quantitative Finance', 'Financial Risk Management', 'Corporate Strategy (Energy Co.)', 'Commodities Trading & Analysis'],
    'Specific Job Titles': ['Energy Portfolio Manager, Equity L/S Analyst (Energy)', 'Project Finance Analyst (Renewables), ESG Analyst, Climate Finance Specialist, Investment Associate (Energy Transition)', 'Quantitative Analyst, Quantitative Trader, Quantitative Developer', 'Market Risk Manager, Credit Risk Analyst, Counterparty Risk VP', 'Strategy Manager, Business Development Manager', 'Commodities Analyst, Trade Support Analyst, Power Trader'],
    'Key NYC Employers (Examples from Research)': ['Hedge Funds (Millennium, Citadel type), Asset Managers (Selby Jennings listings)', 'Banks (Citi), Asset Managers (BlackRock), Specialized Funds (Arevon, Brookfield), NYSERDA', 'Hedge Funds (Systematic), Investment Banks, Prop Trading Firms (Selby Jennings listings)', 'Investment Banks, Commercial Banks, Asset Managers (Selby Jennings listings, NYS DFS)', 'Utilities (Con Edison, National Grid), Renewable Developers (Ørsted, NextEra)', 'Investment Banks (JPMC), Energy Trading Firms (BP)'],
    'Core Skills Leveraged from Your Resume': ['Portfolio Management, Equity Analysis, Risk Management, Energy Sector Expertise, Financial Modeling', 'Financial Modeling, Sector Analysis, Due Diligence, Macro Analysis, Quantitative Skills', 'MIT Physics, Advanced Financial Modeling, Statistical Analysis, Programming (if current)', 'Risk Analysis, Portfolio Risk Management, Fundamental Analysis, Quantitative Aptitude', 'Energy Sector Knowledge, Financial Analysis, Strategic Thinking, Market Assessment', 'Energy Market Analysis, Supply-Demand Modeling, Financial Modeling, Quantitative Skills'],
    'Estimated NYC Salary Range (Annual, from Research)': ['$150k - $750k+ (3)', '$80k - $260k+ (1)', '$150k - $400k+ (12)', '$150k - $250k+ (17)', '$100k - $180k+ (34)', '$75k - $150k+ (Analyst); Trader varies (20)']
}
df_table1 = pd.DataFrame(table1_data)

# Table 2: Key NYC Professional Organizations & Networking Hubs
table2_data = {
    'Organization Name': ['CFA Society New York (CFANY)', 'Financial Women\'s Association (FWA)', '100 Women in Finance', 'Financial Executives International (FEI) NYC', 'CMT Association', 'NYSERDA / NY Green Bank'],
    'Primary Focus': ['Investment management, ethics, professional development', 'Advancement of women in finance', 'Global network for women in finance and alternative investments', 'Senior-level financial executives', 'Technical analysis', 'NY State energy research, development, clean energy financing'],
    'Key Benefits for Your Job Search': ['Networking, career resources, ESG focus, alternative investments, data science groups', 'Networking, mentorship, leadership development, industry voice', 'Networking, job board, educational events, peer engagement (all career stages)', 'Networking with senior leaders, insights on emerging issues (more for currently employed execs)', 'Education, networking for technical analysts/traders, CMT designation', 'Insights into NY\'s clean energy initiatives, potential roles, networking with policy/program staff'],
    'Noteworthy Event Types/Offerings (from Research)': ['Lunch & Learns, conferences (ALTSNY), interest group meetings, book club (49)', 'Free member events, thought leadership sessions, Pacesetter Program for outstanding women (51)', 'Educational sessions, peer engagement groups (MidCareer, ESG PAGs), annual Gala (53)', 'Webinars on CFO priorities, ESG, Cybersecurity, Career Management for board seats (55)', 'Educational webcasts, chapter meetings (58)', 'Job postings, industry events (implied through their mission 27)']
}
df_table2 = pd.DataFrame(table2_data)

# Table 3: Strategic Professional Certifications for Enhanced Marketability
table3_data = {
    'Certification Name': ['CFA (Chartered Financial Analyst)', 'ERP (Energy Risk Professional)', 'SASB FSA Credential', 'GARP SCR (Sustainability and Climate Risk)', 'CFA Institute Certificate in ESG Investing', 'CQF (Certificate in Quantitative Finance)', 'Python/SQL Programming Courses/Certifications'],
    'Issuing Body': ['CFA Institute', 'GARP', 'IFRS Foundation', 'GARP', 'CFA Institute', 'CQF Institute', 'Various (Coursera etc.)'],
    'Relevance to Your Target Roles': ['Investment Management, Equity Analysis, Portfolio Management, ESG', 'Energy Trading, Risk Management in Energy Sector', 'ESG Analysis, Sustainable Finance, Corporate Reporting, Investment Management', 'Climate Risk Management, ESG Risk, Sustainable Finance', 'ESG Analysis, Portfolio Management, Sustainable Investing', 'Quantitative Analyst/Trader roles', 'Quantitative Finance, Data Analysis roles in any finance sector, including energy transition'],
    'Potential Impact on Candidacy': ['Gold standard, demonstrates deep financial acumen and ethical grounding. (60)', 'Specialized, shows expertise in managing risks unique to energy markets. (60)', 'Demonstrates ability to integrate sustainability into financial analysis, materiality focus. (64)', 'Focuses on climate science, policy, and risk strategies; highly relevant for emerging risk roles. (64)', 'Globally recognized, comprehensive ESG curriculum. (64)', 'Demonstrates advanced quantitative skills, useful for a dedicated quant pivot. (60)', 'Demonstrates practical technical skills increasingly in demand.'],
    'Notes (e.g., Cost from Research)': ['Significant time commitment.', '', 'L1: $450, L2: $650 (64)', '$700-$825 (64)', 'Approx. $890 (64)', 'Significant investment.', 'Varies.']
}
df_table3 = pd.DataFrame(table3_data)

# --- Section Definitions and Content ---
# This list defines the structure and content of the page.
# Each item is a dictionary representing a section or subsection.
section_definitions = [
    {
        "title": "I. Introduction: Charting Your Course Back to a High-Impact Career",
        "level": 1,
        "content": [
            ("paragraph", "This report is designed to provide a comprehensive and actionable strategy for navigating a return to the New York City job market, particularly focusing on high-impact roles within the finance sector that align with a distinguished background in energy sector equity long/short analysis. The experience gained at premier institutions such as Millennium, Citadel, and Morgan Stanley, combined with a strong academic foundation in Physics from MIT, forms a powerful platform for future success."),
            ("paragraph", "The past two years of unemployment represent a significant transition. This period, however, also coincides with a dynamic evolution within the energy and finance sectors. The financial landscape, especially concerning energy, has seen a marked shift, with an increasing emphasis on energy transition, sustainability, and renewable resources.[1] This evolving market presents not merely a challenge for re-entry but a unique opportunity to strategically reposition and leverage accumulated expertise in burgeoning, high-demand areas. This report will delve into optimizing your professional profile, understanding the current NYC job market dynamics—both in traditional finance and the rapidly expanding energy transition space—identifying specific adjacent job roles that offer a strong fit, and outlining a concrete action plan to secure such a position. The objective is to transform the career break into a narrative of strategic adaptation and forward-looking engagement with these new market realities."),
        ],
        "search_query": "NYC energy finance career re-entry strategy"
    },
    {
        "title": "II. Maximizing Your Profile: Resume Analysis and Strategic Positioning",
        "level": 1,
        "content": [
            ("paragraph", "Effectively re-entering the competitive NYC finance market after a two-year hiatus requires a meticulously crafted professional profile. This involves a deep appreciation of existing strengths and a proactive, strategic approach to addressing the career break across all professional representations—resume, LinkedIn, and interview narratives.")
        ],
        # This main section has subsections that will carry their own search queries
    },
    {
        "title": "A. Deep Dive into Your Experience: Identifying Core Strengths, Transferable Skills, and Key Accomplishments",
        "level": 2,
        "content": [
            ("paragraph", "A thorough review of your resume reveals a consistent track record of high performance and significant responsibilities. These core strengths and accomplishments must be front and center in your job search materials."),
            ("bullet_heading", "Core Strengths:"),
            ("bullet_list", [
                "Energy Sector Expertise: Your career demonstrates a profound and nuanced understanding of the oil & gas industry, broader commodity markets, intricate market dynamics, fund flows, and the formulation of macro views. This is evident from your roles at Millennium, Citadel, and Morgan Stanley. A particularly notable achievement was successfully predicting and positioning for fund flows into the energy sector at Millennium, a contrarian stance that proved highly prescient during a period when such flows became a primary driver of stock dispersion.",
                "Portfolio Management & Risk Deployment: You have proven experience in building out and managing substantial energy portfolios, including for a commodities team with $1.5 billion in gross deployable capital at Millennium, and autonomously running an $850 million carve-out at Citadel. Responsibility for the vast majority of a team’s beta-neutral risk deployment (Millennium) and the majority of risk deployment on Citadel's largest energy team underscores a sophisticated understanding of risk management.",
                "Investment Acumen & Performance: A consistent record of strong performance, highlighted by a Sharpe ratio greater than 1 at Citadel, even during challenging market conditions for the energy sector, is a significant differentiator. The ability to identify wildly misunderstood companies, such as the $30 billion enterprise value company whose capital structure traded to distressed levels as your research permeated the market, showcases exceptional analytical and value-identification skills. Furthermore, your time at Fore Research & Management involved successfully pushing to short leveraged energy companies ahead of major oil price declines.",
                "Financial Modeling & Quantitative Analysis: The creation and maintenance of comprehensive valuation models, development of localized supply-demand models for North American crude oil price differentials, and the construction of a US natural gas production cost curve by basin (all at Morgan Stanley) highlight advanced financial modeling and quantitative analytical capabilities. An undergraduate degree in Physics from MIT further substantiates this strong quantitative aptitude.",
                "Leadership & Mentorship: Beyond analytical prowess, leadership qualities are evident through roles such as Varsity Wrestling Captain. Professional recognition as a top analyst at Citadel, leading to requests to train and mentor others, speaks to your ability to inspire and develop talent."
            ]),
            ("bullet_heading", "Transferable Skills:"),
            ("bullet_list", [
                "Analytical & Problem-Solving: Expertise in fundamental analysis, dissecting complex financial and operational structures, and accurately predicting market trends.",
                "Strategic Thinking: A proven ability to form insightful macro views, influence investment strategy at the fund level, and strategically position portfolios for anticipated market shifts.",
                "Communication & Influence: Effectively articulating complex research and investment theses to internal teams and stakeholders, as demonstrated by influencing fund views on energy sector shorts."
            ]),
            ("bullet_heading", "Key Accomplishments to Quantify and Highlight:"),
            ("paragraph", "To maximize impact, your resume and communications should consistently quantify achievements:"),
            ("bullet_list", [
                "Clearly state the dollar value of portfolios managed or influenced (e.g., \"$1.5bn gross deployable capital,\" \"$850mm carve-out,\" \"managed over $100mm of lead-role positions\").",
                "Prominently feature performance metrics where possible (e.g., \">1 Sharpe ratio\").",
                "Detail specific impactful investment calls and their outcomes (e.g., \"single-handedly found a $30bn enterprise value company that was wildly misunderstood,\" \"successfully pushed to short leveraged energy companies ahead of large oil price declines\")."
            ]),
            ("card", {
                "title": "Important Consideration: Title vs. Function Discrepancy",
                "text": "A critical observation from your resume is the consistent use of the \"Analyst\" title (Millennium, Citadel) despite descriptions of responsibilities that are characteristic of portfolio management, such as \"autonomously ran an $850mm carve-out\" and \"built out and managed the oil & gas portfolio.\" This apparent discrepancy between title and function could lead to being overlooked for Portfolio Manager roles or an undervaluing of your experience level. It is imperative that your resume summary, cover letters, LinkedIn profile, and interview discussions proactively bridge this gap. Emphasize the autonomy exercised, the direct responsibility for capital deployment and risk, and the impact of your decisions on portfolio performance. While the P&L contribution might have been part of a larger team or beta-neutral, the management of a significant carve-out and the responsibility for substantial risk deployment are key indicators of experience well beyond a typical analyst role. Highlighting these aspects will ensure your candidacy is considered for roles commensurate with your actual experience and capabilities, such as the \"Equity Long Short - Energy Portfolio Manager\" position detailed by Selby Jennings, which seeks individuals with a track record of managing significant books of business.[3]"
            })
        ],
        "search_query": "resume strategic positioning finance energy sector transferable skills"
    },
    {
        "title": "B. Addressing the Career Break: Proactive Strategies for Your Resume, LinkedIn Profile, and Interview Narratives",
        "level": 2,
        "content": [
            ("paragraph", "A two-year career break will undoubtedly be a point of discussion for potential employers.[4] A proactive and positive approach to addressing this period is essential. The goal is to control the narrative, frame the time constructively, and demonstrate continued relevance and eagerness to re-engage."),
            ("subheading", "Resume Strategy:"),
            ("bullet_list", [
                "Placement and Honesty: Do not attempt to hide the gap. Address it directly and concisely within the experience section or a dedicated \"Career Note.\" Some guidance suggests listing it similarly to a work experience entry [5], for example: \"Professional Sabbatical & Skill Enhancement (Dates).\" This maintains transparency.",
                "Positive Framing: Focus on any productive activities undertaken, even if personal. Examples include: \"Career Break for Family Responsibilities and Professional Development\" or \"Strategic Sabbatical focused on [mention any relevant study/research, even if informal]\".[6] The aim is to present the break as an intentional period rather than an unexplained void.",
                "Highlighting Growth: If you engaged in any online courses, certifications, freelance projects, volunteer work, or significant self-study relevant to finance or energy, these should be mentioned.[5] This demonstrates initiative and a commitment to staying current.",
                "Resume Format: A combination resume format, which leads with a strong summary of skills and accomplishments before detailing chronological work history, can be particularly effective.[5] This allows your key qualifications to make an immediate impact."
            ]),
            ("subheading", "LinkedIn Profile Optimization:"),
            ("bullet_list", [
                "Headline: Your LinkedIn headline should be forward-looking and incorporate keywords relevant to your target roles. For instance: \"Senior Energy Finance & Investment Professional | Equity L/S, Portfolio Strategy, Risk Management | Ex-Millennium, Citadel | MIT Physics | Targeting Senior Analyst/Portfolio Manager Roles in NYC.\" This adapts advice for those not currently working to an experienced professional's context.[8]",
                "\"To Present\" Position or Career Break Function: LinkedIn now offers a \"Career Break\" feature which can be utilized. An alternative, effective strategy is to create a \"To Present\" entry.[8] This could be titled \"Strategic Career Sabbatical | Focusing on Energy Transition Research & Advanced Financial Analytics.\" Under this entry, list activities such as relevant courses completed (e.g., on ESG, renewable finance), industry research, significant networking activities, or conferences attended. This approach helps maintain LinkedIn's \"All-Star\" profile status (beneficial for search visibility) and allows for further keyword optimization.",
                "Summary (About) Section: This section is critical for reinforcing your value proposition. Briefly reiterate your most significant achievements and explicitly state your readiness and enthusiasm for a challenging new role in the NYC energy finance sector. Mention your key areas of focus, such as energy markets, financial modeling, portfolio management, and potentially new interests like energy transition finance or ESG integration.[8] Include a clear call to action, inviting connections and discussions about relevant opportunities.",
                "Skills & Endorsements: Ensure your skills section is comprehensive and up-to-date. Include keywords related to your established expertise (e.g., \"Energy Markets,\" \"Oil & Gas,\" \"Equity Valuation,\" \"Financial Modeling,\" \"Portfolio Management,\" \"Risk Management\") and any new areas you're targeting (e.g., \"ESG Analysis,\" \"Renewable Energy Finance,\" \"Sustainable Investing,\" \"Climate Risk\")."
            ]),
            ("subheading", "Interview Narrative:"),
            ("bullet_list", [
                "Honesty, Brevity, and Positivity: When asked about the career break, address it honestly and concisely, without over-explaining or adopting an apologetic tone.[4] Frame the period positively, focusing on what you did, learned, or how you prepared for re-entry. Whether it was for personal reasons, family responsibilities, or a planned sabbatical, emphasize that this period has concluded and you are now re-energized and fully prepared to commit to a demanding role.[10]",
                "Focus on Learnings and Readiness: Highlight any skills honed or new knowledge acquired during the break. This could range from formal certifications to informal research into the evolving energy landscape or deeper reflection on career goals.[4] If applicable, the STAR method (Situation, Task, Action, Result) can be a useful framework for structuring your response.[10]",
                "Connect to the Target Role: Crucially, link any activities or learnings from your time off to the requirements of the specific job for which you are interviewing. Explain how the break, and what you did during it, has made you an even stronger candidate or provided fresh perspectives.[4]",
                "Demonstrate Confidence: Convey genuine enthusiasm for returning to the workforce and unwavering confidence in your ability to contribute significantly from day one."
            ]),
            ("card", {
                "title": "Key Takeaway: Proactive Narrative Management for Career Break",
                "text": "By proactively managing the narrative around your career break, you can transform a potential concern for employers into a demonstration of resilience, strategic thinking, and preparedness. If this narrative includes any upskilling or focused learning in areas that have grown in prominence over the last two years, such as sustainable finance or data analytics, it further strengthens your current market relevance."
            })
        ],
        "search_query": "addressing career break on resume LinkedIn interview strategies"
    },
    {
        "title": "III. The NYC Energy & Finance Job Market: Current Landscape and Emerging Opportunities",
        "level": 1,
        "content": [
            ("paragraph", "New York City remains a global epicenter for finance, and its role in the energy sector is rapidly evolving. Understanding the current demand trends in both traditional finance and the burgeoning energy transition space is crucial for a targeted and effective job search.")
        ],
    },
    {
        "title": "A. Overview of Traditional Finance Roles in Demand (NYC)",
        "level": 2,
        "content": [
            ("paragraph", "Despite the growing focus on sustainability, robust demand continues for experienced professionals in established financial roles, particularly those with specialized sector expertise like yours."),
            ("bullet_heading", "Key Areas:"),
            ("bullet_list", [
                "Investment Management & Research: Major financial institutions and asset managers in NYC consistently seek talent for investment strategy, due diligence, and equity research.[11] Your background in equity long/short analysis is a direct and strong fit for these types of roles.",
                "Hedge Fund Analyst/Portfolio Manager (Energy Focus): Opportunities for seasoned energy sector specialists persist within hedge funds, ranging from multi-strategy platforms to energy-focused boutiques.[3] For example, a recent listing for an \"Equity Long Short - Energy Portfolio Manager\" in New York by Selby Jennings specified a salary range of $250,000 - $750,000 and required a proven track record, including delivering $10 million+ in P&L and achieving a Sharpe ratio of 1% or higher – criteria that align well with your documented performance and experience managing significant capital.[3] Another listing from the same recruiter for an \"Oil or Natural Gas Portfolio Manager\" indicated a negotiable salary, highlighting bespoke opportunities for top talent.[12]",
                "Quantitative Finance: The demand for professionals with strong STEM backgrounds (like your MIT Physics degree) and skills in programming (Python, SQL) and advanced data analysis remains exceptionally high across various financial institutions.[14] A \"Quantitative Analyst\" role in NYC, also listed by Selby Jennings, offered $300,000-$400,000 and specifically sought candidates with STEM degrees and Python/SQL proficiency.[15]",
                "Financial Risk Management: There is a consistent need for experts in managing market, credit, liquidity, and operational risk within NYC's financial ecosystem.[17]",
                "Commodities Trading Support & Analysis: Roles supporting commodities trading desks, requiring a solid understanding of market structures and financial instruments, are also available.[20] For instance, a JPMC Commodities Trade Support Analyst position in New York, with a salary range of $74,850-$95,300, requires an understanding of trading structures and strong analytical skills.[20]"
            ])
        ],
        "search_query": "traditional finance roles demand NYC investment hedge fund quantitative"
    },
    {
        "title": "B. Spotlight on NYC's Energy Transition: Growth in Renewables, Sustainability, and Climate Finance",
        "level": 2,
        "content": [
            ("paragraph", "New York City has rapidly emerged as a North American hub for sustainability-focused careers. This growth is significantly propelled by ambitious state-level policies, such as the Climate Leadership and Community Protection Act (CLCPA) and New York City's Local Law 97, alongside increasing corporate commitments to Environmental, Social, and Governance (ESG) principles.[2] The number of sustainability-related job postings in New York State surged from approximately 9,000 in 2020 to around 15,000 in 2023, underscoring the dynamism of this sector.[2]"),
            ("bullet_heading", "Key Growth Areas:"),
            ("bullet_list", [
                "Renewable Energy Project Finance & Investment: There is substantial activity in developing, financing, and managing investments in renewable energy projects (solar, wind, battery storage). Roles often involve creating complex financial models, conducting due diligence for acquisitions, and supporting capital deployment strategies.[23] An example is Arevon's Analyst, Project Finance & Investment role in NYC, typically requiring 1-3 years of experience in the renewable energy industry, utilities sector, or banking, with strong proficiency in Microsoft Excel for financial modeling and an understanding of project financing structures.[23]",
                "ESG Investing & Sustainable Finance: This broad category encompasses roles focused on integrating ESG factors into investment decision-making processes, engaging with companies on their sustainability performance, and developing ESG-focused investment products and strategies. Demand spans from ESG Analysts to senior leadership positions like VP of Sustainable Investing.[24] A Vice President of Sustainable Investing role in private markets, for instance, can command a salary in the $220,000-$260,000 range and typically requires over 10 years of experience in sustainability within private markets or ESG consulting.[25]",
                "Climate Finance: This specialized area involves analyzing climate-related financial risks and opportunities, understanding carbon markets, developing carbon accounting methodologies, and structuring financing for climate solutions and green initiatives.[2] Roles are found within city agencies (e.g., Senior Climate Finance Officer for the City of New York), major banks (e.g., J.P. Morgan Chase's Climate Macroeconomic Modeler), and specialized advisory firms.[26]",
                "Energy Transition Strategy & Consulting: Professionals in this space advise corporations, utilities, and investors on navigating the complexities of decarbonization, developing net-zero strategies, and adapting business models to the evolving energy landscape.[1]"
            ]),
            ("bullet_heading", "Key Employers:"),
            ("paragraph", "The spectrum of employers in NYC's energy transition space is diverse, including:"),
            ("bullet_list", [
                "Financial Institutions: Major banks like Citi [1], and global asset managers such as BlackRock and Morgan Stanley [2], are significantly expanding their sustainable finance teams.",
                "Specialized Investment Funds: Firms like Brookfield Asset Management and Blackstone are actively investing in energy transition assets and platforms.[1]",
                "Energy Companies & Utilities: Incumbents like Con Edison are heavily involved in local renewable energy initiatives and grid modernization.[2]",
                "Renewable Energy Developers & Operators: Companies like Arevon are focused on project development and investment.[23]",
                "Government & Research Organizations: Entities like the New York State Energy Research and Development Authority (NYSERDA) and the NY Green Bank play a crucial role in policy implementation and financing.[27]",
                "Consulting Firms: Major consultancies and specialized advisory firms are building out their ESG and energy transition practices."
            ])
        ],
        "search_query": "NYC energy transition jobs market growth renewables sustainability climate finance"
    },
    {
        "title": "C. Demand Trends for Energy-Focused Finance Professionals in NYC",
        "level": 2,
        "content": [
            ("paragraph", "The confluence of traditional energy market dynamics and the accelerating energy transition creates a unique demand profile for finance professionals with energy sector expertise in New York City."),
            ("card", {
                "title": "Enduring Value of Traditional Energy Expertise",
                "text": "While the long-term trajectory is towards renewable and low-carbon energy systems, deep knowledge of traditional energy markets (oil, gas, power) remains highly valuable. This expertise is critical for understanding the complex transition pathways, valuing existing energy infrastructure, managing commodity price volatility, and assessing the financial viability of incumbent energy companies as they adapt. Your extensive background in oil & gas equity L/S is directly applicable to roles within investment banks, hedge funds, and asset managers that continue to cover or invest in these sectors."
            }),
            ("card", {
                "title": "The Rise of the \"Transition Expert\"",
                "text": "Professionals who can bridge the gap between the old and new energy worlds—those who understand the fundamentals of conventional energy assets while also grasping the financial, technological, and policy drivers of the energy transition—are in a particularly strong and sought-after position. Your analytical skills, honed in dissecting complex energy companies and markets, can be powerfully applied to evaluating new energy technologies, renewable energy projects, and the strategic challenges facing companies undergoing decarbonization. This ability to connect traditional energy finance with the emerging sustainable finance landscape represents a significant competitive advantage. The energy transition is not a simple replacement of one energy source with another; it involves intricate financial reallocations, the repurposing or decommissioning of existing assets, and the development of entirely new value chains. Expertise in traditional energy markets provides a crucial lens for assessing stranded asset risks, understanding the interplay between conventional and renewable power generation, and identifying investment opportunities in enabling technologies (e.g., carbon capture, hydrogen) that may complement or integrate with existing energy systems."
            }),
            ("card", {
                "title": "Policy as a Sustained Demand Driver",
                "text": "New York City and New York State have enacted some of the most ambitious climate policies in the United States, including the CLCPA (mandating 100% zero-emission electricity by 2040 and an 85% reduction in economy-wide greenhouse gas emissions by 2050) and NYC's Local Law 97 (imposing stringent carbon emission caps on large buildings).[2] These legislative mandates create a non-discretionary, long-term demand for companies and public entities to invest heavily in decarbonization, energy efficiency, and renewable energy. This, in turn, fuels a consistent need for finance professionals skilled in structuring and funding these investments, performing carbon accounting, ensuring ESG compliance, and managing climate-related financial risks. Unlike purely market-driven finance sectors, the demand for these roles in NYC is underpinned by legal and regulatory requirements, suggesting a more stable and potentially less cyclical employment landscape. This is a particularly positive factor for individuals re-entering the job market seeking roles with long-term growth prospects."
            }),
            ("bullet_heading", "Salary Insights in NYC's Energy Finance Space:"),
            ("bullet_list", [
                "Traditional Energy Portfolio Management: Salaries can vary widely. General Energy Portfolio Manager roles in NYC average around $115,000, with a broad range of $80,000 to $205,000.[28] However, specialized, high-performance roles, such as the \"Equity Long Short - Energy Portfolio Manager\" advertised by Selby Jennings, can command significantly higher compensation, in the range of $250,000 to $750,000, contingent on fund size and P&L track record.[3]",
                "Renewable Energy Finance: The average salary for renewable energy finance roles in NYC is approximately $101,000, with top earners reaching $147,000 and beyond.[29] Specific positions, such as an \"Associate, Business Development (Clean Energy Finance)\" at the New York City Energy Efficiency Corporation (NYCEEC), offer base salaries in the $84,000 - $110,000 range, plus potential bonuses.[30]",
                "Sustainable Finance & ESG: Sustainable Finance Analysts in NYC earn an average of $96,000, with top-tier salaries exceeding $127,000.[31] General Sustainability Analyst roles average around $98,000, typically falling within an $85,000 to $111,000 range.[32]",
                "Specialized Roles: Positions like an Energy Tax Credits Business Development Manager can command salaries in the $200,000 - $250,000 range, reflecting the niche expertise required.[13]"
            ])
        ],
        "search_query": "demand trends energy finance professionals NYC salary insights"
    },
    {
        "title": "IV. High-Demand Adjacent Career Pathways in NYC",
        "level": 1,
        "content": [
            ("paragraph", "Leveraging your substantial experience in energy sector equity L/S analysis and your strong quantitative background, several adjacent career pathways in NYC offer excellent prospects. These roles capitalize on your existing skills while providing avenues for growth, potentially in the expanding energy transition and sustainable finance sectors.")
        ]
    },
    {
        "title": "A. Energy Portfolio Management & Hedge Fund Analyst/PM Roles (Directly Leveraging L/S Experience)",
        "level": 2,
        "content": [
            ("expander", {
                "title": "Role Description & Relevance",
                "content": [
                    ("paragraph", "Description: These roles involve managing portfolios of energy-related equities, encompassing both traditional (oil & gas, utilities) and increasingly, renewable energy assets, often within a long/short, event-driven, or relative value strategy. Core responsibilities include deep fundamental research, financial modeling, market trend analysis, idea generation, trade execution, and rigorous risk management."),
                    ("paragraph", "Relevance: This is the most direct application of your experience at Millennium, Citadel, and Fore Research. Your demonstrated ability to autonomously manage significant capital (e.g., the $850mm carve-out at Citadel), consistently achieve strong performance (Sharpe >1), identify mispriced securities, and make impactful sector calls (e.g., shorting leveraged energy companies) are precisely what these roles demand.")
                ]
            }),
            ("bullet_list", [
                "NYC Demand & Employers: New York City remains the global hub for hedge funds and asset management. Opportunities exist within multi-strategy funds, dedicated energy-focused funds, and traditional asset managers expanding their energy coverage. Recruiters like Selby Jennings frequently list such positions, including \"Equity Long Short - Energy Portfolio Manager\" [3] and \"Oil or Natural Gas Portfolio Manager\".[12] ZipRecruiter also features \"Energy Portfolio Manager\" roles across various firm types.[28]",
                "Estimated NYC Salary Range: Compensation is highly variable and performance-driven. Analysts can expect base salaries from $150,000 to $250,000+, with significant bonus potential. Portfolio Managers, particularly those with a proven track record, can see total compensation ranging from $250,000 to $750,000 and significantly higher, often with a direct P&L participation component.[3]",
                "Considerations: The two-year career break may present a hurdle in this highly competitive and fast-paced segment, where recent market experience and an active network are prized. A compelling narrative for the break, coupled with demonstrated recent engagement with the markets (e.g., through personal investing, research, or relevant coursework) and strong networking, will be critical."
            ])
        ],
        "search_query": "energy portfolio management hedge fund analyst PM roles NYC"
    },
    {
        "title": "B. Energy Transition & Sustainable Finance (ESG, Climate Finance, Renewables Investment)",
        "level": 2,
        "content": [
             ("expander", {
                "title": "Role Description & Relevance",
                "content": [
                    ("paragraph", "Description: This rapidly expanding field encompasses a variety of roles focused on financing, investing in, and advising on sustainable energy projects, integrating ESG factors into investment processes, and managing climate-related financial risks and opportunities."),
                    ("bullet_list", [
                        "Project Finance Analyst/Associate (Renewables): Involves financial modeling, due diligence, risk assessment, and transaction support for renewable energy projects such as solar, wind, and battery storage. The Arevon \"Analyst, Project Finance & Investment\" role is a good example, requiring 1-3 years of experience in renewable energy, utilities, or banking, strong Excel modeling skills, and an understanding of project financing structures.[23] Your financial modeling expertise is directly transferable.",
                        "ESG Analyst/Associate/VP: Focuses on researching and integrating material ESG factors into investment analysis and decision-making, engaging with companies on their sustainability performance, developing ESG policies for investment funds, and contributing to ESG reporting. Various roles exist across asset management, private equity, and consulting.[24] A senior role like a VP of Sustainable Investing can command a salary of $220,000-$260,000 and typically requires extensive experience (10+ years) in sustainability or ESG.[25] Your analytical rigor is a key asset here.",
                        "Climate Finance Specialist: Involves analyzing physical and transition climate risks and opportunities, understanding carbon markets and pricing mechanisms, developing climate-related financial products, and structuring financing for green initiatives and climate adaptation/mitigation projects. Employers include city agencies, banks (e.g., JPMC's Climate Macroeconomic Modeler), and specialized advisory firms.[26]",
                        "Investment Roles (Energy Transition Funds): These positions involve sourcing, evaluating, executing, and managing investments in clean energy technologies, renewable energy infrastructure, and companies facilitating the energy transition. Major players include Brookfield Asset Management and Blackstone.[1]"
                    ]),
                    ("paragraph", "Relevance: Your deep understanding of the energy sector provides an invaluable foundation. Your analytical skills, financial modeling capabilities, and experience in forming macro views are highly transferable to assessing renewable energy projects and the broader energy transition. Your MIT Physics degree adds credibility, particularly when evaluating new technologies.")
                ]
            }),
            ("bullet_list", [
                "NYC Demand & Employers: This is a high-growth area in NYC. Key employers include investment banks (e.g., Citi [1]), global asset managers (e.g., BlackRock, Morgan Stanley [2]), specialized energy transition and renewable energy funds (e.g., Arevon [23], Brookfield [1]), consulting firms, and public/quasi-public entities like NYSERDA.[27]",
                "Estimated NYC Salary Range: Analyst roles typically range from $80,000 to $150,000. Vice President level positions can range from $150,000 to $260,000+, with further upside in investment roles tied to fund performance.[1]",
                "Considerations: While your core skills are transferable, demonstrating a genuine interest and foundational knowledge in sustainability concepts, ESG frameworks, and renewable energy technologies (perhaps through recent courses or certifications) will be beneficial."
            ])
        ],
        "search_query": "energy transition sustainable finance ESG climate finance renewables investment jobs NYC"
    },
    {
        "title": "C. Quantitative Finance & Advanced Analytics (Capitalizing on MIT Physics and Analytical Acumen)",
        "level": 2,
        "content": [
            ("expander", {
                "title": "Role Description & Relevance",
                "content": [
                    ("paragraph", "Description: These roles involve the development, implementation, and validation of quantitative models for trading strategies, risk management, portfolio construction, asset pricing, or algorithmic execution. They typically require strong mathematical and statistical skills, along with proficiency in programming languages such as Python, SQL, and C++."),
                    ("paragraph", "Relevance: Your Bachelor of Science in Physics from MIT is a significant asset and a common educational background for quantitative finance professionals. Your experience in building complex financial models (e.g., localized supply-demand models, US natural gas production cost curves) demonstrates strong quantitative aptitude and analytical rigor.")
                ]
            }),
            ("bullet_list", [
                "NYC Demand & Employers: Demand for quantitative talent is consistently high in NYC. Employers include systematic hedge funds, quantitative trading desks at investment banks, proprietary trading firms, and increasingly, asset managers incorporating quantitative techniques. Selby Jennings lists roles such as \"Quantitative Power Trader\" ($150,000-$200,000 + PnL split) focusing on electricity and energy markets [12], \"Quantitative Analyst\" ($300,000-$400,000) for equity market making [15], and \"Quantitative Developer\" ($175,000-$250,000).[12] Google also has Financial Analyst positions that require a quantitative field degree and experience in FP&A or consulting.[14]",
                "Estimated NYC Salary Range: Compensation in quantitative finance is highly competitive, often with substantial performance-based bonuses. Base salaries for experienced individuals can range from $150,000 to $400,000+, depending on the specific role, firm, and level of expertise.[12]",
                "Considerations: While your physics degree is a strong credential, you may need to demonstrate recent proficiency in relevant programming languages (Python, SQL are commonly required) and familiarity with current quantitative finance techniques. Your energy sector expertise could be a unique selling point if applying to quantitative roles that have an energy or commodities focus."
            ])
        ],
        "search_query": "quantitative finance advanced analytics MIT Physics NYC jobs"
    },
    {
        "title": "D. Financial Risk Management (Applying Analytical Rigor to Market and Credit Risk)",
        "level": 2,
        "content": [
            ("expander", {
                "title": "Role Description & Relevance",
                "content": [
                    ("paragraph", "Description: Professionals in financial risk management are responsible for identifying, measuring, monitoring, and mitigating various financial risks, including market risk, credit risk, liquidity risk, and operational risk, within financial institutions or corporations."),
                    ("paragraph", "Relevance: Your experience in managing risk within investment portfolios (e.g., \"responsible for the vast majority of the team’s beta-neutral risk deployment\"), your deep understanding of market drivers in the energy sector, and your rigorous fundamental analysis skills are highly applicable to risk management roles. The analytical discipline developed through your physics education is also a key asset.")
                ]
            }),
            ("bullet_list", [
                "NYC Demand & Employers: There is a steady demand for skilled risk management professionals in NYC's financial services industry. Employers include investment banks, commercial banks, asset managers, insurance companies, and regulatory bodies. Selby Jennings has listings for roles such as \"VP Resolution Planning,\" \"Director of Corporate Credit,\" \"Counterparty Credit Risk VP\" (salary $170,000-$180,000), and \"Senior Risk Manager Options/Volatility\" ($200,000-$250,000 + bonus).[18] ZipRecruiter also shows a variety of risk management positions.[19] The New York State Department of Financial Services (NYS DFS) also has numerous openings in risk management and compliance.[17]",
                "Estimated NYC Salary Range: Compensation varies by level, specialization, and firm. AVP and VP level roles in risk management often command salaries in the $150,000 to $250,000+ range, with more senior roles earning substantially more.[18]",
                "Considerations: Highlighting specific instances where your analytical skills led to successful risk mitigation or identification of potential threats will be important. Certifications like the FRM (Financial Risk Manager) could enhance your candidacy."
            ])
        ],
        "search_query": "financial risk management market credit risk NYC jobs"
    },
    {
        "title": "E. Corporate Strategy & Development within Energy Companies (Broader Strategic Impact)",
        "level": 2,
        "content": [
            ("expander", {
                "title": "Role Description & Relevance",
                "content": [
                    ("paragraph", "Description: These roles are typically situated within energy companies themselves (traditional oil & gas, utilities, renewable energy developers) and involve strategic planning, market analysis, competitive intelligence, mergers and acquisitions (M&A), new business development, and helping the company navigate the evolving energy landscape and the transition to cleaner energy sources."),
                    ("paragraph", "Relevance: Your profound understanding of the energy sector, financial modeling skills, and experience in forming macro-level views would be invaluable to energy companies formulating their long-term strategies. Your experience in influencing fund views also demonstrates strategic thinking and persuasive communication.")
                ]
            }),
            ("bullet_list", [
                "NYC Demand & Employers: While many large energy corporations have headquarters elsewhere, several have significant operations or strategic offices in or near NYC, or offer hybrid/remote roles accessible from NYC. Potential employers include major utilities with a New York presence like Con Edison [34] and National Grid [36], large renewable energy developers such as Ørsted [38] and NextEra Energy (though many of NextEra's corporate strategy roles may be based in Florida, their national presence and specific project needs could create NYC-proximate opportunities).[40] Companies like Energy Solution also list strategy and growth management roles, often with remote or hybrid options.[42]",
                "Estimated NYC Salary Range: Compensation is highly variable depending on the size of the company, the specific responsibilities, and seniority. A Strategy Manager role at Con Edison, for example, was listed with a salary range of $100,000-$140,000.[34] A Manager, Strategy, Policy & Regulatory role at National Grid was listed at $152,000-$179,000.[37]",
                "Considerations: This pathway offers a shift from pure financial markets to a more direct involvement in the operational and strategic growth of energy businesses. It could be appealing if seeking to have a broader impact on the energy transition from within an operating company."
            ])
        ],
        "search_query": "corporate strategy development energy companies NYC jobs"
    },
    {
        "title": "F. Commodities Trading & Analysis (Deepening Energy Sector Specialization)",
        "level": 2,
        "content": [
            ("expander", {
                "title": "Role Description & Relevance",
                "content": [
                    ("paragraph", "Description: These roles involve analyzing physical and financial commodity markets (crude oil, natural gas, power, refined products, renewable energy credits), developing trading strategies, executing trades, or providing analytical support to trading operations."),
                    ("paragraph", "Relevance: This is a natural extension of your deep energy sector expertise. Your experience in building localized supply-demand models and US natural gas production cost curves at Morgan Stanley is highly relevant to commodities analysis.")
                ]
            }),
            ("bullet_list", [
                "NYC Demand & Employers: New York is a major center for commodities trading. Employers include investment banks with active commodities desks (e.g., J.P. Morgan Chase [20]), specialized energy trading firms, commodity-focused hedge funds, and utilities with trading arms. BP, for example, has advertised for a Power Trade Analyst in NYC/Houston with a salary range of $107,000-$153,000.[43]",
                "Estimated NYC Salary Range: Analyst roles supporting commodities trading can range from $75,000 to $150,000+.[20] Salaries for commodities traders themselves vary enormously based on P&L performance and can be very substantial.[45]",
                "Considerations: While your background is in equity L/S, the analytical skills are transferable. Roles focused on financial commodities analysis or supporting trading desks would be a closer fit than physical trading, which has different logistical and operational considerations.[47]"
            ])
        ],
        "search_query": "commodities trading analysis energy sector NYC jobs"
    },
    {
        "title": "Table 1: Summary of High-Demand Adjacent Roles in NYC for Your Profile",
        "level": 2, # Displayed under section IV for context
        "content": [
            ("paragraph", "To provide a consolidated view, the following table summarizes these promising career pathways, linking them to your core skills and providing realistic employer and salary expectations based on current market data."),
            ("table", "table1")
        ],
        # No specific search for a table summary, content is self-contained
    },
    {
        "title": "V. Actionable Re-Entry Strategy: A Roadmap to Your Next Role",
        "level": 1,
        "content": [
            ("paragraph", "A successful return to the workforce after a significant break requires a deliberate, multi-faceted strategy. This involves not only identifying the right opportunities but also proactively marketing your skills, expanding your network, and continuously enhancing your candidacy.")
        ]
    },
    {
        "title": "A. Crafting a Targeted Job Search: Identifying and Approaching Relevant Employers",
        "level": 2,
        "content": [
            ("paragraph", "A systematic approach to identifying and engaging with potential employers will maximize efficiency and effectiveness."),
            ("subheading", "Tiered Approach to Targeting:"),
            ("bullet_list", [
                "Tier 1 (Direct Fit): Focus initially on energy-focused hedge funds and asset management firms seeking professionals with direct equity L/S experience in the energy sector. Your roles at Millennium and Citadel are prime credentials here. Employers mentioned in listings from recruiters like Selby Jennings [3] are good starting points.",
                "Tier 2 (Strong Adjacency - High Growth): Concurrently explore opportunities in the rapidly expanding energy transition and sustainable finance space. This includes firms specializing in ESG investing, renewable project finance, and climate finance. Emphasize your transferable analytical skills, deep energy sector knowledge, and quantitative aptitude. Relevant employers include specialized funds like Arevon [23], large asset managers like BlackRock and Morgan Stanley [2], banks like Citi [1], and organizations like NYSERDA.[1]",
                "Tier 3 (Leveraging Quantitative Strengths): For roles in quantitative finance, particularly those with an energy or commodities angle, or those requiring sophisticated modeling skills. Your MIT Physics degree and experience building complex models are key selling points here. Target systematic hedge funds, investment banks, and proprietary trading firms.[12]"
            ]),
            ("subheading", "In-Depth Company Research:"),
            ("paragraph", "Once target firms are identified, conduct thorough research into their recent activities, investment philosophies (especially concerning energy and sustainability), team structures, and recent hires. Identify alumni from MIT or your previous firms who may work there, as they can be valuable initial contacts."),
            ("subheading", "Utilizing Job Platforms & Niche Boards:"),
            ("paragraph", "While general job platforms like LinkedIn and Indeed are useful, also focus on specialized finance job boards such as eFinancialCareers and the websites of specialist recruiters like Selby Jennings, who feature prominently in sourcing for energy and quantitative finance roles.[3] For sustainability and climate-focused roles, explore niche boards like Terra.do [25], Enable.Green [2], and ClimateTechList.[48] Built In NYC [11] and ZipRecruiter [1] are also good sources for NYC-specific finance and energy job postings."),
            ("subheading", "Direct Applications & Recruiter Engagement:"),
            ("paragraph", "For roles that are a strong match, apply directly through company career portals. Simultaneously, proactively engage with executive recruiters who specialize in your target sectors (finance, energy, sustainability). Provide them with your updated resume and a clear articulation of your career objectives and target roles.")
        ],
        "search_query": "targeted job search strategy finance NYC energy finance recruiters"
    },
    {
        "title": "B. Effective Networking in NYC: Leveraging Professional Organizations and Events",
        "level": 2,
        "content": [
            ("paragraph", "After a career break, networking becomes an even more critical component of the job search strategy than for someone making a direct job-to-job transition. A two-year absence from the daily flow of market interactions and internal company networks means that proactive efforts are needed to rebuild visibility and uncover opportunities, many of which, particularly at senior levels, are filled through professional connections rather than public advertisements. NYC offers a rich ecosystem of professional organizations that provide structured platforms for making these vital connections."),
            ("subheading", "Key Professional Organizations in NYC:"),
            ("bullet_list", [
                "CFA Society New York (CFANY): As a leading forum for investment professionals, CFANY offers a wealth of resources, including numerous events, specialized interest groups (e.g., Alternative Investments, Data Science and Quantitative Investment, Financial Reporting and Analysis, ESG), career development programs, and extensive networking opportunities. Their calendar often features Lunch & Learns, industry conferences like ALTSNY (Alternative Investments New York), and member-exclusive gatherings.[49] Engagement here is crucial for connecting with the mainstream finance community and those focused on ESG.",
                "Financial Women's Association (FWA): The FWA is dedicated to promoting the professional development and advancement of women in the financial industry through education, mentorship, scholarships, networking events, and strategic alliances. Membership provides access to exclusive free and discounted events, opportunities to share expertise by presenting, and a platform to advocate for diversity and inclusion.[51] This is an excellent organization for expanding your professional network and gaining visibility among influential women in NYC finance.",
                "100 Women in Finance: This global organization has a significant and active New York chapter, catering to women at all career stages in the finance and alternative investment industries. They offer a variety of educational events, peer engagement groups (including for Early Career, MidCareer professionals, and Angels), and high-profile networking functions like their annual Gala. Membership also includes access to a job board.[53]",
                "Financial Executives International (FEI) New York City Chapter: FEI is a premier organization for senior-level financial executives. While primarily serving currently employed executives, their events (which have covered topics like CFO priorities, ESG, Cybersecurity, and career management for board seats) can offer valuable insights and networking opportunities with top financial leaders in NYC.[55] Attending open events or connecting with members could be beneficial.",
                "CMT Association: For individuals considering roles with a significant technical analysis component (e.g., certain trading or portfolio management strategies), the CMT Association provides education, networking, and the Chartered Market Technician (CMT) designation.[58]",
                "Global Association of Risk Professionals (GARP): GARP is the offering body for the Financial Risk Manager (FRM) and Energy Risk Professional (ERP) certifications, making it a key organization for those targeting roles in financial or energy risk management.[60]",
                "NYSERDA / NY Green Bank: While not a traditional professional organization, staying informed about NYSERDA's initiatives and events can provide insights into New York's clean energy landscape and potential networking opportunities with professionals in policy, program management, and clean energy finance.[27]"
            ]),
            ("subheading", "Strategic Networking Activities:"),
            ("bullet_list", [
                "Attend Industry Events: Prioritize conferences, seminars, and webinars focused on energy finance, sustainable investing, ESG, renewable energy, or quantitative finance. Platforms like AllEvents.in [61] and Meetup.com [62] list a wide array of finance-related events in NYC, covering topics from real estate finance and fintech to AI in finance and cryptocurrency.",
                "Leverage Alumni Networks: Your MIT alumni network is a powerful asset. Seek out fellow alumni working in your target firms or sectors in NYC.",
                "Informational Interviews: Proactively reach out to professionals working in roles or companies that interest you. Request brief informational interviews to learn more about their experiences, industry trends, and company culture, and to seek advice on your job search. This is a low-pressure way to expand your network and gain valuable insights."
            ]),
            ("table", "table2")
        ],
        "search_query": "effective networking NYC finance professional organizations events"
    },
    {
        "title": "C. Enhancing Your Candidacy: Strategic Professional Development and Certifications",
        "level": 2,
        "content": [
            ("paragraph", "After a career break, demonstrating current competency and a proactive approach to professional development is particularly important. Strategic certifications and targeted learning can signal to employers that your skills are up-to-date and that you are committed to re-engaging with the industry at a high level, especially in rapidly evolving areas like sustainable finance and quantitative methods."),
            ("subheading", "Addressing the Gap & Signaling Current Interest:"),
            ("paragraph", "Pursuing relevant certifications serves multiple purposes: it validates existing knowledge, helps acquire new skills tailored to emerging market demands, and provides tangible evidence of your commitment to professional growth during and after your career break. This is especially valuable when targeting adjacent roles where you may need to demonstrate specific expertise in newer fields."),
            ("subheading", "Relevant Certifications to Consider:"),
            ("bullet_list", [
                "CFA (Chartered Financial Analyst): The CFA designation is globally recognized as the gold standard for investment management professionals, covering a broad range of topics including ethics, financial analysis, portfolio management, and economics.[60] If you have not earned the charter, highlighting any levels passed is still beneficial. For your background, it reinforces core analytical rigor.",
                "ERP (Energy Risk Professional) by GARP: This specialized certification is designed for professionals managing risk in the energy markets, covering physical and financial energy products, and modeling techniques.[60] It would be highly relevant if you are targeting risk management roles within the energy trading or utility sectors.",
                "SASB FSA (Fundamentals of Sustainability Accounting) Credential: Offered by the IFRS Foundation, the FSA Credential focuses on understanding and applying industry-specific sustainability accounting standards that link ESG factors to financial performance and enterprise value.[64] It is excellent for roles in ESG analysis, sustainable investment integration, and corporate sustainability reporting. The credential consists of two levels, with Level 1 costing approximately $450 and Level 2 around $650.[64]",
                "GARP SCR (Sustainability and Climate Risk) Certificate: This certification equips professionals with the knowledge to understand, assess, and manage sustainability and climate-related risks. It covers climate science, policy, regulatory frameworks, and risk management techniques, making it ideal for roles in climate risk, ESG risk, and sustainable finance.[64] The approximate cost is $700-$825.[64]",
                "CFA Institute Certificate in ESG Investing: This certificate provides a comprehensive curriculum covering ESG concepts, materiality, ESG integration techniques across asset classes, and stewardship.[64] It is globally recognized and particularly useful for professionals aiming for roles in ESG analysis, portfolio management with an ESG focus, or sustainable investing. The approximate cost is $890.[64]",
                "CQF (Certificate in Quantitative Finance): If you are seriously considering a pivot towards more dedicated quantitative finance roles, the CQF is a rigorous program that covers advanced mathematical and computational techniques used in modern finance.[60] It requires a significant time and financial investment but can be a powerful credential for demonstrating cutting-edge quantitative skills.",
                "Programming Courses/Certifications (Python, SQL): Given the increasing importance of data analysis and programming in finance, particularly in quantitative roles and even in areas like energy transition modeling, demonstrating proficiency in Python and SQL is highly advantageous. Numerous online courses and certifications are available through platforms like Coursera, edX, and specialized training providers."
            ]),
            ("subheading", "Online Courses and Continuous Learning:"),
            ("paragraph", "Beyond formal certifications, actively engaging in online courses related to financial modeling for renewable energy, advanced Excel techniques, Python for finance, ESG data analysis, or specific aspects of climate finance can further enhance your profile. Mentioning completion of such courses on your resume and LinkedIn profile can demonstrate initiative and a commitment to staying current."),
            ("table", "table3")
        ],
        "search_query": "strategic professional development finance certifications ESG CFA GARP SASB"
    },
    {
        "title": "VI. Concluding Perspectives and Strategic Recommendations",
        "level": 1,
        "content": [
            ("paragraph", "Your distinguished career in energy finance, marked by significant achievements at top-tier firms and a rigorous academic foundation from MIT, provides a formidable base for re-entering the New York City job market. The key to a successful transition after a two-year period of unemployment lies in strategically leveraging this experience while proactively addressing the career break and aligning your job search with current market dynamics, particularly the burgeoning opportunities in energy transition and sustainable finance."),
            ("paragraph", "The opportunities are abundant for a professional with your caliber of energy sector knowledge and analytical prowess. The traditional finance roles in energy-focused investment management and analysis remain viable, while the explosive growth in ESG, renewable energy finance, and climate finance in NYC offers exciting new avenues where your skills are highly transferable and in demand. Furthermore, your quantitative background opens doors to specialized roles in advanced analytics and modeling."),
            ("card", {
                "title": "Overarching Re-Entry Strategy",
                "text": """
                The overarching strategy for your re-entry should be multi-pronged:
                * **Targeted Application:** Focus on roles that are a direct fit for your L/S equity background in energy, while simultaneously exploring high-growth adjacent areas in sustainable finance and roles that capitalize on your quantitative skills.
                * **Proactive Narrative Management:** Consistently and positively address the career break across your resume, LinkedIn profile, and in all interview conversations. Frame it as a period of intentional activity, reflection, or skill enhancement that has prepared you for your next challenge.
                * **Aggressive Networking:** Actively engage with professional organizations in NYC, attend relevant industry events, and leverage your existing and newly formed connections. Networking will be paramount in uncovering opportunities and gaining direct insights.
                * **Strategic Professional Development:** Consider pursuing targeted certifications (such as SASB FSA, GARP SCR, or CFA ESG Investing) to signal current competency, demonstrate commitment, and acquire specialized knowledge in high-demand areas.
                """
            }),
            ("paragraph", "The power of a cohesive narrative cannot be overstated. Your resume, LinkedIn presence, networking interactions, and interview responses must all weave together a consistent and compelling story. This narrative should portray you as a highly accomplished finance professional who, after a necessary and perhaps strategically utilized break, is now re-engaging with the market with renewed focus, targeting roles where deep expertise and a forward-looking perspective can drive significant impact."),
            ("paragraph", "The path to re-entry after a career break can present challenges, but with a well-defined strategy, diligent execution, and a confident presentation of your substantial skills and experience, a return to a rewarding and high-impact career in New York City's dynamic finance landscape is not only possible but highly achievable.")
        ],
        "search_query": "career re-entry strategy unemployment finance strategic recommendations"
    },
    {
        "title": "Works Cited",
        "level": 1,
        "content": [
            ("expander", {
                "title": "View Full List of Works Cited",
                "content": [
                    ("raw_html", """
                    <ol style="font-size: 0.9em; line-height: 1.5;">
                        <li>Energy Transition Jobs in New York - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Sustainability Jobs in New York: Latest market trends 2024, accessed May 16, 2025</li>
                        <li>Equity Long Short - Energy Portfolio Manager job in New York ..., accessed May 16, 2025</li>
                        <li>How to Explain Gaps in Employment: Advice for Job Applicants ..., accessed May 16, 2025</li>
                        <li>How to Write a Resume After a Career Break - Enhancv, accessed May 16, 2025</li>
                        <li>Address Employment Gaps on Your Resume Without Losing Out!, accessed May 16, 2025</li>
                        <li>How to Explain a Five Year Career Gap on Resume - VisualCV, accessed May 16, 2025</li>
                        <li>Unemployed? 3 Suggestions for a Powerful Executive LinkedIn Profile, accessed May 16, 2025</li>
                        <li>Investment Banking Linkedin Profile: How to Make It Great - Mergers & Inquisitions, accessed May 16, 2025</li>
                        <li>How to Explain Gaps in Employment During Interviews - Upwork, accessed May 16, 2025</li>
                        <li>Best Finance Jobs in NYC, NY 2025 | Built In NYC, accessed May 16, 2025</li>
                        <li>Hedge Fund Jobs in New York | Apply for Vacancies | Selby Jennings, accessed May 16, 2025</li>
                        <li>$55k-$250k Energy Hedge Fund Jobs in New York (NOW HIRING) - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Search Jobs — Google Careers, accessed May 16, 2025</li>
                        <li>Quantitative Analyst job in New York | Selby Jennings, accessed May 16, 2025</li>
                        <li>Quantitative Analytics Research And Trading Jobs in New York | Apply for Vacancies, accessed May 16, 2025</li>
                        <li>Careers with DFS | Department of Financial Services - NY.gov, accessed May 16, 2025</li>
                        <li>Risk Management Jobs in New York | Apply for Vacancies | Selby ..., accessed May 16, 2025</li>
                        <li>Financial Risk Management Jobs in New York City, NY - ZipRecruiter, accessed May 16, 2025</li>
                        <li>New York Commodities Trade Support Analyst - JPMC Candidate Experience page Careers, accessed May 16, 2025</li>
                        <li>New York Commodities Trade Support Analyst jobs in New York, NY | The Muse, accessed May 16, 2025</li>
                        <li>VP: Commodities QIS Structurer job in New York | Selby Jennings, accessed May 16, 2025</li>
                        <li>Analyst, Project Finance & Investment - Arevon Energy, Inc. | Built In ..., accessed May 16, 2025</li>
                        <li>$46k-$210k Esg Investing Jobs in New York City, NY - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Vice President - Sustainable Investing - Private Markets at Madison ..., accessed May 16, 2025</li>
                        <li>$82k-$205k Climate Finance Jobs in New York, NY (NOW HIRING), accessed May 16, 2025</li>
                        <li>Jobs at NYSERDA and NY Green Bank, accessed May 16, 2025</li>
                        <li>$80k-$205k Energy Portfolio Manager Jobs in New York - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Renewable Energy Finance Salary in New York City, NY - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Associate, Business Development (Clean Energy Finance), accessed May 16, 2025</li>
                        <li>Salary: Sustainable Finance Analyst in New York (May, 2025) - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Sustainability Analyst Salary in New York, NY, accessed May 16, 2025</li>
                        <li>$82k-$200k Energy Finance Jobs in New York (NOW HIRING) - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Strategy Manager - DER Interconnection - New York - Consolidated Edison | Ladders, accessed May 16, 2025</li>
                        <li>73 Con Edison Jobs Hiring in New York, NY - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Head of Social Impact & Community Engagement Operations at National Grid, accessed May 16, 2025</li>
                        <li>NATIONAL GRID Jobs in New York (Now Hiring) May 2025 - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Vacancies: See All Available Jobs | Ørsted Careers, accessed May 16, 2025</li>
                        <li>Jobs in Renewable Energy | Ørsted Careers, accessed May 16, 2025</li>
                        <li>Senior Financial Analyst- Origination- Renewable Natural Gas at NextEra Energy - Terra.do, accessed May 16, 2025</li>
                        <li>Careers | Join Our Team | Corporate Jobs - NextEra Energy, accessed May 16, 2025</li>
                        <li>Careers - Energy Solutions, accessed May 16, 2025</li>
                        <li>Power Trade Analyst - BP, accessed May 16, 2025</li>
                        <li>Research & Development Analyst - ACT Commodities Group | Built In NYC, accessed May 16, 2025</li>
                        <li>Commodities Trader Salary in New York, New York, accessed May 16, 2025</li>
                        <li>Salary: Commodity Trader in New York City, NY (May, 2025) - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Energy Trader: What Is It? and How to Become One? - ZipRecruiter, accessed May 16, 2025</li>
                        <li>Latest Finance Jobs from 700+ Climate Tech Companies - ClimateTechList, accessed May 16, 2025</li>
                        <li>Upcoming Events – CFA Society New York, accessed May 16, 2025</li>
                        <li>2025 CFA Society New York Lunch & Learn, accessed May 16, 2025</li>
                        <li>About the FWA - Financial Women's Association, accessed May 16, 2025</li>
                        <li>Explore Membership with the Financial Women's Association, accessed May 16, 2025</li>
                        <li>New York - 100 Women In Finance, accessed May 16, 2025</li>
                        <li>Membership - 100 Women In Finance, accessed May 16, 2025</li>
                        <li>FEI New York City - Financial Executives International, accessed May 16, 2025</li>
                        <li>Events | FEI New York City - FEI - Financial Executives International, accessed May 16, 2025</li>
                        <li>skuhns@feinyc.org - FEI New York | financialexecutives.org, accessed May 16, 2025</li>
                        <li>CMT Program - Market Research Hub, accessed May 16, 2025</li>
                        <li>Chartered Market Technician® (CMT) Program - CMT Association, accessed May 16, 2025</li>
                        <li>Finance Organizations and Certifications - Naveen Jindal School of Management | The University of Texas at Dallas, accessed May 16, 2025</li>
                        <li>List Of All Upcoming Financial Services Events In New York - AllEvents, accessed May 16, 2025</li>
                        <li>Find Events & Groups in New York, NY - Meetup, accessed May 16, 2025</li>
                        <li>Finance Certifications - Financial Management Association, accessed May 16, 2025</li>
                        <li>The Best ESG Certificates to Pursue in 2025, accessed May 16, 2025</li>
                        <li>FSA Credential - IFRS Foundation, accessed May 16, 2025</li>
                    </ol>
                    """)
                ]
            })
        ]
        # No search query for works cited
    }
]

# --- Collect all search queries ---
queries_to_search = []
for section in section_definitions:
    if "search_query" in section and section["search_query"] not in queries_to_search:
        queries_to_search.append(section["search_query"])

# --- Simulate Web Search (Tool Call Block) ---
# This is where the actual `Google Search` tool would be called.
# The result of this block (search_api_results) will be used to populate `search_results_store`.
# For now, I will define a placeholder for search_api_results.
# In a real execution, the platform would replace this with the tool's output.
#
# Example of how the tool call would be generated by the AI:
# print(Google Search(queries=queries_to_search))
#
# After the tool call, search_api_results would look something like:
# search_api_results = [
#   # Results for queries_to_search[0]
#   [{"title": "Title 1", "link": "url1", "snippet": "Snippet 1..."}, {"title": "Title 2", "link": "url2", "snippet": "Snippet 2..."}],
#   # Results for queries_to_search[1]
#   [{"title": "Title A", "link": "urlA", "snippet": "Snippet A..."}, ...],
#   ...
# ]
# The following is placeholder data for demonstration if the tool isn't run:

# BEGINNING OF TOOL CODE BLOCK
# This block should be executed by the environment to get actual search results.
# If this is run locally without the `Google Search` tool, it will use the placeholder data below.
if 'Google_Search' in globals() and hasattr(globals()['Google_Search'], 'search'):
    try:
        # This is the actual tool call.
        # It is expected that the environment executes this and provides `search_api_results`.
        print(f"Executing Google Search with {len(queries_to_search)} queries.")
        search_api_results = Google_Search(queries=queries_to_search) # This is the line that triggers the tool

        # Process the results from the tool
        if search_api_results and isinstance(search_api_results, list) and len(search_api_results) == len(queries_to_search):
            for i, query in enumerate(queries_to_search):
                # Ensure results for each query are correctly structured
                query_results = search_api_results[i]
                if isinstance(query_results, list): # Expecting a list of dicts for each query
                     search_results_store[query] = [{"title": r.get("title"), "link": r.get("link"), "snippet": r.get("snippet")} for r in query_results if isinstance(r, dict)]
                elif isinstance(query_results, dict) and "results" in query_results and isinstance(query_results["results"], list): # Alternative structure some tools might return
                     search_results_store[query] = [{"title": r.get("title"), "link": r.get("link"), "snippet": r.get("snippet")} for r in query_results["results"] if isinstance(r, dict)]
                else: # Fallback if the structure is unexpected for a specific query
                    print(f"Warning: Unexpected result format for query: {query}")
                    search_results_store[query] = []
        else:
            print("Warning: Mismatch between queries and results length, or API results are empty/malformed.")
            # Populate with empty results if API call fails or returns unexpected data
            for query in queries_to_search:
                search_results_store[query] = []

    except Exception as e:
        print(f"Error during Google Search call: {e}")
        # Populate with empty results in case of an error
        for query in queries_to_search:
            search_results_store[query] = []
else:
    # Placeholder data if Google Search tool is not available (e.g., local development)
    print("Using placeholder search data as Google Search tool is not available.")
    placeholder_search_data = {
        "NYC energy finance career re-entry strategy": [
            {"title": "Tips for Re-entering Finance in NYC", "link": "#placeholder1", "snippet": "Discover strategies for returning to the NYC finance job market after a break."},
            {"title": "Energy Sector Job Trends in New York", "link": "#placeholder2", "snippet": "Overview of current trends and opportunities in NYC's energy finance sector."}
        ],
        "resume strategic positioning finance energy sector transferable skills": [
            {"title": "Crafting a Finance Resume for Energy Roles", "link": "#placeholder3", "snippet": "How to highlight your energy sector expertise and transferable skills on your resume."},
            {"title": "Strategic Resume Positioning After Career Break", "link": "#placeholder4", "snippet": "Techniques for positioning your resume effectively when re-entering the job market."}
        ],
        # Add more placeholder data for other queries if needed for local testing
    }
    for query in queries_to_search:
        search_results_store[query] = placeholder_search_data.get(query, [
            {"title": f"Sample Link 1 for '{query}'", "link": "#", "snippet": "This is a sample search result snippet..."},
            {"title": f"Sample Link 2 for '{query}'", "link": "#", "snippet": "Authoritative information regarding your query..."}
        ])
# END OF TOOL CODE BLOCK

# --- Sidebar Navigation ---
st.sidebar.markdown("<h2>Navigation</h2>", unsafe_allow_html=True)
for section_data in section_definitions:
    title = section_data["title"]
    anchor_id = generate_anchor(title)
    if section_data["level"] == 1:
        st.sidebar.markdown(f"<b><a href='#{anchor_id}'>{title}</a></b>", unsafe_allow_html=True)
    elif section_data["level"] == 2:
        # Clean up subsection title for display
        display_title = title.split(". ", 1)[1] if ". " in title else title
        st.sidebar.markdown(f"<a href='#{anchor_id}' style='padding-left: 15px;'>&bull; {display_title}</a>", unsafe_allow_html=True)


# --- Main Content Generation ---
for section_data in section_definitions:
    title = section_data["title"]
    anchor_id = generate_anchor(title)
    level = section_data["level"]
    content_items = section_data["content"]
    query_key = section_data.get("search_query")

    if level == 1:
        st.markdown(f"<h2 id='{anchor_id}'>{title}</h2>", unsafe_allow_html=True)
    elif level == 2:
        st.markdown(f"<h3 id='{anchor_id}'>{title}</h3>", unsafe_allow_html=True)

    for item_type, item_data in content_items:
        if item_type == "paragraph":
            st.markdown(item_data, unsafe_allow_html=True)
        elif item_type == "subheading": # For minor headings within a section
            st.markdown(f"<h4>{item_data}</h4>", unsafe_allow_html=True)
        elif item_type == "bullet_heading":
            st.markdown(f"<strong>{item_data}</strong>", unsafe_allow_html=True)
        elif item_type == "bullet_list":
            md_list = ""
            for point in item_data:
                md_list += f"* {point}\n"
            st.markdown(md_list, unsafe_allow_html=True)
        elif item_type == "card":
            st.markdown(f"<div class='card'><div class='card-title'>{item_data['title']}</div><p>{item_data['text']}</p></div>", unsafe_allow_html=True)
        elif item_type == "table":
            if item_data == "table1":
                st.dataframe(df_table1)
            elif item_data == "table2":
                st.dataframe(df_table2)
            elif item_data == "table3":
                st.dataframe(df_table3)
        elif item_type == "expander":
            with st.expander(item_data["title"]):
                for exp_item_type, exp_item_data in item_data["content"]:
                    if exp_item_type == "paragraph":
                        st.markdown(exp_item_data, unsafe_allow_html=True)
                    elif exp_item_type == "bullet_list":
                        exp_md_list = ""
                        for point in exp_item_data:
                            exp_md_list += f"* {point}\n"
                        st.markdown(exp_md_list, unsafe_allow_html=True)
                    elif exp_item_type == "raw_html":
                        st.markdown(exp_item_data, unsafe_allow_html=True)
        elif item_type == "raw_html":
            st.markdown(item_data, unsafe_allow_html=True)


    # Display search links if a query was defined for this section
    if query_key:
        # Use columns for links to not take up full width, or just display as is
        col1, col2 = st.columns([3, 1]) # Main content takes more space
        with col1: # Keep main content flow clear, or put links in a narrower column
             display_links(query_key, search_results_store)
        # If you prefer links to be full width under the section:
        # display_links(query_key, search_results_store)

    st.markdown("---") # Separator between sections/subsections

# --- Footer ---
st.markdown("<hr style='margin-top: 2em;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777; font-size: 0.9em;'>Strategic Blueprint Application | Generated by AI</p>", unsafe_allow_html=True)