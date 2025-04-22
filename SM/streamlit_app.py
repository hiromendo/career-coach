import streamlit as st
import extra_streamlit_components as stx

# --- Page Config & Cookie Manager Init ---
st.set_page_config(layout="wide", page_title="Re‑Entering Accounting Guide")
cookie_manager = stx.CookieManager()

# --- Define your pages ---
page_configs = [
    {"module": "0_Home.py",               "title": "Home"},
    {"module": "0_Job_Market_Analysis.py", "title": "Job Market Analysis"},
    {"module": "1_Strategies.py",         "title": "Strategies"},
    {"module": "2_Recommendations.py",    "title": "Recommendations"},
    {"module": "3_ActionPlan.py",         "title": "Action Plan"},
    {"module": "4_Conclusion.py",         "title": "Conclusion"},
    {"module": "5_VocationalJobs.py",     "title": "Other Jobs"},
]
page_titles = [cfg["title"] for cfg in page_configs]

# --- Hydrate session_state from cookies or initialize flags ---
for title in page_titles:
    if cookie_manager.get(title) == "true":
        st.session_state[title] = True
    elif title not in st.session_state:
        st.session_state[title] = False

# --- Determine current navigation index ---
if "nav_index" not in st.session_state:
    st.session_state.nav_index = next((i for i, t in enumerate(page_titles) if not st.session_state[t]), 0)

# --- Build Page objects with dynamic labels and default selection marker ---
pages = []
for idx, cfg in enumerate(page_configs):
    title = cfg["title"]
    # locked if previous not completed
    if idx > 0 and not st.session_state[page_titles[idx-1]]:
        label = f"🔒 {title}"
    else:
        label = f"✅ {title}" if st.session_state[title] else title
    # mark default page so navigation highlights correctly
    default = (idx == st.session_state.nav_index)
    pages.append(st.Page(cfg["module"], title=label, default=default))

# --- Render navigation menu ---
selected_page = st.navigation(pages, position="sidebar")

# --- Sync nav_index if user manually selected a page ---
current_idx = next(i for i, p in enumerate(pages) if p.title == selected_page.title)
if st.session_state.nav_index != current_idx:
    st.session_state.nav_index = current_idx

# --- Sidebar progress tracker ---
completed = sum(st.session_state[t] for t in page_titles)
st.sidebar.title("Progress")
st.sidebar.progress(completed / len(page_titles))

# --- Lock check before running page ---
if current_idx > 0 and not st.session_state[page_titles[current_idx-1]]:
    st.error("🔒 This page is locked. Please complete the previous step to unlock.")
    st.stop()

# --- Run the selected page script ---
selected_page.run()

# --- Mark-as-complete logic with cookie persistence and auto-advance ---
flag = page_titles[current_idx]
if not st.session_state[flag]:
    if st.button("Mark this page as complete"):
        # 1) set in-memory
        st.session_state[flag] = True
        # 2) persist cookie
        cookie_manager.set(
            cookie=flag,
            val="true",
            max_age=30 * 24 * 60 * 60,
        )
        # 3) advance nav_index
        next_idx = current_idx + 1 if current_idx + 1 < len(pages) else current_idx
        st.session_state.nav_index = next_idx
        # 4) rerun to reflect changes
        st.rerun()


# import streamlit as st
# import extra_streamlit_components as stx

# # --- Page Config & Cookie Manager Init ---
# st.set_page_config(layout="wide", page_title="Re‑Entering Accounting Guide")
# # on top of your script
# cookie_manager = stx.CookieManager()


# # --- Define your pages ---
# page_configs = [
#     {"module": "0_Home.py",              "title": "Home"},
#     {"module": "0_Job_Market_Analysis.py","title": "Job Market Analysis"},
#     {"module": "1_Strategies.py",        "title": "Strategies"},
#     {"module": "2_Recommendations.py",   "title": "Recommendations"},
#     {"module": "3_ActionPlan.py",        "title": "Action Plan"},
#     {"module": "4_Conclusion.py",        "title": "Conclusion"},
#     {"module": "5_VocationalJobs.py",    "title": "Other Jobs"},
# ]

# # Extract titles
# page_titles = [cfg["title"] for cfg in page_configs]

# # Initialize completion flags
# for title in page_titles:
#     if title not in st.session_state:
#         st.session_state[title] = False

# # Build Page objects with dynamic labels (locked/unlocked & completed)
# pages = []
# for idx, cfg in enumerate(page_configs):
#     title = cfg["title"]
#     module = cfg["module"]
#     # Locked if previous not completed
#     if idx > 0 and not st.session_state[page_titles[idx-1]]:
#         label = f"🔒 {title}"
#     else:
#         label = f"✅ {title}" if st.session_state[title] else title
#     pages.append(st.Page(module, title=label))

# # Render navigation menu
# selected_page = st.navigation(pages, position="sidebar", expanded=True)

# # Sidebar progress tracker
# completed = sum(st.session_state[title] for title in page_titles)
# st.sidebar.title("Progress")
# st.sidebar.progress(completed / len(page_titles))
# # for title in page_titles:
# #     st.sidebar.checkbox(label=title, value=st.session_state[title], disabled=True)

# # Determine index of the selected page
# current_idx = next(i for i, p in enumerate(pages) if p.title == selected_page.title)

# # Lock check
# if current_idx > 0 and not st.session_state[page_titles[current_idx-1]]:
#     st.error("🔒 This page is locked. Please complete the previous step to unlock.")
# else:
#     # Run the selected page script
#     selected_page.run()
#     # Mark-as-complete button
#     if not st.session_state[page_titles[current_idx]]:
#         if st.button("Mark this page as complete"):
#             st.session_state[page_titles[current_idx]] = True
#             st.rerun()
