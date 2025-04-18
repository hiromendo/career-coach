# Create this file inside the 'pages' subdirectory
import streamlit as st
from streamlit_react_flow import streamlit_react_flow

# Optional: Set page config for this specific page if needed
# st.set_page_config(page_title="Flowchart View", layout="wide")

st.title("📊 Step-by-Step Plan Flowchart")
st.markdown("This chart visualizes the general sequence of steps for returning to accounting, based on Section 1 of the Detailed Guide.")

# Define the elements for the flowchart (nodes and edges)
# Positions are approximate and might need slight adjustments for perfect alignment
elements = [
    # Nodes
    {"id": "1", "data": {"label": "START:\nDecide to Re-Enter Accounting"},
        "position": {"x": 250, "y": 0},
        "type": "input",
        "style": {"background": '#aaffaa', "width": 170}}, # Greenish background for start
    {"id": "2", "data": {"label": "1. Evaluate Career Goals\n(CPA vs. Non-CPA)"},
        "position": {"x": 250, "y": 120},
        "style": {"width": 170}},
    {"id": "3", "data": {"label": "2. Refresh Knowledge & Skills\n(Principles, Tech, CPE)"},
        "position": {"x": 250, "y": 240},
        "style": {"width": 170}},
    {"id": "4", "data": {"label": "3. Address Education /\nCredential Gaps"},
        "position": {"x": 250, "y": 360},
        "style": {"width": 170}},
    {"id": "5", "data": {"label": "4. Gain Recent Experience\n(Volunteer, Temp, Projects)"},
        "position": {"x": 250, "y": 480},
        "style": {"width": 170}},
    {"id": "6", "data": {"label": "5. Rebuild Professional Network\n(Reconnect, Join Groups)"},
        "position": {"x": 250, "y": 600},
        "style": {"width": 170}},
    {"id": "7", "data": {"label": "6. Update Resume & Narrative\n(Highlight Skills, Address Gap)"},
        "position": {"x": 250, "y": 720},
        "style": {"width": 170}},
    {"id": "8", "data": {"label": "7. Start Job Search\n(Targeted Approach)"},
        "position": {"x": 250, "y": 840},
        "style": {"width": 170}},
    {"id": "9", "data": {"label": "END:\nLand Accounting Role"},
        "position": {"x": 250, "y": 960},
        "type": "output",
        "style": {"background": '#FFCCCB', "width": 170}}, # Reddish background for end

    # Edges (connecting the nodes)
    {"id": "e1-2", "source": "1", "target": "2", "animated": True, "type": "smoothstep"},
    {"id": "e2-3", "source": "2", "target": "3", "animated": True, "type": "smoothstep"},
    {"id": "e3-4", "source": "3", "target": "4", "animated": True, "type": "smoothstep"},
    # Add label to edge e4-5 to hint at dependency
    {"id": "e4-5", "source": "4", "target": "5", "animated": True, "type": "smoothstep", "label": "Needed for Resume"},
    {"id": "e5-6", "source": "5", "target": "6", "animated": True, "type": "smoothstep"},
    {"id": "e6-7", "source": "6", "target": "7", "animated": True, "type": "smoothstep"},
    {"id": "e7-8", "source": "7", "target": "8", "animated": True, "type": "smoothstep"},
    {"id": "e8-9", "source": "8", "target": "9", "animated": True, "type": "smoothstep"}
]

# Define styles for the container (optional, adjust height as needed)
container_style = {"height": 1100, "border":"1px solid #eee", "border-radius":"5px"}

# Display the flowchart using streamlit_react_flow
flow_result = streamlit_react_flow(
    "flow_chart_key", # A unique key for the component
    elements=elements,
    styles=container_style,
    fit_view=True, # Automatically zoom/pan to fit the elements
    # You can add more customization options here if needed
    # e.g., default_edge_options={'animated': True}
)

st.markdown("---")
st.caption("This flowchart visualizes the general process. Refer to the '📖 Detailed Guide' page for comprehensive information on each step, resources, and requirements.")