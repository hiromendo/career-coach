import streamlit as st

# --- Main Title for this section ---
st.header("2. Understanding the Landscape: Key Focus Areas at Origis Energy (and similar firms)")
st.markdown("""
To design impactful personal projects, it is crucial to understand the operational and strategic landscape of leading renewable energy companies.
**Origis Energy** serves as an excellent benchmark, with its activities reflecting broader industry trends and priorities.
""")
st.markdown("---") # Visual separator

# --- Subsection: Core Business ---
st.subheader("Core Business: Powering the Future with Renewables")

col1, col2 = st.columns([3, 1]) # Main content on left, key stats/quotes on right

with col1:
    st.markdown("""
    Origis Energy's primary activities revolve around the **development, financing, construction, and operation of solar energy and energy storage projects**.
    Their substantial portfolio, approaching nearly **17 GW of solar and energy storage capacity to date**, illustrates their significant role in the energy transition.
    The company's scope includes *"grid power generation, performance optimization, and the long-term operation of solar and energy storage plants across the U.S."*.
    """)
    st.markdown("""
    Beyond established solar and storage solutions, Origis Energy is strategically positioning itself in emerging clean energy fields.
    A notable example is their investment in **"green hydrogen,"** with a dedicated team working to *"supply deep decarbonization solutions"*.
    This forward-looking approach indicates an understanding that achieving comprehensive decarbonization requires a diverse portfolio of technologies and solutions.
    """)

with col2:
    st.info(f"""
    **Key Stats (Origis Energy):**
    * ~17 GW Solar & Storage Capacity
    * Focus: Development, Finance, Construction, Operation
    * Emerging: Green Hydrogen
    """)
    


st.markdown("---")

# --- Subsection: Strategic Pillars ---
st.subheader("Strategic Pillars: Beyond Kilowatts and Megawatts")
st.markdown("""
The success and growth of companies like Origis Energy are built on several key strategic pillars that extend beyond the mere generation of renewable energy:
""")

# Using expanders for each pillar to keep the main page cleaner
with st.expander("🌍 Decarbonization as a Mission", expanded=True):
    st.markdown("""
    For Origis, *"decarbonization is the essence of our mission"*. This principle underpins their business strategy, focusing on removing
    *"limits to our customers' decarbonization goals"*. This commitment positions them as a key partner for utilities, corporations, and
    communities striving to meet net-zero targets.
    """)

with st.expander("🌿 ESG and Sustainability Integration", expanded=True):
    st.markdown("""
    There is a formal and deepening commitment to **Environmental, Social, and Governance (ESG) principles**.
    This is evidenced by:
    * Engagement of an *"ESG advisory consultancy"* to conduct a *"materiality assessment"*.
    * Establishment of a *"Sustainability Committee"* with a defined roadmap.

    Identified material topics are comprehensive, including:
    * Supply Chain Management, Material Sourcing and Human Rights
    * Business Ethics
    * Community Engagement
    * Greenhouse Gas Emissions
    * Workforce Health & Safety
    * Ecological Impacts

    This structured approach to sustainability is becoming increasingly standard in the industry.
    """)

with st.expander("🤝 Community and Ethical Engagement", expanded=True):
    st.markdown("""
    A strong emphasis is placed on *"Collaborative Community Outcomes"* and upholding *"Rigorous Business Ethics"*.
    This includes:
    * A commitment to *"Responsible Sourcing,"* involving audits for forced labor in the supply chain.
    * Adherence to industry pledges like the **SEIA Solar Industry Forced Labor Prevention Pledge**.
    * Charitable donations exceeding **$500K**, illustrating their commitment to giving back.

    Such practices are vital for maintaining a positive reputation and ensuring long-term project viability.
    """)

with st.expander("⚙️ Operational Excellence", expanded=True):
    st.markdown("""
    A relentless pursuit of *"operational excellence"* is critical. This involves:
    * Leveraging technology, such as a *"state-of-the-art Remote Operations Center"*.
    * Exploring advanced methodologies like the application of *"AI and Data Science"* in Operations and Maintenance (O&M).

    The goal is to maximize asset performance, ensure reliability, and deliver value over the life of each project.
    """)

st.markdown("---")

# --- Subsection: Holistic Value and Strategic Orientation ---
st.subheader("💡 Strategic Orientation: Holistic Value and Long-Term Success")

columns = st.columns(2)
with columns[0]:
    st.success(f"""
    **Key Insight:** Long-term success in renewables isn't just about tech or assets. It's about:
    * Securing a "social license to operate."
    * Creating holistic value.
    """)
    st.markdown("""
    The pronounced emphasis on **ESG factors**, dedicated **community engagement efforts**, and **ethical supply chain management** are not merely corporate social responsibility initiatives; they are integral components of:
    * De-risking projects.
    * Attracting discerning institutional investors (e.g., partnership with Brookfield and Antin, who likely conduct extensive ESG due diligence).
    * Fostering sustainable growth.

    These elements are fundamental to achieving the *"project certainty"* that utility customers and financiers demand.
    """)

with columns[1]:
    st.warning(f"""
    **Operational Rigor Matters:**
    * Focus on operational excellence (advanced O&M) links to "bankability."
    * Maximizes "ROI on Solar and Storage Assets."
    """)
    st.markdown("""
    Furthermore, the focus on operational excellence, including advanced O&M capabilities, is directly linked to ensuring the *"bankability"*
    of projects and maximizing the *"ROI on Solar and Storage Assets"*. This operational rigor makes the company an attractive partner for
    developers looking to take projects to the next level and for utilities seeking reliable, long-term clean energy solutions.
    """)

st.markdown("---")
st.subheader("🌐 Evolving into a Decarbonization Platform")
st.markdown("""
The company's proactive exploration of **green hydrogen** also signals a strategic evolution, positioning Origis not just as a provider of renewable
electricity but as a comprehensive *"decarbonization solution platform"*. This broadening scope suggests emerging opportunities for
individuals interested in the systemic integration of new clean energy technologies.
""")


# --- Sidebar for navigation or extra info ---
st.sidebar.header("Focus Areas Discussed")

st.sidebar.info(f"Content current as of: {st.session_state.get('current_date', 'May 14, 2025')}")


# To run this app:
# 1. Save the code as a Python file (e.g., `renewable_landscape_app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: `streamlit run renewable_landscape_app.py`
#
# (If you are combining this with the previous script, ensure you manage how sections are displayed,
# perhaps using a selectbox in the sidebar to choose which section to view.)
