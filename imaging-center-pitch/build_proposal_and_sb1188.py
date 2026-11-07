"""Builds the imaging-center proposal and the SB 1188 memo (python-docx). Run: python3 build_proposal_and_sb1188.py <outdir>"""
import sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x59, 0x59, 0x59)


def base(doc, size=10.5):
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(size)
    st.paragraph_format.space_after = Pt(4)
    for s in doc.sections:
        s.left_margin = s.right_margin = Inches(0.9)
        s.top_margin = s.bottom_margin = Inches(0.8)
    for name, sz in (("Heading 1", 14), ("Heading 2", 11.5)):
        h = doc.styles[name]
        h.font.name = "Calibri"
        h.font.size = Pt(sz)
        h.font.bold = True
        h.font.color.rgb = NAVY
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(4)


def footer(doc, text):
    p = doc.sections[0].footer.paragraphs[0]
    p.text = text
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.size = Pt(8)
        r.font.color.rgb = GREY


def para(doc, text, bold=False, italic=False, size=None, color=None, align=None, after=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold, r.italic = bold, italic
    if size:
        r.font.size = Pt(size)
    if color:
        r.font.color.rgb = color
    if align is not None:
        p.alignment = align
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    return p


def rich(doc, parts, style=None):
    """parts: list of (text, bold)."""
    p = doc.add_paragraph(style=style)
    for t, b in parts:
        p.add_run(t).bold = b
    p.paragraph_format.space_after = Pt(3)
    return p


def bullet(doc, text, lead=None):
    p = doc.add_paragraph(style="List Bullet")
    if lead:
        p.add_run(lead).bold = True
    p.add_run(text)
    p.paragraph_format.space_after = Pt(2)
    return p


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto")
    sh.set(qn("w:fill"), hexcolor)
    tcPr.append(sh)


def table(doc, header, rows, widths=None, size=9):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]
        c.text = ""
        r = c.paragraphs[0].add_run(h)
        r.bold = True
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade(c, "1F3A5F")
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            bold = isinstance(v, tuple)
            txt = v[0] if bold else v
            r = cells[i].paragraphs[0].add_run(txt)
            r.font.size = Pt(size)
            r.bold = bold
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


# ---------------------------------------------------------------- PROPOSAL
def proposal():
    doc = Document()
    base(doc)
    footer(doc, "RGF Global Ventures LLC, DBA Elovar Technology Solutions  |  Proposal, November 2026  |  Confidential")

    # 1. Cover
    for _ in range(5):
        doc.add_paragraph()
    para(doc, "ELOVAR TECHNOLOGY SOLUTIONS", bold=True, size=12, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, "Operations and Automation Engagement for Your New Imaging Center", bold=True, size=22,
         color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, after=14)
    para(doc, "Proposal: one engagement, five phases, fixed scope, fixed fee", size=13,
         align=WD_ALIGN_PARAGRAPH.CENTER, after=30)
    para(doc, "Prepared for", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    para(doc, "Dr. Luis Ramos, Fernando Escarzaga and Jesse Martinez", align=WD_ALIGN_PARAGRAPH.CENTER, after=20)
    para(doc, "Prepared by", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    para(doc, "Rick Finlay, RGF Global Ventures LLC, DBA Elovar Technology Solutions", align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    para(doc, "El Paso, Texas  |  November 2026", align=WD_ALIGN_PARAGRAPH.CENTER, after=40)
    para(doc, "This proposal is valid for 30 days from the date above. [RICK CONFIRM: validity period]",
         italic=True, size=9, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_page_break()

    # 2. What we heard
    doc.add_heading("1. What we heard", level=1)
    para(doc, "These are the requirements you gave us on November 5, in your words where we have them. "
              "Phase 1 starts from this list rather than asking again.")
    heard = [
        ("Front end. ", "\"Patients call or text to schedule and show up with their forms done.\" A concierge itinerary, "
         "and a driver's license and insurance card scan at check-in that flows to the RIS and billing."),
        ("Know who will not show. ", "Flag the patients likely to miss before they do, and fill the slot."),
        ("Prior authorization and appeals on day one, ", "working the back end with the clock visible."),
        ("Underpayment detection. ", "\"The payer contracted $150 and paid less.\" Catch it and draft the appeal."),
        ("A Monday push report. ", "\"Show me all the rats\": what happened, why, which tech, which referring physician. "
         "Pushed to you, not a dashboard you have to open."),
        ("Referrer leakage. ", "Know when a referring physician's volume drops or moves elsewhere."),
        ("Walk-outs. ", "\"Nobody walks out the door unless I know.\""),
        ("Billing leakage control. ", "A past billing vendor leaked money. \"Never change your billing system\": "
         "pick it right the first time, then audit it."),
        ("Offshore billing and Texas SB 1188. ", "Answered in a separate memo for your counsel."),
        ("Coding from the radiologist report, ", "so multiple findings are captured as charges."),
        ("Twelve months of support after go-live.", ""),
        ("A full operating budget, ", "on-premises, hybrid and cloud, and the security of data in transit."),
        ("Who owns cybersecurity and patching.", ""),
        ("RIS and PACS selection ", "from your shortlist: RamSoft, Konica Minolta, Exa. AbbaDox as a front end only."),
        ("You own the code and the specification, in perpetuity.", ""),
    ]
    for lead, rest in heard:
        bullet(doc, rest, lead=lead)
    para(doc, "We also asked for your payer mix, monthly volume by modality, and prior authorization, denial and appeal "
              "counts. Those drive the staffing and budget answers in Phases 1 and 3.", italic=True)

    # 3. Approach
    doc.add_heading("2. Approach", level=1)
    para(doc, "Your center has not signed its systems or hired its front office yet. That makes every choice cheaper "
              "now than it will be after opening. The engagement is built around that:")
    bullet(doc, " What you need comes first, then the systems that meet it, then the design, then the build, then testing. "
                "Each phase ends in a document you sign, and the next phase starts only after you sign it.", lead="One order of work.")
    bullet(doc, " The RIS, PACS, phones, dictation and billing are bought from vendors with support organizations. "
                "I build only the pieces no vendor does well for a center your size, and each one is decided per requirement.", lead="Buy the systems of record, build the gaps.")
    bullet(doc, " Every agent drafts, flags or reports. A person on your staff approves every payer submission, every appeal "
                "and every patient-facing change.", lead="A human signs.")
    bullet(doc, " Staff for the manual workflow at opening. I will not ask you to hire thin against a date of mine. "
                "The staffing plan shows which roles change as each piece goes in, and each change is your later decision.", lead="Hiring is never a bet on my schedule.")
    bullet(doc, " The agents handle claims, schedules, eligibility and business reporting. They never read images, "
                "judge a study, or recommend what to order.", lead="Administrative only.")

    # 4. Phases
    doc.add_heading("3. The five phases", level=1)
    table(doc, ["#", "Phase", "Timing", "Fee"], [
        ["1", "Discovery and Requirements", "Nov 2026 to mid-Dec 2026", "$7,000"],
        ["2", "Vendor and System Selection", "Mid-Dec 2026 to Jan 2027", "$8,000"],
        ["3", "Design and Staffing Plan", "Feb 2027", "$7,000"],
        ["4", "Build and Configure", "Mar to Apr 2027", "$14,000"],
        ["5", "Testing, Training and Go-Live", "May 2027", "$9,000"],
        [("",), ("Total, ready for an opening around June 2027 with about a month of buffer",), ("Nov 2026 to May 2027",), ("$45,000",)],
    ], widths=[0.3, 3.4, 1.9, 0.9])

    phases = [
        ("Phase 1. Discovery and Requirements (Nov to mid-Dec, $7,000)", [
            "Working sessions with all three of you, and with your radiologists where it touches them.",
            "Requirements per system, and a flow map from referral to payment.",
            "Make-or-buy decision for each requirement, with a ballpark running cost for anything built.",
            "The contract terms every vendor must accept: data export in DICOM and HL7 with no penalty, interface fees fixed at signing, API access, and worklist access.",
            "First-pass operating budget: running costs for on-premises, hybrid and cloud, based on your volumes.",
            "Security ownership map, first draft: a RACI naming who is responsible for patching, backups, access reviews, monitoring and incident response for each system (you, each vendor, or me).",
            "Opening checklist owners named, starting with payer enrollment and credentialing, the longest lead item.",
        ], "Sign-off: you approve the Requirements and Roadmap document."),
        ("Phase 2. Vendor and System Selection (mid-Dec to Jan, $8,000)", [
            "Selection for scheduling; RIS and PACS (as one bundled system and as separate systems); prior authorization and eligibility; patient phones, IVR and AI answering; radiologist dictation; billing and clearinghouse; modality worklist, reading workstations and image sharing.",
            "Scorecards, live demos with your radiologists, reference calls, and a five-year total cost of ownership per option.",
            "Integration list: every interface the plan needs, HL7 or API, which direction, and what the vendor charges.",
            "Billing vendor selected carefully, once, with audit access written into the contract.",
            "Negotiating support for the contracts you sign. You sign vendor contracts directly.",
        ], "Sign-off: you approve the Vendor Selection Report and its recommendation."),
        ("Phase 3. Design and Staffing Plan (Feb, $7,000)", [
            "Enterprise architecture: how the selected systems and the built pieces connect, where data lives, how it moves and how it is encrypted.",
            "Workflows for the front desk, scheduling, authorization, billing follow-up and records.",
            "Staffing plan: how each role's work runs at opening, and the order in which roles change as each piece goes in. Never a headcount target.",
            "Operating budget, final: three ways to host what I build (your cloud, hybrid, on-site), each with a three-year cost, and a monthly cap I cannot pass without your approval.",
            "Security ownership map, final: the RACI above, carried into the runbooks and the support terms.",
            "Specification and acceptance tests for each piece I build.",
        ], "Sign-off: you approve the Architecture, Workflow and Staffing Plan."),
        ("Phase 4. Build and Configure (Mar to Apr, $14,000)", [
            "Vendors configure their own products. I manage them, connect everything, and build the pieces below.",
            "Every system, bought and built, set up, connected and passing end-to-end tests on test data.",
        ], "Sign-off: you approve the end-to-end test results."),
        ("Phase 5. Testing, Training and Go-Live (May, $9,000)", [
            "Testing with your staff on realistic scenarios, downtime drills, and fixes.",
            "Training by role, with written procedures and runbooks for every built piece.",
            "Go-live readiness review and support through opening week.",
        ], "Sign-off: you sign the go-live readiness checklist."),
    ]
    for title, items, signoff in phases:
        doc.add_heading(title, level=2)
        for it in items:
            bullet(doc, it)
        para(doc, signoff, bold=True, after=4)

    doc.add_heading("Build and buy recommendations", level=2)
    para(doc, "Starting positions from November 5. Phase 1 confirms each one against your requirements.")
    table(doc, ["Area", "Recommendation", "Why"], [
        ["Prior authorization, appeals and the underpayment check (contract rate vs. remittance)", ("BUILD",), "Your top priority. Vendors sell pieces; nobody ties the clock, the appeal and the remit check together for one center."],
        ["Ranked waitlist and backfill, with the no-show risk flag", ("BUILD, small",), "Fills the slots the RIS reminders do not save."],
        ["Records in and out (requests, deadlines, fees, priors)", ("BUILD, small",), "Hard statutory deadlines; small, clear rules."],
        ["Owner agent and the Monday exception report (techs, referrers, walk-outs, billing audit)", ("BUILD",), "Reads your own data and pushes exceptions to you. Delivery date set in the Phase 3 plan, not promised here."],
        ["Voice and IVR, patient reminders, RIS and PACS", ("BUY, with selection help",), "Systems of record and patient-facing systems need a vendor with a support organization."],
        ["Billing vendor and clearinghouse", ("SELECT CAREFULLY",), "\"Never change your billing system.\" Chosen once in Phase 2, with audit access and data in your name."],
    ], widths=[2.3, 1.4, 2.8])

    # 5. Fee and payments
    doc.add_heading("4. Fixed fee and payment schedule", level=1)
    para(doc, "$45,000 total, fixed scope and fixed fee, for one center with one selected system per category. "
              "If your opening date moves, the timeline moves and the price does not.")
    table(doc, ["When", "Amount", "For"], [
        ["At signing", "$4,000", "Phase 1 start"],
        ["Phase 1 delivery (mid-Dec 2026)", "$3,000", "Phase 1 balance"],
        ["Phase 2 start, after Phase 1 sign-off", "$8,000", "Phase 2 in full"],
        ["Phase 3 start (Feb 2027)", "$7,000", "Phase 3 in full"],
        ["March 1, 2027", "$7,000", "Phase 4, first half"],
        ["April 1, 2027", "$7,000", "Phase 4, second half"],
        ["Phase 5 start (May 2027)", "$9,000", "Phase 5 in full"],
        [("Total",), ("$45,000",), ""],
    ], widths=[2.8, 1.0, 2.7])
    bullet(doc, "Each payment falls after you have signed off the phase before it, so you never pay ahead of a deliverable you have not approved.")
    bullet(doc, "Work outside the five phases, including work for additional centers: $150 an hour, approved by you in writing first, "
                "billed against a retainer balance you top up, or rescoped as its own fixed-fee engagement.")
    bullet(doc, "Running costs (cloud, AI usage, texting, clearinghouse, vendor licenses) are not in the $45,000. They run in accounts in your "
                "name, at cost with no markup, with a monthly statement.")
    bullet(doc, "Invoices are due within 15 days. [RICK CONFIRM: payment terms and accepted methods]")

    # 6. Support
    doc.add_heading("5. Support after go-live (12 months)", level=1)
    bullet(doc, "$3,000 a month for up to 20 hours; $150 an hour beyond 20, approved first.")
    bullet(doc, "Starts at go-live (planned June 2027) for a 12-month term, with a 90-day check-in. Separate from the $45,000.")
    bullet(doc, "Covers monitoring, fixes and updates to the pieces I built, security patching under the RACI, vendor coordination, "
                "and small changes inside existing workflows.")
    bullet(doc, "Response times in writing. [RICK CONFIRM: e.g. 4 business hours for a system-down issue, 1 business day otherwise]")
    bullet(doc, "Unused hours do not roll over. [RICK CONFIRM]  Either party may end the plan with 30 days' notice after the 90-day check-in. [RICK CONFIRM]")

    # 7. Ownership
    doc.add_heading("6. Ownership and control", level=1)
    bullet(doc, " Everything I build lives in accounts in your name: code repository, cloud, database. You own the code and the specifications, in perpetuity.", lead="Your accounts, your code.")
    bullet(doc, " My access is a login you grant. You can revoke it at any time, and the systems keep running without me.", lead="Revocable access.")
    bullet(doc, " A person on your staff approves every payer submission, appeal and patient-facing action. Any move from reviewing every item to sampling happens only on measured accuracy and with your written approval.", lead="Human in the loop.")
    bullet(doc, " Each built piece ships with a runbook: what it does, how to restart it, how to turn it off, and who to call.", lead="Runbooks.")
    bullet(doc, " Built pieces connect over standard interfaces (HL7, FHIR, DICOM, X12, documented APIs), so another engineer can maintain them.", lead="Standard interfaces.")
    bullet(doc, " Your data is never used to train AI models, and every AI vendor that touches patient data signs a BAA.", lead="No training on your data.")

    # 8. Assumptions
    doc.add_heading("7. Assumptions, client responsibilities and exclusions", level=1)
    doc.add_heading("Assumptions", level=2)
    for a in ["One center, one selected system per category.",
              "Phase 4 depends on signed vendor contracts, sandbox and test access to the RIS, clearinghouse and payer portals, and a BAA with each vendor in time for March. If vendor access is late, the build moves with it.",
              "The opening is planned for around June 2027. [RICK CONFIRM: current target date from the owners]"]:
        bullet(doc, a)
    doc.add_heading("Your responsibilities", level=2)
    for a in ["A named decision-maker for each sign-off, and sign-off or written comments within 5 business days. [RICK CONFIRM]",
              "Payer mix, volumes by modality, fee schedules and payer contracts (needed for the underpayment check).",
              "Vendor contracts signed directly by the center, and vendor fees and running costs paid directly.",
              "Your own legal and compliance review, including the offshore billing question and payer contracts.",
              "Hiring, credentialing, payer enrollment, accreditation and licensing. I help track them; you own them."]:
        bullet(doc, a)
    doc.add_heading("Exclusions", level=2)
    for a in ["No clinical or FDA-regulated work: nothing that reads or interprets images, judges appropriateness, or recommends studies.",
              "No reselling: I do not resell hardware, software or vendor licenses, and I take no vendor commissions.",
              "No legal, billing-compliance or coding certification advice. The report-to-charge check flags gaps for your coders; it does not code.",
              "Equipment, network cabling and modality installation are not included.",
              "Work for additional centers, or a system of record built by me, is out of scope (see section 4)."]:
        bullet(doc, a)

    # 9. Acceptance
    doc.add_heading("8. Acceptance", level=1)
    para(doc, "Signing below accepts this proposal. A short services agreement with a BAA follows on these terms. [RICK CONFIRM: separate agreement, or sign this proposal as the agreement]")
    t = doc.add_table(rows=5, cols=2)
    labels = [("For the center", "For RGF Global Ventures LLC, DBA Elovar Technology Solutions"),
              ("Entity: [RICK CONFIRM: client legal entity name]", "Name: Richard Finlay"),
              ("Name:", "Title: Managing Member"),
              ("Signature:", "Signature:"),
              ("Date:", "Date:")]
    for i, (l, r) in enumerate(labels):
        for j, txt in enumerate((l, r)):
            c = t.rows[i].cells[j]
            c.text = ""
            run = c.paragraphs[0].add_run(txt)
            run.bold = i == 0
            c.paragraphs[0].paragraph_format.space_after = Pt(12)
    doc.save(f"{OUT}/RGF_Imaging_Center_Proposal_2026-11.docx")


# ---------------------------------------------------------------- SB 1188 MEMO
def memo():
    doc = Document()
    base(doc, size=10)
    footer(doc, "Research for your counsel, not legal advice  |  RGF Global Ventures LLC, DBA Elovar Technology Solutions")
    para(doc, "MEMO", bold=True, size=16, color=NAVY, after=2)
    for k, v in [("To", "Dr. Luis Ramos, Fernando Escarzaga, Jesse Martinez"),
                 ("From", "Rick Finlay, Elovar Technology Solutions"),
                 ("Date", "November 2026"),
                 ("Re", "Offshore (India) billing and Texas SB 1188")]:
        rich(doc, [(f"{k}:  ", True), (v, False)])
    p = para(doc, "This is research for your counsel, not legal advice. Please have your attorney confirm it before you sign a billing contract.",
             italic=True, bold=True, size=9.5, color=RGBColor(0x9C, 0x1C, 0x1C))

    doc.add_heading("Bottom line", level=2)
    bullet(doc, " SB 1188 regulates where records are physically stored, not who accesses them. US-hosted records with properly "
                "scoped offshore billing access appear permissible under SB 1188 itself.", lead="SB 1188 is a storage rule.")
    bullet(doc, " The Texas Medicaid managed care contract (UMCC §4.11) bars offshore remote access by the MCO's \"subcontractors, vendors, "
                "agents, and service providers,\" and MCO provider agreements may flow that down to you. Keep Medicaid work US-only until "
                "counsel reviews your MCO agreements.", lead="The real risk is Medicaid.")

    doc.add_heading("What the law says", level=2)
    rich(doc, [("§183.002(a): ", True), ("records must be \"physically maintained in the United States or a territory of the United States,\" "
               "including records held by a cloud provider.", False)])
    rich(doc, [("§183.002(b): ", True), ("records must be \"accessible only to individuals who require the information to perform duties ... "
               "related to treatment, payment, or health care operations.\"", False)])
    para(doc, "Billing is \"payment,\" and (b) has no geographic limit. The storage duty took effect January 1, 2026. Penalties run up to "
              "$5,000 per negligent violation, $25,000 per knowing violation, and $250,000 where data is used for financial gain. "
              "The billing vendor itself is likely a covered entity under the same law. HIPAA has no offshore ban but requires a BAA. "
              "Medicare Advantage plans may require offshore attestations; traditional Medicare does not bar an offshore billing vendor.")
    para(doc, "The risk point: a remote session that downloads, caches, prints or syncs files to a device in India arguably creates "
              "a record \"physically maintained\" outside the US. The controls below exist to prevent that.")

    doc.add_heading("Safeguards if you use an offshore vendor", level=2)
    for lead, txt in [
        ("No data at rest offshore. ", "Access only through VDI or a browser portal, with download, print, copy and paste, local drives and screenshots disabled. Backups, logs and scans stay US-hosted. Written into the contract."),
        ("BAA chain. ", "A BAA with the vendor and each subcontractor, the vendor's written acknowledgment that Texas ch. 181 and ch. 183 apply to it, HB 300 training records, US governing law and venue, indemnity and cyber insurance."),
        ("Role-based access. ", "Billing fields only, no images or full charts where possible, MFA, IP allow-listing, and quarterly access reviews."),
        ("Logging. ", "Every session logged, a SOC 2 Type II or HITRUST report, an annual audit, and a documented risk analysis that covers offshore access."),
        ("Segregated Medicaid. ", "Medicaid and Medicaid managed care claims handled by US staff only, walled off from offshore work, until counsel clears the MCO contracts."),
    ]:
        bullet(doc, txt, lead=lead)
    rich(doc, [("How the billing-audit agent watches the vendor: ", True),
               ("it compares charges against signed reports and remittances, flags underpayments, gaps and late follow-up, and reviews the "
                "vendor's access logs for logins from outside approved locations and any Medicaid claim touched by an offshore account. "
                "Exceptions go into your Monday report.", False)])

    doc.add_heading("Questions your counsel must confirm", level=2)
    for q in ["Whether any rules or agency agreements adopted under §183.012 define \"maintain\" or \"store\" or address remote access.",
              "Whether your Texas Medicaid, CHIP and STAR managed care provider agreements flow UMCC §4.11 down to your billing vendor.",
              "Any offshore attestation requirements in your Medicare Advantage plan contracts.",
              "Whether a VDI setup with no local storage satisfies \"physically maintained in the United States\" for cached or temporary data.",
              "The specific Indian vendor's BAA and ch. 181 compliance, and whether the contract is enforceable in India.",
              "Any Attorney General enforcement under ch. 183 to date (we found none)."]:
        doc.add_paragraph(q, style="List Number").paragraph_format.space_after = Pt(1)
    para(doc, "Sources: SB 1188 enrolled text (Tex. Health & Safety Code ch. 183); HHSC Uniform Managed Care Contract v2.45 §4.11; "
              "BakerHostetler (Aug 2025) and Shumaker (Dec 2025) commentary. Full research brief available on request.",
         italic=True, size=8.5, color=GREY)
    doc.save(f"{OUT}/RGF_SB1188_Offshore_Billing_Answer_2026-11.docx")


proposal()
memo()
print("built")
