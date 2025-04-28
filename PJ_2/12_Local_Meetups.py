import streamlit as st
import datetime

# --- Main Title ---
st.title("Local Meetups, Associations, and Career Fairs for Accounting/Finance in Portland")

# --- Introduction ---
st.markdown("""
Engaging with the local professional scene through events and career fairs is crucial for networking and discovering opportunities, especially when re-entering the accounting field. Portland offers several events tailored to accounting and finance professionals.
""")

# --- Section 1: Accounting-Specific Career Fairs ("Meet the Firms") ---
st.header("1. Accounting Career Fairs ('Meet the Firms')")
st.markdown("""
These events are prime opportunities to connect directly with accounting firms and companies hiring for accounting/finance roles. While often targeting students, they can be valuable for returning professionals too.

* **Portland State University (PSU):**
    * Hosts annual accounting career fairs, often in the fall ("Meet the Firms") and sometimes a joint [Spring All Majors & Accounting Career Fair](https://www.pdx.edu/events/spring-all-majors-accounting-career-and-internship-fair). Check the [PSU Career Center Events](https://www.pdx.edu/careers/workshops-events) page for current dates.
* **University of Oregon (UO) & Oregon State University (OSU):**
    * Hold similar "Meet the Firms" events on their respective campuses (Eugene/Corvallis). Check UO and OSU Career Services for details.
    * They have previously collaborated with PSU on a [Spring Accounting Career Expo](https://sites.google.com/pdx.edu/actg-resources/spring-accounting-career-expo) in Portland (link is to a past event, check for current joint events).
* **OSCPA Career Showcase:**
    * The Oregon Society of CPAs hosts a large annual [Career Showcase](https://www.orcpa.org/events-activities) event, typically in September in Portland (often at the Oregon Convention Center). Primarily for students but a major gathering of firms and companies. Contact OSCPA regarding attendance possibilities for non-students or alumni.
""")

st.info("""
**Leveraging Student-Focused Fairs:**
* **Attend Respectfully:** If attending an event primarily for students, be transparent about your status ("I'm an alum/returning professional exploring opportunities...").
* **Goal:** Network with recruiters, learn about companies, gather contact info, and inquire about experienced hire channels.
* **Follow Up:** Send thank-you notes via email or LinkedIn to contacts you make.
""")

# --- Section 2: General & Community Job Fairs ---
st.header("2. General Job Fairs in Portland")
st.markdown("""
Broader career fairs can also feature employers seeking accounting and finance talent.

* **Portland Community College (PCC):** Hosts job fairs often [open to the public](https://www.pcc.edu/resources/careers/fairs/), potentially featuring entry-level accounting or bookkeeping roles.
* **Urban League of Portland:** Hosts events like the annual [Career Connections Job Fair](https://ulpdx.org/events/2025/2025-career-connections-job-fair), often featuring employers committed to diversity and inclusion.
* **WorkSource Oregon:** May host or list various [job fairs and hiring events](https://www.worksourceoregon.org/jobseekers) across the region.
* **Technology Association of Oregon (TAO):** While tech-focused, their [events](https://www.techoregon.org/events/) or career fairs might include tech companies hiring for their internal finance/accounting teams.
""")

# --- Section 3: Professional Association Events ---
st.header("3. Professional Association Events & Conferences")
st.markdown("""
Events hosted by professional bodies offer targeted networking and learning.

* **OSCPA Events:** Beyond the Career Showcase, OSCPA hosts various [member events, socials, and conferences](https://www.orcpa.org/cpe) (e.g., Governmental Accounting & Auditing, Not-for-Profit) throughout the year. Check their calendar. Conferences often have networking breaks.
* **IMA Portland Chapter Events:** Hosts regular [CPE dinners, talks, and social events](https://portland.imanet.org/events/chapterevents). Excellent for connecting with professionals in corporate accounting/finance.
* **IIA / ISACA / FEI Portland Events:** Chapters of the Institute of Internal Auditors ([IIA Portland](https://www.theiia.org/en/chapters/united-states/oregon/portland/)), ISACA ([ISACA Portland](https://engage.isaca.org/portlandchapter/home)), and Financial Executives International ([FEI Portland](https://www.financialexecutives.org/Network/Chapters/Portland/Home.aspx)) hold meetings and events relevant to their niches (internal audit, IT audit, senior finance executives). Attending can provide valuable connections.
""")

# --- Section 4: Informal Meetups & Startup Scene ---
st.header("4. Informal Meetups & Startup Community Events")
st.markdown("""
Casual settings can also yield valuable connections.

* **Meetup.com / Eventbrite:** Search platforms like [Meetup](https://www.meetup.com/topics/finance-professionals/) and [Eventbrite](https://www.eventbrite.com/d/or--portland/finance-conference/) for "Portland finance networking," "accounting happy hour," or similar terms. Events can be sporadic but offer informal networking.
* **FinTech Meetups:** If interested in financial technology, look for local FinTech groups.
* **Startup Events:** Keep an eye on events hosted by startup incubators like [PIE (Portland Incubator Experiment)](https://piepdx.com/calendar/) or co-working spaces. You might meet founders of growing companies needing accounting help.
""")

# --- Section 5: Career Development Workshops ---
st.header("5. Career Development Workshops")
st.markdown("""
Workshops focused on job search skills can be beneficial.

* **Resume/Interview Prep:** Look for workshops offered by OSCPA, university career centers ([PSU Career Center](https://www.pdx.edu/careers/workshops-events)), [WorkSource Oregon](https://oregonworkforcepartnership.org/), or organizations like Dress for Success.
* **Professional Development:** Organizations like FEI Portland or the [Portland Business Journal](https://www.bizjournals.com/portland/events) sometimes host career seminars or panels.
""")

# --- Section 6: Making the Most of Events ---
st.header("6. Tips for Attending Events & Fairs")
with st.expander("Click here for Event Strategies"):
    st.markdown("""
    * **Preparation:** Research attending employers/speakers beforehand if possible. Target key contacts.
    * **Attire:** Dress professionally (business casual is usually safe for most events, business professional for formal fairs).
    * **Resume:** Bring updated copies to career fairs.
    * **Introduction:** Practice your concise self-introduction (your background, transition, goals).
    * **Engage:** Ask thoughtful questions and listen actively.
    * **Collect Contacts:** Get business cards or LinkedIn information.
    * **Follow Up:** Send personalized thank-you notes or LinkedIn requests promptly after the event.
    * **Community Calendars:** Regularly check OSCPA, university career center, Portland Business Journal, and Eventbrite calendars for upcoming events.
    """)

# --- Conclusion ---
st.header("Conclusion")
st.markdown("""
Actively participating in Portland's local meetups, association events, and career fairs is a powerful way to immerse yourself in the professional community. These events provide invaluable opportunities to network, learn about companies, discover job leads, and build confidence as you relaunch your accounting career.
""")

# --- Footer ---
st.markdown("---")
current_year = datetime.datetime.now().year
st.caption(f"Information current as of April {current_year}. Event dates and details change annually; always verify information directly with the hosting organizations.")
