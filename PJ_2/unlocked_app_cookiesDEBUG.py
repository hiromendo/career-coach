import streamlit as st
import extra_streamlit_components as stx
import datetime
import json
import traceback # To print detailed errors if JSON parsing fails

# --- Global Config ---
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Cookie Manager Setup ---
# Ensure manager is created on each run OUTSIDE any cache decorator
try:
    cookie_manager = stx.CookieManager()
    st.write("DEBUG: CookieManager initialized.") # DEBUG
except Exception as e:
    st.error(f"Failed to initialize CookieManager: {e}")
    st.stop() # Stop if manager fails

# --- Load Progress Function ---
def load_progress_from_cookie(cookie_manager_instance, page_titles_list):
    st.write("DEBUG: Attempting to load progress from cookie...") # DEBUG
    progress_data = {"loaded": False, "raw_value": None, "parsed_value": {}}

    try:
        # Use a default value of None to explicitly check if the cookie exists
        raw_cookie_value = cookie_manager_instance.get(cookie="page_progress")
        progress_data["raw_value"] = raw_cookie_value
        st.write(f"DEBUG: Raw cookie value retrieved: '{raw_cookie_value}' (Type: {type(raw_cookie_value)})") # DEBUG

        if raw_cookie_value is not None:
            try:
                # Attempt to parse the JSON
                initial_progress = json.loads(raw_cookie_value)
                if isinstance(initial_progress, dict):
                    progress_data["parsed_value"] = initial_progress
                    progress_data["loaded"] = True
                    st.write(f"DEBUG: Successfully parsed JSON: {initial_progress}") # DEBUG
                else:
                    st.warning("Invalid progress data structure in cookie (not a dict). Resetting.")
                    progress_data["parsed_value"] = {}
            except json.JSONDecodeError:
                st.warning("Could not decode progress data from cookie (invalid JSON). Resetting.")
                st.write("--- Traceback ---")
                st.error(traceback.format_exc()) # Show detailed error
                st.write("--- End Traceback ---")
                progress_data["parsed_value"] = {}
        else:
             st.write("DEBUG: 'page_progress' cookie not found.") # DEBUG
             progress_data["parsed_value"] = {}

    except Exception as e:
        st.error(f"An unexpected error occurred during cookie loading: {e}")
        st.error(traceback.format_exc())
        progress_data["parsed_value"] = {} # Default to empty on error

    # Ensure all current page titles exist, default to False
    final_progress = {title: progress_data["parsed_value"].get(title, False) for title in page_titles_list}
    st.write(f"DEBUG: Final progress being used: {final_progress}") # DEBUG
    return final_progress

# --- Page Definitions & Titles ---
page_configs = [
    {"module": "0_Resume_Suggestions.py", "title": "Resume Suggestions"},
    {"module": "1_Career_Explorations.py", "title": "Career Explorations"},
    {"module": "2_Career_Paths.py", "title": "CPA vs Non-CPA"},
    {"module": "5_Credentials_Pathway.py", "title": "Credentials Pathway"},
    {"module": "6_Visual_Skills_Refresh.py", "title": "Refreshing Your Skills & Knowledge"},
    {"module": "7_Gain_Experience.py", "title": "Gain Experience"},
]
page_titles = [cfg["title"] for cfg in page_configs]

# --- Initialize/Load progress into Session State ---
# Force reload from cookie on every run for debugging purposes initially
# (You might reinstate the 'if not in session_state' later for efficiency)
# if 'progress_status' not in st.session_state:
st.write("DEBUG: Forcing load from cookie into session state...") # DEBUG
st.session_state['progress_status'] = load_progress_from_cookie(cookie_manager, page_titles)
# else:
#     st.write("DEBUG: Session state 'progress_status' already exists.") # DEBUG

st.write(f"DEBUG: Current session state 'progress_status': {st.session_state['progress_status']}") # DEBUG

# --- Build Page objects ---
pages = []
for cfg in page_configs:
    title = cfg["title"]
    module = cfg["module"]
    is_complete = st.session_state['progress_status'].get(title, False)
    label = f"✅ {title}" if is_complete else title
    pages.append(st.Page(module, title=label))

# --- Render navigation menu ---
selected_page_object = st.navigation(pages, position="sidebar", expanded=True)

# --- Sidebar progress tracker ---
completed_count = sum(st.session_state['progress_status'].values())
st.sidebar.title("Progress")
st.sidebar.progress(completed_count / len(page_titles))


# --- Get the original title ---
try:
    selected_idx = pages.index(selected_page_object)
    selected_original_title = page_configs[selected_idx]["title"]
except ValueError:
    st.error("Could not identify the selected page. Please reload.")
    st.stop()

# --- Get the original title ---
try:
    selected_idx = pages.index(selected_page_object)
    selected_original_title = page_configs[selected_idx]["title"]
except ValueError:
    st.error("Could not identify the selected page. Please reload.")
    st.stop()

# --- Mark-as-complete button logic (MOVED BEFORE .run()) ---
st.write(f"DEBUG: Checking button state BEFORE running page {selected_original_title}") # DEBUG
button_pressed = False # Flag to track if button was pressed

# Check if the page is NOT already complete
if not st.session_state['progress_status'].get(selected_original_title, False):
    st.write(f"DEBUG: Displaying 'Mark as complete' button for {selected_original_title} (before page run)") # DEBUG

    # Check if the button is pressed
    if st.button("Mark this page as complete", key=f"complete_button_{selected_original_title}"):
        button_pressed = True # Set flag if button is clicked
        st.write(f"DEBUG: 'Mark complete' button clicked for {selected_original_title} (before page run)") # DEBUG

        # 1. Update session state
        st.session_state['progress_status'][selected_original_title] = True
        st.write(f"DEBUG: Session state updated: {st.session_state['progress_status']}") # DEBUG

        # 2. Prepare data and save to cookie
        try:
            progress_to_save = json.dumps(st.session_state['progress_status'])
            st.write(f"DEBUG: JSON prepared for cookie: {progress_to_save}") # DEBUG
            expires_at = datetime.datetime.now() + datetime.timedelta(days=365)
            st.write(f"DEBUG: Setting cookie 'page_progress' with expiry {expires_at}...") # DEBUG
            cookie_manager.set("page_progress", progress_to_save, expires_at=expires_at, key="set_cookie_on_complete")
            st.write("DEBUG: cookie_manager.set() called.") # DEBUG
            st.toast("Progress saved!", icon="🍪")
        except Exception as e:
            st.error(f"Error saving progress to cookie: {e}")
            st.error(traceback.format_exc())

        # 3. Rerun to update UI
        st.write("DEBUG: Rerunning app...") # DEBUG
        st.rerun() # Rerun immediately after processing click
    # This else corresponds to the inner "if st.button" - remove if too confusing
    # else:
    #     st.write(f"DEBUG: Button for {selected_original_title} was NOT clicked this run.") # DEBUG

# This else corresponds to the outer "if not st.session_state..."
else:
     st.write(f"DEBUG: Page {selected_original_title} already marked complete (before page run).") # DEBUG


# --- Run the selected page script ---
# Only run the page if the button wasn't just pressed (to avoid running page content uselessly before rerun)
if not button_pressed:
    st.write(f"DEBUG: Running page script: {selected_original_title}") # DEBUG
    selected_page_object.run()
else:
    st.write(f"DEBUG: Skipping page run for {selected_original_title} because 'Mark complete' button was just pressed.") # DEBUG


# --- Optional: Add a way to clear progress ---
# (Keep Clear button and Cookie Debug Info where they were, likely at the end or sidebar)
# ... (rest of your code: clear button, cookie debug info) ...

# --- Optional: Add a way to clear progress ---
st.sidebar.divider()
if st.sidebar.button("Clear All Progress"):
    st.write("DEBUG: 'Clear All Progress' button clicked.") # DEBUG
    # Clear session state
    st.session_state['progress_status'] = {title: False for title in page_titles}
    # Delete the cookie
    try:
        cookie_manager.delete("page_progress", key="delete_cookie_on_clear") # Added key
        st.write("DEBUG: cookie_manager.delete() called.") # DEBUG
        st.toast("Progress cleared!", icon="🗑️")
    except Exception as e:
         st.error(f"Error deleting cookie: {e}")
    # Rerun to reflect changes
    st.rerun()


# --- Add a section to view raw cookie value directly ---
st.sidebar.divider()
st.sidebar.subheader("Cookie Debug Info")
raw_val = cookie_manager.get("page_progress")
st.sidebar.text_area("Raw 'page_progress' Cookie Value", value=str(raw_val), height=100, disabled=True)