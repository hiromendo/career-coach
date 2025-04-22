import streamlit as st
import pandas as pd


# ─── Title & intro ─────────────────────────────────────────────────────────────
st.title("6. Your Action Plan: Securing Your Target Role (Example: IT Support Technician)")
st.markdown("""
This step-by-step plan outlines actions to take to secure an IT Support Technician role, integrating the support resources available.
""")

# ─── Phase duration metrics ──────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Phase 1", "1–3 weeks")
col2.metric("Phase 2", "Ongoing")
col3.metric("Phase 3", "Ongoing")
col4.metric("Phase 4", "Offer Stage")

# ─── Phase‑1 timeline chart ──────────────────────────────────────────────────────
st.subheader("📅 Phase 1 Timeline")
phase1_df = pd.DataFrame({
    "Week": list(range(1, 4)),
    "Progress": [1, 2, 3]
})
st.bar_chart(phase1_df.set_index("Week"))

# ─── Phase expanders ─────────────────────────────────────────────────────────────
with st.expander("Phase 1: Preparation (1–3 Weeks)", expanded=True):
    colA, colB = st.columns(2)
    with colA:
        st.markdown("""
1. **Resume Tailoring**  
   - Create an IT Support–focused resume  
   - Highlight A.A.S in Applied Computer Technology  
   - Detail R&D Technician equipment management  
   - Frame Amazon experience for problem‑solving  
   - Add “Technical Skills” section (Hardware, OS, Networking, Ticketing)
2. **Skill Validation**  
   - Review CompTIA A+ objectives  
   - Practice in online labs or sandboxes
3. **Target Company List**  
   - Search Indeed/LinkedIn/ZipRecruiter for “IT Support” in Beaverton, Hillsboro, Portland  
   - Consider local gov’t, schools, healthcare, tech firms  
   - Note staffing agencies [2, 9]
    """)
    with colB:
        st.markdown("""
4. **Engage Support Systems**  
   - Contact Oregon Vocational Rehabilitation [30, 31]  
   - Contact Bridges Oregon [25]  
   - Request orientation & intake  
   - State goal: IT Support Technician ($50k–60k+)  
   - Ask for resume review, interview prep, ASL accommodations
        """)
    st.markdown("[2]: https://example.com/agency-list • [9]: https://example.com/job-boards\n[25]: https://example.com/bridges • [30]: https://example.com/vr-info • [31]: https://example.com/vr-services")

with st.expander("Phase 2: Job Search & Networking (Ongoing)"):
    left, right = st.columns(2)
    with left:
        st.markdown("""
1. **Active Job Monitoring**  
   - Daily/weekly searches with location & salary filters  
   - Save searches & enable alerts
2. **Utilize VR/Bridges Network**  
   - Regular check‑ins with VR counselors & Bridges specialists  
   - Ask about direct employer relationships [25, 30]
        """)
    with right:
        st.markdown("""
3. **Informal Networking**  
   - Notify personal/professional contacts of focus  
   - Use LinkedIn to find connections at target firms  
   - Attend accessible virtual tech events (ask Bridges)  
        """)

with st.expander("Phase 3: Application & Interviewing (Ongoing)"):
    left, right = st.columns(2)
    with left:
        st.markdown("""
1. **Targeted Applications**  
   - Submit tailored resume + custom cover letter  
   - Highlight 1–2 key requirements per posting
2. **Track Applications**  
   - Maintain spreadsheet of apps, dates, status
3. **Interview Preparation**  
   - Prep STAR‑method answers for IT scenarios  
   - Practice common questions (boot/troubleshoot, customer care)
        """)
    with right:
        st.markdown("""
4. **Request Accommodations**  
   - Email scheduler ASAP requesting ASL interpreter  
   - Offer to coordinate via VR/Bridges [25, 30]
5. **Interview Execution**  
   - Demonstrate technical skills & problem‑solving  
   - Briefly explain preferred daily communication methods
        """)

with st.expander("Phase 4: Negotiation & Onboarding (Offer Stage)"):
    left, right = st.columns(2)
    with left:
        st.markdown("""
1. **Evaluate Offer**  
   - Compare salary & benefits vs. market ($40k–58k avg) [18]
2. **Salary Negotiation**  
   - If < $50k, reference market data & request adjustment  
   - Consult VR/Bridges for guidance
        """)
    with right:
        st.markdown("""
3. **Discuss Accommodations**  
   - Schedule HR meeting post‑acceptance  
   - Outline ASL interpreter needs, communication channels [30, 32]
4. **Onboarding**  
   - Engage in training  
   - Establish workflows with team & manager
        """)
    st.markdown("[18]: https://example.com/it-support-salary • [32]: https://example.com/accommodation-guidelines")

# ─── Footer note ────────────────────────────────────────────────────────────────
st.info("💡 Keep your tracker updated and lean on your support partners for every step!")
