import streamlit as st

# --- Page Configuration ---
st.set_page_config(layout="wide", page_title="Re-Entering Accounting in Portland, OR")

# --- Define Keys for Checkboxes (Using Expander Labels for Uniqueness) ---
expander_keys = [
    # Section 1
    "Evaluate Your Career Goals (CPA vs. Non-CPA)", "Refresh Your Accounting Knowledge and Skills",
    "Address Education and Credentials Gaps", "Gain Recent Experience (Even in Small Doses)",
    "Rebuild Your Professional Network", "Update Your Resume and Narrative",
    "Start the Job Search (Targeted Approach)",
    # Section 2
    "CPA Licensure in Oregon (New License)", "Reactivating or Reinstating a CPA License",
    "Non-CPA Accounting Roles",
    # Section 3
    "Oregon Society of CPAs (OSCPA) – CPE", "College and University Programs (Portland Area)",
    "CPA Exam Prep Courses (Online and Hybrid)", "AICPA Resources",
    "Online Refresher Courses & MOOCs", "Mentorship and Study Groups",
    "Keeping Skills Current (Self-Directed)",
    # Section 4
    "Leverage Niche and Local Job Boards", "Optimize Your Resume for Applicant Tracking Systems (ATS)",
    "Utilize LinkedIn Effectively", "Tap into Networking for Job Leads",
    "Consider Informational Interviews", "Be Prepared to Address the Gap Positively",
    "Use Staffing Firms and Recruiters", "Remote Work Considerations",
    "Salary Research and Negotiation", "Persistence and Volume",
    # Section 5
    "Oregon Society of CPAs (OSCPA)", "Portland Chapter of the Institute of Management Accountants (IMA)",
    "Accounting & Finance Women’s Alliance (AFWA) – Portland", "Institute of Internal Auditors (IIA) – Portland Chapter",
    "ISACA (Information Systems Audit and Control Association) – Portland Chapter", "Other Associations / Bookkeeping Groups",
    "Meetup.com Networking Groups", "Oregon Society of Tax Consultants (OSTC)",
    "Volunteer for Professional Events", "Social Media and Online Communities",
    "Networking Approach",
    # Section 6
    "Accounting Career Fairs ('Meet the Firms' events)", "OSCPA Career Showcase",
    "General Job Fairs in Portland", "Meetups and Informal Groups",
    "Professional Conferences", "Career Development Workshops",
    "Making the Most of Career Fairs/Events", "Follow Community Calendars"
]
total_sections = len(expander_keys)

# --- Initialize Session State for Checkboxes (if not already done) ---
for key in expander_keys:
    if key not in st.session_state:
        st.session_state[key] = False

# --- Calculate Progress ---
completed_sections = sum(st.session_state[key] for key in expander_keys)
progress_value_float = completed_sections / total_sections if total_sections > 0 else 0
# Use integer 0-100 for HTML progress tag
progress_value_int = int(progress_value_float * 100)

# --- HTML & CSS for Fixed Header ---
# Adjust header_height_px if the content overlaps or has too much space
# This needs to be enough for the text, progress bar, padding, AND Streamlit's own top bar
# Experiment with this value (e.g., 60, 70, 80) if the spacing is off
effective_header_height_px = 75

# Note: Streamlit's own header bar is roughly 50-60px high.
# We position our fixed header slightly below that.
fixed_header_css_top_offset = "55px"

progress_bar_html = f"""
<style>
    .fixed-header {{
        position: fixed;
        top: {fixed_header_css_top_offset}; /* Position below Streamlit's default header */
        left: 0;
        width: 100%;
        background: white; /* White background to overlay content */
        padding: 10px 25px; /* Adjust padding as needed */
        z-index: 999;
        border-bottom: 1px solid #e0e0e0; /* Light border */
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); /* Subtle shadow */
    }}
    .fixed-header p {{
        margin-bottom: 8px; /* Space between text and bar */
        font-weight: 500; /* Slightly bolder text */
        font-size: 0.95rem; /* Adjust font size */
        color: #333; /* Darker text color */
    }}
    .fixed-header progress {{
        width: 100%; /* Make progress bar span width */
        height: 12px; /* Adjust height */
        appearance: none; /* Needed for custom styling in some browsers */
    }}
    /* Basic styling for the progress bar track (background) */
    .fixed-header progress::-webkit-progress-bar {{
        background-color: #eee;
        border-radius: 5px;
    }}
    /* Basic styling for the progress bar value (foreground) */
    .fixed-header progress::-webkit-progress-value {{
        background-color: #007bff; /* Blue color */
        border-radius: 5px;
        transition: width 0.2s ease-in-out;
    }}
    .fixed-header progress::-moz-progress-bar {{ /* Firefox */
        background-color: #007bff;
        border-radius: 5px;
        transition: width 0.2s ease-in-out;
    }}

    /* Add padding to the top of the main content block-container */
    /* This selector might change in future Streamlit versions */
    .main .block-container {{
        padding-top: {effective_header_height_px}px !important;
    }}
</style>

<div class="fixed-header">
    <p>Your Progress: {completed_sections} / {total_sections} sections reviewed</p>
    <progress value="{progress_value_int}" max="100"></progress>
</div>
"""

# Inject the HTML/CSS for the fixed header
st.markdown(progress_bar_html, unsafe_allow_html=True)

# --- App Title and Introduction (Content starts below the fixed header) ---
st.title("Roadmap to Re-Entering the Accounting Profession in Portland, Oregon")
st.markdown("""
Welcome! This guide is designed to help you navigate the process of transitioning back into the accounting field in the Portland, Oregon area after a career break.
It covers key steps, requirements, resources, and strategies to support your journey, whether you're aiming for a CPA license or other accounting roles.
Use the sections below to explore specific topics. Check the box within each expanded section once you've reviewed it to track your progress in the bar above.
""")
st.divider()

# --- Section 1: Step-by-Step Plan ---
st.header("1. Step-by-Step Plan to Return to Accounting")

# (Keep all the expander sections exactly as in the previous version)
# Example structure:
exp_key = "Evaluate Your Career Goals (CPA vs. Non-CPA)"
with st.expander(exp_key):
    st.markdown("""
    Begin by clarifying whether you want to pursue a Certified Public Accountant (CPA) license or aim for accounting roles that don't require CPA certification. This decision will shape your next steps.

    * **Factors to Consider:** Kinds of jobs desired (public accounting vs. private industry), time/effort for CPA, long-term career growth.
    * **CPA Path:** Opens doors to higher-level roles, especially in public accounting and some corporate positions.
    * **Non-CPA Path:** Roles like bookkeeper, staff accountant, accounting manager can be rewarding but might have different advancement paths.
    * **Importance:** Knowing your target path helps prioritize licensing, education, and job search efforts.
    """)
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")

exp_key = "Refresh Your Accounting Knowledge and Skills"
with st.expander(exp_key):
    st.markdown("""
    After 10+ years away, updating your knowledge is crucial.

    * **Accounting Principles & Standards:** Review major updates in GAAP or tax law (e.g., revenue recognition, lease accounting).
    * **Technology:** Familiarize yourself with current software (QuickBooks, ERPs like Oracle/NetSuite/SAP) and advanced Excel. Data analysis tools are increasingly common. Consider certifications (e.g., QuickBooks Online).
    * **Continuing Education:** Enroll in refresher courses or CPE seminars. Portland Community College (PCC) offers an [Accelerated Accounting certificate](https://www.pcc.edu/programs/accounting/accelerated-accounting/) covering basics and tech (Excel, payroll).
    * **Self-Study:** Read trade publications (e.g., *Journal of Accountancy*, *FM Magazine*), subscribe to accounting news, engage with professional networks. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
    """)
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")

# ... include ALL other expander sections from Section 1 to 6 here ...
# Section 1 continued...
exp_key = "Address Education and Credentials Gaps"
with st.expander(exp_key):
    st.markdown("""Determine necessary updates for your credentials... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Gain Recent Experience (Even in Small Doses)"
with st.expander(exp_key):
    st.markdown("""Bridge the experience gap with current activities... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Rebuild Your Professional Network"
with st.expander(exp_key):
    st.markdown("""Networking is critical for finding opportunities... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Update Your Resume and Narrative"
with st.expander(exp_key):
    st.markdown("""Craft a compelling story for employers... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Start the Job Search (Targeted Approach)"
with st.expander(exp_key):
    st.markdown("""Begin applying strategically... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
st.divider()

# Section 2
st.header("2. Oregon Certification and Licensing Requirements")
exp_key = "CPA Licensure in Oregon (New License)"
with st.expander(exp_key):
    st.markdown("""Requirements set by the Oregon Board of Accountancy... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Reactivating or Reinstating a CPA License"
with st.expander(exp_key):
    st.markdown("""Steps depend on license status and duration... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Non-CPA Accounting Roles"
with st.expander(exp_key):
    st.markdown("""Oregon does not require licenses for most private industry... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
st.divider()

# Section 3
st.header("3. Continuing Education & Certification Prep Resources")
exp_key = "Oregon Society of CPAs (OSCPA) – CPE"
with st.expander(exp_key):
    st.markdown("""Premier resource for ongoing education... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "College and University Programs (Portland Area)"
with st.expander(exp_key):
    st.markdown("""Local options for refreshers or fulfilling requirements... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "CPA Exam Prep Courses (Online and Hybrid)"
with st.expander(exp_key):
    st.markdown("""Essential for passing the CPA exam... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "AICPA Resources"
with st.expander(exp_key):
    st.markdown("""Use resources from the American Institute of CPAs... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Online Refresher Courses & MOOCs"
with st.expander(exp_key):
    st.markdown("""Flexible, often low-cost options for targeted learning... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Mentorship and Study Groups"
with st.expander(exp_key):
    st.markdown("""Learn from others... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Keeping Skills Current (Self-Directed)"
with st.expander(exp_key):
    st.markdown("""Proactively improve key skills... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
st.divider()

# Section 4
st.header("4. Job Search Strategies and Platforms Tailored to Portland")
exp_key = "Leverage Niche and Local Job Boards"
with st.expander(exp_key):
    st.markdown("""Go beyond major sites like Indeed/LinkedIn... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Optimize Your Resume for Applicant Tracking Systems (ATS)"
with st.expander(exp_key):
    st.markdown("""Increase chances of getting past initial screening... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Utilize LinkedIn Effectively"
with st.expander(exp_key):
    st.markdown("""Essential for professional job searching... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Tap into Networking for Job Leads"
with st.expander(exp_key):
    st.markdown("""Many jobs are found through connections... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Consider Informational Interviews"
with st.expander(exp_key):
    st.markdown("""Learn and make connections without direct job pressure... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Be Prepared to Address the Gap Positively"
with st.expander(exp_key):
    st.markdown("""Have a confident explanation ready for applications/interviews... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Use Staffing Firms and Recruiters"
with st.expander(exp_key):
    st.markdown("""Agencies can be allies... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Remote Work Considerations"
with st.expander(exp_key):
    st.markdown("""If pursuing remote roles... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Salary Research and Negotiation"
with st.expander(exp_key):
    st.markdown("""Know your worth in the current market... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Persistence and Volume"
with st.expander(exp_key):
    st.markdown("""Job searching takes time and effort... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
st.divider()

# Section 5
st.header("5. Networking Opportunities and Local Accounting Organizations")
exp_key = "Oregon Society of CPAs (OSCPA)"
with st.expander(exp_key):
    st.markdown("""Statewide association, cornerstone for networking... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Portland Chapter of the Institute of Management Accountants (IMA)"
with st.expander(exp_key):
    st.markdown("""Global association for accountants in business (CMA focus)... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Accounting & Finance Women’s Alliance (AFWA) – Portland"
with st.expander(exp_key):
    st.markdown("""Supports women in accounting/finance (open to all)... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Institute of Internal Auditors (IIA) – Portland Chapter"
with st.expander(exp_key):
    st.markdown("""For those interested in internal audit or risk advisory... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "ISACA (Information Systems Audit and Control Association) – Portland Chapter"
with st.expander(exp_key):
    st.markdown("""More IT-audit focused, relevant if interested in tech intersection... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Other Associations / Bookkeeping Groups"
with st.expander(exp_key):
    st.markdown("""Groups for bookkeeping and small business accounting services... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Meetup.com Networking Groups"
with st.expander(exp_key):
    st.markdown("""Informal networking opportunities... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Oregon Society of Tax Consultants (OSTC)"
with st.expander(exp_key):
    st.markdown("""For those leaning towards tax roles... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Volunteer for Professional Events"
with st.expander(exp_key):
    st.markdown("""Overlooked way to network and get noticed... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Social Media and Online Communities"
with st.expander(exp_key):
    st.markdown("""Engage online... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Networking Approach"
with st.expander(exp_key):
    st.markdown("""Strategy for attending events... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
st.divider()

# Section 6
st.header("6. Local Meetups, Associations, and Career Fairs")
exp_key = "Accounting Career Fairs ('Meet the Firms' events)"
with st.expander(exp_key):
    st.markdown("""Primarily student-focused, but potentially accessible... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "OSCPA Career Showcase"
with st.expander(exp_key):
    st.markdown("""Annual OSCPA event, typically September at Oregon Convention Center... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "General Job Fairs in Portland"
with st.expander(exp_key):
    st.markdown("""Broader fairs that may include accounting/finance roles... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Meetups and Informal Groups"
with st.expander(exp_key):
    st.markdown("""Casual networking beyond formal fairs... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Professional Conferences"
with st.expander(exp_key):
    st.markdown("""Deeper dive into topics + networking (usually requires fee)... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Career Development Workshops"
with st.expander(exp_key):
    st.markdown("""Skill-building and job search support... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Making the Most of Career Fairs/Events"
with st.expander(exp_key):
    st.markdown("""Tips for maximizing impact... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
exp_key = "Follow Community Calendars"
with st.expander(exp_key):
    st.markdown("""Stay informed about upcoming events... (content omitted for brevity)""")
    st.checkbox("Mark as reviewed", key=exp_key, help="Check this box to update your progress tracker.")
st.divider()

# --- Section 7: Actionable Next Steps Recap (Not included in progress tracker) ---
st.header("Actionable Next Steps Recap")
# (Content as before)
st.markdown("""
Here’s a checklist to guide your immediate actions:
* **Skill Up:** Enroll in a refresher course or start CPA review soon... (content omitted for brevity)
""")
st.divider()

# --- Conclusion (Not included in progress tracker) ---
st.success("""
**Good luck on your journey back into accounting!** ... (content omitted for brevity)
""")
st.divider()

# --- Sources (Not included in progress tracker) ---
st.subheader("Sources Referenced")
with st.expander("View Full Source List"):
    # (Content as before)
    st.markdown("""
    * Oregon Board of Accountancy – CPA licensure requirements: ... (content omitted for brevity)
    """)