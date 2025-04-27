import streamlit as st

# --- Entrypoint for Multipage App using st.navigation ---
# Global page configuration
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Page Definitions ---
page_configs = [
    {"module": "0_Resume_Suggestions.py", "title": "Resume Suggestions"},
    {"module": "1_Career_Explorations.py", "title": "Career Explorations"},
    {"module": "2_Career_Paths.py", "title": "CPA vs Non-CPA"},
    {"module": "5_Credentials_Pathway.py", "title": "Credentials Pathway"},
    {"module": "6_Visual_Skills_Refresh.py", "title": "Refreshing Your Skills & Knowledge"},
    {"module": "7_Gain_Experience.py", "title": "Gain Experience"},
]

# Extract titles
page_titles = [cfg["title"] for cfg in page_configs]

# Initialize completion flags in session state if they don't exist
for title in page_titles:
    if title not in st.session_state:
        st.session_state[title] = False

# Build Page objects with dynamic labels (completed or not)
pages = []
for cfg in page_configs:
    title = cfg["title"]
    module = cfg["module"]
    # Determine label based only on completion status
    label = f"✅ {title}" if st.session_state[title] else title
    pages.append(st.Page(module, title=label)) # Use the dynamic label here

# Render navigation menu
# This returns the selected st.Page object from the 'pages' list
selected_page_object = st.navigation(pages, position="sidebar", expanded=True)

# Sidebar progress tracker
completed_count = sum(st.session_state[title] for title in page_titles)
st.sidebar.title("Progress")
st.sidebar.progress(completed_count / len(page_titles))
# Optional: display checkboxes showing completion status (disabled)
# st.sidebar.write("Completion Status:")
# for title in page_titles:
#     st.sidebar.checkbox(label=title, value=st.session_state[title], disabled=True)

# --- Get the original title using the index ---
try:
    # Find the index of the selected page object within the 'pages' list
    selected_idx = pages.index(selected_page_object)
    # Use this index to get the original title from the corresponding config
    selected_original_title = page_configs[selected_idx]["title"]
except ValueError:
    # This should theoretically not happen if st.navigation works correctly
    st.error("Could not identify the selected page. Please reload.")
    st.stop() # Stop script execution if we can't find the page

# --- No Lock Check Needed ---

# Run the selected page script
selected_page_object.run()

# Mark-as-complete button logic (use the original title found via index)
if not st.session_state[selected_original_title]:
    if st.button("Mark this page as complete"):
        st.session_state[selected_original_title] = True
        st.rerun() # Rerun to update the sidebar labels and progress bar