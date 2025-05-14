import streamlit as st


# --- App Title ---
st.title("🛠️ Operational Specialist Task #1")
st.markdown("""
Identify an operational inefficiency in your current role (e.g., Mail Handler)
and develop a simple improvement proposal. This exercise mirrors tasks often performed by
Operations Specialists and can help you build relevant skills and examples for job applications.
""")

# --- Target Role Information ---
st.sidebar.header("🎯 Target Role: Operations Specialist")
with st.sidebar.expander("View Operations Specialist Job Description", expanded=False):
    st.markdown("""
    **Operations Specialist Job Description (Example)**

    The Operations Specialist will provide administrative support to senior-level management responsible for the overall management and performance of communities within the designated portfolio. The Operations Specialist will perform tasks in various areas to include administrative support, research, analysis, marketing, and financials.

    **Essential Duties & Responsibilities**
    * Provide ongoing support to assigned senior-level managers.
    * Collect and review historical income and expense information of apartment buildings.
    * Interface with clients to facilitate understanding of property performance and unique characteristics of assets.
    * Gather and analyze market information to include market trends and rent comparables through both internal and third-party reports.
    * Lead and manage various internal projects.
    * Preparation of materials as necessary.
    * Prepare and ensure accurate and timely weekly/monthly/quarterly property reporting.
    * Answer and direct resident calls at the Corporate Level.
    * Coordinate travel, hotel, and rental car arrangements, as needed.
    * Other duties as assigned.

    **Travel Requirement:** This position may entail travel, estimated at 10% of work time annually for property visits or internal meetings.

    **Education & Experience**
    * Bachelor's degree in quantitative majors such as finance, real estate, or economics a plus.
    * Strong Proficiency in Microsoft Office Suite (Outlook, Word, Excel, PowerPoint).
    * Experience and/or knowledge in Property Management Software, such as MRI or One-Site a plus.
    * Problem solving, decision making, and analytical skills required.
    * Meticulous attention to detail.
    * Must be able to work with multiple deadlines and tasks while maintaining efficiency and control over projects assigned.
    """)
st.sidebar.info("Notice the emphasis on **analysis, problem-solving, reporting, and supporting management**.")

# --- Main Application Flow ---

st.header("Step 1: Analyze Your Current Role (Mail Handler)")
current_tasks = st.text_area(
    "Describe your main tasks and responsibilities as a Mail Handler:",
    height=150,
    placeholder="Example: Sorting incoming mail by department, operating postage machines, delivering packages internally, logging tracked mail, preparing outgoing shipments..."
)
common_problems = st.text_area(
    "What are some common challenges, bottlenecks, or frustrations you encounter in your daily work?",
    height=150,
    placeholder="Example: Delays in sorting specific mail types, difficulty tracking packages, inefficient routes for internal delivery, manual logging takes too long, frequent errors in addressing..."
)

st.header("Step 2: Identify a Specific Operational Inefficiency")
st.markdown("""
Based on the challenges you listed, pinpoint **one specific, manageable inefficiency** you could potentially improve. Think about processes that cause delays, errors, waste resources, or frustrate people.
""")
inefficiency = st.text_input(
    "State the specific inefficiency you want to focus on:",
    placeholder="Example: Manual logging process for incoming tracked packages is time-consuming and prone to errors."
)

# Initialize workflow variables to prevent errors if inefficiency is not yet entered
current_workflow = ""
proposed_solution = ""
proposed_workflow = ""

if inefficiency: # Only proceed if an inefficiency has been identified
    st.header("Step 3: Describe the Current Workflow")
    st.markdown(f"""
    Detail the exact steps involved in the **current process** related to the inefficiency you identified: **'{inefficiency}'**. Be specific.
    """)
    current_workflow = st.text_area(
        "Current Workflow Steps:",
        height=200,
        placeholder="Example:\n1. Receive tracked package from carrier.\n2. Manually find the recipient's name/department in a physical logbook or spreadsheet.\n3. Write down the tracking number, sender, recipient, date, and time in the logbook.\n4. Place package on the sorting shelf for delivery.\n5. If errors occur (e.g., illegible handwriting), time is spent correcting the log."
    )

    st.header("Step 4: Propose an Improvement")
    st.markdown("""
    Brainstorm a simple, practical solution to address this inefficiency. How could the process be changed to make it faster, more accurate, or less resource-intensive? Think about small changes, not necessarily huge system overhauls.
    """)
    proposed_solution = st.text_area(
        "Describe your proposed improvement:",
        height=150,
        placeholder="Example: Implement a simple barcode scanning system using a dedicated scanner or even a smartphone app. Scan the package tracking barcode, scan a pre-printed barcode for the recipient's department/location, automatically timestamping the entry in a digital log (e.g., a shared spreadsheet or simple database)."
    )

    st.header("Step 5: Describe the Proposed (Improved) Workflow")
    st.markdown(f"""
    Detail the steps involved in the **new, improved process** using your proposed solution.
    """)
    proposed_workflow = st.text_area(
        "Proposed Workflow Steps:",
        height=200,
        placeholder="Example:\n1. Receive tracked package from carrier.\n2. Scan the package's tracking barcode using the scanner/app.\n3. Scan the recipient's department/location barcode.\n4. The system automatically records tracking number, recipient location, date, and time in a digital log.\n5. Place package on the sorting shelf for delivery.\n6. Digital log allows for easy searching and reduces manual entry errors."
    )

st.header("Step 6: Review Your Improvement Proposal")
st.markdown("---")

if inefficiency and current_workflow and proposed_solution and proposed_workflow:
    st.subheader("Summary of Your Proposal")
    st.markdown(f"**Identified Inefficiency:** {inefficiency}")
    st.markdown(f"**Proposed Solution:**")
    st.markdown(proposed_solution) # Use markdown to preserve formatting if user used lists

    col_summary1, col_summary2 = st.columns(2)
    with col_summary1:
        st.markdown("**Current Workflow (Description):**")
        st.markdown(current_workflow) # Use markdown to preserve formatting
    with col_summary2:
        st.markdown("**Proposed Workflow (Description):**")
        st.markdown(proposed_workflow) # Use markdown to preserve formatting

    st.markdown("---")
    st.subheader("Visual Workflow Comparison (Example)")
    st.markdown("This shows how your described workflows might look as diagrams.")

    # Define the Mermaid diagrams as strings
    current_workflow_diagram = """
    ```mermaid
    graph TD
        A[Start: Package Received] --> B{Find Recipient Info};
        B --> C[Manual Entry: Write Tracking #, Sender, Recipient, Date/Time in Logbook];
        C --> D{Error Check};
        D -- Error Found --> E[Correct Logbook Entry];
        D -- No Error --> F[Place Package on Sorting Shelf];
        E --> F;
        F --> G[End: Package Logged & Sorted];

        style A fill:#f9f,stroke:#333,stroke-width:2px
        style G fill:#f9f,stroke:#333,stroke-width:2px
        style B fill:#ccf,stroke:#333,stroke-width:1px
        style C fill:#ccf,stroke:#333,stroke-width:1px
        style E fill:#ccf,stroke:#333,stroke-width:1px
        style F fill:#ccf,stroke:#333,stroke-width:1px
        style D fill:#fcf,stroke:#333,stroke-width:1px
    ```
    """

    proposed_workflow_diagram = """
    ```mermaid
    graph TD
        A[Start: Package Received] --> B[Scan Package Tracking Barcode];
        B --> C[Scan Recipient Department/Location Barcode];
        C --> D[System Auto-Logs: Tracking #, Location, Date/Time];
        D --> E[Place Package on Sorting Shelf];
        E --> F[End: Package Logged & Sorted];

        style A fill:#f9f,stroke:#333,stroke-width:2px
        style F fill:#f9f,stroke:#333,stroke-width:2px
        style B fill:#bbf,stroke:#333,stroke-width:1px
        style C fill:#bbf,stroke:#333,stroke-width:1px
        style D fill:#bbf,stroke:#333,stroke-width:1px
        style E fill:#bbf,stroke:#333,stroke-width:1px
    ```
    """

    col_diag1, col_diag2 = st.columns(2)
    with col_diag1:
        st.markdown("**Current Workflow Diagram:**")
        # Render the Mermaid diagram using st.markdown
        st.markdown(current_workflow_diagram)
    with col_diag2:
        st.markdown("**Proposed Workflow Diagram:**")
        # Render the Mermaid diagram using st.markdown
        st.markdown(proposed_workflow_diagram)


    st.markdown("---")
    st.subheader("Next Steps & Connecting to Operations Specialist Role")
    st.markdown("""
    * **Refine:** Review your descriptions and the diagrams. Are they clear, concise, and logical?
    * **Visualize:** You've now seen an example visualization! You can create your own specific diagrams using tools like:
        * Microsoft PowerPoint (SmartArt)
        * [draw.io](https://app.diagrams.net/) (Free online tool)
        * Lucidchart
        A visual representation is a powerful way to communicate your idea.
    * **Quantify (Optional):** Can you estimate the potential benefits? (e.g., time saved per package, reduction in errors). Even rough estimates add value.
    * **Connect the Skills:** This exercise directly demonstrates skills relevant to the Operations Specialist role:
        * **Analysis:** You analyzed your current process to find a problem.
        * **Problem Solving:** You identified an inefficiency and proposed a solution.
        * **Process Improvement:** You outlined and visualized a better workflow.
        * **Communication:** You articulated the problem and solution.
        * **Attention to Detail:** Describing and diagramming the workflow steps requires careful thought.

    Save this proposal! It's a great example to discuss in interviews or potentially even suggest (appropriately) within your current workplace. It shows initiative and analytical thinking.
    """)
else:
    st.info("Complete steps 1-5 above to generate your improvement proposal summary and see the example diagrams.")


st.markdown("---")
st.markdown("End of Helper Tool")
