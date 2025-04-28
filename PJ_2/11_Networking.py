import streamlit as st
import datetime

# --- Main Title ---
st.title("Networking Opportunities & Local Accounting Organizations in Portland")

# --- Introduction ---
st.markdown("""
Rebuilding your professional network is one of the most impactful steps when re-entering the accounting field. Portland boasts a vibrant community of accounting and finance professionals. Plugging into local organizations and attending events can open doors to opportunities, mentorship, and peer support.
""")

# --- Section 1: Major Professional Organizations ---
st.header("1. Major Professional Organizations")
st.markdown("These organizations are central hubs for accounting professionals in Oregon.")

st.subheader("Oregon Society of CPAs (OSCPA)")
st.markdown("""
The OSCPA is the primary statewide association for CPAs and accounting professionals. It's a cornerstone for networking.
* **Membership:** Offers various categories, including [Affiliate memberships](https://www.orcpa.org/join) for non-CPAs or those with inactive licenses. Membership provides access to events, directories, and potentially mentorship.
* **Events:** Hosts numerous networking events, CPE seminars, conferences, and socials. Check their [CPE & Events Calendar](https://www.orcpa.org/cpe). Attending educational sessions also provides networking opportunities.
* **Chapters:** OSCPA has [local chapters](https://www.orcpa.org/chapters) (Portland is in the Upper NW Region) that may host luncheons or mixers, offering more localized networking.
* **Community:** OSCPA fosters a welcoming environment and supports professional development, advocacy, and leadership. Getting involved can raise your profile.
""")

st.subheader("Institute of Management Accountants (IMA) - Portland Chapter")
st.markdown("""
The IMA focuses on management accounting (professionals in business/industry) and offers the CMA certification.
* **Membership:** Open to all accounting and finance professionals, not just CMAs. Connects you with professionals in various Portland-area companies (industry focus).
* **Events:** The [Portland IMA Chapter](https://portland.imanet.org/portlandchapter/home) is active, hosting monthly events like CPE dinners, talks on current topics (e.g., FinTech, AI in Finance), and social gatherings. Check their [events page](https://portland.imanet.org/events/chapterevents).
* **Resources:** The chapter may offer mentorship programs and sometimes features job postings on their site or through member communications ([IMA Financial Group Job Openings](https://imacorp.com/careers/openings) - Note: This is the parent company site, chapter-specific jobs might be on the chapter site or newsletter).
* **Atmosphere:** Often noted for being welcoming to newcomers. Attending IMA events complements OSCPA networking by connecting you with the corporate accounting side.
""")

# --- Section 2: Specialized and Affinity Groups ---
st.header("2. Specialized and Affinity Groups")
st.markdown("These groups cater to specific interests or demographics within the accounting and finance field.")

st.subheader("Accounting & Finance Women’s Alliance (AFWA)")
st.markdown("""
AFWA focuses on supporting women in the accounting and finance professions (but is open to all supporters).
* **Local Presence:** Historically, Portland has had chapter activity, though it can fluctuate. It's recommended to check the [national AFWA website](https://www.afwa.org/) for current chapter status or nearby active chapters (like Seattle).
* **Benefits:** Provides networking, CPE, leadership opportunities, and a supportive community. They often host meetings, workshops, and social events.
""")

st.subheader("Institute of Internal Auditors (IIA) - Portland Chapter")
st.markdown("""
Relevant if you have an interest in internal audit, risk management, or governance roles.
* **Local Chapter:** The [IIA Portland Chapter](https://www.theiia.org/en/chapters/united-states/oregon/portland/) supports local internal audit professionals.
* **Events:** Holds regular luncheons, seminars, and training sessions on audit-related topics.
* **Networking:** Connect with internal audit managers and professionals from local corporations and government entities. Internal audit roles can sometimes be a pathway into a company's finance team.
""")

st.subheader("ISACA (Information Systems Audit and Control Association) - Portland Chapter")
st.markdown("""
Focuses on IT audit, cybersecurity, risk, and governance. Relevant if your interests lie at the intersection of accounting/finance and technology.
* **Local Chapter:** Check the [ISACA Portland Chapter](https://engage.isaca.org/portlandchapter/home) (link is to the general ISACA Engage platform, navigate to find Portland) for events and membership info.
* **Networking:** Connect with professionals in IT audit and security roles.
""")

st.subheader("Oregon Association of Independent Accountants (OAIA)")
st.markdown("""
Caters to independent accountants, bookkeepers, and professionals serving small businesses.
* **Focus:** Often discusses topics like tax preparation, QuickBooks, and practice management.
* **Networking:** Good for connecting with peers if you are considering freelance work or roles in smaller firms/serving small clients. ([OAIA Directory Listing](https://directoryofassociations.com/view.asp?di={0C6CE361-3A5A-462E-8CD5-FE754845416A}) - *Note: Official website link may require further search.*)
""")

st.subheader("Oregon Society of Tax Consultants (OSTC)")
st.markdown("""
An organization for tax preparers and consultants (CPAs, EAs, Licensed Tax Consultants).
* **Focus:** Tax law, preparation, and consulting.
* **Events:** Hosts local chapter meetings (including Portland area) and educational sessions. Visit the [OSTC website](https://www.ostcinc.org/).
* **Networking:** Ideal if you are targeting tax-specific roles.
""")

# --- Section 3: Other Networking Avenues ---
st.header("3. Other Networking Avenues")
st.markdown("Explore less formal or broader professional networking opportunities.")

st.markdown("""
* **Meetup.com:** Search for groups related to "[Portland finance professionals](https://www.meetup.com/topics/finance-professionals/)" or "Portland accounting". Activity varies, but you might find informal happy hours or discussion groups.
* **University Events & Volunteering:**
    * Connect with student accounting clubs like the [PSU Accounting Club](https://sites.google.com/pdx.edu/actg-resources/psu-accounting-club) or the [University of Portland Accounting Association](https://sites.up.edu/upaa/). They often host events where professionals are welcome or needed as speakers/mentors.
    * Volunteer for OSCPA or IMA committees or events. This provides deeper interaction with other professionals.
* **Online Communities:** Engage in relevant online forums (like LinkedIn groups or subreddits) and follow local business news sources like the [Portland Business Journal](https://www.bizjournals.com/portland/).
""")

# --- Section 4: Effective Networking Approach ---
st.header("4. Your Networking Approach")
st.markdown("Maximize your networking efforts with a strategic approach:")

with st.expander("Click here for Networking Tips"):
    st.markdown("""
    * **Business Cards:** Create simple personal business cards listing your name, "Accounting Professional," email, LinkedIn profile URL, and phone number.
    * **Prepare Your Intro:** Have a concise (30-second) introduction ready: "Hi, I’m [Name]. I started my career in accounting, then gained experience in digital marketing for several years. I'm now excited to be transitioning back to accounting, refreshing my skills [mention specifics like CPA study if applicable], and exploring opportunities here in Portland."
    * **Be Curious:** Ask others about their roles and experiences. Show genuine interest. People appreciate being listened to.
    * **Listen More Than You Talk:** Focus on understanding others' perspectives and needs.
    * **Follow Up:** Connect on LinkedIn within 24-48 hours after meeting someone. Reference your conversation in the connection request (e.g., "Great meeting you at the IMA event!").
    * **Set Goals:** Aim to meet 2-3 new people per event rather than trying to talk to everyone. Quality over quantity.
    * **Offer Help:** Networking is reciprocal. If you can help someone else (e.g., share an article, make an introduction), do so.
    """)

# --- Conclusion ---
st.header("Conclusion")
st.markdown("""
Portland's accounting community is generally supportive and interconnected. By actively participating in these organizations and events, you'll build valuable connections, gain insights into the local market, and create a strong support system for your return to the accounting profession. Consistent effort in networking often leads to unexpected opportunities.
""")

# --- Footer ---
st.markdown("---")
current_year = datetime.datetime.now().year
st.caption(f"Information current as of April {current_year}. Please verify event details, membership requirements, and chapter activity directly with the organizations.")
