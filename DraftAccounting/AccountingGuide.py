import streamlit as st

# --- Page Configuration ---
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Define Keys IN ORDER & Map to Content/Links ---
# Use a list of tuples: (key, content_markdown, optional_page_link_tuple)
# optional_page_link_tuple = (target_page_file, label, icon)

section_content_map = [
    # Section 1
    ("Evaluate Your Career Goals (CPA vs. Non-CPA)",
     """
     Begin by clarifying whether you want to pursue a Certified Public Accountant (CPA) license or aim for accounting roles that don't require CPA certification. This decision will shape your next steps.

     * **Factors to Consider:** Kinds of jobs desired (public accounting vs. private industry), time/effort for CPA, long-term career growth.
     * **CPA Path:** Opens doors to higher-level roles, especially in public accounting and some corporate positions.
     * **Non-CPA Path:** Roles like bookkeeper, staff accountant, accounting manager can be rewarding but might have different advancement paths.
     * **Importance:** Knowing your target path helps prioritize licensing, education, and job search efforts.
    """, None),

    ("Refresh Your Accounting Knowledge and Skills",
     """
     After 10+ years away, updating your knowledge is crucial. Key areas include:

     * **Accounting Principles & Standards:** Review major updates (e.g., ASC 606 Rev Rec, ASC 842 Leases, Tax Law changes).
     * **Technology:** Familiarize yourself with current software (QuickBooks, ERPs) & advanced Excel.
     * **Continuing Education:** Enroll in refresher courses or CPE seminars.
     * **Self-Study:** Read publications, follow news, network.
    """, None),

    ("Address Education and Credentials Gaps",
     """
     Determine necessary updates for your credentials.

     * **CPA Path (New License):** Requires 150 semester hours (incl. specific courses), passing the Uniform CPA Exam, and supervised experience. Consider post-bacc certs (PSU, Linfield) if needed.
     * **Prior CPA License Reactivation:** Contact Oregon Board. Requires CPE catch-up, fees. Requirements vary based on inactive/lapsed duration. Lapsed 6+ years may require re-exam.
     * **Alternative Certifications (Non-CPA):** Consider CMA (management acct.), CIA (internal audit), EA (tax) to boost profile.
     """, None),

    ("Gain Recent Experience (Even in Small Doses)",
     """
     Bridge the experience gap with current activities.

     * **Volunteer/Freelance:** Offer skills to nonprofits (Hands On Greater Portland), join VITA tax program, take small gigs.
     * **Returnships/Internships:** Look for formal programs or propose project work.
     * **Temp/Contract:** Use staffing agencies (Robert Half, Ledgent) for short-term roles.
     """, None),

    ("Rebuild Your Professional Network",
     """
     Networking is critical. Many jobs are found via connections.

     * **Reconnect:** Contact former colleagues/supervisors.
     * **Join/Attend:** Actively participate in OSCPA, IMA, AFWA events.
     * **Online:** Update LinkedIn, connect with local pros, join groups.
     """, None),

    ("Update Your Resume and Narrative",
     """
     Craft a compelling story for employers.

     * **Highlight:** Past accounting achievements + recent updates (courses, volunteer work).
     * **Address Gap:** Frame break positively, emphasizing transferable skills (e.g., from marketing).
     * **Keywords:** Optimize for ATS (GAAP, Reconciliation, QuickBooks, Excel, etc.).
     * **Narrative:** Use cover letter to explain transition back with enthusiasm.
     """, None),

    ("Start the Job Search (Targeted Approach)",
     """
     Begin applying strategically.

     * **Target Roles:** May start slightly below previous level to re-enter.
     * **Leverage Network:** Seek introductions/referrals.
     * **Be Open:** Consider remote/hybrid roles.
     * **Persistence:** Job searching takes time; stay positive.
     """, None),

    # Section 2
    ("CPA Licensure in Oregon (New License)", # Key is now unique
     """
     Requirements set by the Oregon Board of Accountancy:

     * **Education:** 150 semester hours (incl. specific courses).
     * **Exam:** Pass Uniform CPA Exam + Ethics Exam. Can sit with 120hrs (but 150 needed for license).
     * **Experience:** ~1 year supervised experience.
     * **Application:** Submit all docs + fees. Requires Oregon-specific ethics CPE.
     * **Maintain:** Biennial renewal with 80 CPE hours.
     * **Sources:** [OR CPA Reqs](https://www.ais-cpa.com/oregon-cpa-requirements/), [OR Board](https://www.oregon.gov/boa)
     """, None), # Keep key slightly different if needed, or ensure unique

    ("Reactivating or Reinstating a CPA License", # Key is now unique
     """
     Steps depend on license status/duration:

     * **Inactive:** Catch up CPE (min 32hrs), apply, pay fee.
     * **Lapsed (<2 yrs):** ~80 CPE hrs + penalty + OR ethics.
     * **Lapsed (>2 yrs):** More CPE required, scaling up.
     * **Lapsed (6+ yrs):** May require re-examination. Contact OR Board!
     * **Out-of-State:** Reciprocity available if license active/reactivatable elsewhere.
     * **Source:** [OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791)
     """, None),

    ("Non-CPA Accounting Roles", # Key is now unique
     """
     No state license needed unless using "CPA" title. Focus on employer needs:

     * **Strengthen Profile:** Recent courses/certs (PCC), relevant skills (Excel, QB), consider optional certs (CMA, CIA, EA).
     * **Highlight Experience:** Combine past experience with evidence of current skills.
     * **Job Descriptions:** Tailor applications to specific role requirements.
     """, None),

    # Section 3
    ("Oregon Society of CPAs (OSCPA) – CPE", # Key is unique
     """
     Premier local resource for Continuing Professional Education.

     * **Offerings:** Courses, seminars, conferences (many formats).
     * **Benefit:** Excellent for refreshers (GAAP/Tax updates) & networking.
     * **Membership:** Affiliate options often available for non-CPAs/candidates.
     * **Resource:** [OSCPA CPE Catalog](https://www.orcpa.org/cpe)
     """, None),

    ("College and University Programs (Portland Area)", # Key is unique
     """
     Local structured programs for refreshers or CPA requirements.

     * **PSU:** Post-Bacc Accounting Certificate. Strong reputation.
     * **PCC:** Accelerated Accounting Certificate (fundamentals & tech).
     * **Linfield:** Online Post-Bacc Accounting Certificate.
     * **Resource:** See links on "Refresh Skills" page.
     """, ("pages/4_📚_Refresh_Skills_Resources.py", "Go to Refresh Skills Page", "📚")),

    ("CPA Exam Prep Courses (Online and Hybrid)", # Key is unique
     """
     Essential if pursuing the CPA license.

     * **Providers:** Becker, Wiley, UWorld Roger, Gleim, etc.
     * **Format:** Usually self-paced online video lectures, practice questions, simulations.
     * **Cost:** Significant investment, but comprehensive. Check for discounts (OSCPA/Alumni).
     """, None),

    ("AICPA Resources", # Key is unique
     """
     Leverage resources from the national professional organization.

     * **Exam:** Free Exam Blueprints & Sample Tests on aicpa.org.
     * **CPE:** AICPA Store offers webcasts, self-study, certificate programs.
     * **News:** Journal of Accountancy, FM Magazine.
     * **Resource:** [AICPA CPE & Learning](https://www.aicpa-cima.com/cpe-learning)
     """, None),

    ("Online Refresher Courses & MOOCs", # Key is unique
     """
     Flexible and often low-cost options for specific topics.

     * **Platforms:** Coursera, edX (University courses); LinkedIn Learning, Udemy (Practical skills - Excel, QB).
     * **Benefit:** Target specific knowledge gaps at your own pace.
     """, ("pages/4_📚_Refresh_Skills_Resources.py", "Go to Refresh Skills Page", "📚")),


    ("Mentorship and Study Groups", # Key is unique
     """
     Learn from and with others.

     * **Formal:** Check OSCPA for mentorship programs.
     * **Informal:** Network for coffee chats; form study groups with peers from courses.
     * **Benefit:** Gain real-world insights and support.
     """, None),

    ("Keeping Skills Current (Self-Directed)", # Key is unique
     """
     Proactively practice and learn independently.

     * **Tech:** Use free software trials (QB); practice advanced Excel with online datasets/tutorials.
     * **Reading:** Follow industry news (Accounting Today), firm publications.
     * **Finance:** Supplement with basic finance concepts if needed (online courses).
     """, None),

    # Section 4
    ("Leverage Niche and Local Job Boards", # Key is unique
     """
     Expand beyond Indeed/LinkedIn.

     * **Portland Specific:** Mac's List (SMB/Non-Profit), OSCPA Career Center.
     * **Staffing Agencies:** Robert Half, Ledgent, etc. (check their sites).
     * **Government:** City/County/State job portals.
     * **Remote:** FlexJobs, We Work Remotely, Accountingfly.
     * **Resource:** [Mac's List](https://www.macslist.org/)
     """, None),

    ("Optimize Your Resume for Applicant Tracking Systems (ATS)", # Key is unique
     """
     Get past the initial computer screening.

     * **Keywords:** Match terms from job descriptions (GAAP, Reconciliation, Month-End Close, software names).
     * **Tailor:** Customize for each application.
     * **Clarity:** Ensure it's still readable and compelling for humans.
     """, None),

    ("Utilize LinkedIn Effectively", # Key is unique
     """
     Crucial for networking and job searching.

     * **Profile:** Update summary, headline, experience. Set "Open to Work".
     * **Connect:** Reach out to recruiters, local pros, alumni. Personalize requests.
     * **Engage:** Follow companies, share relevant content, join groups.
     """, None),

    ("Tap into Networking for Job Leads", # Key is unique
     """
     Unlock the "hidden job market".

     * **Be Specific:** Tell contacts what roles you're seeking.
     * **Ask:** Request informational interviews or referrals.
     * **Attend:** Use events (OSCPA, IMA) to meet potential hiring managers.
     """, None),

    ("Consider Informational Interviews", # Key is unique
     """
     Low-pressure way to learn and connect.

     * **Reach Out:** Contact people in target roles/companies via LinkedIn.
     * **Goal:** Learn about their work, company culture, needed skills. May lead to future referrals.
     """, None),

    ("Be Prepared to Address the Gap Positively", # Key is unique
     """
     Frame your career break as an asset.

     * **Narrative:** Confidently explain transition, highlighting transferable skills gained.
     * **Answer "Why Return?":** Show genuine enthusiasm for accounting.
     * **Show Action:** Mention recent courses, volunteer work, networking efforts.
     """, None),

    ("Use Staffing Firms and Recruiters", # Key is unique
     """
     Recruiters can be valuable allies.

     * **Connect:** Register with multiple relevant firms (Robert Half, Accountemps, Parker+Lynch, etc.).
     * **Communicate:** Be clear about goals, skills, flexibility. Follow up.
     * **Temp-to-Hire:** Can be a great re-entry strategy.
     """, None),

    ("Remote Work Considerations", # Key is unique
     """
     If seeking remote roles:

     * **Logistics:** Understand time zones, potential travel, state nexus issues.
     * **Showcase:** Highlight remote work skills (communication, self-discipline, tech proficiency).
     * **Competition:** Remote roles attract more applicants; tailor applications strongly.
     """, None),

    ("Salary Research and Negotiation", # Key is unique
     """
     Know your worth in the Portland market.

     * **Benchmark:** Use resources like Robert Half Salary Guide.
     * **Flexibility:** May start slightly lower, but aim for market rate based on skills/experience level sought.
     * **Negotiate:** Focus on total compensation (benefits, flexibility, training support) once offer is made.
     """, None),

    ("Persistence and Volume", # Key is unique
     """
     Job searching is often a numbers game.

     * **Routine:** Set aside time daily/weekly for searching and applying.
     * **Track:** Use a spreadsheet to manage applications & follow-ups.
     * **Stay Positive:** Rejection is normal. Learn and adapt. Accounting skills are in demand!
     """, None),

    # Section 5
    ("Oregon Society of CPAs (OSCPA)", # Key is unique
     """
     Primary state association for CPAs & accounting professionals.

     * **Value:** Networking, CPE, career resources, advocacy.
     * **Get Involved:** Join as member (Affiliate possible), attend chapter meetings/events.
     * **Resource:** [OSCPA Website](https://www.orcpa.org/)
     """, None),

    ("Portland Chapter of the Institute of Management Accountants (IMA)", # Key is unique
     """
     Focuses on management accounting (CMA credential).

     * **Value:** Networking with industry professionals (corporate roles), CPE events.
     * **Get Involved:** Attend monthly chapter meetings/events. Open to all.
     * **Resource:** [IMA Portland Chapter](https://portland.imanet.org/)
     """, None),

    ("Accounting & Finance Women’s Alliance (AFWA) – Portland", # Key is unique
     """
     Supports women in the profession (open to all).

     * **Value:** Networking, mentorship, leadership development, support.
     * **Get Involved:** Check for local chapter activity and events.
     * **Resource:** Search "AFWA Portland"
     """, None),

    ("Institute of Internal Auditors (IIA) – Portland Chapter", # Key is unique
     """
     For those interested in internal audit roles (CIA credential).

     * **Value:** Networking with internal auditors, specialized CPE.
     * **Get Involved:** Attend chapter meetings/events if internal audit is a target.
     * **Resource:** [IIA Portland Chapter](https://chapters.theiia.org/portland/Pages/default.aspx)
     """, None),

    ("ISACA (Information Systems Audit and Control Association) – Portland Chapter", # Key is unique
     """
     Focuses on IT audit, governance, risk, security (CISA credential).

     * **Value:** Relevant if interested in roles bridging accounting and IT/systems.
     * **Get Involved:** Attend events if interested in this niche.
     * **Resource:** Search "ISACA Portland Chapter"
     """, None),

    ("Other Associations / Bookkeeping Groups", # Key is unique
     """
     Groups tailored to specific niches.

     * **Examples:** Oregon Association of Independent Accountants (OAIA), QuickBooks Meetups.
     * **Value:** Useful for freelance/bookkeeping focus.
     """, None),

    ("Meetup.com Networking Groups", # Key is unique
     """
     Informal local groups.

     * **Search:** Look for "Portland Finance," "PDX Accounting," "Bookkeeping" groups.
     * **Value:** Casual networking opportunities. Activity varies.
     """, None),

    ("Oregon Society of Tax Consultants (OSTC)", # Key is unique
     """
     For tax preparers (CPAs, EAs, Licensed Tax Consultants).

     * **Value:** Networking and education focused purely on tax.
     * **Get Involved:** Attend chapter meetings if targeting tax roles.
     * **Resource:** Search "OSTC Oregon"
     """, None),

    ("Volunteer for Professional Events", # Key is unique
     """
     Great way to meet people and contribute.

     * **Action:** Offer to help at OSCPA/IMA events, committees, or university accounting clubs.
     * **Benefit:** Increased visibility and connections.
     """, None),

    ("Social Media and Online Communities", # Key is unique
     """
     Engage where professionals gather online.

     * **LinkedIn:** Groups, follow companies/influencers, share content.
     * **Other:** Subreddits (r/Accounting), Facebook groups (search locally).
     """, None),

    ("Networking Approach", # Key is unique
     """
     Be strategic and genuine.

     * **Prepare:** Have a concise intro ("elevator pitch"). Get personal business cards.
     * **Engage:** Ask questions, listen actively.
     * **Follow Up:** Connect on LinkedIn, send brief thank-you notes.
     """, None),

    # Section 6
    ("Accounting Career Fairs ('Meet the Firms' events)", # Key is unique
     """
     Primarily student-focused, but often accessible.

     * **Events:** PSU/UO/OSU host fall "Meet the Firms" & often a joint Spring Expo in Portland.
     * **Strategy:** Attend respectfully, explain you're a returning professional, ask about experienced roles. Collect contacts.
     * **Resource:** Check university career center websites.
     """, None),

    ("OSCPA Career Showcase", # Key is unique
     """
     Annual OSCPA event (usually Sept) connecting students & employers.

     * **Strategy:** Inquire with OSCPA about attending as a professional, or attend panels if open. Great visibility to many firms/companies.
     * **Resource:** [OSCPA Events](https://www.orcpa.org/events/event_list.asp)
     """, None),

    ("General Job Fairs in Portland", # Key is unique
     """
     Broader fairs sometimes featuring accounting/finance roles.

     * **Sources:** Check WorkSource Oregon, Urban League of Portland, local college job fairs (PCC often open to public).
     """, None),

    ("Meetups and Informal Groups", # Key is unique
     """
     Casual networking opportunities.

     * **Sources:** Meetup.com, Eventbrite (search "finance networking portland"), tech/startup events.
     """, None),

    ("Professional Conferences", # Key is unique
     """
     In-depth learning and high-level networking (usually paid).

     * **Sources:** OSCPA topic-specific conferences (A&A, NFP, Tech), national AICPA/IMA conferences if local/regional.
     """, None),

    ("Career Development Workshops", # Key is unique
     """
     Focus on job search skills.

     * **Sources:** Look for resume/interview workshops from OSCPA, WorkSource Oregon, professional groups, alumni associations.
     """, None),

    ("Making the Most of Career Fairs/Events", # Key is unique
     """
     Maximize your impact.

     * **Prep:** Research attending employers. Dress professionally. Bring resumes/cards.
     * **Engage:** Have focused conversations. Ask good questions.
     * **Follow Up:** Send prompt thank-you notes/LinkedIn requests to key contacts.
     """, None),

    ("Follow Community Calendars", # Key is unique
     """
     Stay informed about upcoming opportunities.

     * **Sources:** OSCPA Events, Portland Business Journal Events, Eventbrite, University Alumni calendars.
     """, None)
]

# Extract just the keys in order for state management and progress calculation
expander_keys_ordered = [item[0] for item in section_content_map]
total_sections = len(expander_keys_ordered)

# --- Initialize Session State for Checkboxes ---
for key in expander_keys_ordered:
    if key not in st.session_state:
        st.session_state[key] = False

# --- Calculate Progress ---
completed_sections = sum(st.session_state[key] for key in expander_keys_ordered)

# --- Display Progress Tracker at the Top ---
st.markdown(f"### Your Progress: {completed_sections} / {total_sections} sections reviewed")
progress_value_float = completed_sections / total_sections if total_sections > 0 else 0
st.progress(progress_value_float)
st.divider()

# --- App Title and Introduction ---
st.title("📖 Roadmap to Re-Entering Accounting (Detailed Guide)") # Added Icon
st.markdown("""
Welcome! This guide helps you return to accounting in Portland, OR. Work through the sections sequentially.
**You must mark a section as reviewed to unlock the checkbox for the next section.** Read ahead anytime, but complete in order.
""")
st.divider()

# --- Define Section Headers and Key Groupings ---
# Map header titles to the first key in that section group
section_headers = {
    "Evaluate Your Career Goals (CPA vs. Non-CPA)": "1. Step-by-Step Plan to Return to Accounting",
    "CPA Licensure in Oregon (New License)": "2. Oregon Certification and Licensing Requirements",
    "Oregon Society of CPAs (OSCPA) – CPE": "3. Continuing Education & Certification Prep Resources",
    "Leverage Niche and Local Job Boards": "4. Job Search Strategies and Platforms Tailored to Portland",
    "Oregon Society of CPAs (OSCPA)": "5. Networking Opportunities and Local Accounting Organizations",
    "Accounting Career Fairs ('Meet the Firms' events)": "6. Local Meetups, Associations, and Career Fairs"
}
current_header = None

# --- Loop Through Content Map to Display Expanders and Checkboxes ---
last_checked_index = -1
for i, key in enumerate(expander_keys_ordered):
    if st.session_state[key]:
        last_checked_index = i
    # else: # Optional: If you want strict locking (must be consecutive)
    #     break

# Now render based on the last completed index
previous_item_completed = True # Start with the first item assumed enabled

for i, (key, content, link_info) in enumerate(section_content_map):

    # Print header if this is the start of a new section
    if key in section_headers and section_headers[key] != current_header:
        current_header = section_headers[key]
        st.header(current_header)

    # Determine if the checkbox for *this* item should be enabled
    # Enabled if it's the first item OR the previous item's state is True
    is_enabled = (i == 0) or st.session_state[expander_keys_ordered[i-1]]
    # More strict version: is_enabled = (i <= last_checked_index + 1) # Use this if you want to allow skipping ahead once unlocked

    with st.expander(key):
        # Display content
        st.markdown(content)

        # Display page link if provided
        if link_info:
            page_file, label, icon = link_info
            st.page_link(page_file, label=label, icon=icon)
            st.markdown("---") # Add separator after link

        # Display checkbox (conditionally enabled)
        help_text = "Mark section as reviewed to unlock the next."
        display_warning = False
        if not is_enabled:
             help_text = "Complete the previous section to enable this checkbox."
             display_warning = True # Show warning only if disabled

        # Add visual cue if section is locked
        if display_warning:
            st.warning("🔒 Complete the previous section to enable checkbox.", icon="🔒")

        st.checkbox("Mark as reviewed",
                     key=key,
                     disabled=not is_enabled,
                     help=help_text)

    # Update the flag for the next iteration (only relevant for strict sequential check)
    # previous_item_completed = st.session_state[key] # Use this if disabling based *only* on immediate predecessor

st.divider()

# --- Actionable Next Steps Recap & Conclusion (Render unconditionally) ---
st.header("✅ Actionable Next Steps Recap")
st.markdown("""
Here’s a checklist to guide your immediate actions:

* **Skill Up:** Enroll in a refresher course or start CPA review soon. Schedule regular study time.
* **Contact Oregon Board:** Clarify CPA status/requirements if applicable. Obtain necessary forms.
* **Join Organizations:** Sign up for OSCPA and/or IMA Portland. Plan to attend one event soon.
* **Network Outreach:** List 10 former contacts; reach out to reconnect. Aim for 3 coffee chats/calls in the next two months.
* **Resume Update:** Refresh resume this week. Seek feedback if possible.
* **Online Presence:** Update LinkedIn (set "Open to Work"). Engage weekly.
* **Job Search Routine:** Set up job alerts (Indeed, LinkedIn, Mac’s List). Aim to apply consistently (e.g., 5-10/week).
* **Career Fairs:** Register for upcoming relevant fairs (Spring Expo, Meet the Firms, OSCPA Showcase).
* **Continuing Ed:** Book at least one relevant CPE course/webinar soon.
* **Follow Up & Iterate:** Track contacts/applications. Follow up politely. Adjust approach based on results.
""")

st.divider()

st.success("""
**Good luck on your journey back into accounting!** With your background and a structured approach using these resources, you are positioning yourself for success. Portland has a strong market for accounting professionals. Stay persistent, engage with the community, and you'll be well on your way to your next role.
""")

st.divider()

# --- Sources (Render unconditionally) ---
st.subheader("Sources Referenced")
with st.expander("View Full Source List"):
    st.markdown("""
    * Oregon Board of Accountancy – CPA licensure requirements: [Oregon CPA Requirements 2024-2025](https://www.ais-cpa.com/oregon-cpa-requirements/)
    * Oregon Board of Accountancy – Rule changes (120 hours to sit): [Oregon Board Town Hall Meeting PDF](https://www.oregon.gov/boa/Documents/2023_Fall_Town_Hall_Meeting_Presentation.pdf)
    * Oregon Board of Accountancy – License reactivation and CPE: [Board of Accountancy CPE Page](https://www.oregon.gov/boa/Pages/CPE.aspx)
    * Oregon Board of Accountancy – Reinstatement Rules: [OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791)
    * Oregon Board of Accountancy - License Renewal Info: [Board of Accountancy Renewal Information](https://www.oregon.gov/boa/Pages/Renewal_Information.aspx)
    * Oregon Society of CPAs – Membership, Networking, Events: [OSCPA LinkedIn](https://www.linkedin.com/company/oregon-society-of-cpas/), [OSCPA Events List](https://www.orcpa.org/events/event_list.asp), [OSCPA Login Page](https://www.orcpa.org/login.aspx)
    * Institute of Management Accountants, Portland Chapter – Events, Networking: [IMA Portland Chapter Home](https://portland.imanet.org/)
    * FM Magazine (AICPA/CIMA) – Advice on returning to work: [How to re-enter finance after an extended leave](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html)
    * Mac’s List – Portland job board: [Mac's List Home](https://www.macslist.org/), [Portland Jobs on Mac's List](https://jobs.macslist.org/locations/7730-portland-or)
    * PSU/University Accounting Career Expo: [PSU Accounting & Finance Student Resources](https://www.pdx.edu/business/student-resources/accounting-finance-student-resources)
    * PCC Accelerated Accounting Certificate: [PCC Program Page](https://www.pcc.edu/programs/accounting/accelerated-accounting/)
    * PCC Accounting Fundamentals Series (via Ed2Go): [PCC Ed2Go Course](https://careertraining.ed2go.com/pcc/training-programs/accounting-fundamentals-series/)
    * Linfield University Online Accounting Certificate: [Linfield Program Page](https://www.linfield.edu/faculty/oce-only/accounting-certificate.html)
    * Journal of Accountancy - Article on graduate learning program: [Program to offer new accounting graduates...](https://www.journalofaccountancy.com/news/2023/oct/program-offer-new-accounting-graduates-chance-learn-while-they-earn.html)
    * FEI - Tips for returning professionals (example source): [Tips to accounting professionals returning to work](https://www.financialexecutives.org/FEI-Daily/November-2017/Tips-to-accounting-professionals-returning-to-work.aspx)
    * IIA Portland Chapter: [IIA Portland Chapter Website](https://chapters.theiia.org/portland/Pages/default.aspx)
    * Jones & Roth CPAs (attended PSU fair): [Jones & Roth Event Page](https://www.jrcpa.com/event/psu-accounting-career-fair-meet-the-firms-2/)
    * PSU Career Fairs: [PSU Career Services Fairs](https://www.pdx.edu/careers/career-fairs)
    * PCC Job Fairs: [PCC Career Services Fairs](https://www.pcc.edu/resources/careers/fairs/)
    * Urban League of Portland Career Fair: [ULPDX Career Fair Page](https://ulpdx.org/careerfair)
    * OSCPA Instagram (NFP Conf example): [OSCPA Instagram Post](https://www.instagram.com/p/C5o1o4jRufr/)
    * Reddit - Perspective on returning (Note: Used for general context, not direct advice): [Reddit r/Accounting Post](https://www.reddit.com/r/Accounting/comments/15z66u0/thinking_about_going_back_into_accounting_after_a/)
    """)