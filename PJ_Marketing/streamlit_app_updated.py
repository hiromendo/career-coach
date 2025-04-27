import streamlit as st
import os
import json


# --- Global Page Configuration (MUST be the first Streamlit command) ---
# Ensure absolutely no st. calls happen before this line.
st.set_page_config(
    layout="wide",
    page_title="PJ Marketing Guide"
)
from streamlit_cookies_manager import EncryptedCookieManager
# --- Initialize Cookie Manager ---
# Use a password from environment variables or a default for development
# IMPORTANT: Set a strong secret password in your production environment!
cookies = EncryptedCookieManager(
    prefix="pj_marketing_guide/",
    password=os.environ.get("COOKIE_PASSWORD", "default_secret_password_change_me"),
)

# Initialize save flag in session state if it doesn't exist
if 'cookie_save_needed' not in st.session_state:
    st.session_state.cookie_save_needed = False

# Wait until cookies are ready before proceeding
if not cookies.ready():
    st.stop() # Stop execution until cookies are available

# --- Page Definitions ---
page_configs = [
    {"module": "0_Introduction.py", "title": "Introduction"},
    {"module": "1_Understanding_the_Market.py", "title": "Understanding the market"},
    {"module": "2_Assessing_Your_Profile.py", "title": "Assessing Your Profile"},
    {"module": "3_Job_Search_Application.py", "title": "Job Search"},
    {"module": "4_Next_Steps_Resources.py", "title": "Next Steps & Resources"},
]

# Extract titles
page_titles = [cfg["title"] for cfg in page_configs]

# --- Load Progress from Cookie ---
# Load saved completion flags from cookie (if exists)
if cookies.get("progress_flags"):
    try:
        saved_progress = json.loads(cookies.get("progress_flags") or "{}")
        for title in page_titles:
            if title in saved_progress:
                st.session_state[title] = saved_progress[title]
    except json.JSONDecodeError:
        # If cookie data is corrupted, start fresh
        st.session_state.clear() # Clear potentially bad state
        for title in page_titles:
             st.session_state[title] = False
        pass # Ignore error and use default False values

# Initialize completion flags in session state if not loaded from cookie
for title in page_titles:
    if title not in st.session_state:
        st.session_state[title] = False

# --- Build Pages with Dynamic Labels ---
pages = []
for idx, cfg in enumerate(page_configs):
    title = cfg["title"]
    module = cfg["module"]
    # Locked if previous not completed
    is_locked = idx > 0 and not st.session_state[page_titles[idx-1]]
    is_complete = st.session_state[title]

    if is_locked:
        label = f"🔒 {title}"
    elif is_complete:
        label = f"✅ {title}"
    else:
        label = title
    pages.append(st.Page(module, title=label, default=(idx == 0))) # Set first page as default

# --- Render Navigation and Get Selected Page ---
# Try to load the last viewed page from cookies
last_viewed_page_title = cookies.get("current_page_title")
initial_page_index = 0
if last_viewed_page_title:
    try:
        # Find the index corresponding to the last viewed title
        initial_page_index = next(i for i, p in enumerate(pages) if p.title.strip("🔒 ✅ ") == last_viewed_page_title)
        # Ensure the page isn't locked
        if initial_page_index > 0 and not st.session_state[page_titles[initial_page_index-1]]:
            initial_page_index = 0 # Fallback to first page if locked
    except StopIteration:
        initial_page_index = 0 # Fallback if title not found

selected_page = st.navigation(pages, position="sidebar")

# --- Sidebar Progress Tracker ---
completed = sum(st.session_state[title] for title in page_titles)
total_pages = len(page_titles)
st.sidebar.title("Progress")
st.sidebar.progress(completed / total_pages if total_pages > 0 else 0)
# Optionally display completion status checkboxes (disabled)
# for title in page_titles:
#     st.sidebar.checkbox(label=title, value=st.session_state[title], disabled=True)

# --- Determine Current Page Index and Check Lock ---
# Extract the base title (without icons) for logic checks
current_base_title = selected_page.title.strip("🔒 ✅ ")
try:
    current_idx = page_titles.index(current_base_title)
except ValueError:
    # Should not happen if titles match config, but handle defensively
    st.error("Error determining current page index.")
    st.stop()

# Save the current page title to the cookie
# This tracks the *last selected* page by the user
cookies["current_page_title"] = current_base_title

# --- Page Execution and Completion Logic ---
page_rerun_needed = False
if current_idx > 0 and not st.session_state.get(page_titles[current_idx-1], False):
    st.error("🔒 This page is locked. Please complete the previous step to unlock.")
else:
    # Run the selected page script
    selected_page.run()

    # Mark-as-complete button logic
    if not st.session_state.get(current_base_title, False):
        if st.button("Mark this page as complete"):
            st.session_state[current_base_title] = True
            # Prepare progress flags to save
            progress_to_save = {t: st.session_state.get(t, False) for t in page_titles}
            cookies["progress_flags"] = json.dumps(progress_to_save)

            # *** Set the flag to trigger save later ***
            st.session_state.cookie_save_needed = True
            # *** Do NOT call cookies.save() here ***

            # Signal that a rerun is needed after the save
            page_rerun_needed = True

    elif current_idx < total_pages -1: # If page is complete and not the last one
         st.success("Page marked as complete. Proceed to the next page when ready.")
    else: # If last page is complete
         st.success("Congratulations! You have completed all sections.")


# --- Perform Cookie Save Conditionally (Near End of Script) ---
if st.session_state.cookie_save_needed:
    try:
        cookies.save()
        # Reset the flag only after successful save
        st.session_state.cookie_save_needed = False
    except Exception as e:
        # Handle potential errors during save if necessary
        st.error(f"Error saving cookies: {e}")
        # Decide if you want to keep the flag True to retry or reset it
        # st.session_state.cookie_save_needed = False

# --- Perform Rerun if Needed (AFTER potential save) ---
if page_rerun_needed:
    st.rerun()