import streamlit as st


def main():
    """
    Main function to render the Streamlit application page for the PT Pathway.
    """

    # --- Main Header for this Page/Section ---
    st.header("Becoming a Licensed Physical Therapist (PT) with Sports Specialization")
    st.markdown("---") # Visual separator

    # --- A. Scope of Practice and Typical Work Environments for PTs in Sports ---
    st.subheader("A. Scope of Practice and Typical Work Environments for PTs in Sports")
    st.markdown(
        """
        Physical Therapists are healthcare professionals who diagnose and treat individuals with conditions
        that limit their ability to move and perform functional activities. PTs specializing in sports apply
        these principles to athletes and physically active individuals, focusing on areas such as:
        * Biomechanical analysis
        * Sport-specific injury rehabilitation
        * Performance enhancement strategies
        * Injury prevention programs

        Their work environments include outpatient orthopedic and sports medicine clinics, hospitals,
        rehabilitation centers, and direct work with sports teams or athletic organizations.
        """
    )
    st.info(
        """
        **Example:** PT Central, an Oklahoma-based practice, exemplifies services offered by sports-focused
        PTs, including pre-participation screenings, various re-education exercise programs, taping and
        bracing, and development of ergonomic and training regimens.
        """
    )
    st.markdown(
        """
        The general scope of physical therapy in Oklahoma includes patient evaluations, therapeutic exercises,
        activities of daily living training, and the use of physical agents.
        """
    )
    st.markdown("---")

    # --- B. Educational Requirements: The Doctor of Physical Therapy (DPT) Degree ---
    st.subheader("B. Educational Requirements: The Doctor of Physical Therapy (DPT) Degree (CAPTE Accreditation)")
    st.markdown(
        """
        The entry-level degree required to become a Physical Therapist is the **Doctor of Physical Therapy (DPT)**.
        This degree must be obtained from a program accredited by the Commission on Accreditation in Physical
        Therapy Education (CAPTE). Admission to a DPT program typically requires a bachelor's degree and
        the completion of specific prerequisite coursework.
        """
    )

    st.markdown("#### Accredited DPT programs in Oklahoma include:")

    # Table: Accredited Doctor of Physical Therapy Programs in Oklahoma
    dpt_programs_table_md = """
    | University Name                               | Program Name                     | Location(s)         | Program Length (Typical) | Key Admission Prerequisites (Examples)                                                                | Application Process (Typical) | CAPTE Accreditation |
    |:----------------------------------------------|:---------------------------------|:--------------------|:-------------------------|:------------------------------------------------------------------------------------------------------|:------------------------------|:--------------------|
    | University of Oklahoma Health Sciences Center (OUHSC) | Doctor of Physical Therapy (DPT) | Oklahoma City & Tulsa | 3 years (108 credit hours) | Bachelor's degree, Min. 2.75 cumulative & science GPA, Prerequisite courses (Psych, Chem, Anatomy, Physio, Bio, Physics, Stats) | PTCAS                         | Accredited          |
    | Oklahoma City University (OCU)                | Doctor of Physical Therapy (DPT) | Oklahoma City       | 2.5 years                | Bachelor's degree, Min. 3.0 GPA, Prerequisite courses                                                 | PTCAS (likely)                | Accredited          |
    | Langston University                           | Doctor of Physical Therapy (DPT) | Langston            | 3 years                  | Bachelor's degree, Min. 3.0 GPA, Prerequisite courses                                                 | PTCAS (likely)                | Accredited          |
    """
    st.markdown(dpt_programs_table_md)
    st.warning(
        """
        **Note:** Program details, especially prerequisites and deadlines, can change.
        It is **essential** to consult the official program websites and PTCAS for the most current information.
        """
    )
    st.markdown(
        """
        Hybrid DPT programs, combining online coursework with on-campus immersions, are also an option
        for students in Oklahoma.
        """
    )
    st.markdown("---")

    # --- C. Oklahoma Licensure Process for PTs ---
    st.subheader("C. Oklahoma Licensure Process for PTs")
    st.markdown(
        """
        Physical Therapists in Oklahoma are licensed by the **Oklahoma State Board of Medical Licensure
        and Supervision (OSBMLS)**, with advisement from the Physical Therapy Committee. The primary
        requirements for licensure are:
        * Graduation from a CAPTE-accredited DPT program.
        * Successful passage of the National Physical Therapy Exam (NPTE), which is administered by the
            Federation of State Boards of Physical Therapy (FSBPT).
        * Submission of a complete application to the OSBMLS, typically through their online portal,
            along with the required fees (an application fee of \$150 was noted).
        * Completion of a biometric criminal background check.
        """
    )
    st.info(
        """
        PT licenses in Oklahoma generally require renewal annually by January 31st or February 1st,
        often in even-numbered years. To maintain licensure, PTs must complete **40 hours of approved
        continuing education (CEUs)** every two years.
        """
    )
    st.markdown("---")

    # --- D. Achieving Sports Specialization (e.g., Sports Certified Specialist - SCS) ---
    st.subheader("D. Achieving Sports Specialization (e.g., Sports Certified Specialist - SCS)")
    st.markdown(
        """
        After obtaining a DPT degree and initial licensure, Physical Therapists can pursue board
        certification as a **Sports Certified Specialist (SCS)**. This advanced credential is awarded by
        the American Board of Physical Therapy Specialties (ABPTS) and signifies a high level of clinical
        knowledge, skill, and experience in sports physical therapy. Earning the SCS can enhance a PT's
        credibility, potentially increase patient referrals, and may lead to greater earning power.
        """
    )
    
    st.markdown(
        """
        The general requirements for SCS certification include:
        * A current, unrestricted license to practice physical therapy.
        * A minimum of 2,000 hours of direct patient care in sports physical therapy within the last 10 years,
            with 500 of those hours occurring in the last 3 years, **OR** successful completion of an
            APTA-credentialed sports residency program.
        * Current CPR certification.
        * Successful passage of the SCS certification examination.
        """
    )
    st.markdown(
        """
        The SCS certification is valid for 10 years and requires a Maintenance of Specialty Certification (MOSC)
        process for renewal. This process involves ongoing professional development, continued clinical practice
        in sports, submission of a case reflection portfolio, and passing a non-proctored recertification
        examination in the tenth year.
        """
    )
    st.success(
        """
        **Other Valuable Certifications:**
        * **Certified Strength and Conditioning Specialist (CSCS)** by NSCA: Demonstrates expertise in strength
            training and conditioning programs. Requires a Bachelor’s degree and CPR/AED.
        * **Orthopedic Certified Specialist (OCS)** by ABPTS: Beneficial for PTs working with musculoskeletal
            and sports-related injuries.
        """
    )
    st.markdown(
        """
        Pursuing specialization like the SCS is a significant commitment beyond the DPT and initial licensure,
        involving focused clinical hours and additional examination. However, for those aiming to be
        recognized experts in "sports therapy," such credentials are key differentiators.
        """
    )
    st.markdown("---")

    # --- E. Time Commitment and Financial Investment ---
    st.subheader("E. Time Commitment and Financial Investment")
    st.markdown(
        """
        DPT programs typically span **2.5 to 3 years** of full-time, post-baccalaureate study.
        If prerequisite courses are needed, this could extend the timeline by 1-2 years.
        Achieving SCS certification requires an additional **2,000 hours** of specialized sports PT experience
        (roughly equivalent to one year of full-time work) post-licensure before exam eligibility.
        """
    )
    st.warning(
        """
        **Financial Investment Considerations:**
        * **DPT Program Tuition:** Can be substantial. Verify current rates with OUHSC, OCU, and Langston University.
        * Fees, books, and living expenses.
        * **NPTE & Licensure Fees:** Application fee for OSBMLS was noted as $150.
        * **Specialty Certification Exam Fees:**
            * SCS: \$535-\$635 (APTA members), \$880-\$980 (non-members).
            * CSCS: \$340 (NSCA members), \$475 (non-members).
        * Potential for significant student loan debt.
        * Lost income from current \$80,000/year position during studies.
        """
    )
    st.markdown("---")

    # --- F. Earning Potential for PTs (Sports Focus) in Oklahoma and the Claremore/Tulsa Area ---
    st.subheader("F. Earning Potential for PTs (Sports Focus) in Oklahoma and the Claremore/Tulsa Area")
    st.markdown(
        """
        The earning potential for Physical Therapists in Oklahoma appears to align well with the \$80,000+ salary target.
        * **BLS Data (May 2023):** National median annual salary for PTs was **\$99,710**. Top 10% > $130,870.
        * **Oklahoma State-Level Data:** Annual mean salary range for PTs in Oklahoma: **\$94,130 – \$96,760**.
        * **Specialty Data (General):** "Sports PT" at \$75,000, "Orthopedics PT" at \$82,000 (note: "Sports PT"
            figure seems low compared to overall median). Home healthcare highest at \$107,870 nationally.
        * **Salary.com (May 2025 estimates for OK):** Average for "Sports Physical Therapist" in Oklahoma: \$66,517
            (range \$60,296 - \$71,559). This is notably lower than BLS data.
        * **Local Job Postings (Tulsa):** Select Physical Therapy (outpatient ortho/sports) listed **\$75,000 - \$90,000/year**,
            pending experience.

        Considering the BLS data for Oklahoma PTs showing mean salaries well above \$90,000, and specific job
        postings like the one in Tulsa offering up to \$90,000 for roles involving sports medicine patients,
        the PT pathway offers a strong likelihood of meeting or exceeding the \$80,000 income target,
        particularly with experience and potential specialization.
        """
    )

    st.markdown("#### Table: Estimated Salary Ranges for Physical Therapists (Sports Focus) in Oklahoma/Claremore Area")
    salary_table_md = """
    | Data Source          | Geographic Area   | Role/Setting (if specified)             | Salary Information                     |
    |:---------------------|:------------------|:----------------------------------------|:---------------------------------------|
    | BLS (May 2023)       | National          | All PTs                                 | Median: \$99,710                        |
    | BLS (State Data)     | Oklahoma          | All PTs                                 | Mean Range: \$94,130 - \$96,760          |
    | Job Posting (2025)   | Tulsa             | Outpatient Ortho/Sports PT              | \$75,000 - \$90,000 (pending experience) |
    | Salary.com (2025)    | Oklahoma          | Sports Physical Therapist (specific title)| Average: \$66,517                       |
    """
    st.markdown(salary_table_md)
    st.markdown("---")

    # --- G. Job Outlook and Opportunities in/near Claremore ---
    st.subheader("G. Job Outlook and Opportunities in/near Claremore")
    st.markdown(
        """
        Nationally, employment for Physical Therapists is projected to grow **much faster than the average**
        for all occupations (typically cited around 15-17% over a decade by the BLS). There are also reports
        of staffing shortages in outpatient physical therapy practices, indicating demand.
        """
    )
  
    st.markdown(
        """
        Local job opportunities in and around Claremore include:
        * **PT Solutions:** Advertised for outpatient PT in Claremore (sports medicine included). Locations in Pryor, Owasso.
        * **Select Physical Therapy (Tulsa):** Outpatient clinic seeing sports medicine patients.
        * **Ascension St. John:** Outpatient PT positions in Tulsa, Broken Arrow. Claremore hospital exists.
        * **Hillcrest Hospital Claremore:** Offers physical therapy and sports rehabilitation. Hillcrest Tulsa has PT openings.
        * **Excel Therapy:** Therapist-owned company with Oklahoma locations.
        * **Travel PT Agencies (e.g., AMN Healthcare):** List opportunities in Tulsa (ortho/sports common).

        These listings indicate a market for Physical Therapists with skills applicable to sports
        rehabilitation in the Claremore and greater Tulsa region.
        """
    )
    st.markdown("---")


    # --- Sidebar Navigation for this Page ---
   

if __name__ == "__main__":
    main()
