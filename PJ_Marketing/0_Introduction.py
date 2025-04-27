import streamlit as st


# --- Main Title ---
# Using an emoji can add a bit of visual interest
st.title("🎯 Strategic Guide: Marketing Analytics Manager in Portland, OR")

# --- Introduction Section ---
# Using columns to potentially add an image or separate text blocks
col1, col2 = st.columns([2, 1]) # Make the text column wider

with col1:
    st.header("Your Roadmap to Success")
    st.markdown("""
    Welcome! This guide provides a comprehensive strategy tailored for professionals with **accounting and digital marketing backgrounds** aiming for **Marketing Analytics Manager** positions specifically within the **Portland, Oregon metropolitan area**.
    """)

    # Use an st.info, st.success or st.expander to highlight key takeaways
    st.info("""
    **What this guide covers:**
    * 🏙️ **Portland Job Market:** Analysis of local opportunities and employer expectations.
    * 🛠️ **Skill Alignment:** Assessing how your current skills match role requirements.
    * 🗺️ **Actionable Steps:** A clear plan for your job search and application process.
    """)

with col2:
    # Placeholder for a relevant image - uncomment and replace path if you have one
    # st.image("path/to/your/portland_or_analytics_image.jpg", caption="Data-driven insights for Portland")
    # Or use a simple visual element like a metric or focused text
    st.markdown("<br>", unsafe_allow_html=True) # Add some vertical space
    st.metric(label="Focus Area", value="Portland, OR", delta="Marketing Analytics")
    st.caption("📍 Targeting roles in the Portland metro area.")


# --- Divider ---
# Use st.divider() for a cleaner visual break
st.divider()

# --- Navigation Instruction ---
st.subheader("🧭 How to Use This Guide")
st.markdown("""
Use the **navigation panel on the left sidebar** to explore the different sections of this guide. Each section dives deeper into specific aspects of your career transition.
""")
st.caption("Select a topic from the sidebar to begin your journey!")

# --- Sidebar Content (Example) ---
# Add a header or some context to the sidebar itself
st.sidebar.header("Guide Navigation")
st.sidebar.markdown("Select a section below:")
# In a real multi-page app, you'd have st.page_link() here.
# For a single page, you might structure it differently or just leave this hint.
st.sidebar.info("Tailored for Accounting & Digital Marketing professionals.")