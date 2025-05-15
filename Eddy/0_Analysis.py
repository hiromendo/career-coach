import streamlit as st


def main():
    """
    Main function to render the Streamlit application.
    """

    # --- Main Title ---
    st.title("Navigating a Career Transition to Sports Rehabilitation in Claremore, Oklahoma: An Actionable Guide")
    st.markdown("---") # Visual separator

    # --- Introduction ---
    st.markdown(
        """
        This report provides a comprehensive analysis for an individual currently employed as a Management Analyst
        in real estate, earning \$80,000 annually, who is seeking to transition to a sports therapy-related career
        in Claremore, Oklahoma, with a target income of at least \$80,000 per year. It outlines the necessary steps,
        educational pathways, licensure requirements, earning potential, and an actionable plan to facilitate
        this career change.
        """
    )
    st.markdown("---") # Visual separator

    # --- Section I: Understanding Your Goal ---
    st.header("I. Understanding Your Goal: Becoming a \"Sports Therapist\" in Claremore, Oklahoma")

    # --- Subsection A: Defining "Sports Therapist" ---
    st.subheader("A. Defining \"Sports Therapist\" in the U.S. and Oklahoma Context")
    st.markdown(
        """
        The term **"Sports Therapist"** does not represent a distinct, formally licensed profession within the
        United States, including the state of Oklahoma, in the same way it might be recognized in other
        countries, such as the United Kingdom or Abu Dhabi.

        In the U.S. context, individuals who work with athletes and active populations on the prevention,
        assessment, treatment, and rehabilitation of injuries are typically either:
        * **Athletic Trainers (ATs)**
        * **Physical Therapists (PTs)**

        Physical Therapists may further choose to specialize in sports. It is important to understand this
        distinction from the outset, as pursuing a non-existent or non-licensed "sports therapist"
        credential would not lead to a viable career path in Oklahoma.

        The focus of this report, therefore, will be on the established and licensed professions of
        **Athletic Training** and **Physical Therapy** with a sports emphasis.

        Some sources note that *"sports physical therapy, often known as sports therapy, is a type of
        physical treatment that focuses on sports teams and athletes"*. This underscores that the desired
        role likely falls under the umbrella of sports-focused physical therapy or athletic training.
        """
    )
    st.info(
        """
        **Key Takeaway:** The term "Sports Therapist" isn't a formal U.S. license.
        Focus on becoming an Athletic Trainer (AT) or a Physical Therapist (PT) with a sports specialization.
        """
    )
    st.markdown("---") # Visual separator

    # --- Subsection B: Introduction to ATs and PTs ---
    st.subheader("B. Introduction to Athletic Trainers (ATs) and Physical Therapists (PTs) with Sports Specialization")

    # Using columns for a more engaging layout
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Athletic Trainers (ATs)")
       
        st.markdown(
            """
            ATs are healthcare professionals who collaborate with physicians to provide:
            * Preventative services
            * Emergency care
            * Clinical diagnosis
            * Therapeutic intervention
            * Rehabilitation of injuries and medical conditions

            They often work directly with sports teams, in educational settings, or with other physically
            active populations, operating under the direction or supervision of a physician. Their scope
            includes providing immediate care of injuries, assessing and treating injuries, and implementing
            rehabilitation programs within a sport and exercise context.
            """
        )

    with col2:
        st.markdown("### Physical Therapists (PTs) with Sports Specialization")
       
        st.markdown(
            """
            PTs are movement experts who improve quality of life through:
            * Prescribed exercise
            * Hands-on care
            * Patient education

            They diagnose and treat individuals of all ages who have medical problems or other health-related
            conditions that limit their abilities to move and perform functional activities in their daily lives.
            PTs who specialize in sports apply their expertise to athletes and active individuals, focusing on
            areas such as:
            * Biomechanics
            * Exercise science
            * Development of sport-specific rehabilitation and performance enhancement programs.
            """
        )

    st.success(
        """
        **In Summary:**
        * **Athletic Trainers (ATs):** Focus on on-field/immediate care, prevention, and rehab, often embedded with teams.
        * **Physical Therapists (PTs) - Sports Specialization:** Broader scope, can diagnose and treat a wider range of movement issues, with a focus on sports-specific recovery and performance.
        """
    )
    st.markdown("---") # Visual separator

    # --- Subsection C: High-Level Comparison Table ---
    st.subheader("C. Table: High-Level Comparison: Athletic Trainer vs. Physical Therapist (Sports Focus) in Oklahoma")
    st.markdown(
        """
        To aid in the initial decision-making process, the following table provides a high-level comparison
        of these two professions in the Oklahoma context. This comparison highlights key differences in
        education, licensure, and typical practice, which are fundamental considerations for a career transition.
        """
    )

    # Using st.markdown for the table to allow for more control over cell content and formatting.
    # Markdown tables are rendered nicely by Streamlit.
    table_md = """
    | Feature                                 | Athletic Trainer (AT)                                                                 | Physical Therapist (PT) with Sports Specialization                                                              |
    |:----------------------------------------|:--------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
    | **Primary Role Focus** | Prevention, emergency care, diagnosis, intervention, rehabilitation for athletes/active individuals | Diagnosis & treatment of movement dysfunction, rehabilitation, performance enhancement for broad population, can specialize in sports |
    | **Entry-Level Education** | Master's Degree (from CAATE-accredited program)                                         | Doctor of Physical Therapy (DPT) Degree (from CAPTE-accredited program)                                           |
    | **Typical Program Length** | ~2 years post-baccalaureate                                                             | ~2.5-3 years post-baccalaureate                                                                                   |
    | **Licensure Body in OK** | Oklahoma State Board of Medical Licensure and Supervision (OSBMLS)                      | Oklahoma State Board of Medical Licensure and Supervision (OSBMLS)                                              |
    | **National Certification** | Board of Certification (BOC) - ATC® credential                                        | National Physical Therapy Exam (NPTE) for licensure; Optional: Sports Certified Specialist (SCS) via ABPTS          |
    | **Oklahoma Salary Outlook (Mean/Median)** | ~\$55,000 - \$76,000 (varies by source/location)                                          | ~\$94,000 - \$97,000 (mean range for all PTs)                                                                       |
    | **Work Environments** | Schools, colleges, pro sports, clinics, industrial settings                             | Hospitals, outpatient clinics (ortho/sports), private practice, home health, schools                              |
    """
    st.markdown(table_md, unsafe_allow_html=True) # unsafe_allow_html can be useful for complex markdown, but ensure content is safe.
                                                 # For simple tables like this, it might not be strictly necessary but doesn't hurt.
    st.markdown("---") # Visual separator


    # --- Sidebar Navigation ---
    # This section defines the navigation links in the sidebar.
    # The links use Markdown anchors to jump to the respective sections in the app.
   

if __name__ == "__main__":
    main()
