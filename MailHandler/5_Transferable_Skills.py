# pages/3_🛠️_Skills_-_Mail_Handler_Role.py
import streamlit as st

# --- Header ---
st.title("🛠️ Your Practical Skills: From the Mail Handler Role")
st.markdown("""
Your Mail Handler experience provides a **strong foundation of practical skills**. Recognizing these is key to showcasing your value for new roles.
This page visually breaks down those core competencies.
""")
# Changed icon for better context
st.info("💡 **Connect the Dots:** Think about how *each* skill listed translates to requirements in Logistics, Operations, or Project Coordination jobs.", icon="🔗")

st.markdown("---") # Visual separator

# --- Skill Categories in Columns with Containers ---
st.header("Key Skill Areas Developed:")
col_logistics, col_tech, col_soft = st.columns(3)

# Column 1: Logistics & Operations Skills
with col_logistics:
    # Using st.container with border for a card-like effect
    with st.container(border=True):
        st.subheader("📦 Core Logistics & Ops")
        st.markdown("""
        * 📋 **Organization & Detail:** Accurate sorting/processing.
        * 🚚 **Distribution & Scheduling:** Understanding routing & timelines.
        * 📊 **Inventory Basics:** Managing supplies/postage.
        * 🗺️ **Logistics Coordination:** Efficient item movement foundation.
        * 🛡️ **Safety & Compliance:** Adhering to workplace standards.
        * 🏗️ **Equipment Handling:** Using pallet jacks/forklifts.
        """)

# Column 2: Technical & Administrative Skills
with col_tech:
    with st.container(border=True):
        st.subheader("💻 Technical & Admin")
        st.markdown("""
        * ⌨️ **Data Entry:** Accurate tracking & updating records.
        * 📄 **MS Office Suite:** Proficient in Outlook, Excel, Word.
        * ⚙️ **Specific Software:** Potential familiarity with Mail/Inventory systems.
        * 🗂️ **Record Keeping:** Systematic filing & info management.
        """)
        # Add padding if needed visually, e.g., st.markdown("<br>", unsafe_allow_html=True) if columns look uneven

# Column 3: Soft Skills & Attributes
with col_soft:
    with st.container(border=True):
        st.subheader("🤝 Soft Skills & Attributes")
        st.markdown("""
        * ⏱️ **Time Management:** Meeting deadlines consistently.
        * 🎯 **Attention to Detail:** High accuracy focus.
        * 👍 **Reliability:** Dependable & punctual performance.
        * 💡 **Problem-Solving:** Handling routine operational issues.
        * 🗣️ **Communication (Basic):** Effective team/supervisor interaction.
        """)

st.markdown("---") # Visual separator

# --- Concluding Takeaway ---
# Changed icon for emphasis
st.success(
    "✅ **Solid Foundation:** These skills show capability in execution, organization, time management, and reliability – valued across many professional roles.",
    icon="💪"
    )

st.caption("Next up: Complementary skills gained from your undergraduate degree.")