# pages/3_📊_Potential_Career_Paths.py

import streamlit as st
import pandas as pd

# Page Title
st.title("📊 Potential Career Paths: Comparative Analysis")
st.markdown("This table provides a side-by-side comparison of the three recommended roles based on key criteria relevant to your career transition goals.")
st.markdown("---") # Visual separator

# --- Data Preparation ---
# Data extracted directly from the provided markdown table content
# Adding reference numbers back for clarity, as implied by the original text sections
data = {
    'Feature': [
        'Est. Atlanta Salary Range',
        'Ease of Transition',
        'Hybrid Schedule Option',
        '4x10 Schedule Option',
        'Key Skills Leveraged',
        'Key Skills to Develop'
    ],
    'Logistics Coordinator': [
        '\$40k - \$55k+ (Avg \$45k, 75th$50k)',
        'High (Direct skill overlap: logistics basics, organization)',
        'Common',
        'Less Common (Possible in shifts/ops)',
        'Organization, Detail, Time Mgmt, Logistics Basics, MS Office]',
        'Logistics Software (TMS/ERP), Advanced Excel, Negotiation (potential)'
    ],
    'Operations Specialist (Entry/Assoc.)': [
        '\$46k - \$78k+ (Avg \$60-65k, 25th \$46k)',
        'Medium (Leverages organization, process focus; requires more analysis)',
        'Very Common',
        'Less Common (Possible in shifts/ops)',
        'Analysis, Problem Solving, Organization, Communication, MS Excel',
        'Data Analysis Tools, Process Mapping, Industry Knowledge'
    ],
    'Project Coordinator (Entry Level)': [
        '\$45k - \$55k+ (Avg \$47k, 75th \$55k)',
        'Medium-High (Leverages organization, time mgmt, communication; less direct industry overlap)',
        'Common',
        'Less Common (Possible by company policy)',
        'Organization, Communication, Time Mgmt, Detail, MS Office',
        'Project Mgmt Software, Budgeting Basics, Formal PM Methodologies'
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Set the 'Feature' column as the DataFrame index for a cleaner row header display
df = df.set_index('Feature')

# --- Display the Table ---
st.subheader("Comparative Analysis Table")

# Use st.table() for a clean, static, nicely formatted table that fits the width
# It generally maintains font consistency with the rest of the Streamlit app
st.table(df)

st.markdown("---") # Visual separator

# Concluding text from the original content
st.caption("This table synthesizes key data points regarding salary, schedule likelihood, and skill alignment. Use it to evaluate these potential career paths against your personal criteria and priorities.")

# Optional link back to the detailed strategy
st.markdown("For more context on each role and the data references, please see **Section III** in the **📄 Detailed Strategy** page.")