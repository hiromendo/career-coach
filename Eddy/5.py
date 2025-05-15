import streamlit as st

def week_card_html(week_number: int, status: str, is_highlighted: bool = False) -> str:
    """
    Generates HTML/CSS for a styled week card.

    Args:
        week_number: The number of the week.
        status: "unlocked" or "locked".
        is_highlighted: True if this week should be visually emphasized (e.g., current locked week).

    Returns:
        HTML string for the week card.
    """
    # Determine icon, colors, and status text based on the week's status
    if status == "unlocked":
        icon = "✅"  # Checkmark for unlocked
        border_color = "#28a745"  # Green
        background_color = "#e6ffed" # Light green
        status_text = "Unlocked"
        icon_color = border_color
    elif status == "locked":
        icon = "🔒"  # Lock icon for locked
        if is_highlighted:
            border_color = "#dc3545"  # Red for the highlighted locked week
            background_color = "#ffebee" # Light red
            status_text = "Locked"
            icon_color = border_color
        else:
            border_color = "#6c757d"  # Grey for other locked weeks
            background_color = "#f8f9fa" # Light grey
            status_text = "Locked"
            icon_color = border_color
    else: # Default fallback, though not expected with current logic
        icon = "❓"
        border_color = "#6c757d"
        background_color = "#f8f9fa"
        status_text = "Unknown"
        icon_color = border_color

    # Base style for the card
    card_style = f"""
        border: 2px solid {border_color};
        background-color: {background_color};
        border-radius: 12px; /* Slightly more rounded corners */
        padding: 20px;
        text-align: center;
        height: 180px; /* Increased height for better spacing */
        display: flex;
        flex-direction: column;
        justify-content: space-around; /* Better content distribution */
        align-items: center;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; /* Smooth hover effect */
    """

    # Add shadow and slight scale effect for the highlighted card
    if is_highlighted:
        card_style += "box-shadow: 0 6px 12px rgba(0,0,0,0.15);"
    else:
        card_style += "box-shadow: 0 3px 6px rgba(0,0,0,0.1);"


    # HTML structure for the card
    return f"""
    <div style="{card_style}" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 16px rgba(0,0,0,0.2)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='{ '0 6px 12px rgba(0,0,0,0.15)' if is_highlighted else '0 3px 6px rgba(0,0,0,0.1)' }';">
        <div style="font-size: 2.5rem; color: {icon_color}; margin-bottom: 5px;">{icon}</div>
        <div style="font-size: 1.25rem; font-weight: bold; color: #333;">Week {week_number}</div>
        <div style="font-size: 0.9rem; font-weight: 500; color: {border_color};">{status_text.upper()}</div>
    </div>
    """

def main():
    """
    Main function to run the Streamlit app.
    This app displays a visual timeline indicating that Week 2 is locked.
    """

    # Custom CSS for overall page styling and column adjustments
    st.markdown("""
        <style>
            /* Ensure body has a light background for cards to pop */
            body {
                background-color: #f0f2f5; /* Light grey background */
            }
            /* Center the main title */
            .main-title {
                text-align: center;
                color: #333; /* Darker title color */
                margin-bottom: 40px; /* More space below title */
                font-weight: 600;
            }
            /* Adjust column padding for responsiveness */
            .stMultiColumn > div[data-testid="stVerticalBlock"] { /* More specific selector */
                padding-left: 10px !important;
                padding-right: 10px !important;
                margin-bottom: 15px; /* Add margin for stacked columns on mobile */
            }
        </style>
    """, unsafe_allow_html=True)

    # Main title for the page
    st.markdown("<h1 class='main-title'>Module Access Timeline</h1>", unsafe_allow_html=True)

    # Define the weeks and their statuses
    # "Locked Week2" means Week 2 is the one we are highlighting as locked.
    weeks_data = [
        {"number": 1, "status": "unlocked"},
        {"number": 2, "status": "locked", "highlight": True},  # Week 2 is the focus, highlighted as locked
        {"number": 3, "status": "locked"},
        {"number": 4, "status": "locked"},
        {"number": 5, "status": "locked"},
    ]

    num_weeks = len(weeks_data)
    # Create columns for the timeline
    # The number of columns will match the number of weeks.
    cols = st.columns(num_weeks)

    # Populate each column with a week card
    for i, week_info in enumerate(weeks_data):
        with cols[i]:
            # Check if the current week card should be highlighted
            is_highlighted_week = week_info.get("highlight", False)
            # Generate and display the HTML for the week card
            st.markdown(
                week_card_html(
                    week_number=week_info["number"],
                    status=week_info["status"],
                    is_highlighted=is_highlighted_week
                ),
                unsafe_allow_html=True
            )

    # Optional: Add a concluding remark or instruction
    st.markdown(
        "<p style='text-align:center; margin-top: 30px; font-style: italic; color: #555;'>"
        "Please complete prior modules or wait for the scheduled unlock date to access locked content."
        "</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
