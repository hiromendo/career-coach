import streamlit as st

# --- Page Configuration (Optional: Sets page title and layout) ---
st.set_page_config(layout="wide", page_title="Re-Entering Accounting in Portland, OR")

# --- App Title and Introduction ---
st.title("Roadmap to Re-Entering the Accounting Profession in Portland, Oregon")

st.markdown("""
Welcome! This guide is designed to help you navigate the process of transitioning back into the accounting field in the Portland, Oregon area after a career break.
It covers key steps, requirements, resources, and strategies to support your journey, whether you're aiming for a CPA license or other accounting roles.
Use the sections below to explore specific topics.
""")

st.divider() # Adds a horizontal line for separation

# --- Section 1: Step-by-Step Plan ---
st.header("1. Step-by-Step Plan to Return to Accounting")

with st.expander("Evaluate Your Career Goals (CPA vs. Non-CPA)"):
    st.markdown("""
    Begin by clarifying whether you want to pursue a Certified Public Accountant (CPA) license or aim for accounting roles that don't require CPA certification. This decision will shape your next steps.

    * **Factors to Consider:** Kinds of jobs desired (public accounting vs. private industry), time/effort for CPA, long-term career growth.
    * **CPA Path:** Opens doors to higher-level roles, especially in public accounting and some corporate positions.
    * **Non-CPA Path:** Roles like bookkeeper, staff accountant, accounting manager can be rewarding but might have different advancement paths.
    * **Importance:** Knowing your target path helps prioritize licensing, education, and job search efforts.
    """)

with st.expander("Refresh Your Accounting Knowledge and Skills"):
    st.markdown("""
    After 10+ years away, updating your knowledge is crucial.

    * **Accounting Principles & Standards:** Review major updates in GAAP or tax law (e.g., revenue recognition, lease accounting).
    * **Technology:** Familiarize yourself with current software (QuickBooks, ERPs like Oracle/NetSuite/SAP) and advanced Excel. Data analysis tools are increasingly common. Consider certifications (e.g., QuickBooks Online).
    * **Continuing Education:** Enroll in refresher courses or CPE seminars. Portland Community College (PCC) offers an [Accelerated Accounting certificate](https://www.pcc.edu/programs/accounting/accelerated-accounting/) covering basics and tech (Excel, payroll).
    * **Self-Study:** Read trade publications (e.g., *Journal of Accountancy*, *FM Magazine*), subscribe to accounting news, engage with professional networks. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
    """)

with st.expander("Address Education and Credentials Gaps"):
    st.markdown("""
    Determine necessary updates for your credentials.

    * **CPA Path (New License):**
        * **Oregon Education:** 150 semester hours (including bachelor's), with 24 upper-division accounting hours and 24 related business hours. [Source: Oregon CPA Requirements 2024-2025](https://www.ais-cpa.com/oregon-cpa-requirements/)
        * **Addressing Gaps:** If below 150 hours, consider additional coursework, post-baccalaureate certificates (e.g., [PSU Accounting Certificate](https://www.pdx.edu/business/certificate-programs), [Linfield University Online Certificate](https://www.linfield.edu/faculty/oce-only/accounting-certificate.html)), or a master's degree.
        * **CPA Exam:** Prepare for the Uniform CPA Exam (updated "Core + Discipline" model in 2024). Use review programs (Becker, Wiley, Roger, Gleim). [Source: PSU Accounting Resources](https://www.pdx.edu/business/student-resources/accounting-finance-student-resources). Self-study online is common.
    * **Prior CPA License Reactivation (if applicable):**
        * Research reactivation requirements with the Oregon Board of Accountancy.
        * Generally involves application, fees, and catching up on CPE (e.g., inactive requires 32+ hours including ethics). [Source: Oregon Board CPE](https://www.oregon.gov/boa/Pages/CPE.aspx)
        * Lapsed licenses require more CPE (scaling with lapse duration) and possibly a state ethics course. [Source: OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791)
        * **Caution:** Licenses lapsed over 6 years may expire, potentially requiring re-examination unless reciprocity applies. Contact the Board directly. [Source: OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791)
    * **Alternative Certifications (Non-CPA Path):**
        * Consider optional credentials like:
            * **CMA (Certified Management Accountant):** For corporate/industry roles (IMA).
            * **CIA (Certified Internal Auditor):** For internal audit roles (IIA).
            * **EA (Enrolled Agent):** For tax expertise (IRS).
        * These can differentiate you and demonstrate current knowledge. Studying for them also serves as a refresher.
    """)

with st.expander("Gain Recent Experience (Even in Small Doses)"):
    st.markdown("""
    Bridge the experience gap with current activities.

    * **Volunteer or Freelance:**
        * Offer bookkeeping/treasurer services to nonprofits (check Hands On Greater Portland) or community groups.
        * Participate in IRS VITA (Volunteer Income Tax Assistance) during tax season.
        * Undertake short-term freelance gigs (e.g., for small businesses).
    * **"Returnship" or Internship Programs:**
        * Look for formal return-to-work programs (less common but worth checking).
        * Propose project-based work to past contacts or employers. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
    * **Temp Agencies and Contract Roles:**
        * Register with accounting staffing firms in Portland (e.g., Robert Half, Aston Carter, Ledgent, Parker + Lynch).
        * Temporary roles (AP/AR clerk, staff accountant for month-end) provide current experience and can lead to permanent jobs.
    """)

with st.expander("Rebuild Your Professional Network"):
    st.markdown("""
    Networking is critical for finding opportunities.

    * **Reconnect:** Reach out to former colleagues, supervisors, and classmates in Portland.
    * **Join Associations:** Actively participate in local professional groups (see Section 5). Networking can uncover unadvertised jobs. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
    * **Attend Events:** Go to meetups, CPE seminars. Introduce yourself and your goals.
    * **Online Networking:** Update LinkedIn profile, connect with local professionals, join relevant LinkedIn groups.
    """)

with st.expander("Update Your Resume and Narrative"):
    st.markdown("""
    Craft a compelling story for employers.

    * **Highlight Past Accomplishments:** Emphasize achievements from previous accounting roles.
    * **Showcase Recent Efforts:** Include recent courses, certifications, volunteer work, or projects (dated 2024-2025).
    * **Address the Break Positively:** Be transparent but frame the break constructively. Mention transferable skills gained (e.g., analysis, communication from marketing). Example: "2014–2025: Career period focused on digital marketing, developing strong analytical and client communication skills."
    * **Emphasize Transferable Skills:** Connect skills from marketing (analysis, software use, project management) to accounting needs. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
    * **Cover Letter Narrative:** Briefly explain your transition back, highlighting enthusiasm and enhanced skills. Avoid apologizing; focus on current value.
    """)

with st.expander("Start the Job Search (Targeted Approach)"):
    st.markdown("""
    Begin applying strategically.

    * **Target Appropriate Roles:** Consider roles slightly below your previous peak to re-enter, with potential for quick advancement.
    * **Leverage Your Network:** Seek introductions and referrals.
    * **Be Open:** Consider remote and hybrid roles to broaden options.
    * **Continue Building Experience:** Maintain volunteer or contract work while searching.
    * **Proactive & Positive:** Stay persistent. Overcoming barriers is possible with the right strategy. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
    """)

st.divider()

# --- Section 2: Certification and Licensing ---
st.header("2. Oregon Certification and Licensing Requirements")

with st.expander("CPA Licensure in Oregon (New License)"):
    st.markdown("""
    Requirements set by the Oregon Board of Accountancy:

    * **Education:** Minimum 150 semester hours (incl. bachelor's degree). Must include 24 semester hours of upper-division accounting and 24 semester hours of related business courses. [Source: Oregon CPA Requirements 2024-2025](https://www.ais-cpa.com/oregon-cpa-requirements/), [Source: OR Board Town Hall](https://www.oregon.gov/boa/Documents/2023_Fall_Town_Hall_Meeting_Presentation.pdf).
    * **CPA Exam:** Pass the Uniform CPA Examination (new "Core + Discipline" format from 2024). Requires score of 75+ per section. Oregon allows sitting for the exam with 120 hours (degree + required courses), but 150 hours needed for license. [Source: OR Board Town Hall](https://www.oregon.gov/boa/Documents/2023_Fall_Town_Hall_Meeting_Presentation.pdf). Requires rigorous study (300-400+ hours). Pass a separate ethics exam (often AICPA Professional Ethics course). [Source: Oregon CPA Requirements 2024-2025](https://www.ais-cpa.com/oregon-cpa-requirements/).
    * **Experience:** 1 year (approx. 2,000 hours) full-time accounting experience supervised and verified by a licensed CPA (can be in public, industry, government, or academia). Check with Board if prior work qualifies; often needs to be recent or post-exam. [Source: Oregon CPA Requirements 2024-2025](https://www.ais-cpa.com/oregon-cpa-requirements/).
    * **Licensing Application:** Submit application, fees, transcripts, scores, experience verification, ethics proof. Requires 4 hours Oregon-specific ethics CPE for initial license/first renewal. [Source: OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791). Maintain active license via biennial renewal (80 hours CPE). [Source: OR Board Renewal Info](https://www.oregon.gov/boa/Pages/Renewal_Information.aspx).
    """)

with st.expander("Reactivating or Reinstating a CPA License"):
    st.markdown("""
    Steps depend on license status and duration:

    * **Inactive Oregon License:** Requires catching up on CPE (min. 32 hours incl. 4 ethics), application, and fee to reactivate. [Source: Oregon Board CPE](https://www.oregon.gov/boa/Pages/CPE.aspx). Must not have used CPA title improperly while inactive.
    * **Lapsed Oregon License:** Reinstatement possible. Requirements increase with time:
        * *Under 2 years:* Need full 80 CPE hours + penalty (e.g., 16 extra hours) + Oregon ethics course. [Source: OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791).
        * *Over 2 years:* CPE requirement increases (up to 160 hours + penalty for 4+ years lapse). [Source: OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791).
        * CPE must typically be completed within 12 months before application. Must affirm no unlawful practice during lapse. Pay back fees and penalties.
    * **Lapsed 6+ Years (Expired):** Reinstatement not automatic. May require re-examination (passing CPA exam again) or reciprocity if licensed elsewhere during the lapse. Contact the Oregon Board for specific guidance. [Source: OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791).
    * **Out-of-State CPAs:** Oregon offers reciprocity if your license from another state is active (or can be reactivated). Apply for Oregon license via reciprocity, meet requirements, possibly take Oregon law/ethics exam.
    * **Key Action:** Contact the Oregon Board of Accountancy directly for personalized guidance on reactivation/reinstatement.
    """)

with st.expander("Non-CPA Accounting Roles"):
    st.markdown("""
    Oregon does not require licenses for most private industry or government accounting jobs (accountant, bookkeeper, financial analyst, AP/AR specialist, etc.), unless you use the CPA title.

    * **Strengthening Your Profile (Career Tips, Not Legal Requirements):**
        * **Continuing Education Certificates:** Short certificates (e.g., PCC's) or courses reassure employers of up-to-date skills.
        * **Optional Certifications:** CMA, CIA, or EA can differentiate you (see Section 1). Consider listing "CPA (Inactive)" if applicable and allowed.
        * **Enrolled Agent (EA):** Useful for tax roles if not pursuing CPA. Requires passing IRS exam. Network via Oregon Association of Tax Consultants.
        * **Focus on Experience & Skills:** Highlight prior accounting experience and demonstrate current skills (software, Excel, regulations) through recent learning/projects. Discuss your upskilling efforts in interviews.
    * **Key Takeaway:** For non-CPA roles, focus on demonstrating qualifications valued by employers (experience, skills, recent training), rather than formal state licensing. Check job descriptions for specific requirements (e.g., degree, years of experience).
    """)

st.divider()

# --- Section 3: Education and Prep Resources ---
st.header("3. Continuing Education & Certification Prep Resources")

with st.expander("Oregon Society of CPAs (OSCPA) – CPE"):
    st.markdown("""
    Premier resource for ongoing education.

    * **Offerings:** Wide catalog of CPE courses, seminars, conferences (live, virtual, self-study). Open to members and non-members (fee difference).
    * **Benefits for Returners:** Take update courses (Accounting, Auditing, Tax Law) as refreshers. Shows initiative. Doubles as networking.
    * **Membership:** Consider joining OSCPA (Affiliate options available) for discounts and access. [Source: OSCPA Events](https://www.orcpa.org/events/event_list.asp).
    * **Ethics:** Provides Oregon Ethics Exam & Course needed for CPA licensure. [Source: PSU Accounting Resources](https://www.pdx.edu/business/student-resources/accounting-finance-student-resources).
    """)

with st.expander("College and University Programs (Portland Area)"):
    st.markdown("""
    Local options for refreshers or fulfilling requirements:

    * **Portland State University (PSU):**
        * School of Business offers courses (potentially non-degree).
        * Post-Baccalaureate Accounting Certificate helps meet 150-hour rule or refresh knowledge. [Source: Linfield University (mentions PSU's)](https://www.linfield.edu/faculty/oce-only/accounting-certificate.html).
    * **Portland Community College (PCC):**
        * [Accelerated Accounting certificate](https://www.pcc.edu/programs/accounting/accelerated-accounting/) (entry-level refresher).
        * Community Education classes (e.g., Small Business Accounting, Excel).
        * Online courses via Ed2Go partner (e.g., [Accounting Fundamentals Series](https://careertraining.ed2go.com/pcc/training-programs/accounting-fundamentals-series/)).
    * **Linfield University OCE:**
        * [Online Post-Baccalaureate Accounting Certificate](https://www.linfield.edu/faculty/oce-only/accounting-certificate.html). Flexible online option.
    * **Other Oregon Colleges (OSU, UO):** May offer online accounting courses via distance learning (e.g., OSU Ecampus).
    """)

with st.expander("CPA Exam Prep Courses (Online and Hybrid)"):
    st.markdown("""
    Essential for passing the CPA exam.

    * **Major Providers:** Becker, Wiley CPAexcel, UWorld Roger, Gleim, Kaplan. Offer updated materials for 2024 exam.
    * **Format:** Typically self-paced online modules, videos, testbanks. Comprehensive but costly (potential discounts via OSCPA/alumni networks). [Source: PSU Accounting Resources](https://www.pdx.edu/business/student-resources/accounting-finance-student-resources).
    * **Live Classes:** Less common, but inquire with OSCPA or local firms about live/live-online bootcamps or study groups.
    """)

with st.expander("AICPA Resources"):
    st.markdown("""
    Use resources from the American Institute of CPAs.

    * **Exam Blueprints & Sample Tests:** Free resources on aicpa.org explaining exam content.
    * **Potential Future Programs:** Keep an eye on initiatives like apprenticeship models for learning practical skills. [Source: AICPA Program News](https://www.journalofaccountancy.com/news/2023/oct/program-offer-new-accounting-graduates-chance-learn-while-they-earn.html).
    * **CMA Prep:** If pursuing CMA, IMA and providers like Wiley offer prep courses. Portland IMA chapter has resources. [Source: IMA Portland](https://portland.imanet.org/).
    """)

with st.expander("Online Refresher Courses & MOOCs"):
    st.markdown("""
    Flexible, often low-cost options for targeted learning.

    * **Coursera / edX:** University courses/specializations (e.g., Financial Accounting Fundamentals). Audit for free or pay for certificate.
    * **Udemy / LinkedIn Learning:** Practical courses on specific software (QuickBooks) or skills (Advanced Excel, Accounting Foundations). Good for resume/profile.
    * **AICPA CPE & Certificates:** Specialized certificates (Data Analytics, IFRS) or "Back to Basics" CPE bundles. On-demand courses via AICPA Store/CPALearning.
    * **Webinars & Workshops:** Free webinars from OSCPA/AICPA on updates. Check WorkSource Oregon or nonprofits for return-to-work programs (may cover general skills).
    """)

with st.expander("Mentorship and Study Groups"):
    st.markdown("""
    Learn from others.

    * **Formal Programs:** Inquire with OSCPA or Oregon Board about mentorship programs for candidates/returners. OSCPA has student/new CPA mentorship.
    * **Informal Mentoring:** Connect with practicing CPAs for coffee chats to discuss industry changes and real-world practices.
    * **Study Groups:** Form groups with peers met in courses or associations.
    """)

with st.expander("Keeping Skills Current (Self-Directed)"):
    st.markdown("""
    Proactively improve key skills.

    * **Technology:** Leverage digital marketing tech-savviness. Practice with free software trials (QuickBooks) or Excel datasets (Kaggle, YouTube tutorials).
    * **Finance Concepts:** Supplement accounting with online finance courses (valuation, corporate finance) if needed for target roles.
    """)

st.divider()

# --- Section 4: Job Search ---
st.header("4. Job Search Strategies and Platforms Tailored to Portland")

with st.expander("Leverage Niche and Local Job Boards"):
    st.markdown("""
    Go beyond major sites like Indeed/LinkedIn.

    * **Mac’s List:** Well-known Portland board featuring nonprofit and SMB jobs. [Source: Mac's List](https://www.macslist.org/), [Source: Mac's List Home](https://www.macslist.org/). Check newsletter/articles.
    * **OSCPA Career Center:** Targets accounting talent in Oregon (CPA firms, companies). Member access might be needed for full details. [Source: OSCPA Login (Career Center link often here)](https://www.orcpa.org/login.aspx). May list non-CPA roles too.
    * **Staffing Agency Listings:** Check websites of Portland agencies (Robert Half, PrideStaff, Kelly, VanderHouwen, Ledgent) for current openings. Apply directly or contact recruiters.
    * **Government/Public Sector:** Check job portals for City of Portland, Multnomah County, State of Oregon (e.g., `oregon.gov/jobs`). Often need accountants/analysts; may value experience over CPA for some roles.
    * **Remote Job Boards:** Use FlexJobs (paid), We Work Remotely, Accountingfly (remote accounting focus), or filter locations on Indeed/LinkedIn to "Remote". Verify legitimacy of remote postings.
    """)

with st.expander("Optimize Your Resume for Applicant Tracking Systems (ATS)"):
    st.markdown("""
    Increase chances of getting past initial screening.

    * **Keywords:** Include terms relevant to accounting roles (Accounts Payable/Receivable, Reconciliation, Financial Statements, General Ledger, GAAP, Month-end Close, Audit, Variance Analysis, CPA Candidate if applicable).
    * **Software:** List specific software (QuickBooks, Excel - mention Pivot Tables/advanced functions, ERPs).
    * **Tailoring:** Customize keywords for each job description.
    * **Clarity:** Ensure resume is clear and concise for human readers post-ATS. Highlight unique skills (data analysis, communication).
    """)

with st.expander("Utilize LinkedIn Effectively"):
    st.markdown("""
    Essential for professional job searching.

    * **Profile Update:** Reflect your return narrative in summary. Indicate you're seeking accounting/finance roles. Set profile to "Open to Work".
    * **Connections:** Connect with Portland recruiters, hiring managers, professionals in target companies. Personalize requests.
    * **Job Search:** Use LinkedIn Jobs filters (Portland, remote). Apply early.
    * **Follow Companies:** Track target companies (Nike, Intel, Columbia Sportswear, local startups) for openings.
    * **Engagement:** Share/comment on accounting-related content to increase visibility.
    """)

with st.expander("Tap into Networking for Job Leads"):
    st.markdown("""
    Many jobs are found through connections.

    * **Be Specific:** Let your network know the type of role you seek (Staff Accountant, Financial Analyst, Portland/Remote).
    * **Ask for Referrals:** Referrals significantly increase visibility.
    * **Attend Events:** Use networking events (Section 5 & 6) with a job-search mindset. Meet hiring managers or those who know of openings.
    * **Portland Community:** Known to be interconnected and helpful. Don't hesitate to mention you're looking.
    """)

with st.expander("Consider Informational Interviews"):
    st.markdown("""
    Learn and make connections without direct job pressure.

    * **Reach Out:** Contact professionals on LinkedIn in roles/companies of interest (e.g., accounting at Vacasa, Columbia Sportswear). Request brief chats (20 min) to learn about their work.
    * **Benefits:** Gain insights into required skills, company culture. Can lead to referrals later. Portland culture often supports coffee meetings.
    """)

with st.expander("Be Prepared to Address the Gap Positively"):
    st.markdown("""
    Have a confident explanation ready for applications/interviews.

    * **Concise Narrative:** Frame the break as a period of skill broadening. Example: "Started in accounting, gained analytical/project management skills in marketing, now excited to return combining past experience with new skills."
    * **Counter Objections:** Prepare answer for "How will you get up to speed?". Mention specific actions (courses, self-study) and current knowledge of software/standards. [Source: FEI Article (similar topic)](https://www.financialexecutives.org/FEI-Daily/November-2017/Tips-to-accounting-professionals-returning-to-work.aspx). Emphasize enthusiasm.
    * **Focus on Value:** Highlight how diverse background is an asset.
    """)

with st.expander("Use Staffing Firms and Recruiters"):
    st.markdown("""
    Agencies can be allies.

    * **Contact Directly:** Reach out to recruiters at Portland firms specializing in accounting/finance (Robert Half, Parker + Lynch, Boly:Welch, Accountemps, CyberCoders). Send resume, request meeting.
    * **Be Clear:** Communicate your background, goals, flexibility. Temp-to-hire can be a good re-entry path.
    * **Maintain Contact:** Check in regularly so recruiters remember you.
    * **Coordinate:** Avoid multiple agencies submitting you for the same job.
    """)

with st.expander("Remote Work Considerations"):
    st.markdown("""
    If pursuing remote roles:

    * **State Requirements:** Verify if any state-specific needs apply (e.g., home state CPA for some firm roles).
    * **Logistics:** Note potential travel requirements.
    * **Highlight Suitability:** Emphasize ability to work independently, tech readiness (Zoom/Teams, home office).
    * **Competition:** Be aware remote roles attract wider applicant pools; tailor applications strongly.
    """)

with st.expander("Salary Research and Negotiation"):
    st.markdown("""
    Know your worth in the current market.

    * **Benchmark:** Use resources like the Robert Half Salary Guide for Portland accounting roles.
    * **Flexibility:** May need to start slightly lower after a break, but Portland market is strong.
    * **Negotiation:** Focus on getting the offer first. Consider negotiating benefits like training support or CPA exam assistance.
    """)

with st.expander("Persistence and Volume"):
    st.markdown("""
    Job searching takes time and effort.

    * **Routine:** Check job boards daily, set up alerts (Indeed, LinkedIn, Mac’s List).
    * **Apply Consistently:** Aim for a reasonable number of targeted applications per week.
    * **Track Applications:** Use a spreadsheet to manage applications and follow-ups.
    * **Stay Positive:** Don't get discouraged by lack of response; it's often a numbers game. Refine approach based on feedback.
    * **Demand:** Accounting is high-demand; Portland has many opportunities.
    """)

st.divider()

# --- Section 5: Networking and Organizations ---
st.header("5. Networking Opportunities and Local Accounting Organizations")

with st.expander("Oregon Society of CPAs (OSCPA)"):
    st.markdown("""
    Statewide association, cornerstone for networking.

    * **Membership:** Consider joining (Affiliate options available). Access events, directories, potential mentorship.
    * **Events:** Hosts networking (dinners, socials), CPE seminars (also networking), conferences, annual Strategic Leadership Forum. [Source: OSCPA Events](https://www.orcpa.org/events/event_list.asp), [Source: OSCPA LinkedIn](https://www.linkedin.com/company/oregon-society-of-cpas/).
    * **Chapters:** Attend local chapter meetings (Portland, Willamette Valley) for luncheons/mixers.
    * **Benefit:** Connect with hundreds of professionals (public practice, industry). Welcoming atmosphere.
    """)

with st.expander("Portland Chapter of the Institute of Management Accountants (IMA)"):
    st.markdown("""
    Global association for accountants in business (CMA focus).

    * **Portland Chapter:** Active, open to all finance/accounting pros. Hosts monthly events (CPE dinners, socials) combining learning & networking. [Source: IMA Portland](https://portland.imanet.org/).
    * **Audience:** Good for connecting with professionals in Portland companies (Nike, Intel, manufacturing). Complements OSCPA network.
    * **Resources:** Offers mentorship, job board. [Source: IMA Portland](https://portland.imanet.org/). Check event calendar for relevant topics/socials.
    """)

with st.expander("Accounting & Finance Women’s Alliance (AFWA) – Portland"):
    st.markdown("""
    Supports women in accounting/finance (open to all).

    * **Portland Chapter:** Check current status/activity (may operate with Seattle).
    * **Focus:** Networking, CPE, leadership, supportive community. Hosts meetings, workshops, social events.
    * **Benefits:** Can boost confidence; offers scholarships/education resources.
    """)

with st.expander("Institute of Internal Auditors (IIA) – Portland Chapter"):
    st.markdown("""
    For those interested in internal audit or risk advisory.

    * **Focus:** Supports internal audit professionals. Holds regular luncheons/seminars on audit topics. [Source: IIA Portland](https://chapters.theiia.org/portland/Pages/default.aspx).
    * **Networking:** Connect with audit managers at local companies (may oversee accounting or know openings). Niche group, but potentially useful.
    """)

with st.expander("ISACA (Information Systems Audit and Control Association) – Portland Chapter"):
    st.markdown("""
    More IT-audit focused, relevant if interested in tech intersection.

    * **Topics:** Cybersecurity, IT governance, finance controls.
    * **Networking:** Useful for roles combining accounting and IT (data analytics, systems). Optional based on interest.
    """)

with st.expander("Other Associations / Bookkeeping Groups"):
    st.markdown("""
    Groups for bookkeeping and small business accounting services.

    * **Examples:** Oregon Association of Independent Accountants (OAIA), local QuickBooks user groups, bookkeeping meetups.
    * **Benefit:** Good network if considering freelance or small business focus. Often discuss tax prep, software training.
    """)

with st.expander("Meetup.com Networking Groups"):
    st.markdown("""
    Informal networking opportunities.

    * **Search:** Look for "Portland finance," "PDX Accounting," "Young Finance Professionals" on Meetup.com. Activity varies.
    * **Related:** Check LinkedIn Local Portland events (general professional networking). Consider CFO Network events if accessible.
    """)

with st.expander("Oregon Society of Tax Consultants (OSTC)"):
    st.markdown("""
    For those leaning towards tax roles.

    * **Focus:** Tax preparers and consultants (CPAs, EAs, Licensed Tax Consultants).
    * **Chapters:** Local chapters (Portland) host monthly education meetings. Good network for tax accounting jobs.
    """)

with st.expander("Volunteer for Professional Events"):
    st.markdown("""
    Overlooked way to network and get noticed.

    * **Opportunities:** Help at OSCPA/IMA events (committees, registration).
    * **University Involvement:** Volunteer for accounting club events (mock interviews, judging) at PSU, UP, etc. Connects you with faculty/professionals.
    """)

with st.expander("Social Media and Online Communities"):
    st.markdown("""
    Engage online.

    * **Forums:** Participate in r/Accounting (global but supportive). Search Facebook for local groups ("Accounting Jobs Portland").
    * **Follow:** Track local business journals (Portland Business Journal) and organizations on LinkedIn/Twitter for news/leads.
    """)

with st.expander("Networking Approach"):
    st.markdown("""
    Strategy for attending events:

    * **Business Cards:** Create personal cards (Name, "Accounting Professional," contact info).
    * **Introduction:** Prepare a 30-second intro explaining your background and goal.
    * **Engage Others:** Ask questions, show genuine interest.
    * **Follow Up:** Send LinkedIn requests/emails after meeting key contacts. Reference your conversation.
    * **Mindset:** Portland community is collegial. Your story will likely resonate. Consistency builds support system.
    """)

st.divider()

# --- Section 6: Meetups, Associations, Career Fairs ---
st.header("6. Local Meetups, Associations, and Career Fairs")

with st.expander("Accounting Career Fairs ('Meet the Firms' events)"):
    st.markdown("""
    Primarily student-focused, but potentially accessible.

    * **PSU Meet the Firms:** Held each fall (e.g., Oct). Attracts public accounting firms and companies. Alumni/grad students often welcome. Check PSU School of Business event calendar. [Source: Jones & Roth (attended PSU fair)](https://www.jrcpa.com/event/psu-accounting-career-fair-meet-the-firms-2/).
    * **UO & OSU Events:** Similar fairs in Eugene/Corvallis. Collaborative Spring Accounting Career Expo often held in Portland (e.g., April 2024 at PSU). Open to students from multiple schools, possibly others. [Source: PSU Accounting Resources](https://www.pdx.edu/business/student-resources/accounting-finance-student-resources). Excellent opportunity if held again.
    * **OSU in Portland:** Check for OSU Portland Center business networking events.
    * **Leveraging Student Fairs:** Attend respectfully, be transparent about being an experienced professional returning. Ask about experienced hire roles or application process. Collect cards, follow up.
    """)

with st.expander("OSCPA Career Showcase"):
    st.markdown("""
    Annual OSCPA event, typically September at Oregon Convention Center.

    * **Format:** Primarily for students to network with firms/companies (like a career fair). Many employer booths. [Source: OSCPA Events](https://www.orcpa.org/events/event_list.asp).
    * **Attendance:** Contact OSCPA to inquire about attending as a returning professional. May be possible to attend as observer.
    * **Benefits:** Wide range of employers. Attend panels/presentations for insights. Great networking potential.
    """)

with st.expander("General Job Fairs in Portland"):
    st.markdown("""
    Broader fairs that may include accounting/finance roles.

    * **Community Fairs:** Hosted by Urban League of Portland (e.g., [Career Connections Job Fair](https://ulpdx.org/careerfair)), WorkSource Oregon. Focus on diversity/inclusion.
    * **College General Fairs:** PSU Spring All-Majors Fair, PCC Job Fairs (open to public, good for entry-level). [Source: PSU Career Fairs](https://www.pdx.edu/careers/career-fairs), [Source: PCC Job Fairs](https://www.pcc.edu/resources/careers/fairs/).
    * **Tech Fairs (TAO):** Technology Association of Oregon events might connect you with tech companies needing accountants.
    * **MBA Events:** University MBA programs (PSU, UP) have career fairs; might be accessible via sponsors.
    """)

with st.expander("Meetups and Informal Groups"):
    st.markdown("""
    Casual networking beyond formal fairs.

    * **Meetup/Eventbrite:** Search for "Finance Networking Happy Hour," "Women in Finance PDX."
    * **Tech/Startup Events:** FinTech meetups, startup incubator events (PIE), co-working space networking nights. Might find growing companies needing accounting help.
    """)

with st.expander("Professional Conferences"):
    st.markdown("""
    Deeper dive into topics + networking (usually requires fee).

    * **OSCPA Conferences:** Specific topics (Accounting & Auditing, Technology, Not-for-Profit). Breaks/lunches are prime networking times. [Source: OSCPA Instagram (NFP Conf example)](https://www.instagram.com/p/C5o1o4jRufr/).
    * **National Conferences:** AICPA/IMA conferences if held regionally.
    """)

with st.expander("Career Development Workshops"):
    st.markdown("""
    Skill-building and job search support.

    * **Resume/Interview Prep:** Look for sessions hosted by OSCPA, firms, Oregon Workforce Partnership, Dress for Success.
    * **Check Calendars:** Portland Business Journal events, FEI Portland chapter seminars.
    """)

with st.expander("Making the Most of Career Fairs/Events"):
    st.markdown("""
    Tips for maximizing impact:

    * **Dress:** Business or business-casual attire.
    * **Resume:** Bring copies (even if applying online). Helps guide conversation.
    * **Prepare:** Research attending employers beforehand. Target key companies.
    * **Follow Up:** Send thank-you emails/LinkedIn notes to key contacts met.
    """)

with st.expander("Follow Community Calendars"):
    st.markdown("""
    Stay informed about upcoming events:

    * **OSCPA:** [Events & Activities page](https://www.orcpa.org/events/event_list.asp).
    * **Portland Business Journal:** Events calendar.
    * **Eventbrite:** Search relevant keywords.
    * **University Alumni Associations:** Check calendars for business/networking mixers.
    """)

st.divider()

# --- Section 7: Actionable Next Steps Recap ---
st.header("Actionable Next Steps Recap")

st.markdown("""
Here’s a checklist to guide your immediate actions:

* **Skill Up:** Enroll in a refresher course or start CPA review soon. Schedule regular study time. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
* **Contact Oregon Board:** Clarify CPA status/requirements if applicable. Obtain necessary forms. [Source: OAR 801-010-0130](https://secure.sos.state.or.us/oard/viewSingleRule.action?ruleVrsnRsn=288791).
* **Join Organizations:** Sign up for OSCPA and/or IMA Portland. Plan to attend one event soon. [Source: IMA Portland](https://portland.imanet.org/).
* **Network Outreach:** List 10 former contacts; reach out to reconnect. Aim for 3 coffee chats/calls in the next two months. [Source: FM Magazine](https://www.fm-magazine.com/news/2023/jun/how-re-enter-finance-after-extended-leave.html).
* **Resume Update:** Refresh resume this week. Seek feedback if possible.
* **Online Presence:** Update LinkedIn (set "Open to Work"). Engage weekly.
* **Job Search Routine:** Set up job alerts (Indeed, LinkedIn, Mac’s List). Aim to apply consistently (e.g., 5-10/week).
* **Career Fairs:** Register for upcoming relevant fairs (Spring Expo, Meet the Firms, OSCPA Showcase). [Source: PSU Accounting Resources](https://www.pdx.edu/business/student-resources/accounting-finance-student-resources), [Source: OSCPA Events](https://www.orcpa.org/events/event_list.asp).
* **Continuing Ed:** Book at least one relevant CPE course/webinar soon.
* **Follow Up & Iterate:** Track contacts/applications. Follow up politely. Adjust approach based on results.
""")

st.divider()

# --- Conclusion ---
st.success("""
**Good luck on your journey back into accounting!** With your background and a structured approach using these resources, you are positioning yourself for success. Portland has a strong market for accounting professionals. Stay persistent, engage with the community, and you'll be well on your way to your next role.
""")

st.divider()

# --- Sources ---
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
    * OSCPA Instagram (NFP Conference example): [OSCPA Instagram Post](https://www.instagram.com/p/C5o1o4jRufr/)
    * Reddit - Perspective on returning (Note: Used for general context, not direct advice): [Reddit r/Accounting Post](https://www.reddit.com/r/Accounting/comments/15z66u0/thinking_about_going_back_into_accounting_after_a/)
    """)