import streamlit as st

# --- HEADER ---
st.title("Your Actionable Transition Plan to a Sports Therapy Career in Claremore")
st.markdown(
    "This plan outlines a phased, project-based approach to guide your transition. Each project includes objectives, key activities, and estimated timelines."
)
st.markdown("---")

# --- PHASE 1 ---
st.header("Phase 1: Foundational Research & Decision-Making")
st.markdown("**Estimated Timeline: 1 Week**")

# --- Project 1.1 ---
st.subheader("Project 1.1: Deep Dive Verification & Pathway Clarification (AT Focus)")
st.markdown("---")

col1_1, col1_2 = st.columns((2, 1))

with col1_1:
    st.markdown(
        "**Objective:** Obtain definitive clarification from the Oklahoma State Board of Medical Licensure and Supervision (OSBMLS) regarding the Athletic Trainer (AT) apprentice and Physical Therapist (PT)-to-AT licensure pathways."
    )

    st.markdown("##### Key Activities:")
    activities_1_1_markdown = """
- **Locate Current OSBMLS Contact Information:**
    - Official Website: [Oklahoma State Board of Medical Licensure and Supervision](https://www.okmedicalboard.org/)
    - Licensure Contact: Phone: (405) 962-1400 (ask for Licensing Department); Email: licensing@okmedicalboard.org
    - Address: 101 NE 51st Street, Oklahoma City, OK 73105
- **Formulate Specific Written Questions:** Address the following to the OSBMLS:
    - The exact nature, requirements, and current availability of an AT *apprentice pathway* in Oklahoma.
    - The specific requirements and process for a licensed PT in Oklahoma to become a licensed AT (PT-to-AT pathway).
    - Details of any state-administered examination for these pathways (if they exist) versus the national Board of Certification (BOC) exam.
    - Whether successful completion of any alternative Oklahoma-specific examination (if applicable) confers eligibility to sit for the national BOC certification exam.
    - The practical marketability and employer acceptance in Oklahoma of an AT license obtained via these alternative pathways, especially if it does *not* include BOC certification.
- **Contact OSBMLS:**
    - Initiate contact preferably via email (licensing@okmedicalboard.org) to have a written record.
    - Follow up with phone calls if necessary.
- **Thoroughly Document:** Keep records of all communications (emails, call logs, names of individuals spoken to) and official responses.
"""
    st.markdown(activities_1_1_markdown)


with col1_2:
    st.markdown(
        """
    ##### Rationale:
    This step is of **paramount importance**. There is significant ambiguity regarding alternative AT licensure routes in Oklahoma and their alignment with the national standard of Board of Certification (BOC) certification.

    Current research indicates:
    - Standard AT Licensure in Oklahoma typically requires graduation from a CAATE-accredited master's program and passing the BOC exam. ([Source: OATA](https://www.oata.net/become-an-at))
    - The BOC is the recognized national certification for ATs. ([Source: BOCATC](https://bocatc.org/))

    Investing time and resources into a pathway that does not lead to a widely recognized and marketable credential (i.e., BOC certification) would be a critical misstep. This project directly addresses that risk. Clarification is essential before making a career path decision.
    """
    )
    st.info(
        "**Note:** While an 'Athletic Trainer Apprentice License Learning Course' is found online, its official standing and relation to OSBMLS recognized pathways needs direct verification from the OSBMLS."
    )


# --- Project 1.2 ---
st.subheader("Project 1.2: Career Path Finalization")
st.markdown("---")

col2_1, col2_2 = st.columns((2, 1))

with col2_1:
    st.markdown(
        "**Objective:** Make a definitive choice between the Athletic Trainer (AT) and Physical Therapist (PT) career paths based on comprehensive research and personal alignment."
    )

    st.markdown("##### Key Activities:")
    activities_1_2_markdown = """
- **Review Comparative Information:** Carefully analyze all gathered data, including:
    - **Educational Requirements:**
        - **AT:** Master's degree from a CAATE-accredited program required for BOC certification and Oklahoma licensure. ([See OK AT Programs](https://www.oata.net/become-an-at))
        - **PT:** Doctor of Physical Therapy (DPT) degree from a CAPTE-accredited program and passing the National Physical Therapy Exam (NPTE). ([See OK PT Info](https://www.occupationaltherapylicense.org/oklahoma-physical-therapy/))
    - **Scope of Practice in Oklahoma:**
        - **AT:** Works under physician direction; focuses on prevention, emergency care, clinical diagnosis, therapeutic intervention, and rehabilitation of injuries and medical conditions, typically for athletes and physically active individuals. ([See OK AT Scope Info](https://medicine.okstate.edu/athletic-training/profession.html), [OATA State Practice Act](https://www.oata.net/become-an-at))
        - **PT:** Broader scope treating diverse populations with injuries, illnesses, or conditions affecting mobility and function; can evaluate and treat for up to 30 days in Oklahoma without physician referral (with exceptions). ([See OK PT Practice Act Details](https://stoverpt.com/oklahoma-pt-practice-laws/))
    - **Work Environments:**
        - **AT:** High schools, colleges/universities, professional sports, sports medicine clinics, military, industrial settings. Often involves on-field presence.
        - **PT:** Hospitals, outpatient clinics, private practices, rehab centers, schools, home health, sports facilities. More commonly clinic-based.
    - **Work-Life Balance Considerations:**
        - **AT:** Can involve irregular hours, evenings, weekends, and travel, especially in sports settings. ([NATA Statement on Work-Life Balance](https://pmc.ncbi.nlm.nih.gov/articles/PMC6188079/))
        - **PT:** Can offer more regular hours in some settings, but demand can still be high. Setting boundaries is key. ([PT Work-Life Balance Tips](https://thejacksonclinics.com/maximizing-work-life-balance-in-physical-therapy/))
    - **Earning Potential in Oklahoma (Note: These are averages and can vary based on experience, setting, and location):**
        - **AT:** Average around \$50,000 - \$57,000/year. ([ZipRecruiter AT Salary OK](https://www.ziprecruiter.com/Salaries/Athletic-Trainer-Salary--in-Oklahoma))
        - **PT:** Average around \$79,000 - \$85,000+/year. ([CareerExplorer PT Salary OK](https://www.careerexplorer.com/careers/physical-therapist/salary/oklahoma/))
    - **General Career Comparison Resources:**
        - [AT vs PT - Ohio State](https://health.osu.edu/wellness/exercise-and-nutrition/athletic-trainers-vs-physical-therapists)
        - [AT vs PT - GCU](https://www.gcu.edu/blog/nursing-healthcare/athletic-trainer-vs-physical-therapist)
- **Critically Assess OSBMLS Findings (from Project 1.1):** How do the official responses about AT apprentice or PT-to-AT pathways impact the viability and attractiveness of the AT route for you?
- **Reflect on Personal Aspirations & Fit:**
    - Preferred work settings (e.g., dynamic team-based sports environment vs. diverse clinical setting).
    - Tolerance for irregular hours and travel.
    - Long-term income goals (the PT pathway generally shows a more direct route to the $80,000+ salary target in Oklahoma).
    - Passion for specific patient populations (e.g., athletes vs. general population).
"""
    st.markdown(activities_1_2_markdown)

with col2_2:
    st.markdown(
        """
    ##### Rationale:
    This decision is the **linchpin** for all subsequent educational and licensing efforts. A clear, well-informed choice allows for focused planning and resource allocation.

    Making a premature decision without full clarity on licensure (Project 1.1) or a thorough understanding of each profession's realities could lead to wasted effort or dissatisfaction.
    """
    )
    st.success(
        "**Goal:** Achieve a confident decision that aligns your career ambitions with a realistic and viable professional pathway in Claremore, Oklahoma."
    )

st.markdown("---")
st.caption(f"Information current as of May 15, 2025. Always verify details with official sources.")