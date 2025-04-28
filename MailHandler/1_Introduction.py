# 1_🚀_Introduction.py
import streamlit as st

# --- Header ---
st.title("🚀 Your Career Transition Starting Point")
st.markdown("Understanding where you are now helps map the journey ahead. This page summarizes your current situation and transition goals based on the initial report.")

# --- Optional Header Image ---
# Using a generic image URL representing pathways/decisions.
# Replace with a more specific, properly licensed image if you have one.
try:
    # Example image URL from Unsplash (check license/terms if using specific images)
    st.image(
        "https://images.unsplash.com/photo-1542332213-9b5a5a3fad35?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
        caption="Defining the path forward from your current position.",
        use_container_width=True
        )
except Exception as e:
    st.warning(f"Note: Could not load header image. {e}", icon="🖼️")

st.markdown("---") # Visual separator

# --- Section 1: Current Snapshot ---
st.header("📌 Current Snapshot")
col_profile, col_stats = st.columns([2, 1]) # Give profile column more space

with col_profile:
    st.subheader("Your Profile")
    st.markdown(f"""
    * 👤 **Who:** 26-year-old Mail Handler
    * 📍 **Where:** Near Conley, Georgia
    * 🏢 **Status:** Employed Full-time
    * 🎓 **Education:** Undergraduate Degree
    """)

with col_stats:
    st.subheader("Key Numbers")
    st.metric(label="Approx. Annual Salary", value="$50,000")
    # You can add more metrics here if relevant (e.g., years in role)

st.markdown("---") # Visual separator

# --- Section 2: Motivation & Values ---
st.header("🧭 Motivation & Values")
col_why, col_what_works = st.columns(2)

with col_why:
    st.subheader("Why Seek Change?")
    # Using st.warning to indicate points of dissatisfaction
    st.warning("""
    Primary drivers for seeking a new opportunity:
    * Concerns regarding **Management Practices**.
    * A desire for greater **Employee Appreciation**.
    """, icon="👎")

with col_what_works:
    st.subheader("What's Valued Now?")
    # Using st.success for positive aspects to retain or acknowledge
    st.success("""
    Aspects of the current role that are appreciated:
    * Relative **Ease** of the work.
    * Provision of **Paid Time Off (PTO)**.
    """, icon="👍")

st.markdown("---") # Visual separator

# --- Section 3: Transition Objectives ---
st.header("🎯 Transition Objectives")
st.info("These are the clear goals for your next career move:", icon="✅")

col_env, col_comp, col_path = st.columns(3)

with col_env:
    st.subheader("Work Environment")
    st.markdown("- Improved Management")
    st.markdown("- Feeling Valued & Appreciated")

with col_comp:
    st.subheader("Pay & Schedule")
    st.metric(label="Target Salary", value="$50,000 +")
    st.markdown("**Desired Flexibility (Either/Or):**")
    st.markdown("  - 🗓️ Compressed Week (4x10)")
    st.markdown("  - 🏠 Hybrid Arrangement")


with col_path:
    st.subheader("The Transition Itself")
    st.markdown("- Path should be relatively **straightforward**.")
    st.markdown("- Leverage existing background and qualifications effectively.")

st.markdown("---")
st.caption("With this clear picture, you can now explore the detailed strategy, journey map, and potential career paths using the sidebar navigation.")