import streamlit as st
import extra_streamlit_components as stx # Ensure this is installed: pip install extra-streamlit-components
import datetime
import json # To handle serialization of progress data

# --- Entrypoint for Multipage App using st.navigation ---
# Global page configuration
st.set_page_config(layout="wide", page_title="Career Coach")

# --- Cookie Manager Setup ---
# Instantiate CookieManager directly, NOT inside a cached function
# Remove this:
# @st.cache_resource
# def get_cookie_manager():
#     return stx.CookieManager()
# cookie_manager = get_cookie_manager()

# Add this:
cookie_manager = stx.CookieManager()


# --- Load Progress from Cookie ---
# Function to load progress, handling potential errors or missing cookie
def load_progress_from_cookie(cookie_manager_instance, page_titles_list):
    # Pass the instantiated manager
    progress_json = cookie_manager_instance.get(cookie="page_progress")
    initial_progress = {}
    if progress_json:
        try:
            initial_progress = json.loads(progress_json)
            # Ensure it's a dictionary (basic validation)
            if not isinstance(initial_progress, dict):
                st.warning("Invalid progress data found in cookie. Resetting progress.")
                initial_progress = {}
        except json.JSONDecodeError:
            st.warning("Could not decode progress data from cookie. Resetting progress.")
            initial_progress = {} # Reset if JSON is corrupted

    # Ensure all current page titles exist in the loaded progress, default to False
    final_progress = {title: initial_progress.get(title, False) for title in page_titles_list}
    return final_progress

# --- Page Definitions ---
page_configs = [
    {"module": "0_Analysis.py",        "title": "Introduction"},
    {"module": "1.py",         "title": "Maximizing Your Profile "},
    {"module": "2.py",    "title": "NYC Energy & Finance Job Market"},
    {"module": "3.py",    "title": "Adjacent Career Pathways in NYC"},
    {"module": "4.py",    "title": "A Roadmap to Your Next Role"},
   
]


# Extract titles
page_titles = [cfg["title"] for cfg in page_configs]

# --- Initialize/Load progress into Session State ---
# Use session state to hold the progress *for the current run*, loading from cookie initially
if 'progress_status' not in st.session_state:
    # Pass the created cookie_manager instance here
    st.session_state['progress_status'] = load_progress_from_cookie(cookie_manager, page_titles)

# --- Build Page objects with dynamic labels (completed or not) ---
pages = []
for cfg in page_configs:
    title = cfg["title"]
    module = cfg["module"]
    # Read completion status from session state (which was loaded from cookie)
    is_complete = st.session_state['progress_status'].get(title, False)
    label = f"✅ {title}" if is_complete else title
    pages.append(st.Page(module, title=label))

# --- Render navigation menu ---
selected_page_object = st.navigation(pages, position="sidebar", expanded=True)

# --- Sidebar progress tracker ---
# Calculate progress based on session state
completed_count = sum(st.session_state['progress_status'].values())
st.sidebar.title("Progress")
st.sidebar.progress(completed_count / len(page_titles))
# Optional: display checkboxes showing completion status (disabled)
# st.sidebar.write("Completion Status:")
# for title in page_titles:
#     st.sidebar.checkbox(label=title, value=st.session_state['progress_status'].get(title, False), disabled=True)


# --- Get the original title using the index ---
try:
    selected_idx = pages.index(selected_page_object)
    selected_original_title = page_configs[selected_idx]["title"]
except ValueError:
    st.error("Could not identify the selected page. Please reload.")
    st.stop()

# --- Run the selected page script ---
selected_page_object.run()

# --- Mark-as-complete button logic ---
# Check completion status using session state
if not st.session_state['progress_status'].get(selected_original_title, False):
    if st.button("Mark this page as complete"):
        # 1. Update session state
        st.session_state['progress_status'][selected_original_title] = True

        # 2. Prepare data and save to cookie
        progress_to_save = json.dumps(st.session_state['progress_status'])
        # Set a long expiry date (e.g., 1 year)
        expires_at = datetime.datetime.now() + datetime.timedelta(days=365)
        # Use the cookie_manager instance directly
        cookie_manager.set("page_progress", progress_to_save, expires_at=expires_at)

        # 3. Rerun to update UI (sidebar label, progress bar)
        st.rerun()

# --- Optional: Add a way to clear progress ---
st.sidebar.divider()
if st.sidebar.button("Clear All Progress"):
    # Clear session state
    st.session_state['progress_status'] = {title: False for title in page_titles}
    # Delete the cookie
    cookie_manager.delete("page_progress")
    # Rerun to reflect changes
    st.rerun()