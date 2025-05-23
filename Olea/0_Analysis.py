import streamlit as st

# --- Page Title ---
st.title("🚀 8-Week Actionable Plan: Gain Software Engineering Experience with LLMs")
st.markdown("---") # Equivalent to st.divider()

# --- Introduction ---
st.subheader("🎯 Your Intensive Journey into Software Development")
st.markdown(
    "This plan is designed to be **intensive and project-focused**. "
    "The key is **consistent effort** and building **tangible things**. "
    "Let's get started!"
)
st.markdown("---")

# --- Core Principles ---
st.header("🌟 Core Principles") # Removed anchor as sidebar navigation is gone
principles = {
    "🛠️ Learn by Doing:": "Prioritize building projects over passive learning.",
    "💻 Modern Stack:": "Focus on technologies relevant in today's market.",
    "🧠 LLM Integration:": "Leverage the power of LLMs to build innovative applications and to assist your learning process.",
    "📁 Portfolio Building:": "Every project is a potential portfolio piece.",
    "🔄 Iterative Progress:": "Don't aim for perfection in the first go. Build, get feedback (even from yourself or an LLM), and iterate."
}

col1, col2 = st.columns(2)
principles_items = list(principles.items())

with col1:
    for i in range(0, len(principles_items), 2):
        emoji_title, desc = principles_items[i]
        st.markdown(f"**{emoji_title}** {desc}")
        st.markdown("") # Adds a bit of space

with col2:
    for i in range(1, len(principles_items), 2):
        emoji_title, desc = principles_items[i]
        st.markdown(f"**{emoji_title}** {desc}")
        st.markdown("") # Adds a bit of space
st.markdown("---")

# --- Weekly Breakdown ---
st.header("🗓️ Weekly Breakdown") # Removed anchor
weeks_data = {
    "Week 1: Foundation & Exploration": {
        "emoji": "📚",
        "title": "Language Proficiency & LLM Basics",
        "details": [
            "Choose your primary programming language (e.g., Python). Solidify fundamentals.",
            "Understand what LLMs are, their capabilities, and limitations.",
            "Explore popular LLM APIs (e.g., OpenAI, Gemini, Hugging Face Transformers).",
            "Set up your development environment."
        ],
        "tip": "Focus on understanding core concepts. Don't get bogged down in too many tools yet."
    },
    "Week 2: Core Concepts & LLM-Assisted Learning": {
        "emoji": "💡",
        "title": "Core Software Concepts & LLM-Assisted Learning",
        "details": [
            "Review fundamental software engineering concepts (data structures, algorithms, version control with Git).",
            "Learn about API integration, JSON, and basic web requests.",
            "Practice using an LLM as a learning assistant: ask it to explain code, debug, or suggest approaches.",
            "Start a small project: e.g., a script that calls an LLM API to summarize text."
        ],
        "tip": "Git is your best friend. Commit often!"
    },
    "Week 3: Building Blocks & First Project": {
        "emoji": "🧱",
        "title": "Web/App Development Basics & Project Scaffolding",
        "details": [
            "Learn the basics of a web framework (e.g., Flask/Django for Python, or a simple frontend framework if you prefer).",
            "Understand basic HTML, CSS, and JavaScript if building a web interface.",
            "Scaffold your first LLM-powered application: define features, user flow, and tech stack.",
            "Focus on a simple but complete end-to-end flow."
        ],
        "tip": "Keep it simple! A working prototype is better than a complex, unfinished idea."
    },
    "Week 4: LLM Integration & Deployment Prep": {
        "emoji": "🔗",
        "title": "LLM Integration & Deployment Prep",
        "details": [
            "Deepen your LLM integration: prompt engineering, handling responses, error management.",
            "Explore techniques for managing context and conversation history if building a chatbot.",
            "Learn about basic deployment options (e.g., Heroku, Streamlit Sharing, Docker basics).",
            "Get your first project to a deployable state, even if it's simple."
        ],
        "tip": "Prompt engineering is an art and a science. Experiment!"
    },
    "Week 5: Advanced Concepts & Capstone Planning": {
        "emoji": "⚙️",
        "title": "Advanced Concepts & Project Planning",
        "details": [
            "Explore more advanced LLM topics: fine-tuning (conceptual understanding), embeddings, vector databases (basics).",
            "Learn about responsible AI and ethical considerations when using LLMs.",
            "Start planning a more significant capstone project. Define scope, features, and success criteria.",
            "Research tools and techniques relevant to your capstone idea."
        ],
        "tip": "Think about a project that genuinely interests you – it will keep you motivated."
    },
    "Week 6: Capstone Project - Development Sprint": {
        "emoji": "🚀",
        "title": "Capstone Project Development",
        "details": [
            "Intensive development phase for your capstone project.",
            "Focus on core functionality. Apply iterative development principles.",
            "Regularly test and debug. Use version control extensively.",
            "Seek feedback if possible (peers, mentors, or even use an LLM to review your logic)."
        ],
        "tip": "Break down large tasks into smaller, manageable chunks."
    },
    "Week 7: Finalizing & Polishing": {
        "emoji": "✨",
        "title": "Project Finalization & Portfolio Creation",
        "details": [
            "Finalize your capstone project: bug fixing, UI/UX improvements, documentation (README).",
            "Prepare a compelling project description and demo for your portfolio.",
            "Start building or updating your online portfolio (e.g., GitHub Pages, personal website).",
            "Ensure your code is clean and well-commented."
        ],
        "tip": "A good README can make a huge difference in how your project is perceived."
    },
    "Week 8: Review, Practice & Future Roadmap": {
        "emoji": "🗺️",
        "title": "Review, Practice & Future Planning",
        "details": [
            "Review everything you've learned. Identify areas for further study.",
            "Practice coding challenges and mock interviews (technical and behavioral).",
            "Refine your portfolio and resume.",
            "Plan your next steps: job applications, further learning, contributing to open source."
        ],
        "tip": "Learning is a continuous journey. Stay curious!"
    }
}

for week_title_key, week_info in weeks_data.items():
    with st.expander(f"{week_info['emoji']} **{week_title_key}** - {week_info['title']}"):
        st.markdown("#### Key Activities:")
        for detail in week_info['details']:
            st.markdown(f"- {detail}")
        if "tip" in week_info:
            st.success(f"💡 **Pro Tip:** {week_info['tip']}")
        st.markdown("<br>", unsafe_allow_html=True) # Add some space at the end of each expander

st.markdown("---")

# --- Call to Action / Conclusion ---

st.success(
    "🎉 **Congratulations on starting this journey!** "
    "Remember to adapt this plan to your own pace and interests. Consistent effort is key. Good luck!"
)
st.caption("This plan provides a structured approach. Feel free to customize it to your learning style and goals.")

# To run this Streamlit app:
# 1. Save this code as a Python file (e.g., llm_action_plan_app.py).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: streamlit run llm_action_plan_app.py
