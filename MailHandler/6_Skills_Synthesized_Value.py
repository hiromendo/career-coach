# pages/4_💡_Skills_-_Synthesized_Value.py
import streamlit as st

# --- Header ---
st.title("💡 Your Synthesized Value Proposition")
st.markdown("Combining your practical experience with your academic skills creates a unique and compelling profile for potential employers. Understand how to leverage this blend.")

st.markdown("---") # Visual separator

# --- The Core Value ---
st.header("The Power of Your Unique Blend ➕")
# Using st.success to highlight the positive core message
st.success(f"""
**Your Key Advantage:** You combine **💪 Practical Know-How** (from mail handling: process execution, organization, detail) with **🧠 Intellectual Abilities** (from your degree: critical thinking, analysis, communication).

This blend makes you highly **🔄 Adaptable and Versatile**. You can grasp operational realities *and* analyze situations to improve them – a major asset for Coordinator and Specialist roles!
""", icon="⭐")

st.markdown("---") # Visual separator

# --- Strategic Positioning ---
st.header("Positioning Yourself for Success 🎯")
st.markdown("Beyond having the skills, *how* you present them and *where* you apply matters significantly:")

col_reframe, col_culture = st.columns(2)

with col_reframe:
    # Container for visual grouping
    with st.container(border=True):
        st.subheader("✨ Reframe Your Current Role")
        # Using st.info for actionable advice
        st.info("Shift the focus from the 'ease' of your current role to the **valuable professional qualities** demonstrated:", icon="🗣️")
        st.markdown("""
        **Highlight These Instead:**
        * **📈 Consistency:** Meeting processing targets reliably.
        * **✅ Accuracy:** Maintaining high standards in routine tasks.
        * **⏱️ Efficiency:** Managing time effectively.
        * **📜 Discipline:** Adhering strictly to procedures.

        ➡️ **Showcases:** Reliability, Efficiency, Discipline.
        """)

with col_culture:
    # Container for visual grouping
    with st.container(border=True):
        st.subheader("😊 Target the Right Culture")
        # Using st.warning as this addresses a pain point (dissatisfaction)
        st.warning("Your desire for appreciation means **proactive research** into company culture is essential:", icon="🔍")
        st.markdown("""
        **Action Steps:**
        * **Investigate:** Check company reviews, values, 'Best Places to Work' lists.
        * **Look For:** Signs of supportive management & genuine employee appreciation.
        * **Critical Goal:** Find an environment where you feel valued.
        """)


st.markdown("---") # Visual separator
st.caption("Understanding your synthesized value and these strategic points prepares you to effectively explore specific roles and tailor your applications.")