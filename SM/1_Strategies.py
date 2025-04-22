import streamlit as st
import pandas as pd

# Title
st.title("🌟 Navigating the Job Market: Accessibility & Success")

# Intro
st.markdown("""
Leverage your unique strengths and Oregon’s support systems to thrive in your job search.
""")

# Key Strengths & Communication Styles
st.header("1️⃣ Leverage Your Strengths")
col1, col2, col3 = st.columns(3)
col1.metric("ASL Fluency", "Native-level")
col1.write("Cultural competency & clear visual communication.")
col2.metric("Written Focus", "High")
col2.write("Ideal for roles heavy in documentation & reporting.")
col3.metric("Remote Flexibility", "Available")
col3.write("Controlled environment for effective communication.")

# Suitable Environments
st.header("2️⃣ Identify Ideal Roles & Environments")
df_roles = pd.DataFrame([
    {"Role Category": "Data Analysis & BI", "Comm Style": "Written/Visual", "Example Tools": "Power BI, Tableau"},
    {"Role Category": "IT Support", "Comm Style": "Ticketing/Email", "Example Tools": "Zendesk, Jira"},
    {"Role Category": "Salesforce Admin", "Comm Style": "Config & Docs", "Example Tools": "Salesforce Flow"},
    {"Role Category": "Business Analysis", "Comm Style": "Reports/Presentations", "Example Tools": "Excel, Confluence"}
])
st.dataframe(df_roles)

# Oregon Resources
st.header("3️⃣ Oregon-Specific Resources")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Vocational Rehabilitation (VR)")
    st.metric("Services Offered", "Counseling, Training, Assistive Tech")
    st.metric("Timeline", "60+ days intake")
    st.markdown("- Intake & eligibility\n- Individualized Plan for Employment\n- 90-day follow-up")
with col2:
    st.subheader("Bridges Oregon")
    st.metric("Focus", "Deaf & Hard of Hearing")
    st.metric("Services", "Job Coaching, Interpreters")
    st.markdown("- Culturally responsive support\n- Communication access services\n- Self-advocacy training")

# Accommodations
st.header("4️⃣ Reasonable Accommodations")
df_acc = pd.DataFrame([
    {"Accommodation": "ASL Interpreter", "Use Case": "Interviews, Meetings"},
    {"Accommodation": "CART Services", "Use Case": "Live Captioning"},
    {"Accommodation": "Visual Alerts", "Use Case": "Auditory Signals"},
    {"Accommodation": "Assistive Devices", "Use Case": "Workstation Setup"}
])
st.dataframe(df_acc)

# Inclusive Employers Tips
st.header("5️⃣ Targeting Inclusive Employers")
c1, c2 = st.columns([2, 1])
with c1:
    st.write("**Look for DEI & Accessibility Statements** on company websites and job postings.")
    st.write("**Examples of Inclusive Practices:** Interpreters provided, remote work policies, clear documentation processes.")
with c2:
    st.metric("Example Organizations", "PRIDE Industries, Apple, PPS")

st.markdown("""
---
💡 **Tip:** Document your accommodation plan early and share it when you receive an offer to negotiate smoothly.
""")
