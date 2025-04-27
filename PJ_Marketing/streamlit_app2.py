import streamlit as st

# --- Entrypoint for Multipage App using st.navigation ---
# Global page configuration
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Page Definitions (no icons) ---
# Simplified page configurations - no need for completion tracking
page_configs = [
    {"module": "0_Introduction.py", "title": "Introduction"},
    {"module": "1_Understanding_the_Market.py", "title": "Understanding the market"},
    {"module": "2_Assessing_Your_Profile.py", "title": "Assessing Your Profile"},
    {"module": "3_Job_Search_Application.py", "title": "Job Search"},
    {"module": "4_Next_Steps_Resources.py", "title": "Next Steps & Resources"},
]

# Build Page objects directly using the title from config
pages = [
    st.Page(cfg["module"], title=cfg["title"]) for cfg in page_configs
]

# Render navigation menu
selected_page = st.navigation(pages, position="sidebar", expanded=True)

# --- Sidebar Content (Example) ---
# Add a header or some context to the sidebar itself
# st.sidebar.header("Guide Navigation")
# st.sidebar.markdown("Select a section below:")
# st.sidebar.info("Tailored for Accounting & Digital Marketing professionals.") # Kept from original

# Run the selected page script - no lock check needed
selected_page.run()

# No "Mark as complete" button or progress bar needed anymore