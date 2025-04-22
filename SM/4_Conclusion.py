import streamlit as st
import pandas as pd

# ─── Title ───────────────────────────────────────────────────────────────────────
st.title("7. Conclusion")

# ─── Highlights ─────────────────────────────────────────────────────────────────
st.subheader("📌 Key Highlights")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
- **IT Support Technician**  
- **Junior Salesforce Administrator**  
- **Junior Data Analyst**  
""")
with col2:
    st.markdown("""
- **Salary Goal:** $50k–$60k+  
- **Location:** Beaverton area  
- **Unique Strengths:** AAS degree, Salesforce cert, ASL fluency  
""")

# ─── Support Resources Table ───────────────────────────────────────────────────
st.subheader("🔗 Support Resources")
resources = pd.DataFrame({
    "Resource": ["Vocational Rehabilitation (VR)", "Bridges Oregon"],
    "Action": ["Contact for job search & accommodations", "Engage for placement support"]
})
st.table(resources)

# ─── Full Narrative Expander ────────────────────────────────────────────────────
with st.expander("Read the full analysis and next steps"):
    st.markdown("""
The analysis indicates a strong potential for a successful career transition into a more engaging and rewarding role within the Beaverton, Oregon area. The combination of technical education (AAS degree, Salesforce certification), diverse work experience (R&D, Salesforce internship, Amazon operations), and unique skills (ASL fluency) provides a solid foundation for several viable career paths.

Specifically, roles such as **IT Support Technician**, **Junior Salesforce Administrator**, and **Junior Data Analyst** emerge as strong contenders that align well with the stated preferences for non-repetitive work, salary expectations ($50k–$60k or more), and local opportunities. Each path offers distinct advantages and considerations regarding direct experience match, salary potential, and necessary skill demonstration.

Crucially, Oregon provides dedicated resources through **Vocational Rehabilitation (VR)** and the specialized services of **Bridges Oregon** to support Deaf individuals in their job search, accommodation requests, and career development. Actively engaging with these resources, as outlined in the action plan, will significantly enhance the effectiveness of the job search process.

By leveraging the identified strengths, strategically targeting suitable roles, and utilizing the available support systems, there is high confidence in the ability to secure a fulfilling position that meets both professional aspirations and personal requirements. The next step is to initiate Phase 1 of the action plan, beginning with resume tailoring and outreach to VR and Bridges Oregon.
""")

# ─── Final Callout & Success ────────────────────────────────────────────────────
st.info("🚀 **Next step:** Kick off Phase 1—tailor your resume and reach out to VR & Bridges Oregon right away!")
st.success("End of Report Analysis.")
