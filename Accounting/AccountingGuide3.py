import streamlit as st

# --- Page Configuration ---
# Set page config in the main app file, it often applies globally
st.set_page_config(layout="wide", page_title="Re-Entering Accounting Guide")

# --- Define Keys IN ORDER & Map to Content/Links ---
# Structure: (key, content_markdown, list_of_link_tuples_or_None)
# Link tuple: (target_page_file, label, icon)
section_content_map = [
    # Section 1
    ("Evaluate Your Career Goals (CPA vs. Non-CPA)",
     """
     Begin by clarifying whether you want to pursue a Certified Public Accountant (CPA) license or aim for accounting roles that don't require CPA certification. This decision will shape your next steps.

     * **Factors to Consider:** Kinds of jobs desired (public accounting vs. private industry), time/effort for CPA, long-term career growth.
     * **CPA Path:** Opens doors to higher-level roles, especially in public accounting and some corporate positions.
     * **Non-CPA Path:** Roles like bookkeeper, staff accountant, accounting manager can be rewarding but might have different advancement paths.
     * **Importance:** Knowing your target path helps prioritize licensing, education, and job search efforts.
     """,
     [ # Now a list, containing one link tuple
         ("Accounting/pages/3_🎯_Career_Goal_Evaluation.py", "**➡️ Go to Detailed Career Goal Evaluation Page**", "🎯"),
         # Optionally add the visual link here too if desired, but it might be less relevant
         # ("pages/5_✨_Visual_Career_Paths.py", "**✨ Switch to Visual Career Path View**", "✨")
     ]),

    ("Refresh Your Accounting Knowledge and Skills",
     """
     After 10+ years away, updating your knowledge is crucial. Key areas include:

     * **Accounting Principles & Standards:** Review major updates (e.g., ASC 606 Rev Rec, ASC 842 Leases, Tax Law changes).
     * **Technology:** Familiarize yourself with current software (QuickBooks, ERPs) & advanced Excel.
     * **Continuing Education:** Enroll in refresher courses or CPE seminars.
     * **Self-Study:** Read publications, follow news, network.
     """,
     [ # Now a list, containing TWO link tuples
         ("pages/4_📚_Refresh_Skills_Resources.py", "**➡️ Go to Detailed Skills Refresh Resources Page**", "📚"),
         ("pages/6_💡_Visual_Skills_Refresh.py", "**✨ Switch to Visual Resource Guide**", "💡") # Added the new link here
     ]),

    ("Address Education and Credentials Gaps",
     """
     Determine necessary updates for your credentials.

     * **CPA Path (New License):** Requires 150 semester hours (incl. specific courses), passing the Uniform CPA Exam, and supervised experience. Consider post-bacc certs (PSU, Linfield) if needed.
     * **Prior CPA License Reactivation:** Contact Oregon Board. Requires CPE catch-up, fees. Requirements vary based on inactive/lapsed duration. Lapsed 6+ years may require re-exam.
     * **Alternative Certifications (Non-CPA):** Consider CMA (management acct.), CIA (internal audit), EA (tax) to boost profile.
     """, None), # No links for this one

    # ... (Keep all other tuples in section_content_map exactly as they were before) ...
    # Example for one more:
     ("Gain Recent Experience (Even in Small Doses)",
     """
     Bridge the experience gap with current activities.

     * **Volunteer/Freelance:** Offer skills to nonprofits (Hands On Greater Portland), join VITA tax program, take small gigs.
     * **Returnships/Internships:** Look for formal programs or propose project work.
     * **Temp/Contract:** Use staffing agencies (Robert Half, Ledgent) for short-term roles.
     """, None), # Still None

    # MAKE SURE ALL OTHER ENTRIES IN section_content_map ARE PRESENT HERE
    # (Content Omitted for Brevity - Use your previous full map)
    # Section 2 Keys...
    ("CPA Licensure in Oregon (New License)", """ ... """, None),
    ("Reactivating or Reinstating a CPA License", """ ... """, None),
    ("Non-CPA Accounting Roles", """ ... """, None),
    # Section 3 Keys...
    ("Oregon Society of CPAs (OSCPA) – CPE", """ ... """, None),
    ("College and University Programs (Portland Area)", """ ... """, [("pages/4_📚_Refresh_Skills_Resources.py", "Go to Refresh Skills Page", "📚")]), # Keep original link style if only one
    ("CPA Exam Prep Courses (Online and Hybrid)", """ ... """, None),
    ("AICPA Resources", """ ... """, None),
    ("Online Refresher Courses & MOOCs", """ ... """, [("pages/4_📚_Refresh_Skills_Resources.py", "Go to Refresh Skills Page", "📚")]), # Keep original link style if only one
    ("Mentorship and Study Groups", """ ... """, None),
    ("Keeping Skills Current (Self-Directed)", """ ... """, None),
    # Section 4 Keys...
    ("Leverage Niche and Local Job Boards", """ ... """, None),
    ("Optimize Your Resume for Applicant Tracking Systems (ATS)", """ ... """, None),
    ("Utilize LinkedIn Effectively", """ ... """, None),
    ("Tap into Networking for Job Leads", """ ... """, None),
    ("Consider Informational Interviews", """ ... """, None),
    ("Be Prepared to Address the Gap Positively", """ ... """, None),
    ("Use Staffing Firms and Recruiters", """ ... """, None),
    ("Remote Work Considerations", """ ... """, None),
    ("Salary Research and Negotiation", """ ... """, None),
    ("Persistence and Volume", """ ... """, None),
    # Section 5 Keys...
    ("Oregon Society of CPAs (OSCPA)", """ ... """, None),
    ("Portland Chapter of the Institute of Management Accountants (IMA)", """ ... """, None),
    ("Accounting & Finance Women’s Alliance (AFWA) – Portland", """ ... """, None),
    ("Institute of Internal Auditors (IIA) – Portland Chapter", """ ... """, None),
    ("ISACA (Information Systems Audit and Control Association) – Portland Chapter", """ ... """, None),
    ("Other Associations / Bookkeeping Groups", """ ... """, None),
    ("Meetup.com Networking Groups", """ ... """, None),
    ("Oregon Society of Tax Consultants (OSTC)", """ ... """, None),
    ("Volunteer for Professional Events", """ ... """, None),
    ("Social Media and Online Communities", """ ... """, None),
    ("Networking Approach", """ ... """, None),
    # Section 6 Keys...
    ("Accounting Career Fairs ('Meet the Firms' events)", """ ... """, None),
    ("OSCPA Career Showcase", """ ... """, None),
    ("General Job Fairs in Portland", """ ... """, None),
    ("Meetups and Informal Groups", """ ... """, None),
    ("Professional Conferences", """ ... """, None),
    ("Career Development Workshops", """ ... """, None),
    ("Making the Most of Career Fairs/Events", """ ... """, None),
    ("Follow Community Calendars", """ ... """, None)
]


# --- Derive ordered keys list ---
expander_keys_ordered = [item[0] for item in section_content_map]
total_sections = len(expander_keys_ordered)

# --- Initialize Session State ---
for key in expander_keys_ordered:
    if key not in st.session_state:
        st.session_state[key] = False

# --- Calculate Progress ---
completed_sections = sum(st.session_state[key] for key in expander_keys_ordered)

# --- Display Progress Tracker ---
st.markdown(f"### Your Progress: {completed_sections} / {total_sections} sections reviewed")
progress_value_float = completed_sections / total_sections if total_sections > 0 else 0
st.progress(progress_value_float)
st.divider()

# --- App Title and Introduction ---
st.title("📖 Roadmap to Re-Entering Accounting (Detailed Guide)")
st.markdown("""
Welcome! This guide helps you return to accounting in Portland, OR. Work through the sections sequentially.
**You must mark a section as reviewed to open and review the next section.**
""")
st.divider()

# --- Define Section Headers ---
section_headers = {
    "Evaluate Your Career Goals (CPA vs. Non-CPA)": "1. Step-by-Step Plan to Return to Accounting",
    "CPA Licensure in Oregon (New License)": "2. Oregon Certification and Licensing Requirements",
    "Oregon Society of CPAs (OSCPA) – CPE": "3. Continuing Education & Certification Prep Resources",
    "Leverage Niche and Local Job Boards": "4. Job Search Strategies and Platforms Tailored to Portland",
    "Oregon Society of CPAs (OSCPA)": "5. Networking Opportunities and Local Accounting Organizations",
    "Accounting Career Fairs ('Meet the Firms' events)": "6. Local Meetups, Associations, and Career Fairs"
}
current_header = None

# --- Apply Custom CSS ---
st.markdown("""
<style>
    div.locked-section { /* Style for the locked placeholder */
        margin-left: 5px; padding: 10px 10px 10px 13px; border-left: 3px solid #e0e0e0;
        border-radius: 5px; background-color: white; opacity: 0.6; margin-bottom: 10px; }
    div.locked-section h4 { margin-bottom: 0.2rem; color: #555; }
    div.locked-section small { color: #777; }
    div[data-testid="stExpander"] { /* Style for unlocked expanders */
        border-left: 3px solid #ccc; margin-left: 5px; padding-left: 10px; margin-bottom: 10px; }
    h1, h2, h3 { margin-bottom: 0.5rem !important; } /* Reduce space below headers */
</style>
""", unsafe_allow_html=True)


# --- Loop Through Content Map ---
# MODIFY THIS LOOP TO HANDLE A LIST OF LINKS
for i, (key, content, link_info_list) in enumerate(section_content_map): # Renamed link_info to link_info_list

    # Print header if this is the start of a new section
    if key in section_headers and section_headers[key] != current_header:
        current_header = section_headers[key]
        if i > 0: st.markdown("<br>", unsafe_allow_html=True)
        st.header(current_header)

    # Determine if this section is unlocked
    is_unlocked = (i == 0) or st.session_state[expander_keys_ordered[i-1]]

    if is_unlocked:
        expander_label = f"✅ {key}" if st.session_state[key] else key
        with st.expander(expander_label):
            st.markdown(content)

            # --- MODIFIED LINK HANDLING ---
            if link_info_list: # Check if the list exists and has items
                st.markdown("---") # Separator before links
                # Iterate through the list of link tuples
                for link_tuple in link_info_list:
                    if len(link_tuple) == 3: # Ensure tuple is formatted correctly
                        page_file, label, icon = link_tuple
                        st.page_link(page_file, label=label, icon=icon)
                st.markdown("---") # Separator after links
            # --- END MODIFIED LINK HANDLING ---

            st.checkbox("Mark as reviewed", key=key, help="Mark section as reviewed to unlock the next.")
    else:
        # Render locked placeholder
        st.markdown(f"""
        <div class="locked-section">
            <h4>🔒 {key}</h4>
            <small><i>Complete the previous step to unlock this section.</i></small>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- Actionable Next Steps Recap & Conclusion ---
st.header("✅ Actionable Next Steps Recap")
#...(Keep Recap content as before)...
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

# --- Sources ---
st.subheader("Sources Referenced")
with st.expander("View Full Source List"):
     #...(Keep Sources content as before)...
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