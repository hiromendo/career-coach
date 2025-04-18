import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Networking Strategy", layout="wide")

# --- Page Title and Introduction ---
st.title("🤝 Rebuild Your Professional Network in Portland")
st.markdown("""
Networking is **essential** when returning to accounting, especially after a break. Many opportunities aren't advertised!
It helps you learn about the current market, get advice, find support, and uncover job leads.

This page provides actionable strategies tailored for the Portland area.
""")
st.success("💡 **Key Goal:** Re-establish yourself as an active member of the Portland accounting community.", icon="🎯")
st.divider()

# --- Use Columns for Different Networking Avenues ---
col1, col2 = st.columns(2, gap="large")

# === Column 1: Reconnect & Engage Associations ===
with col1:
    # --- Reconnecting with Existing Network ---
    with st.container(border=True):
        st.subheader("🔗 Reconnect with Past Contacts")
        st.markdown("**Why:** Warm contacts are often most willing to help (advice, referrals).")
        st.markdown("##### 🚀 Actionable Steps:")
        st.markdown("""
        1.  **List:** Brainstorm former colleagues, managers, clients, classmates (Portland focus).
        2.  **Prioritize:** Start with positive relationships & well-connected individuals.
        3.  **Reach Out:** Use LinkedIn/Email. Keep it brief & positive: "Returning to accounting, would value catching up & getting your perspective..." (Don't ask for a job directly).
        4.  **Prepare for Chats:** Ask about industry changes, advice for re-entry, their company culture. Share your update concisely.
        5.  **Follow Up:** Send a thank-you note promptly.
        """)
        st.info("☕ Aim for 2-3 'coffee chats' (virtual or in-person) per month initially.", icon="ℹ️")

    st.markdown("<br/>", unsafe_allow_html=True) # Add space

    # --- Professional Associations ---
    with st.container(border=True):
        st.subheader("🧑‍🤝‍🧑 Join Professional Associations")
        st.markdown("**Why:** Access events, CPE, member directories, hidden job boards, stay current.")
        st.markdown("##### 🚀 Actionable Steps:")
        st.markdown("""
        1.  **Identify & Join:** Prioritize **OSCPA** (State CPA Society) and **IMA Portland** (Management Acct.). Consider others based on interest (IIA, OSTC, AFWA). *Check for affiliate/candidate rates!*
        2.  **Check Calendars Often:** Add relevant CPE & networking events to *your* calendar.
        3.  **Attend Actively:** Go to mixers, webinars, lunches. Prepare your 30-sec intro. Aim to meet 2-3 new people each time.
        4.  **Engage:** Ask questions during sessions, participate in discussions.
        5.  **Volunteer (Optional):** Join a committee for deeper connections.
        """)
        st.markdown("##### 🌐 Key Portland Resources:")
        st.link_button("OSCPA Website", "https://www.orcpa.org/")
        st.link_button("IMA Portland Chapter", "https://portland.imanet.org/")
        st.link_button("IIA Portland Chapter", "https://chapters.theiia.org/portland/Pages/default.aspx")
        st.link_button("OSTC (Tax Consultants)", "https://www.ostc-oregon.com/") # Check for local chapter info


# === Column 2: Online Presence & Events/Informal ===
with col2:
    # --- Online Networking (LinkedIn) ---
    with st.container(border=True):
        st.subheader("💻 Leverage LinkedIn")
        st.markdown("**Why:** Build visibility, research companies/people, connect with recruiters.")
        st.markdown("##### 🚀 Actionable Steps:")
        st.markdown("""
        1.  **Optimize Profile:** Professional photo, clear headline ("Accounting Professional Returning | Seeking...") summary explaining your goal, add recent skills/courses.
        2.  **Connect:** Find & connect with Portland CPAs, Acct. Managers, Recruiters. *Personalize requests!* ("Returning to accounting in PDX...")
        3.  **Join Groups:** Search for "OSCPA Members," "Portland Finance Professionals," "Oregon Accountants," etc.
        4.  **Engage:** Like/comment thoughtfully on posts. Share occasional relevant articles.
        5.  **Set to 'Open to Work':** Let recruiters know you're looking (can be private to recruiters only).
        """)
        st.link_button("Go to LinkedIn", "https://www.linkedin.com/")

    st.markdown("<br/>", unsafe_allow_html=True) # Add space

    # --- Events & Informal Networking ---
    with st.container(border=True):
        st.subheader("🗓️ Attend Events & Seek Info")
        st.markdown("**Why:** Face-to-face (or direct virtual) interaction builds rapport quickly.")
        st.markdown("##### 🚀 Actionable Steps:")
        st.markdown("""
        1.  **Prioritize Association Events:** Combine CPE/learning with networking (see Associations).
        2.  **Attend Career Fairs:** Check PSU/UO/OSU/OSCPA events (even if student-focused) to meet recruiters directly. (See 'Local Meetups' page for details).
        3.  **Request Informational Interviews:** Use LinkedIn/Network to ask professionals for brief chats (~20 min) about their role/company/industry. *Focus on learning, not job hunting.*
        4.  **Monitor Event Sites:** Check Eventbrite, Meetup.com for local finance/business networking events.
        5.  **Follow Local Business News:** Check Portland Business Journal for events.
        6.  **Alumni Groups:** Participate in relevant university alumni events.
        """)
        st.markdown("##### 🌐 Key Resources:")
        # Link to the relevant page in this app
        st.link_button("Eventbrite (Search Portland)", "https://www.eventbrite.com/d/or--portland/business--professional-networking/")
        st.link_button("Portland Business Journal Events", "https://www.bizjournals.com/portland/events")


st.divider()

# --- Networking Mindset ---
st.header("💡 Networking Mindset & Tips")
col1, col2 = st.columns(2)
with col1:
    st.info("""
    * **Be Prepared:** Have a concise (30-sec) intro ready.
    * **Be Curious:** Ask questions, listen more than you talk.
    * **Be Helpful:** Offer connections or info if you can.
    * **Be Patient:** Building relationships takes time.
    """, icon="🧠")
with col2:
    st.success("""
    * **Be Specific:** Know what roles/industries interest you.
    * **Be Professional:** Online and in person.
    * **Follow Up:** Send thank yous & connect on LinkedIn.
    * **Be Yourself:** Authenticity builds trust.
    """, icon="✅")


st.divider()
st.caption("Networking is a continuous activity, not just for job searching. Maintain connections throughout your career.")