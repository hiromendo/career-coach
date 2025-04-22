import streamlit as st

# --- Entrypoint for Multipage App using st.navigation ---
# Global page configuration
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Page Definitions (no icons) ---
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

# Initialize completion flags
for title in page_titles:
    if title not in st.session_state:
        st.session_state[title] = False

# Build Page objects with dynamic labels (locked/unlocked & completed)
pages = []
for idx, cfg in enumerate(page_configs):
    title = cfg["title"]
    module = cfg["module"]
    # Locked if previous not completed
    if idx > 0 and not st.session_state[page_titles[idx-1]]:
        label = f"🔒 {title}"
    else:
        label = f"✅ {title}" if st.session_state[title] else title
    pages.append(st.Page(module, title=label))

# Render navigation menu
selected_page = st.navigation(pages, position="sidebar", expanded=True)

# Sidebar progress tracker
completed = sum(st.session_state[title] for title in page_titles)
st.sidebar.title("Progress")
st.sidebar.progress(completed / len(page_titles))
# for title in page_titles:
#     st.sidebar.checkbox(label=title, value=st.session_state[title], disabled=True)

# Determine index of the selected page
current_idx = next(i for i, p in enumerate(pages) if p.title == selected_page.title)

# Lock check
if current_idx > 0 and not st.session_state[page_titles[current_idx-1]]:
    st.error("🔒 This page is locked. Please complete the previous step to unlock.")
else:
    # Run the selected page script
    selected_page.run()
    # Mark-as-complete button
    if not st.session_state[page_titles[current_idx]]:
        if st.button("Mark this page as complete"):
            st.session_state[page_titles[current_idx]] = True
            st.rerun()
