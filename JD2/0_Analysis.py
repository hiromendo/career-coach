import streamlit as st



# Custom CSS for styling (optional, for more card-like appearance if border=True isn't enough)
# You can inject custom CSS for more refined card styling, but st.container(border=True) offers a good start.
# st.markdown("""
# <style>
#     .card {
#         border: 1px solid #e6e6e6;
#         border-radius: 0.5rem;
#         padding: 1.5rem;
#         margin-bottom: 2rem;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         background-color: #f9f9f9;
#     }
#     .card-header {
#         font-size: 1.5rem;
#         font-weight: bold;
#         margin-bottom: 1rem;
#         color: #2c3e50;
#     }
#     .card-content p {
#         line-height: 1.6;
#         color: #34495e;
#     }
# </style>
# """, unsafe_allow_html=True)

# Main Title of the Page
st.title("Navigating Your Next Chapter: A Strategic Blueprint for Re-entry into NYC's Energy Finance Landscape")
st.markdown("---")

# --- Introduction Section ---
st.header("I. Introduction: Charting Your Course Back to a High-Impact Career")

with st.container(border=True):
    # st.markdown("<div class='card-header'>Charting Your Course</div>", unsafe_allow_html=True) # Uncomment if using custom CSS
    # st.subheader("Charting Your Course") # Alternative to custom CSS header
    st.markdown(
        """
        <div class='card-content'>
        <p>This report is designed to provide a comprehensive and actionable strategy for navigating a return to the New York City job market, particularly focusing on high-impact roles within the finance sector that align with a distinguished background in energy sector equity long/short analysis. The experience gained at premier institutions such as <strong>Millennium, Citadel, and Morgan Stanley</strong>, combined with a strong academic foundation in <strong>Physics from MIT</strong>, forms a powerful platform for future success.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with st.container(border=True):
    # st.markdown("<div class='card-header'>Transition and Opportunity</div>", unsafe_allow_html=True) # Uncomment if using custom CSS
    st.subheader("Transition and Opportunity in an Evolving Market")
    st.markdown(
        """
        <div class='card-content'>
        <p>The past two years of unemployment represent a significant transition. This period, however, also coincides with a dynamic evolution within the energy and finance sectors. The financial landscape, especially concerning energy, has seen a marked shift, with an increasing emphasis on <strong>energy transition, sustainability, and renewable resources</strong>.<sup>1</sup></p>
        <p>This evolving market presents not merely a challenge for re-entry but a <strong>unique opportunity</strong> to strategically reposition and leverage accumulated expertise in burgeoning, high-demand areas.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with st.container(border=True):
    # st.markdown("<div class='card-header'>Report Scope & Objectives</div>", unsafe_allow_html=True) # Uncomment if using custom CSS
    st.subheader("Report Scope & Strategic Objectives")
    st.markdown(
        """
        <div class='card-content'>
        <p>This report will delve into the following key areas to facilitate a successful re-entry:</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Using columns for a more structured "card" layout for these points
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("<h5>Optimizing Your Professional Profile</h5>", unsafe_allow_html=True)
            # st.write("Strategies to refine and enhance your professional narrative and materials.")
    with col2:
        with st.container(border=True):
            st.markdown("<h5>Understanding Current NYC Job Market Dynamics</h5>", unsafe_allow_html=True)
            # st.write("Insights into traditional finance roles and the expanding energy transition space.")

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.markdown("<h5>Identifying Specific Adjacent Job Roles</h5>", unsafe_allow_html=True)
            # st.write("Pinpointing roles that offer a strong fit for your expertise.")
    with col4:
        with st.container(border=True):
            st.markdown("<h5>Outlining a Concrete Action Plan</h5>", unsafe_allow_html=True)
            # st.write("A step-by-step guide to secure a high-impact position.")

    st.markdown(
        """
        <div class='card-content'>
        <br>
        <p>The ultimate objective is to transform the career break into a narrative of <strong>strategic adaptation and forward-looking engagement</strong> with these new market realities.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("<sup>1</sup> Placeholder for citation if available in the full report.")

# To run this Streamlit page:
# 1. Save the code as a Python file (e.g., `app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: `streamlit run app.py`