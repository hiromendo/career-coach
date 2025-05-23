import streamlit as st

# --- Main Title ---
st.title("V. Actionable Re-Entry Strategy: A Roadmap to Your Next Role 🗺️")
st.markdown("""
A successful return to the workforce after a significant break requires a deliberate, multi-faceted
strategy. This involves not only identifying the right opportunities but also proactively marketing
your skills, expanding your network, and continuously enhancing your candidacy.
""")

st.divider()

# --- Section A: Crafting a Targeted Job Search ---
st.header("A. Crafting a Targeted Job Search: Identifying and Approaching Relevant Employers 🎯")
st.markdown("""
A systematic approach to identifying and engaging with potential employers will maximize
efficiency and effectiveness.
""")

with st.expander("🔍 Tiered Approach to Targeting"):
    st.markdown("""
    Organize your job search by focusing on roles that best match your experience and growth areas.
    """)
    st.subheader("🥇 Tier 1: Direct Fit")
    st.markdown("""
    Focus initially on **energy-focused hedge funds and asset management firms** seeking professionals
    with direct equity L/S experience in the energy sector. Your roles at Millennium and Citadel
    are prime credentials here.
    * **Starting Points:** Employers mentioned in listings from recruiters like Selby Jennings (3).
    """)
    st.info("Leverage your strong background at Millennium and Citadel for these roles.")

    st.subheader("🥈 Tier 2: Strong Adjacency - High Growth")
    st.markdown("""
    Concurrently explore opportunities in the rapidly expanding **energy transition and sustainable
    finance space**. This includes firms specializing in ESG investing, renewable project finance,
    and climate finance.
    * **Emphasis:** Transferable analytical skills, deep energy sector knowledge, and quantitative aptitude.
    * **Relevant Employers:** Specialized funds like Arevon²³, large asset managers like BlackRock
        and Morgan Stanley², banks like Citi¹, and organizations like NYSERDA.¹
    """)
    st.success("Highlight your analytical skills and energy knowledge for this high-growth sector.")

    st.subheader("🥉 Tier 3: Leveraging Quantitative Strengths")
    st.markdown("""
    For roles in **quantitative finance**, particularly those with an energy or commodities angle,
    or those requiring sophisticated modeling skills.
    * **Key Selling Points:** Your MIT Physics degree and experience building complex models.
    * **Target Employers:** Systematic hedge funds, investment banks, and proprietary trading firms.¹²
    """)
    st.warning("Your MIT Physics degree is a significant asset for quantitative roles.")

with st.expander("🏢 In-Depth Company Research"):
    st.markdown("""
    Once target firms are identified, conduct thorough research:
    * **Areas to Investigate:** Recent activities, investment philosophies (especially concerning
        energy and sustainability), team structures, and recent hires.
    * **Networking Tip:** Identify alumni from MIT or your previous firms who may work there,
        as they can be valuable initial contacts.
    """)

with st.expander("🌐 Utilizing Job Platforms & Niche Boards"):
    st.markdown("""
    Combine general and specialized job boards for a comprehensive search:
    * **General Platforms:** LinkedIn, Indeed.
    * **Specialized Finance Boards:** eFinancialCareers.
    * **Specialist Recruiters:** Websites of recruiters like Selby Jennings (prominent for energy
        and quantitative finance roles).³
    * **Sustainability & Climate-Focused Boards:** Terra.do²⁵, Enable.Green², ClimateTechList.⁴⁸
    * **NYC-Specific Boards:** Built In NYC¹¹, ZipRecruiter.¹
    """)
   

with st.expander("📬 Direct Applications & Recruiter Engagement"):
    st.markdown("""
    A two-pronged approach for applications:
    1.  **Direct Applications:** For roles that are a strong match, apply directly through company
        career portals.
    2.  **Recruiter Engagement:** Proactively engage with executive recruiters who specialize in your
        target sectors (finance, energy, sustainability).
        * **What to Provide:** Your updated resume and a clear articulation of your career
            objectives and target roles.
    """)
    st.markdown("---")
    st.markdown("##### Example Recruiter Outreach Snippet:")
    st.code("""
Subject: Experienced Energy Finance Professional (Equity L/S, MIT Physics) Seeking Senior Analyst/PM Role

Dear [Recruiter Name],

I am an accomplished energy finance professional with [Number] years of experience, including significant roles at Millennium and Citadel, where I managed substantial energy portfolios (e.g., $850mm carve-out) and consistently delivered strong performance (Sharpe >1). My expertise lies in equity long/short strategies within the oil & gas sector, complemented by a strong quantitative background (B.S. Physics, MIT) and proven financial modeling skills.

After a planned career break, I am actively seeking a challenging Senior Analyst or Portfolio Manager position in the NYC area, with a focus on the energy sector or opportunities within the growing energy transition space. My resume, attached for your review, provides further detail on my track record and capabilities.

I am particularly interested in [Mention specific types of roles or firms the recruiter specializes in, if known]. I am confident I can bring significant value and am eager to discuss how my skills align with your current mandates.

Thank you for your time and consideration.

Sincerely,
[Your Name]
[Your LinkedIn Profile URL]
[Your Phone Number]
    """, language='text')


st.divider()
st.caption("Disclaimer: This page is based on the provided text. Citation numbers (e.g., ³, ¹²) refer to sources in the original document.")

# To run this Streamlit app:
# 1. Save this code as a Python file (e.g., reentry_strategy_app.py).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: streamlit run reentry_strategy_app.py
