import streamlit as st



# --- Page Title ---
st.title("🚀 Phase 1: Foundations & LLM Exploration") # Main phase title
st.subheader("🗓️ Week 2: Core Concepts & LLM-Assisted Learning")
st.markdown("---")

# --- Goal for Phase 1 (can be repeated or referred to) ---
# st.subheader("🎯 Overall Phase 1 Goal Reminder:")
# st.info(
#    "Solidify programming fundamentals and understand how to interact with Large Language Models (LLMs)."
# )
# st.markdown("---")


# --- Action 1 (Week 2) ---
with st.expander("🧠 Action 1: Essential Data Structures & Algorithms (DSA) (10-12 hours)", expanded=True):
    st.markdown("""
    Focus on understanding and implementing fundamental DSAs:
    - Arrays
    - Strings
    - Linked Lists
    - Trees (Basics)
    - Hash Tables (Dictionaries in Python / Objects in JavaScript)
    """)
    st.markdown("""
    Learn basic algorithm concepts:
    - Sorting (e.g., Bubble Sort, Merge Sort)
    - Searching (e.g., Binary Search)
    - Time & Space Complexity (Big O notation - understand the concept)
    """)

    st.info("""
    🤖 **LLM Assist:** Use an LLM to:
    - Explain DSA concepts in different ways or with analogies.
    - Generate practice problems tailored to specific DSAs.
    - Help debug your DSA implementations.
    *Prompt example:* "I'm trying to implement a linked list in Python. Here's my code: `[your code]`. I'm getting this error: `[error message]`. Can you help me find the bug and explain it?"
    """)

    st.markdown("<h5>📚 Resources:</h5>", unsafe_allow_html=True)
    col1_w2_a1, col2_w2_a1 = st.columns(2)
    with col1_w2_a1:
        st.markdown("- \"Grokking Algorithms\" by Aditya Bhargava (Book - very visual and beginner-friendly)")
        st.markdown("- [LeetCode](https://leetcode.com/) (Filter by Easy difficulty for DSA topics)")
    with col2_w2_a1:
        st.markdown("- [HackerRank](https://www.hackerrank.com/) (Practice problems for various DSAs)")
        st.markdown("- YouTube channels like freeCodeCamp, CS Dojo for visual explanations.")
    st.markdown("")

# --- Action 2 (Week 2) ---
with st.expander("🐙 Action 2: Version Control with Git & GitHub (5-7 hours)", expanded=True):
    st.markdown("""
    Learn the basics of Git for tracking changes and collaborating:
    - `git init` (initialize a repository)
    - `git add` (stage changes)
    - `git commit` (save changes to local repository)
    - `git push` (upload local commits to a remote repository like GitHub)
    - `git pull` (fetch and download content from a remote repository)
    - `git branch` (manage different lines of development)
    - `git merge` (combine branches)
    """)
    st.success("""
    ✅ **Task:**
    1. Create a GitHub account if you don't have one.
    2. Create a new repository on GitHub.
    3. Push your mini-project from Week 1 to this repository.
    4. Push your DSA practice code (from Action 1 of this week) to the same or a new repository.
    """)

    st.markdown("<h5>📚 Resources:</h5>", unsafe_allow_html=True)
    st.markdown("- [GitHub's own guides (e.g., GitHub Skills)](https://skills.github.com/)")
    st.markdown("- [Atlassian Git Tutorials (Comprehensive and well-structured)](https://www.atlassian.com/git/tutorials)")
    st.markdown("- [Learn Git Branching (Interactive Tutorial)](https://learngitbranching.js.org/)")
    st.markdown("")

# --- Action 3 (Week 2) ---
with st.expander("💡 Action 3: Plan Your First LLM-Integrated Project (3-5 hours)", expanded=True):
    st.markdown("""
    Brainstorm ideas for a slightly more complex project you'll aim to build in Weeks 3-4.
    The project should have a clear use case for an LLM. Think about problems an LLM can help solve.
    """)
    st.markdown("<h6>🤔 Considerations for your project:</h6>", unsafe_allow_html=True)
    st.markdown("""
    - What problem will it solve or what value will it provide?
    - Who is the target user (even if it's just you)?
    - What will be the core features?
    - How will the LLM be integrated? (e.g., text generation, summarization, Q&A, classification)
    """)

    st.info("""
    🤖 **LLM Assist:** Use an LLM to help brainstorm or refine your chosen idea:
    - *Prompt example:* "I want to build a small web app using Python and the Gemini API. I'm interested in [your interest, e.g., 'education', 'productivity', 'creative writing']. Can you give me 5 project ideas that a beginner could complete in about two weeks, highlighting how the LLM would be used?"
    - *Prompt example:* "I'm thinking of building [your project idea]. What are some potential challenges I might face, and how could an LLM help enhance its features?"
    """)
    st.warning("📋 **Deliverable:** Write a short paragraph or a few bullet points outlining your chosen project idea, its core functionality, and how the LLM will be used. This will be your starting point for Week 3.")
    st.markdown("")


st.markdown("---")
st.success("🌟 **Phase 1 Complete!** You've built a strong foundation. Get ready for more project-based learning in Phase 2 (Weeks 3-4)!")
st.caption("This plan is a guide. Adjust timings and resources based on your learning pace and interests.")
