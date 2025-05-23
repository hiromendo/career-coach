import streamlit as st

# --- Page Title ---
st.title("🚀 Phase 1: Foundations & LLM Exploration")

st.markdown("---")

# --- Goal ---
st.subheader("🎯 Goal:")
st.success(
    "Solidify programming fundamentals and understand how to interact with Large Language Models (LLMs)."
)
st.markdown("---")

# --- Week 1 ---
st.header("🗓️ Week 1: Language Proficiency & LLM Basics")
st.markdown("---")

# --- Action 1 ---
with st.expander("🛠️ Action 1: Choose Your Weapon & Sharpen It (10-15 hours)", expanded=True):
    st.markdown("""
    Select a modern programming language. **Python** is highly recommended due to its versatility and extensive LLM libraries.
    **JavaScript (with Node.js)** is another excellent choice, especially for web-focused projects.
    """)

    st.info("""
    💡 **Focus:**
    - If you know one, do a refresher.
    - If new, focus on core syntax, data types, control flow, functions, and object-oriented principles (or functional programming concepts for JS).
    """)

    st.markdown("<h5>📚 Resources:</h5>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- Official language documentation (e.g., [Python Docs](https://docs.python.org/3/), [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript))")
        st.markdown("- [Codecademy](https://www.codecademy.com/)")
        st.markdown("- [freeCodeCamp](https://www.freecodecamp.org/)")
    with col2:
        st.markdown("- Udemy courses (search for beginner Python or JavaScript)")
        st.markdown("- Coursera courses (similar search)")
    st.markdown("") # Extra space

# --- Action 2 ---
with st.expander("🧠 Action 2: Introduction to LLMs (5-7 hours)", expanded=True):
    st.markdown("""
    Understand what LLMs are, their capabilities, and their limitations.
    Explore available LLM APIs:
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **⭐ Gemini API (Google):**
        * Excellent for a wide range of tasks.
        * Features: Text generation, translation, Q&A, multimodal capabilities.
        * **Action:** Sign up for an API key.
        """)
    with col2:
        st.markdown("""
        **🔹 (Optional) OpenAI API:**
        * Another popular and powerful choice.
        * Explore if time permits or if specific projects benefit from it.
        """)

    st.info("💡 **Focus:** Learn how to make basic API calls to an LLM (e.g., send a prompt, receive a response).")

    st.markdown("<h5>📚 Resources:</h5>", unsafe_allow_html=True)
    st.markdown("- [Gemini API Documentation](https://ai.google.dev/docs/gemini_api_overview)")
    st.markdown("- Search 'Introduction to LLMs'.")
    st.markdown("")

# --- Action 3 ---
with st.expander("💬 Action 3: Your First LLM Interaction (3-5 hours)", expanded=True):
    st.markdown("<h5>🔬 Mini-Project: CLI LLM Tool</h5>", unsafe_allow_html=True)
    st.markdown("""
    Write a simple command-line interface (CLI) tool that takes user input,
    sends it to an LLM (e.g., Gemini), and prints the LLM's response.
    """)

    st.markdown("<h6>💡 Example Ideas:</h6>", unsafe_allow_html=True)
    st.markdown("""
    - A simple "ask me anything" bot.
    - A text summarizer for short paragraphs.
    - A creative story idea generator.
    - A code explainer for small snippets.
    """)

    st.warning("""
    🔒 **Key Learnings:**
    - Understand the request-response cycle with an LLM API.
    - Practice handling API keys securely (e.g., using environment variables or a `.env` file). **Never hardcode API keys!**
    """)
    st.markdown("")

st.markdown("---")
st.success("🎉 **Well done on completing the plan for Week 1!** Keep up the momentum for Week 2.")

# Placeholder for Week 2 content - can be added similarly
# st.header("🗓️ Week 2: Deep Dive & Practical Application")
# st.markdown("---")
# ... (add content for Week 2 here) ...

st.caption("This plan is a guide. Adjust timings and resources based on your learning pace and interests.")
