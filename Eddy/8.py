import streamlit as st

# --- Initialize Session State ---
# These flags will track whether each step's submit button has been clicked
if 'step1_submitted' not in st.session_state:
    st.session_state.step1_submitted = False
if 'step2_submitted' not in st.session_state:
    st.session_state.step2_submitted = False
if 'step3_submitted' not in st.session_state:
    st.session_state.step3_submitted = False
if 'step4_submitted' not in st.session_state:
    st.session_state.step4_submitted = False
if 'step5_submitted' not in st.session_state:
    st.session_state.step5_submitted = False

# Store the input values in session state as well
if 'current_tasks' not in st.session_state:
    st.session_state.current_tasks = ""
if 'common_problems' not in st.session_state:
    st.session_state.common_problems = ""
if 'inefficiency' not in st.session_state:
    st.session_state.inefficiency = ""
if 'current_workflow' not in st.session_state:
    st.session_state.current_workflow = ""
if 'proposed_solution' not in st.session_state:
    st.session_state.proposed_solution = ""
if 'proposed_workflow' not in st.session_state:
    st.session_state.proposed_workflow = ""


# --- App Title ---
st.title("🛠️ Operations Specialist Task #1")
st.markdown("""
Identify an operational inefficiency in your current role (e.g., Mail Handler)
and develop a simple improvement proposal. This exercise mirrors tasks often performed by
Operations Specialists and can help you build relevant skills and examples for job applications.
""")
st.markdown("---") # Separator

# --- Target Role Information (Sidebar) ---
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

# --- Step 1 ---
st.header("Step 1: Analyze Your Current Role (Mail Handler)")
# Use session state to keep input values across reruns
st.session_state.current_tasks = st.text_area(
    "Describe your main tasks and responsibilities as a Mail Handler:",
    value=st.session_state.current_tasks, # Set initial value from state
    height=100,
    placeholder="Example: Sorting incoming mail by department...",
    key="current_tasks_input" # Unique key
)
st.session_state.common_problems = st.text_area(
    "What are some common challenges, bottlenecks, or frustrations?",
    value=st.session_state.common_problems, # Set initial value from state
    height=100,
    placeholder="Example: Delays in sorting, difficulty tracking packages...",
    key="common_problems_input" # Unique key
)

# Submit button for Step 1
if st.button("Submit Step 1", key="submit_step1"):
    if st.session_state.current_tasks and st.session_state.common_problems:
        st.session_state.step1_submitted = True
    else:
        st.warning("Please fill in both fields for Step 1 before submitting.")


# --- Step 2 (Show only if Step 1 submitted) ---
if st.session_state.step1_submitted:
    st.markdown("---") # Separator
    st.header("Step 2: Identify a Specific Operational Inefficiency")
    st.markdown("""
    Based on the challenges you listed, pinpoint **one specific, manageable inefficiency**.
    """)
    st.session_state.inefficiency = st.text_input(
        "State the specific inefficiency you want to focus on:",
        value=st.session_state.inefficiency, # Set initial value from state
        placeholder="Example: Manual logging process for incoming tracked packages...",
        key="inefficiency_input" # Unique key
    )

    # Submit button for Step 2
    if st.button("Submit Step 2", key="submit_step2"):
        if st.session_state.inefficiency:
            st.session_state.step2_submitted = True
        else:
            st.warning("Please identify an inefficiency before submitting Step 2.")


# --- Step 3 (Show only if Step 2 submitted) ---
if st.session_state.step2_submitted:
    st.markdown("---") # Separator
    st.header("Step 3: Describe the Current Workflow")
    st.markdown(f"""
    Detail the exact steps involved in the **current process** related to: **'{st.session_state.inefficiency}'**.
    """)
    st.session_state.current_workflow = st.text_area(
        "Current Workflow Steps:",
        value=st.session_state.current_workflow, # Set initial value from state
        height=150,
        placeholder="Example:\n1. Receive tracked package...\n2. Manually find recipient...\n3. Write in logbook...",
        key="current_workflow_input" # Unique key
    )

    # Submit button for Step 3
    if st.button("Submit Step 3", key="submit_step3"):
        if st.session_state.current_workflow:
            st.session_state.step3_submitted = True
        else:
            st.warning("Please describe the current workflow before submitting Step 3.")


# --- Step 4 (Show only if Step 3 submitted) ---
if st.session_state.step3_submitted:
    st.markdown("---") # Separator
    st.header("Step 4: Propose an Improvement")
    st.markdown("""
    Brainstorm a simple, practical solution to address this inefficiency.
    """)
    st.session_state.proposed_solution = st.text_area(
        "Describe your proposed improvement:",
        value=st.session_state.proposed_solution, # Set initial value from state
        height=100,
        placeholder="Example: Implement a simple barcode scanning system...",
        key="proposed_solution_input" # Unique key
    )

    # Submit button for Step 4
    if st.button("Submit Step 4", key="submit_step4"):
        if st.session_state.proposed_solution:
            st.session_state.step4_submitted = True
        else:
            st.warning("Please propose an improvement before submitting Step 4.")


# --- Step 5 (Show only if Step 4 submitted) ---
if st.session_state.step4_submitted:
    st.markdown("---") # Separator
    st.header("Step 5: Describe the Proposed (Improved) Workflow")
    st.markdown(f"""
    Detail the steps involved in the **new, improved process**.
    """)
    st.session_state.proposed_workflow = st.text_area(
        "Proposed Workflow Steps:",
        value=st.session_state.proposed_workflow, # Set initial value from state
        height=150,
        placeholder="Example:\n1. Receive tracked package...\n2. Scan package barcode...\n3. Scan recipient barcode...",
        key="proposed_workflow_input" # Unique key
    )

    # Submit button for Step 5
    if st.button("Submit Step 5", key="submit_step5"):
        if st.session_state.proposed_workflow:
            st.session_state.step5_submitted = True
        else:
            st.warning("Please describe the proposed workflow before submitting Step 5.")


# --- Step 6 (Show only if Step 5 submitted) ---
if st.session_state.step5_submitted:
    st.markdown("---") # Separator
    st.header("Step 6: Review Your Improvement Proposal")
    st.markdown("---")

    st.subheader("Summary of Your Proposal")
    # Display the submitted values from session state
    st.markdown(f"**Identified Inefficiency:** {st.session_state.inefficiency}")
    st.markdown(f"**Proposed Solution:**")
    st.markdown(st.session_state.proposed_solution)

    col_summary1, col_summary2 = st.columns(2)
    with col_summary1:
        st.markdown("**Current Workflow (Description):**")
        st.markdown(st.session_state.current_workflow)
    with col_summary2:
        st.markdown("**Proposed Workflow (Description):**")
        st.markdown(st.session_state.proposed_workflow)

    st.markdown("---")
    st.subheader("Visual Workflow Comparison (Example)")
    st.markdown("This shows how the *example* package logging workflows might look as diagrams. Adapt these for your specific proposal.")

    # Define the Mermaid diagrams as strings (using the example)
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
        st.markdown("**Current Workflow Diagram (Example):**")
        st.markdown(current_workflow_diagram)
    with col_diag2:
        st.markdown("**Proposed Workflow Diagram (Example):**")
        st.markdown(proposed_workflow_diagram)


    st.markdown("---")
    st.subheader("Next Steps & Connecting to Operations Specialist Role")
    st.markdown("""
    * **Refine:** Review your descriptions. Are they clear, concise, and logical?
    * **Visualize:** Create your *own* specific diagrams based on your described workflows using tools like:
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

# Add a message if the process hasn't started or is incomplete
if not st.session_state.step1_submitted:
    st.info("Complete Step 1 and click 'Submit Step 1' to begin.")
elif not st.session_state.step5_submitted:
     st.info("Continue completing the steps above and clicking 'Submit' to see the final review.")


st.markdown("---")
st.markdown("End of Helper Tool")
