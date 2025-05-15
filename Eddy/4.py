import streamlit as st

def main():
    """
    Main function to run the Streamlit app.
    This app displays a "Locked Week 2" message.
    """

    # Custom CSS to center the content and style the message
    st.markdown("""
        <style>
        .main .block-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 80vh; /* Adjust height as needed */
        }
        .locked-message {
            font-size: 2.5rem; /* Large font size */
            font-weight: bold;
            color: #FF4B4B; /* A reddish color for emphasis */
            text-align: center;
            padding: 20px;
            border: 2px solid #FF4B4B;
            border-radius: 10px;
            background-color: #fff0f0; /* Light reddish background */
        }
        </style>
    """, unsafe_allow_html=True)

    # Display the locked message
    st.markdown('<div class="locked-message">🔒 Week 2</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
