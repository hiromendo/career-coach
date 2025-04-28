import streamlit as st
import pandas as pd

# --- Introduction ---
st.title("High-Paying Vocational Career Paths for a Deaf Worker in Beaverton, OR")

st.markdown("""
**Profile & Goals:** You have hands-on experience (warehouse operations, R&D tech work, Salesforce admin) and are fluent in ASL. As a Deaf individual currently in a repetitive Amazon warehouse job, you’re seeking a more stimulating skilled trade job near Beaverton, Oregon.

The ideal role:
* Pays around **\$50,000–\$60,000+ annually**.
* Involves **manual or technical work** (like electrician or other trades).
* Has **short training (3–6 months) or paid apprenticeships**.
* Doesn’t require long commutes or extensive driving.
* Offers a **deaf-friendly environment** (small teams or solo work, safety accommodations, openness to ASL).

Below, we explore the top five career paths that match these criteria, with details on job duties, pay, training requirements, local programs, potential employers, and steps to transition into each role.
""")

# --- Career Path Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Electrician",
    "2. Plumber / Pipefitter",
    "3. HVAC/R Technician",
    "4. Machinist / CNC Operator",
    "5. Facilities Maintenance Tech"
])

# --- Content for Each Tab ---

with tab1:
    st.header("1. Electrician (Inside Wireman)")

    st.subheader("Overview")
    st.markdown("""
    Electricians install, maintain, and repair electrical wiring, equipment, and fixtures in homes, businesses, and industrial buildings. They ensure all work meets electrical code standards and safety regulations. This trade is hands-on and visual, which suits a deaf worker well – you’ll be working with tools, diagrams, and visible indicators (voltage testers, lights), rather than relying on hearing. On job sites, clear visual communication and safety signals (like flashing lights or waving hands) can replace verbal warnings. Electricians often work independently or in small crews, planning layouts or troubleshooting circuits on their own. Job satisfaction can be high since the work is dynamic and skilled.

    Importantly, it’s a well-paying field: in Oregon, electricians earn about **$87,600 per year on average**, well above your target range (entry-level apprentices earn less, but pay rises as you gain experience). The demand for licensed electricians is very strong – it’s one of the most in-demand trades in the Portland metro. In fact, the local electricians’ union notes that “the demand for licensed electricians has never been higher” with over 200 contractors in the area seeking electricians.
    """)

    st.subheader("Why It’s Deaf-Friendly")
    st.markdown("""
    Electrical work is primarily visual/manual. Many deaf electricians have succeeded by using accommodations like visual alarm systems and vibrating devices to alert them to any issues. For example, instead of relying on a fire alarm’s sound, a deaf electrician can wear a vibrating pager or work under strobe-light alarms. On construction sites, it’s standard to use hand signals for safety (which aligns well with ASL use).

    While hearing colleagues might listen for a live wire “buzz” or equipment noise, you will learn to double-check with instruments and ensure power is off using visual indicators – standard safe practice for all electricians. With proper safety protocols (lockout/tagout, visual signals), being deaf is not a barrier in this trade. Many employers are aware of ADA requirements to accommodate hearing impairments. It’s also a solo-friendly job: electricians often spend stretches of time working on wiring runs or panels alone. Communication with a partner or client can be handled through written notes or sign (and many contractors have experience working with diverse crews).
    """)

    st.subheader("Typical Duties")
    st.markdown("""
    Electricians wire new construction, install lighting and outlets, test electrical systems, and diagnose/repair faults. For example, an inside electrician might read blueprints, run conduit (electrical tubing) through walls, pull wire, connect circuit breakers, and install switches or machinery hookups. They use tools like pliers, voltage testers, and conduit benders daily. Maintenance electricians in factories or facilities troubleshoot motors and control systems.

    The work is physical but not as labor-intensive as some trades – it involves climbing ladders, working in crawl spaces or attics, and handling moderate-weight equipment. You do need to be careful about electrical hazards, but safety training will teach you to work de-energized and use protective gear. Overall, it’s a moderate-risk job but very safe when proper procedures are followed (e.g. always turning off breakers and using lock-out tags). Electricians also keep updated on code changes and may specialize in areas like industrial controls or solar installations.
    """)

    st.subheader("Salary and Outlook")
    st.markdown("""
    Electricians are well compensated due to their specialized skills and licensing. In the Portland/Beaverton area, journey-level electricians often earn **\$40–\$60 per hour** (union scale is around \$54/hr in Portland), which translates to **\$80k–\$120k+ per year** when fully licensed. State data shows Oregon electricians’ median wage is about **\$87,600 annually**.

    As a brand-new electrician (apprentice), you might start around 50% of the journeyman wage (roughly \$20–\$30/hr, i.e. **~\$40k–\$50k/year**), and receive raises every 6 months as you progress in training. Reaching the $60k mark typically happens by the later years of apprenticeship or once you become a licensed Journeyman Electrician.

    The job outlook is excellent – employment of electricians is projected to grow ~11% from 2023 to 2033, and Oregon in particular has a thriving construction and high-tech industry driving demand. This means plenty of job openings and overtime opportunities. Electricians also enjoy career flexibility: you can work for electrical contractors on construction projects, for facilities (maintaining one site like Nike’s campus or Intel’s factory), or even go into business for yourself after licensing.
    """)

    st.subheader("Training & Certification")
    st.markdown("""
    To work as an electrician, state licensing is required. In Oregon, the typical path is to complete an **apprenticeship (4–5 years of supervised training)** and then pass the state exam to become a General Journeyman Electrician. Apprenticeships combine paid on-the-job training with classroom instruction – a big perk is you **earn wages from day one**, avoiding student debt.

    The standard inside electrician apprenticeship is about 8,000 hours of on-the-job training (approx. 4 years) plus around 576 hours of classroom instruction. During this period, you are registered as an apprentice licensee. After completing the hours and classes, you can take the journeyman exam. Shorter programs exist for limited scopes (e.g., Limited Residential Electrician, ~2–3 year programs), but the full General Electrician ticket gives you the broadest job options and highest pay.

    No college degree is required – you generally need a high school diploma (or GED) and must be at least 18. Strong math and problem-solving skills are important; apprenticeships often have an entrance exam covering algebra and technical aptitude. Self-study alone isn’t sufficient – you must accumulate state-approved hours. Most apprenticeships in this region are run either by the union (IBEW Local 48) or by non-union contractors (IEC). Both routes have similar training quality and state recognition. You should be prepared for ~4-5 years of training, but remember, you get paid during that time. Apprentices attend classes (often at night or in week-long daytime bursts).
    """)

    st.subheader("Local Training Programs")
    st.markdown("""
    In the Beaverton/Portland area, you have excellent apprenticeship programs available:

    * **NECA-IBEW Local 48 Apprenticeship (Area 1 Inside Electrician JATC):** Union program, 5 years in Portland. Apprentices work with union contractors. State-of-the-art training center, free instruction, Day 1 medical benefits. Will coordinate ASL interpreter accommodation (often paid by VR or union funds per ADA). Highly motivated to bring in diverse candidates.
    * **Independent Electrical Contractors (IEC) of Oregon Apprenticeship:** State-approved non-union program. Offers 4-year Inside Electrician and shorter Limited Energy Technician apprenticeships. May have more frequent application windows. Classes might be at PCC or IEC center. Will also accommodate ASL interpretation.
    * **Portland Community College (PCC):** Partners with apprenticeship programs for related instruction credits (night classes might be through PCC). Offers Trades Preparation courses. PCC's catalog notes "Electrical Trades" curriculum for apprentices.
    * **Pre-Apprenticeship Programs:** Short programs (8–12 weeks) like Constructing Hope or Oregon Tradeswomen (if female) can prepare you for trades and improve acceptance chances. Often partner with BOLI and may help arrange interpreters. Might not be needed given your experience.
    """)

    st.subheader("Local Employers & Job Opportunities")
    st.markdown("""
    Once licensed, many employers exist in Beaverton/PDX:
    * **Electrical Contractors:** Christenson Electric, EC Company, OEG, Dynalectric, etc. (IBEW Local 48 has 200+ signatory employers). Focus areas: high-tech (Intel), commercial, residential.
    * **In-House Maintenance:** Nike World HQ, Intel, etc. hire facility electricians. Often accommodating (fixed location, steady hours).
    * **Government Agencies:** TriMet, City of Beaverton/Portland (e.g., traffic signals). Typically welcome diversity.
    * **Job Listings:** Indeed currently shows numerous Electrician jobs in Beaverton, OR (Apprentice, Journeyman, Maintenance). Union has job hotline; apprentices are assigned employers.

    Being deaf in these environments is typically fine; accommodations like text-based devices can replace radio communication. Construction boom ensures high demand.
    """)

    st.subheader("How to Become an Electrician – Step by Step")
    st.markdown("""
    1.  **Research and Prepare:** Read up on the trade (BLS profile). Ensure you meet basic requirements (18+, HS/GED, driver's license). Brush up on algebra/physics. Prep for the math test.
    2.  **Apply for Apprenticeship:** Monitor openings for Area 1 JATC (IBEW Local 48/NIETC) or IEC. Submit application/transcripts, take aptitude test, interview. Mention deafness positively, emphasizing success strategies.
    3.  **Secure Accommodations:** Upon acceptance, coordinate with the program and Oregon Vocational Rehabilitation Services (VR) for interpreters (for classes), etc. Discuss on-the-job needs (written communication, visual alerts).
    4.  **Complete Apprenticeship Training:** Work full-time under journeyman supervision, attend classes. Rotate through job types. Log hours. Study hard (NEC, theory, blueprints). Use interpreters/demos as needed. Build rapport with crew.
    5.  **Get Your License and Join the Workforce:** After hours/classes, pass the Oregon Journeyman Electrician exam. Join the union dispatch list or apply directly to companies.
    6.  **Continuous Learning and Specialization:** Pursue specialty licenses (Supervisor) or certifications (solar PV). Maintain safety training. Use captioned videos/simulations. Mentor others.
    """)

    st.subheader("Deaf Community Tip")
    st.markdown("""
    Connect with other Deaf/HoH individuals in trades (Reddit, Facebook groups). Share tips on tools (flashing multimeters) and job site communication. Reach out to Hearing Loss Association of Oregon or union contacts. Educate employers/coworkers on communication needs (most are open, ADA requires accommodation). Electrical work heavily uses sight and touch (color codes, meters, vibrations), making it a good fit.
    """)

with tab2:
    st.header("2. Plumber / Pipefitter")

    st.subheader("Overview")
    st.markdown("""
    Plumbers and pipefitters assemble, install, and repair piping systems for water, gas, and other fluids. This includes residential (sinks, toilets, water heaters) and commercial/industrial work (sprinklers, process pipelines). They also maintain and troubleshoot existing systems (leaks, clogs). It’s a hands-on job using tools (wrenches, cutters, torches) and reading blueprints.

    For a deaf worker, plumbing is very accessible: tasks are visual (seeing flow, reading gauges/plans) and often involve independent or partner work. Communication is typically one-on-one (gestures, notes). Safety cues can use hand signals. Many deaf tradespeople thrive in plumbing, relying on touch and sight (feeling pipe vibrations, watching gauges) rather than hearing. Minimal phone/radio use; communication can use writing or ASL.
    """)

    st.subheader("Job Duties")
    st.markdown("""
    Duties vary by setting:
    * **Construction:** Lay out and install new piping systems. Cut/join pipes (copper, PVC, steel), weld/solder, install fixtures, test for leaks (pressure gauges, visual methods). Follow codes/plans.
    * **Maintenance/Service:** Respond to service calls (unclogging drains, replacing water heaters, fixing pipes). Often solo diagnostic work.
    * **Pipefitting/Steamfitting:** Work on heavier systems (boilers, HVAC chillers, industrial pipelines). May install specialized lines (e.g., pure water in semiconductor fabs). Involves schematics and potentially welding.
    * **Safety:** Use safety gear (gloves, goggles). Moderate physical risk (hot water, chemicals, strain from posture/lifting). Safety relies on visual checks (gauges, valves) not just sound. Leak testing uses visual methods (gauge drop, soap bubbles). Modern tools often have visual displays.
    """)

    st.subheader("Salary and Demand")
    st.markdown("""
    Plumbers are among the best-paid trades. In Oregon, the median annual wage is about **\$87,900**. Union scale in Portland is often **\$40+/hour**. Apprentices start around 50% (roughly **$\20–\$25/hour, ~$45k/year**) and increase. Reaching \$60k typically happens upon journeyman status or late apprenticeship with overtime.

    Demand is strong: Oregon employs 5,000+ plumbers/pipefitters with consistent openings. Occupation projected to grow ~6% nationally, plus retirements create openings. Portland metro construction (housing, commercial, Intel expansion) fuels demand. Maintenance plumbing is always needed. High job security. Overtime potential, especially for emergency calls (dispatch can use text/vibrating alerts).
    """)

    st.subheader("Training & Certification")
    st.markdown("""
    Plumbers are state-licensed. Standard path: registered **apprenticeship (4-5 years, ~8,000 hours)** followed by journeyman license exam. Main program in Portland area is via **UA Local 290** (Plumbers and Steamfitters union) - 5-year apprenticeship. Also a 4-year Area I Plumbing apprenticeship (likely union-overseen).

    Entry requirements: 18+, HS diploma, driver's license, algebra proficiency. Apprentices work under journeymen and attend classes (evenings/blocks at union center) covering code, math, welding, safety, plan reading. After apprenticeship, pass Oregon Journeyman Plumber license exam.

    Alternative (less common in OR): start as helper + trade school, but still need documented apprenticeship hours for license. Community colleges integrate with apprenticeships (e.g., Clackamas CC partners with Area I Plumbers). Earn-while-learning is key. You start earning day one, gain independence gradually.
    """)

    st.subheader("Local Training Programs")
    st.markdown("""
    Primary training avenue in Beaverton/Portland:

    * **UA Local 290 Apprenticeship (Tualatin Training Center - 290 Tech):** Comprehensive 5-year union program covering plumbing, steamfitting, HVAC. Highly regarded. Located just south of Beaverton. Will arrange accommodations (interpreters). Application often annual (form, interview). Can integrate with an optional Associate's Degree.
    * **Area I Plumbers Apprenticeship (State BOLI program):** Likely the same as Local 290's program, listed as 4 years. BOLI website has application info. Apply via BOLI or union directly.
    * **Non-Union/Trade School:** Less common for plumbing here. Some large non-union firms (e.g., Apollo Mechanical) might have internal training or sponsor apprentices. Might require more initiative to find employer-sponsor. Union route recommended for structure.
    * **Related Short Courses:** Consider welding courses (PCC, VOCTECH) or backflow tester certification (5-day course) later to enhance skills. Pre-apprenticeship programs are optional.
    """)

    st.subheader("Potential Employers & Deaf-Friendly Workplaces")
    st.markdown("""
    Variety of options:
    * **Plumbing Contractors:** Residential service (Rescue Rooter, Roto-Rooter) or commercial/industrial (Jet Industries, Apollo Plumbing, Reitmeier). Actively hiring apprentices/helpers. Larger firms may have better ADA familiarity. Inquire about deaf employees.
    * **Union Contractors:** Work for signatory contractors dispatched by Local 290. Range from large industrial to small shops. Formal safety protocols, supportive of training. Union helps coordinate interpreters for safety meetings.
    * **Facilities Maintenance:** Work directly for hospitals, schools (Beaverton School District), universities, large campuses (Intel), government (City Water Bureau). Often quite deaf-friendly (diverse staff, text pagers). More routine work.
    * **Self-Employment:** Long-term option after getting contractor's license. Control your environment/clients. Deaf-owned trade businesses exist.
    """)

    st.subheader("Deaf-Friendliness")
    st.markdown("""
    Plumbing requires little hearing. Compensate for missed sound cues (running water) with visual/tactile checks (feel vibration, watch gauges). Leak testing uses accurate visual methods (pressure gauge, leak spray). Adapt to job site awareness visually (mirrors, checking surroundings). Many Deaf individuals succeed in plumbing/mechanical trades.

    Employers must provide reasonable accommodations (strobing phone alarm, captioned videos, interpreters for meetings). Trades culture is often straightforward; skill speaks volumes. Coworkers may learn basic signs. Use tech like notepad apps or voice-to-text for communication. Discuss needs with employer.
    """)

    st.subheader("How to Become a Plumber – Step by Step")
    st.markdown("""
    1.  **Learn About the Trade:** Familiarize yourself (watch captioned videos, read BLS). Practice basic skills if possible. Ensure physical ability (kneeling, crawling, lifting ~50-75 lbs). Refresh math (fractions, geometry).
    2.  **Apply for Plumbing Apprenticeship:** Watch for openings from UA Local 290 or Area I Plumber JATC (via 290tech or BOLI). Submit application, transcripts, references. Possible aptitude test/interview. Express enthusiasm, discuss deafness positively ("visual asset"). Driver's license needed.
    3.  **Utilize Support Services:** Once accepted, connect with Vocational Rehabilitation (VR) for interpreter funding, specialized equipment. Coordinate accommodations with apprenticeship coordinator/employer/union.
    4.  **Complete the Apprenticeship (Work and Learn):** Work under experienced plumbers for 4-5 years, progressing from simple to complex tasks. Attend classes (code, calculations, techniques). Ask questions, review materials. Log work hours.
    5.  **Get Licensed:** Upon completion, apply for and pass the Oregon Journeyman Plumber exam. Obtain JP license for higher pay and independence.
    6.  **Continuous Improvement and Specializations:** Pursue certifications (medical gas piping, backflow tester, steamfitter). Advance to Foreman (possible for deaf individuals using visual direction). Consider contractor's license later.
    """)

    st.subheader("Deaf Worker Tips")
    st.markdown("""
    Use visual alert devices (digital flashing gauge). For customer interaction: use notepad/app; most are patient. Embrace solo work aspects. For teamwork: establish simple signals (thumbs up, nod). Coworkers often become supportive ("have your back"). Ensure safety accommodations (flashing alarms - often already present). Communicate needs openly with supervisors. Plumbing is rewarding, pays well, has clear entry via apprenticeship, and aligns with manual work/deaf-friendly preferences.
    """)

with tab3:
    st.header("3. HVAC/R Technician (Heating, Ventilation, & Air Conditioning Mechanic)")

    st.subheader("Overview")
    st.markdown("""
    HVAC/R Technicians install and repair heating, cooling, and refrigeration systems (furnaces, ACs, heat pumps, ventilation, commercial refrigeration). It's a hands-on, technical job combining electrical, pipe fitting, and troubleshooting. Often work solo (service calls) or in small teams (installations), allowing easy visual coordination.

    Deafness is generally not an impediment: rely on gauges, digital meters, touch (air flow, vibration) for diagnostics. Visual/measurement alternatives exist for any auditory cues (e.g., reading pressure gauges instead of listening to compressors). Safety signals can be made visual. HVAC techs often wear ear protection anyway, relying on sight/touch. Considered quite deaf-friendly.
    """)

    st.subheader("Job Duties")
    st.markdown("""
    * **Installation:** Set up new furnaces/ACs (wiring, refrigerant lines, ductwork). Use tools for sheet metal, brazing torches, wiring. Run ducts, mount equipment.
    * **Maintenance & Repair:** Diagnose and fix heating/cooling issues. Use multimeters, pressure gauges, inspect filters/fans. Replace motors, fix leaks, swap components, clean coils. Often solitary diagnostic work.
    * **Refrigeration (if applicable):** Service commercial refrigeration (ice machines, freezers). Similar skills, focus on temperature controls.
    * **Safety & Compliance:** Handle refrigerants safely (requires EPA Section 608 Certification). Ensure proper venting, electrical codes.
    * **Work Environment:** Indoors and outdoors (basements, rooftops). Deal with weather. Moderate physical work (lifting, ladders, crawlspaces). Less continuously laborious than some trades.
    """)

    st.subheader("Salary and Job Outlook")
    st.markdown("""
    Solid income in Oregon. Median wage around **\$30.95/hour (~\$64,000/year)**. Average annual wage about **\$66,600**. Entry-level near **\$45k-\$50k**, crossing $60k common with experience/certs. Overtime potential during peak seasons. Union roles (Local 290) can pay higher (\$40+/hr).

    Very bright job outlook: Growing field due to energy efficiency focus and construction. Expected ~6% national growth, **11% Oregon growth by 2030 (~360 jobs/year)**. Steady need in Beaverton/Portland due to climate. Retirements create openings. Good job security. Somewhat seasonal workload, but year-round employment typical.
    """)

    st.subheader("Training & Certification")
    st.markdown("""
    Two main paths: formal education (certificate/degree) or apprenticeship. HVAC techs **not required** to complete state apprenticeship to work (unlike electricians/plumbers), except for specialized licenses.

    * **Certificate/Diploma Programs (3–12 months):** Learn fundamentals at trade school/community college. **PCC** offers a **14-credit HVAC Installer Certificate (one term)**, BOLI-approved pre-apprenticeship. Also 1-year certificate & 2-year AAS degree (Facilities Maintenance/HVAC). Advantage: quick entry, structured learning, labs. PCC has disability services for accommodations. Start as entry-level tech with knowledge base.
    * **Apprenticeship (Earn-while-learn):** **UA Local 290** offers 5-year HVAC/R Service Technician apprenticeship (similar to plumbing). Comprehensive training, union wages/benefits. Sheet Metal Local 16 also has HVAC installer apprenticeship (ductwork focus).
    * **EPA Section 608 Certification:** **Required** to handle refrigerants. Federal requirement. Test on safe handling (Types I, II, III or Universal). Included in many programs or taken separately. Multiple-choice test; accommodations available.
    * **State Licenses:** No single "HVAC license." Aspects covered by others (limited electrical license often held by company, possible Limited Maintenance Electrician - LME license later). Self-employed need Limited Maintenance Specialty Contractor – HVAC/R (LHR) license eventually (requires 4,000 hours experience + exam).
    """)

    st.subheader("Local Training Options")
    st.markdown("""
    * **Portland Community College (PCC):** Offers short HVAC/R Installation certificate (14 credits, 1 term), 1-year certificate, and 2-year AAS degree (Facilities Maintenance/HVAC). Programs at Sylvania Campus & OMIC center. Flexible, self-paced options. Great starting point.
    * **Other Colleges:** Mt. Hood CC (Gresham) and Lane CC (Eugene) also have programs. PCC is largest locally.
    * **Trade Schools:** Private schools (Apollo Technical) offer ~6-month programs. Ensure quality and hands-on time. Short bootcamps (6 weeks) might be too brief.
    * **UA Local 290 Apprenticeship (HVAC):** Apply if interested in 5-year union path. Can potentially do short PCC course first, then join apprenticeship.
    """)

    st.subheader("Employers and Job Market")
    st.markdown("""
    Hired by:
    * **HVAC Contractors:** Residential/commercial service/installation (Sunset Heating, Pyramid Heating, Wolfer’s, Jacobs, AAA Heating, etc.). Ensure dispatch system is text/app-based.
    * **Mechanical Contractors:** Larger firms doing big commercial projects (Hunter-Davisson, McKinstry, Hermanson). Often union work.
    * **Facilities/Plant Operations:** Dedicated techs at data centers (Hillsboro), malls, office parks, manufacturing plants. Data centers offer controlled environment, good for deaf tech.
    * **Government/Institutional:** City/county buildings, schools (Beaverton School District). Stable, inclusive policies.
    * **Self-Employment:** Option later as independent contractor.
    """)

    st.subheader("Deaf-Friendly Considerations")
    st.markdown("""
    Involves local driving for service calls (need license). Adapt van with visual alerts if needed (wide mirrors, siren detectors - optional). Stationary roles (facility tech) minimize driving if preferred. Communication via text/apps for dispatch/customers is common. Use tablets for work orders. Emergency on-call handled via text/vibrating pager.

    Hearing not critical for diagnostics (use visual/digital gauges, error codes, feel vibration instead of listening to motors). Safety relies on visual checks, lockout procedures, fall protection – same for everyone. Standard accommodations (strobe alarms) easy to implement.
    """)

    st.subheader("How to Become an HVAC Technician – Step by Step")
    st.markdown("""
    1.  **Basic Preparation:** Strengthen math/science basics (pressure, temperature, algebra, Ohm's law). Get comfortable with hand/power tools. Basic electrical/plumbing knowledge helpful.
    2.  **Choose a Training Path:** Decide between short college certificate (PCC's 1-term installer cert) for quick entry, or longer apprenticeship (UA Local 290). Can combine: short course first, then apprenticeship. Or seek direct hire with on-the-job training (less common without basics).
    3.  **Enroll in Training / Apprenticeship:** Register at school (PCC), arrange accommodations (interpreter/captions) via disability services. Participate in hands-on labs. Or apply for apprenticeship.
    4.  **Obtain Mandatory Certification:** Pass EPA Section 608 exam (aim for Universal). Crucial for hireability.
    5.  **Start Working in the Field:** Apply for HVAC Tech/Installer jobs, highlighting training/EPA cert. Explain deafness positively, focusing on communication strategies (text, notes) and successful training completion. Start by shadowing experienced tech, learn real-world skills.
    6.  **On the Job – Accommodation and Mastery:** Set up communication accommodations (text dispatch). Use helpful apps (speech-to-text). Leverage digital diagnostic tools. Continue learning different systems. Build troubleshooting expertise.
    7.  **Pursue Additional Credentials (Optional):** Consider NATE certification (industry standard). Pursue LME license if doing significant electrical work.
    8.  **Career Progression:** Advance to senior tech, specialize (controls, energy management), move to facility HVAC role, or become service manager. Skills are portable. Pivot to related green energy fields possible. Use deaf community networks for support.
    """)

with tab4:
    st.header("4. Machinist / CNC Machine Operator")

    st.subheader("Overview")
    st.markdown("""
    Machinists operate machine tools (lathes, mills, grinders, CNC machines) to manufacture metal parts with high precision. Great fit for hands-on work and detail-orientation. Work involves reading blueprints, setting up machines, monitoring cutting, and measuring parts. Environment is often a loud machine shop (everyone wears earplugs).

    Communication is minimal and visual (blueprints, machine parameters). Being deaf is usually not an issue; communication uses gestures or stopping machines. Safety signals (flashing lights) easily accommodate. Manufacturing is a common sector for deaf employment, suggesting accessibility. Offers stimulating, problem-solving work with tangible results.
    """)

    st.subheader("Job Duties")
    st.markdown("""
    * **Reading Blueprints/Specifications:** Understand technical drawings or CAD files for dimensions and tolerances.
    * **Machine Setup:** Select material, load into machine, choose cutting tools, align/secure workpiece, set reference points.
    * **Operating Machines:** Manually control cuts on manual machines, or input/load programs and monitor automated CNC machines. Ensure correct operation.
    * **Measuring & Quality Control:** Use precision instruments (micrometers, calipers, gauges) to ensure parts meet tight tolerances (e.g., 0.001 inches). Entirely visual/tactile.
    * **Maintenance & Problem-Solving:** Maintain machines, replace worn tools, troubleshoot issues (dimension errors). May involve creative setups or custom fixtures.
    * **Work Context:** Usually work individually at a machine. Interact with supervisor for assignments, QC inspectors occasionally. Interactions manageable via writing or face-to-face.
    """)

    st.subheader("Salary and Outlook")
    st.markdown("""
    High-skill trade with good compensation. Oregon average: **~\$59,700/year**. Entry-level ~**\$18–\$20/hour (~\$38k–\$42k/year)**. Experienced CNC machinists reach **\$25–\$30+/hour (\$50k–\$60k+/year)**. Specialized industries (aerospace - Boeing Portland journey level potentially \$50+/hr) pay more. Median statewide wage \$61,200/year**.

    Stable outlook with some growth. Automation increases productivity but skilled operators/programmers still needed. Retirements create demand. Precision manufacturing remains crucial. Career has longevity and upward mobility (CNC programmer, supervisor, engineer). Secure path with opportunities in aerospace, medical, high-tech, general manufacturing.
    """)

    st.subheader("Work Environment & Deaf Accessibility")
    st.markdown("""
    Machine shops have hazards (machinery, sharp tools, shavings) managed by safety protocols. Hearing not primary safety need; rely on visual cues (watching operation, indicator lights, measuring). Machines often have visual status lights/displays. Flashing stack lights can supplement audible alarms. Colleagues use taps/waves in loud shops. Focus on solo tasks minimizes missed conversation. Meetings manageable with notes. Deaf-friendly role; many deaf individuals work as machinists/toolmakers.
    """)

    st.subheader("Training & Skills Development")
    st.markdown("""
    Need skills in machine operation, blueprint reading, precision measurement. Paths:
    * **Formal Apprenticeship:** Oregon has machinist apprenticeships (BOLI lists 4-year programs), often employer-sponsored (Boeing, manufacturing consortiums). Earn while learning. Can be competitive.
    * **Community College / Trade School Program:** Common route. **PCC** has well-regarded **Machine Manufacturing Technology** program (2-yr AAS, 1-yr certificates in CNC Milling/Turning, <1yr Manufacturing Tech cert). Teaches manual/CNC, CAD/CAM, metrology. Hands-on practice in labs. **Clackamas CC (CCC)** also has Machine Tool Technology program. College programs offer structured learning and internship potential. Accommodations (interpreters) available.
    * **On-the-job Training:** Start as operator/assistant and learn from senior machinists. Many employers now prefer foundational training first.
    * **Combination:** Short certificate (PCC <1yr) for basics, then get job as trainee and continue learning (maybe night classes). Short bootcamps exist; verify quality/machine time.
    """)

    st.subheader("Local Programs and Resources")
    st.markdown("""
    * **PCC Machine Manufacturing Technology:** Prime resource (Sylvania Campus, OMIC center). Offers certificates and AAS degree.
    * **Clackamas Community College (CCC):** Machine Tool Technology program (AAS degree option). Partners with industry for apprenticeships.
    * **Chemeketa CC (Salem):** Machining program (might be far).
    * **Oregon Manufacturing Innovation Center (OMIC):** May offer short workshops/pre-apprenticeship.
    * **WorkSource Oregon / PCC:** Inquire about short-term machining courses.
    * **Access to Machines:** College labs are key for hands-on practice.
    """)

    st.subheader("Potential Employers")
    st.markdown("""
    Needed in various Portland-area industries:
    * **Precision Machine Shops:** Contract work for larger companies.
    * **Aerospace/Defense:** Boeing (Gresham), Columbia Helicopters.
    * **High-Tech Manufacturers:** Intel (tooling shops), Tektronix. Some roles titled "Manufacturing Technician" involving machine operation.
    * **Medical Device Manufacturers.**
    * **General Manufacturing:** Precision Castparts Corp., Vigor Industrial.
    * **Job Titles:** CNC Machinist, Manual Machinist, Manufacturing Technician.

    Shortage of skilled machinists means employers may train entry-level with basic skills. Larger manufacturers (Boeing - IAM union) often have diversity experience and union support for accommodations. Task-focused environment with written/digital communication (work orders, CAD drawings).
    """)

    st.subheader("Why It’s Deaf-Friendly")
    st.markdown("""
    Leverages visual acuity and tactile skills. Precision measurement/observation are key. Audible alarms supplemented by visual indicators (stack lights, screen messages, text alerts). Machinists monitor visually (chip formation, surface finish) rather than by sound. Loud shop environment makes hearing less relevant; gestures/taps common. Communication with engineers via drawings/email. Infrequent group training manageable with interpreter/captions.
    """)

    st.subheader("How to Become a Machinist – Step by Step")
    st.markdown("""
    1.  **Explore and Build Aptitude:** Watch captioned videos ("Basics of machining"). Visit PCC/maker space if possible. Practice math (geometry, trig). Develop attention to detail/patience. Seek informational interview/shop tour via WorkSource Oregon.
    2.  **Pursue Formal Training or Apprenticeship:** Enroll in machining course/program (PCC certificate <1yr is good start). Apply to PCC, coordinate accommodations via Disability Services. Or apply for apprenticeships (BOLI, Boeing) - may do PCC concurrently.
    3.  **Leverage Vocational Rehabilitation and Networks:** Engage VR for support (funding, tools, job leads). Network with instructors/classmates for job leads.
    4.  **Apply for Machining Jobs (Entry-Level):** Target "Machinist Trainee," "CNC Operator," "Manufacturing Technician." Highlight hands-on skills from training, relevant past experience (reliability, technical inclination). Be upfront about deafness, explain communication strategies positively. Target diverse employers/large HR departments first. Prepare for practical tests (request written instructions if needed).
    5.  **On the Job: Master the Craft:** Focus on skill development. Start with simpler tasks, show initiative to learn setup/programming. Use visual attention to detail. Establish communication methods (notebook, tablet, messaging apps). Ensure access to visual alarms/captioned training.
    6.  **Continuous Learning and Certification:** Aim for NIMS certifications. Learn CNC programming (CAM software - visual/textual). Advance to CNC Programmer, Manufacturing Engineer, Shop Lead/Supervisor (manageable with written/face-to-face communication). Use adaptive strategies (watch load meters instead of listening).
    """)

with tab5:
    st.header("5. Facilities Maintenance Technician (Building Maintenance)")

    st.subheader("Overview")
    st.markdown("""
    A versatile tradesperson responsible for keeping building systems operational. A "jack-of-all-trades" fixing minor plumbing, electrical, HVAC, carpentry, painting issues. Ensures facilities (offices, warehouses, schools, hospitals) are safe and functional. Ideal for variety and hands-on problem-solving.

    Being deaf poses minimal difficulty: tasks often solo or partner work, rely on skills/planning. Receive written work orders. Follow visual procedures/checklists. Coordinate with others via text/signals. Safety managed via visual checks (voltage testers). Employers can provide visual alarms. Strong observational skills are an asset.
    """)

    st.subheader("Job Duties")
    st.markdown("""
    Broad range, depending on facility:
    * **Electrical Maintenance:** Replace fuses/breakers, bulbs/ballasts, outlets/switches. Troubleshoot power issues. Some tasks may require Limited Maintenance Electrician (LME) license.
    * **Plumbing Maintenance:** Stop leaks, unclog drains/toilets, replace valves/gaskets. Small repairs, not full installs.
    * **HVAC/Mechanical:** Change filters, replace belts, clean coils. May assist HVAC contractor or do minor troubleshooting (if EPA certified).
    * **General Repairs:** Fix door hardware, patch drywall, paint, ceiling tiles, flooring, furniture assembly/moving. Possibly minor welding, conveyor maintenance (industrial).
    * **Preventive Maintenance:** Follow schedules for inspecting lights, generators, fire extinguishers, boilers. Log checks. Visual confirmation for alarms.
    * **Safety & Compliance:** Follow OSHA guidelines, use Lockout/Tagout (LOTO - inherently visual). Participate in safety drills (ensure visual cues).
    * **Work Setting:** Any building type (schools, corporate campuses, hospitals, apartments, manufacturing). Can target preferred environment. Small teams or solo work. Communication manageable with writing/basic sign.
    """)

    st.subheader("Salary")
    st.markdown("""
    Wide range based on industry/skill. Portland average **~\$53,700/year (\$25.80/hr)**. Majority earn **\$42,000 - \$65,000 annually**. Entry-level general maintenance ~**\$18–\$22/hr (~\$40k/yr)**. Skilled techs or those with licenses (LME, boiler operator) earn \$60k+. Government/union positions often have good pay/benefits. Your \$50-60k target is achievable with experience/skills. Stable field - needed everywhere.
    """)

    st.subheader("Training & Qualifications")
    st.markdown("""
    No single required license for general maintenance. Employers look for experience in 1-2 trades + willingness to learn. Certifications boost hireability:
    * **Limited Maintenance Electrician (LME) license:** 2-year Oregon apprenticeship license for basic electrical work. Preferred by many employers. Can pursue while working.
    * **HVAC knowledge / EPA 608 Certification:** Plus if facility has HVAC. EPA cert can be obtained independently.
    * **Plumbing knowledge:** Demonstrated by experience. Short repair courses available.
    * **Boiler Operator License:** Required for some facilities (hospitals, central plants). Leads to "Stationary Engineer" roles (often higher pay).
    * **General handyman skills:** Learn on job, but base ability with tools/instructions helps. R&D/Amazon experience relevant (troubleshooting, facility operations).
    """)

    st.subheader("Training Resources")
    st.markdown("""
    * **PCC Facilities Maintenance Technology AAS:** Comprehensive 2-year program covering HVAC, electrical, water systems, boilers. Can take individual courses (e.g., "Electrical Systems for Facilities") or shorter certificates (HVAC installer cert).
    * **Short Courses/Workshops:** Check ORACCA, PHCC, BOMA for relevant training.
    * **OSHA Safety Training (10/30-hour):** Good foundation, looks good to employers. Online options available.
    * **Entry-Level Job + Classes:** Start as assistant/helper, take evening classes in trades.
    * **Internal Transfer (Amazon):** Inquire about facilities tech openings at current employer; may offer training.
    """)

    st.subheader("Potential Employers")
    st.markdown("""
    Many local options:
    * **Commercial Buildings:** Corporate campuses (Nike, Columbia), managed by companies like CBRE, JLL. Large, equal-opportunity employers.
    * **Educational Institutions:** Beaverton School District, PCC, universities. Stable schedules, support accommodations.
    * **Hospitals/Healthcare:** Providence St. Vincent, Kaiser Westside. 24/7 operations, may need specialized knowledge (training provided). Union roles possible (Stationary Engineers Local 701). Robust safety/visual alarm systems.
    * **Manufacturing/Distribution:** Intel, Columbia distribution center, warehouses. Maintain equipment and building. Intel known for inclusive policies.
    * **Property Management/Apartments:** Maintain units. More resident interaction (manageable with notes/app). May include housing perk.
    * **Municipal/City Jobs:** City of Beaverton/Portland (Utility Worker, Facility Tech). Government roles, strong EOE policies.
    """)

    st.subheader("Deaf-Friendly Workplace Adaptations")
    st.markdown("""
    Key need: reachable communication. Use text/apps instead of radio/phone for work orders/dispatch. Emergency on-call via relay/text. Ensure visual alarms (flashing lights) in work areas (mechanical rooms). Request text/email alerts from system panels if possible. Small team communication via notes, gestures, basic sign, whiteboards. JAN suggests visual paging, interpreters for training. Accommodations typically low-cost and feasible.
    """)

    st.subheader("How to Transition into a Maintenance Tech Role – Step by Step")
    st.markdown("""
    1.  **Self-Assessment and Skill Building:** List known skills. Self-study/DIY tutorials (captioned) for gaps. Focus on 1-2 core areas (electrical/plumbing). Do small home projects for practice. Take relevant safety training at current job (LOTO, forklift).
    2.  **Get Some Formal Training (short-term):** Enroll in night class (PCC basic electrical/welding/HVAC). Complete OSHA 30. Consider LME apprenticeship later. Obtain EPA 608 cert independently. These signal seriousness and provide foundational knowledge.
    3.  **Target and Apply for Jobs:** Look for entry-level ("Maintenance Tech I," "Facilities Tech," "Building Engineer Jr."). Emphasize transferable skills (problem-solving from R&D, reliability/physical capability from Amazon). Express enthusiasm for learning. Address deafness positively, explain communication/safety strategies.
    4.  **Leverage Connections:** Consider internal transfer at Amazon first for experience. Use personal network, WorkSource Oregon (can educate employers via DHHS).
    5.  **Ace the Interview/Practical Test:** Prepare for scenario questions. Explain thought process if unsure. Emphasize responsibility, safety, problem-solving, strong observation skills.
    6.  **On the Job: Establish Communication & Prove Yourself:** Discuss communication methods (texting, pagers). Ensure visual access to alarms. Collaborate on solutions. Perform tasks well, ask questions, learn from senior techs. Follow safety procedures diligently. Keep personal log.
    7.  **Grow Your Skillset & Earn Certifications:** Build skills in weaker areas. Pursue LME license or HVAC training if applicable. Advance to Lead Tech or Facilities Manager. Consider advanced certs (CFM, BOC) later.
    8.  **Accommodation Outlook:** Employers legally required (ADA) to provide reasonable, low-cost accommodations. Educate team on communication. Supportive workplaces adapt quickly.
    """)

# --- Comparison Table ---
st.header("Career Path Comparison")

# Data for the table
data = {
    "Career Path": ["Electrician", "Plumber", "HVAC/R Technician", "Machinist (CNC)", "Maintenance Tech"],
    "Typical Salary (OR)": ["~$87.6k (median), ~$45k (apprentice start)", "~$87.9k (median), ~$45k (apprentice start)", "~$66.6k (avg), ~$45k-50k (entry)", "~$59.7k (avg), ~$40k (entry)", "~$53.7k (avg), ~$40k-45k (entry)"],
    "Training Time & Requirements": ["4–5 yr apprenticeship + license", "4–5 yr apprenticeship + license", "6mo–2yr school OR 5yr apprenticeship; EPA Cert required", "2yr degree OR 3–4yr apprenticeship; or <1yr cert + OJT", "Varies; experience valued; 6–12mo courses helpful; optional LME/certs"],
    "Work Setting (Solo/Team)": ["Small crews or solo tasks", "2-person teams or solo service", "Solo service or small install teams", "Individual work at machine", "Largely solo work orders; small team"],
    "Safety Level": ["Moderate (electrical hazard, strict codes)", "Moderate (physical, hot water, confined spaces)", "Moderate (electricity, refrigerants, heights)", "Moderate (machine hazards, requires focus)", "Low–Moderate (general building, tools)"],
    "Deaf-Friendliness": ["High (visual/manual, signals)", "High (tactile/visual, written orders)", "High (visual diagnostics, text alerts)", "High (loud shop, visual indicators)", "High (written orders, solo tasks, visual alerts)"]
}
df_comparison = pd.DataFrame(data)

# Display the table using st.dataframe for better horizontal scrolling if needed
st.dataframe(df_comparison, hide_index=True)


# --- Next Steps and Resources ---
st.header("Next Steps and Resources")

st.subheader("Next Steps")
st.markdown("""
Transitioning requires effort, but you have a strong work ethic and relevant experience. Here’s a game plan:

1.  **Contact Vocational Rehabilitation (VR):** Reach out to Oregon VR Services for deaf/hard-of-hearing (DHHS). They can help fund training, provide interpreters, assist with tools, and connect with employers.
2.  **Shadow or Informational Interview:** Try to observe or talk to workers in target fields (especially Deaf tradespeople) for firsthand insight.
3.  **Enroll in Short-Term Training:** Based on your chosen path, enroll in the next available program (PCC, CCC, trade school for Summer/Fall 2025). Secure interpreting services. Apply early for apprenticeships.
4.  **Inform Your Employer (Optional):** Discuss ambitions with Amazon HR; explore internal roles, tuition reimbursement, or schedule adjustments for classes.
5.  **Update Your Resume and Apply Broadly:** Tailor resume to the trade, highlighting transferable skills (physical, safety, reliability, tools, tech aptitude, ASL). Apply to entry-level openings via job boards (Indeed, LinkedIn), WorkSource Oregon, Oregon Apprenticeship Division.
6.  **Prepare for Interviews:** Practice discussing experience and explaining accommodation needs confidently. Bring a written explanation if helpful. Emphasize meeting all non-hearing requirements.
7.  **Secure Accommodations for Training/Work:** Promptly discuss needs upon starting. Use resources like Job Accommodation Network (JAN). Request exam accommodations in advance. VR can support interpreting costs. ADA requires effective communication.
8.  **Join Deaf and Trade Networks:** Connect with peers via Facebook groups ("Deaf Electricians/Tradespeople"), NAD, HEARING ERG, Oregon DHHS contacts for support and mentoring.
9.  **Maintain Positive Attitude & Persistence:** Transition takes time (months to a year). Stay proactive. Your skills and determination are valuable in today's labor market.
""")

st.subheader("Resources")
st.markdown("""
* **Oregon Apprenticeship Opportunities:** [BOLI Apprenticeship Search](https://www.oregon.gov/boli/apprenticeship/Pages/apprenticeship-opportunities.aspx) (Searchable by trade/county)
* **Oregon Vocational Rehabilitation (Deaf/HH Services):** [Oregon VR Website](https://www.oregon.gov/odhs/vr/Pages/index.aspx) (Support for training, job placement)
* **Job Accommodation Network (JAN):** [JAN Website](https://askjan.org/) (Guides on workplace accommodations for deafness)
* **PCC Trades Programs:** [PCC Website](https://www.pcc.edu/) (Info on Machine Manufacturing, HVAC, etc.) - Search specific programs.
* **Local Union Halls:** Websites for IBEW Local 48 (electricians), UA Local 290 (plumbers/HVAC), IAM Lodge (machinists) often have apprenticeship info.
* **Job Boards:** Indeed, LinkedIn (Search for relevant titles in Beaverton/Portland)
* **Oregon Deaf and Hard of Hearing Services (DHS):** [ODHHS Website](https://www.oregon.gov/dhs/seniors-disabilities/Pages/odhhs.aspx) (May offer connections/resources)

By tapping into these resources and following a plan, you can achieve your goal of a satisfying, higher-paying career. Good luck!
""")