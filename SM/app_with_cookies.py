import streamlit as st
import os
import json
from streamlit_cookies_manager import EncryptedCookieManager

# Global page configuration (must be first Streamlit command)
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Entrypoint for Multipage App with Cookie-Persisted Progress ---
# Initialize cookie manager (use your own secret in production)
cookies = EncryptedCookieManager(
    prefix="career_coach/",
    password=os.environ.get("COOKIE_PASSWORD", "default_secret_password"),
)

# Wait until cookies are loaded before rendering content
if not cookies.ready():
    st.stop()

# --- Page Definitions ---
page_configs = [
    {"module": "0_Resume_Suggestions.py", "title": "Resume Suggestions"},
    {"module": "1_Career_Goal_Evaluation.py", "title": "Career Goal Evaluation"},
    {"module": "2_Refresh_Skills_Resources.py", "title": "Refresh Skills & Knowledge"},
    {"module": "3_Career_Paths.py", "title": "Visual Career Paths"},
    {"module": "4_Visual_Skills_Refresh.py", "title": "Visual Skills Refresh"},
    {"module": "5_Credentials_Pathway.py", "title": "Credentials Pathway"},
    {"module": "6_Gain_Experience.py", "title": "Gain Experience"},
]
page_titles = [cfg["title"] for cfg in page_configs]

# Load saved progress from cookie (if exists)
if cookies.get("progress_flags"):
    try:
        saved = json.loads(cookies.get("progress_flags") or "{}")
        for title in page_titles:
            if title in saved:
                st.session_state[title] = saved[title]
    except json.JSONDecodeError:
        pass

# Initialize completion flags in session state
for title in page_titles:
    if title not in st.session_state:
        st.session_state[title] = False

# Build dynamic pages with lock/completion indicators
pages = []
for idx, cfg in enumerate(page_configs):
    title = cfg["title"]
    module = cfg["module"]
    # lock if previous page not done
    if idx > 0 and not st.session_state[page_titles[idx-1]]:
        label = f"🔒 {title}"
    else:
        label = f"✅ {title}" if st.session_state[title] else title
    pages.append(st.Page(module, title=label))

# Render navigation sidebar with selected page
selected_page = st.navigation(pages, position="sidebar", expanded=True)

# Sidebar progress overview
total = len(page_titles)
completed = sum(st.session_state[title] for title in page_titles)
st.sidebar.title("Progress")
st.sidebar.progress(completed / total)
for title in page_titles:
    st.sidebar.checkbox(label=title, value=st.session_state[title], disabled=True)

# Determine index of current page
current_idx = next(i for i, p in enumerate(pages) if p.title == selected_page.title)

# Enforce sequential locking
if current_idx > 0 and not st.session_state[page_titles[current_idx-1]]:
    st.error("🔒 This page is locked. Complete the previous step to unlock.")
else:
    # Run the selected page
    selected_page.run()
    # Offer to mark as complete
    if not st.session_state[page_titles[current_idx]]:
        if st.button("Mark this page as complete"):
            st.session_state[page_titles[current_idx]] = True
            # Save updated flags to cookie
            cookies["progress_flags"] = json.dumps({t: st.session_state[t] for t in page_titles})
            cookies.save()
            st.rerun()
