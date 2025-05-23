import streamlit as st
import pandas as pd # For the date in the sidebar

# --- Main Title for this project idea page ---
st.title("📊 Project Idea 3: Building a Pro-Forma Financial Model and Analyzing Key PPA Terms")
st.subheader("For a Utility-Scale Solar Project")
st.markdown("---")

# --- Rationale ---
st.subheader("🎯 Rationale")
st.markdown("""
This project directly addresses the need for:
* *"clean energy financial modeling experience,"*
* Supports understanding for *"PPA negotiations support"*
* And *"project finance negotiations support."*

Financial viability underpins all project development.
""")
st.success( # Using st.success to highlight the direct alignment with JD requirements
    "**Key Alignment:** Crucial for understanding project bankability and contractual frameworks."
)
st.markdown("---")

# --- Actionable Steps ---
st.subheader("🛠️ Actionable Steps")

st.markdown("""
1.  **Define Project Assumptions:**
    Establish basic parameters for a hypothetical utility-scale solar project.
    * *Example:* 50 MW capacity, specific location (e.g., West Texas), estimated annual generation (e.g., using NREL's PVWatts Calculator).
    * *Tip: Document all your assumptions clearly.*

2.  **Develop Pro-Forma Model Structure (in Excel or Google Sheets):**
    Create a simplified financial model structure including sections for:
    * **Inputs:**
        * Capital Expenditures (CAPEX): $/Watt (e.g., solar modules, inverters, racking, installation)
        * Operating Expenditures (OPEX): $/kW/year (e.g., maintenance, insurance, land lease)
        * PPA Price: $/MWh (fixed or with an escalator)
        * Debt/Equity Financing: Debt percentage, interest rate, loan term.
        * Tax Incentives: Investment Tax Credit (ITC) percentage, depreciation schedule (e.g., MACRS).
        * Degradation Rate: Annual % reduction in energy output.
    * **Calculations:**
        * Annual Energy Production (Year 1, accounting for degradation in subsequent years)
        * Annual Revenue (Energy Production * PPA Price)
        * Annual Operating Costs
        * Debt Service (Principal and Interest payments)
        * Pre-Tax Cash Flow
        * Taxes (considering tax incentives)
        * After-Tax Cash Flow
    * **Key Metrics (Outputs):**
        * Project Internal Rate of Return (Project IRR)
        * Equity Internal Rate of Return (Equity IRR)
        * Net Present Value (NPV)
        * Debt Service Coverage Ratio (DSCR)
    * *Resource: Look for basic project finance or renewable energy financial modeling tutorials online for structural guidance.*

3.  **Populate and Test Model:**
    Use publicly available industry data (e.g., NREL ATB, Lazard LCOE reports for cost estimates) or reasonable estimates for your inputs.
    * Ensure the model calculates basic financial returns and that formulas are working correctly.
    * *Perform sensitivity analysis on key inputs like PPA price or CAPEX if time permits.*

4.  **Research PPA Terms:**
    Find publicly available sample Power Purchase Agreements (PPAs) for utility-scale solar or summaries of common PPA terms.
    * *Resource: University research, law firm publications, or energy agency websites sometimes have sample documents or term sheets.*

5.  **Analyze Key PPA Clauses:**
    Identify and analyze 5-7 critical PPA clauses from your research. Examples include:
    * **Term:** Length of the contract (e.g., 15, 20, 25 years).
    * **Pricing:** Fixed price, fixed escalator (e.g., 2% per year), time-of-day (TOD) factors, or other structures.
    * **Performance Guarantees:** Minimum energy delivery, availability guarantees, and associated liquidated damages.
    * **Curtailment Provisions:** Who bears the risk and cost if the grid operator or offtaker curtails the project's output?
    * **Change of Law:** How are unforeseen changes in laws or regulations handled?
    * **Default and Termination:** Conditions leading to default and consequences of termination.
    * **Force Majeure:** What happens during unforeseeable events?
    * *Focus: Understand what the clause means and how it allocates risk between the project owner (seller) and the offtaker (buyer).*

6.  **Summarize Insights:**
    Prepare a brief summary of your financial model's key outputs under a base case scenario.
    * Include a short analysis of the selected PPA terms, focusing on the risk allocation implications for both the buyer and the seller.
    * This would be relevant for *"reviewing and providing inputs for financial models."*
    * *Structure: Model Overview (Assumptions, Key Outputs), PPA Clause Analysis (Key Terms & Risk Allocation), Conclusion.*
""")
st.markdown("---")

# --- Strategic Importance & Alignment ---
st.subheader("🌟 Value Proposition for Candidacy")
st.info( # Using st.info to emphasize the project's impact
    "**Demonstrates Financial Acumen:** This project showcases your ability to think about project economics and contractual frameworks, which are essential for a Project Development Manager."
)

st.markdown("""
Origis Energy's success relies on securing *"bankable projects"*, and understanding financial models and PPAs is fundamental to this.

By completing this project, you demonstrate:
* An understanding of the key drivers of solar project financial viability.
* The ability to analyze and interpret complex contractual terms.
* A practical approach to assessing project risk and return.
""")

# --- Sidebar for navigation or extra info ---
st.sidebar.header("Project Detail")
st.sidebar.markdown("This page details the **Financial Model & PPA Analysis** project idea for a PDM role.")
st.sidebar.markdown("---")
# Example link back if part of a multi-page app structure
# st.sidebar.page_link("your_main_app_file.py", label="Back to PDM Projects Overview", icon="↩️")
st.sidebar.success(f"Content current as of: {pd.Timestamp.now(tz='America/Los_Angeles').strftime('%B %d, %Y')}")

# To run this app:
# 1. Save the code as a Python file (e.g., `pdm_financial_model_app.py`).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: `streamlit run pdm_financial_model_app.py`
#
# For a multi-page app structure, you would typically save this in a 'pages'
# directory and Streamlit would handle the navigation.
