# Run Costs After the Build: One El Paso Imaging Center

**Prepared:** 2026-11-03 by Sherlock, for the 2026-11-05 lunch
**Scope:** monthly cost to keep running what the $45k engagement builds (prior auth agent + eligibility, cancellation backfill, records tracker, owner's agent, report-assistance integration). Excludes the RIS, PACS, and phones the center buys anyway.

## Sourcing note (read first)

Prices below come from my knowledge of published vendor price pages up to mid-2026. I did **not** live-fetch each page in this pass. Every line is marked **[S]** (a published list price, re-check before quoting) or **[E]** (my estimate). Before anything goes on a slide as a dollar figure, re-confirm the five **[S]** lines that matter most: Anthropic per-token prices, AWS RDS and Fargate rates, the Twilio HIPAA plan, the clearinghouse quote, and the interface engine license.

---

## Plain-English summary

- **Expected run cost: about $1,500 to $2,000 a month in vendors, plus Rick's $4k retainer for support.** Low case about $900; high case about $3,800 in vendors.
- **The AI itself is cheap.** Even at 900 studies a month, the Claude tokens are roughly $100 to $400 a month. That is not where the money goes.
- **The money goes to the boring HIPAA plumbing:** a properly locked-down cloud setup (about $500 to $900), the clearinghouse for payer transactions ($150 to $700), and texting under a signed HIPAA agreement (which can be the biggest surprise, see item 3).
- **One-time setup outside the $45k: about $6k to $20k,** mostly a penetration test and the clearinghouse/interface onboarding.
- **Compare to staff time:** one prior auth coordinator costs roughly $3,500 to $4,500 a month loaded in El Paso [E]. If the agent saves even half a person, it pays for its own plumbing.

---

## Volume assumptions

| Driver | Low | Expected | High |
|---|---|---|---|
| Studies / month | 400 | 650 | 900 |
| Needing prior auth (40 to 60%) | 160 | 300 | 540 |
| Appeals (denials, ~8 to 12% of auths) | 15 | 30 | 65 |
| Eligibility checks (every scheduled study + rechecks) | 500 | 850 | 1,200 |
| Patient SMS (backfill offers, a few hundred) | 300 | 600 | 1,500 |
| Owner questions / month | 50 | 150 | 400 |

---

## 1. HIPAA-eligible cloud hosting (one isolated instance)

AWS us-east/us-west assumed. The AWS BAA is free and self-serve via AWS Artifact **[S]**; Azure and GCP also include the BAA at no charge **[S]**. All three keep data in US regions, which satisfies Texas SB 1188 if region-locked.

| Component | Monthly | Basis |
|---|---|---|
| Compute (2 small containers, Fargate or 2 small EC2) | $60 to $150 | [S] list rates, [E] sizing |
| Managed Postgres, Multi-AZ, encrypted (db.t4g.medium class) | $130 to $260 | [S] |
| Storage + backups (S3, RDS snapshots, 35-day retention) | $20 to $60 | [E] |
| Logging + audit trail (CloudWatch, CloudTrail, 6-year archive) | $40 to $120 | [E] |
| WAF + load balancer | $40 to $70 | [S] |
| KMS keys, Secrets Manager, NAT, data transfer | $50 to $120 | [E] |
| Security services (GuardDuty, Security Hub, Config) | $30 to $100 | [E] |
| **Subtotal** | **$370 to $880** | |

Mostly fixed. Volume barely moves it at this size.

## 2. LLM tokens (Claude under BAA)

Anthropic offers a BAA for the API on eligible features (excludes Computer Use and Web Fetch, as the constraint states). Bedrock in a US region is also covered by the AWS BAA and keeps billing on one invoice. Pricing on a Sonnet-class model: about **$3 per million input tokens, $15 per million output [S, re-check]**; prompt caching cuts repeated policy text by up to 90% [S].

| Transaction | Tokens per item [E] | Cost per item [E] |
|---|---|---|
| Prior auth packet (order, history, payer criteria, draft) | 40k in / 4k out | $0.18 to $0.30 |
| Appeal letter (denial + record + policy) | 80k in / 6k out | $0.35 to $0.60 |
| Owner question (SQL generated, numbers checked) | 10k in / 1k out | $0.04 to $0.08 |
| Backfill / records triage | 3k in / 0.5k out | ~$0.02 |

| Case | Monthly tokens cost |
|---|---|
| Low | ~$60 |
| Expected | ~$150 |
| High (Opus-class for appeals, retries, 3x overhead for agent loops) | ~$400 |

Scales directly with volume. Budget 2 to 3x the raw math for retries and multi-step agent loops.

## 3. SMS / voice

The catch: Twilio signs a BAA only on its higher-tier editions, historically with a minimum annual commitment in the thousands [S, verify current terms]. Per-message rates are cheap (about $0.008 to $0.01 per SMS plus carrier fees, plus 10DLC registration around $4 to $15/month [S]).

| Option | Monthly |
|---|---|
| A. Use the RIS vendor's built-in texting (already under its BAA) | $0 incremental [E] |
| B. HIPAA-eligible SMS vendor with BAA included (several healthcare SMS vendors) | $100 to $300 [E] |
| C. Twilio on a BAA-eligible edition | $300 to $1,500+ effective, driven by the commitment [E] |

**Recommendation:** option A or B. Keep message content PHI-light ("You have an offer for an earlier appointment, reply YES") regardless, for TCPA and HIPAA.

## 4. Clearinghouse: EDI 278 and 270/271 eligibility

Payer FHIR PAS (CMS-0057-F) APIs are free to call but rolling out unevenly through 2027, so expect the clearinghouse to carry most traffic at opening.

| Item | Monthly |
|---|---|
| Clearinghouse platform fee (Availity, Change/Optum, Waystar, Stedi class) | $0 to $300 [E] |
| Eligibility 270/271 at ~$0.10 to $0.30 each [E] | $50 to $360 |
| Prior auth 278 at ~$0.25 to $1.00 each, where the payer supports it [E] | $40 to $540 |
| **Subtotal** | **$100 to $1,000** (expected ~$350) |

Often bundled into the center's claims clearinghouse contract, which they need anyway. **Ask the billing vendor first;** the marginal cost may be close to zero. Scales with volume.

## 5. Interface engine (HL7 v2 from the RIS)

NextGen changed Mirth Connect in 2025: newer versions are no longer open source and require a commercial license [S, re-check exact version and price]. Options:

| Option | Monthly |
|---|---|
| Open Integration Engine (community fork of the last open Mirth) or a small custom HL7 listener Rick maintains | $0 license, labor only |
| Commercial Mirth / NextGen Connect license | ~$400 to $1,500 [E, get a quote] |
| RIS vendor's interface fee (very common, often one-time $2k to $10k plus a monthly) | $0 to $300 [E] |

**Recommendation:** fork or custom listener, inside the same AWS account. The RIS vendor's per-interface fee is the line most likely to surprise; put it in the RIS contract negotiation now (candidate #3).

## 6. Monitoring, security, domain, email, testing

| Item | Monthly |
|---|---|
| Uptime + error monitoring (BAA-capable tier, or self-hosted on AWS) | $0 to $150 [E] |
| Endpoint/vuln scanning, MFA, password manager | $30 to $100 [E] |
| Domain + DNS + transactional email (AWS SES under the BAA) | $5 to $30 [S/E] |
| Off-site backup copy (second US region) | $10 to $40 [E] |
| Annual pen test + HIPAA security risk analysis, amortized ($6k to $15k/yr) | $500 to $1,250 [E] |
| **Subtotal** | **$545 to $1,570** |

## 7. Support and maintenance labor (separate from infra)

Already priced: the **$4,000/month retainer**, $150/hr beyond it. Covers payer rule changes, RIS upgrades, monitoring, patching, monthly statement. Not a vendor line.

---

## Totals (vendors only, before retainer)

| | Low | Expected | High |
|---|---|---|---|
| 1. Cloud hosting | $370 | $600 | $880 |
| 2. Claude tokens | $60 | $150 | $400 |
| 3. SMS | $0 | $150 | $600 |
| 4. Clearinghouse | $100 | $350 | $1,000 |
| 5. Interface engine | $0 | $50 | $300 |
| 6. Monitoring, security, pen test | $400 | $650 | $1,000 |
| **Monthly** | **~$930** | **~$1,950** | **~$4,180** |
| **Annual** | **~$11k** | **~$23k** | **~$50k** |

**Scales with volume:** tokens, clearinghouse, SMS. **Fixed:** hosting, security, pen test, interface.

**One-time setup (outside the $45k):** pen test before go-live $6k to $15k; clearinghouse enrollment $0 to $1k; RIS interface fee $0 to $10k; 10DLC/SMS registration under $100. **Total about $6k to $25k,** most of it negotiable or avoidable via the RIS contract.

---

## How to present it

These owners have been burned by vendors. What makes them receptive: **they own everything, they see every dollar, nothing is hidden in a bundle.**

1. **Pass-through at cost, not bundled.** Bundling looks like markup and lock-in. Pass-through with receipts is the opposite of what burned them.
2. **The center owns the accounts.** AWS, Anthropic, clearinghouse, and SMS accounts are opened in the center's name on the center's card; the center signs each BAA. Rick is an administrator. If Rick disappears, they keep running and hand the keys to anyone.
3. **An estimate with a cap.** Give the expected number and a ceiling. Budget alerts at 80%; Rick must get written OK before exceeding the cap.
4. **A one-page monthly statement:** each vendor's bill, volume handled, cost per authorization, hours saved.
5. **Frame against staff time, never against "AI".** Cost per prior auth (about $5 to $7 all-in at expected volume) versus the coordinator time it replaces.

### Slide-ready table

| What keeps it running | Expected / month | Who owns it |
|---|---|---|
| Secure US cloud (HIPAA agreement signed) | about $600 | Your account |
| AI usage | about $150 | Your account |
| Payer transactions | about $350, often in your billing contract | Your account |
| Texting, security, testing | about $850 | Your account |
| **Total, billed to you at cost** | **about $2,000, capped at $3,000** | **You own it all** |
| Support and upkeep (Rick) | $4,000 retainer | Cancel any time |

### Three spoken lines

1. "Everything runs in accounts in your name. I hold the admin keys, you hold the ownership. If you ever let me go, nothing stops."
2. "I don't mark any of it up. You see the actual bills every month on one page, with what each one did for you."
3. "At expected volume it is about two thousand a month, with a cap I can't pass without your OK. That's less than half of one coordinator."

### Contract clause (draft, have counsel review)

> **Third-Party Services and Operating Costs.** All cloud, software, AI, messaging, clearinghouse, and security services required to operate the Deliverables ("Third-Party Services") shall be contracted in Client's name, billed directly to Client, and covered by business associate agreements executed by Client. Consultant shall act as administrator of the Third-Party Services under Client's authority and shall not mark up their cost. Consultant estimates Third-Party Service costs at approximately $2,000 per month and shall not take any action expected to cause those costs to exceed $3,000 in any month (the "Cap") without Client's prior written approval. Consultant shall deliver a monthly statement itemizing each Third-Party Service charge, transaction volumes, and any variance from the estimate. On termination, Consultant shall within ten business days transfer all administrative credentials, documentation, and data to Client or its designee, and remove its own access. Third-Party Service costs are separate from the Fees and the Support Retainer.

---

## Total cost of ownership and operating budget: three hosting options

**Deliverable framing:** a ballpark range in Phase 1 (this section), refined into a firm operating budget in Phase 3 once the RIS, clearinghouse, and payer mix are known.

**Common assumptions:** expected volume of 650 studies and 300 prior auths a month (see the volume table). Support labor is Rick's $4,000 monthly retainer at $150/hr, plus the extra hours each option needs beyond it. Clearinghouse, texting, and pen test costs apply to all three options. Hardware prices are Apple US list prices as I know them to mid-2026 **[S, re-check]**. Everything else is **[E]**.

### Privacy, stated precisely

- **External LLM API (options A and B):** the prompt data **is sent to the provider** (Anthropic directly, or AWS Bedrock). The BAA makes the provider a business associate. Zero-data-retention terms govern whether the provider stores the data and confirm it is not used for training. "No data leaves" is false. Accurate wording: "it leaves under a signed HIPAA agreement and is not retained or trained on."
- **Local tokenization (option B):** the appliance swaps names, MRNs, member IDs, dates of birth, addresses, and phone numbers for tokens before the call, then swaps them back afterward. This **reduces, but does not remove**, PHI. A prior auth packet or appeal has to carry clinical content (diagnosis, history, prior imaging, symptoms, dates of service), and in context that is still health information about an identifiable patient. It is not HIPAA de-identification under Safe Harbor or Expert Determination. The BAA is still required.
- **Local LLM (option C):** no PHI goes to an AI provider. But **PHI still leaves the building** for the payer itself (the 278 or PAS submission goes to the payer through the clearinghouse), for eligibility checks, for texting, and in offsite backups (encrypted before upload). Accurate wording: "no AI company sees your patients' data."

### Option A: fully hosted cloud

Everything runs in the center's own AWS account under the AWS BAA. Claude runs via Bedrock or Anthropic directly under a BAA with zero data retention.

- **Pros:** highest uptime (Multi-AZ, survives a power or internet outage at the center). AWS covers physical security. No new HIPAA facility duties for staff. Least maintenance. Best model quality.
- **Cons:** clinical content goes to the LLM provider under the BAA. Monthly cloud bill. The agents depend on the center's internet only for staff access, not for the agents themselves to run.

### Option B: hybrid (on-site Mac mini + local tokenization + cloud DB and backup)

A Mac mini at the center runs the agents and the tokenization layer and receives HL7 from the RIS. The cloud holds the database, backups, and audit logs. Claude is called with tokenized prompts.

- **Pros:** names and IDs never reach the LLM provider. A good fit if the RIS only sends HL7 over the local network. Cloud data survives a building outage.
- **Cons:** clinical PHI still reaches the provider, so the BAA is still required. Two environments to secure and patch. The agents stop when the center loses power or internet, and messages queue until it comes back. The tokenization layer is custom code that must be tested against every packet type: if it misses one field, the privacy claim is broken. The center takes on physical-safeguard duties (locked room, access log, device inventory, contingency plan; 45 CFR 164.310).

### Option C: fully on-site with a local open-weight LLM

A Mac Studio class machine (M-series Ultra, 256 to 512GB unified memory) runs an open-weight model in roughly the 70B to 120B class (Llama, Qwen, or gpt-oss families). The database and agents also run on-site, with a second unit for failover. Encrypted backups go offsite.

- **Pros:** no AI provider sees PHI. No per-token cost. The owners own the hardware outright.
- **Cons:**
  - **Quality:** open models in this size class are noticeably weaker than frontier Claude at long, rule-heavy reasoning such as matching a payer's medical-necessity criteria and drafting a persuasive appeal. Expect more drafts that staff have to fix, and possibly lower approval rates on appeals. This must be measured on real (synthetic-first) packets before committing.
  - **Speed:** local generation on a long packet takes tens of seconds to minutes. That is fine for batch work but slower for live owner questions.
  - **Maintenance:** Rick owns model selection, quantization, upgrades, a regression test set, and re-validation every time the model changes. There is no vendor fixing quality problems.
  - **Risk:** single-site uptime, theft risk, and the full physical-safeguard burden fall on the center. The hardware is obsolete in 3 to 4 years.

### Numbers

| | A. Cloud | B. Hybrid | C. Fully on-site + local LLM |
|---|---|---|---|
| **One-time** | $6k to $25k (pen test, interfaces, onboarding) | $12k to $37k (adds Mac mini + spare, UPS, cabinet ~$3.5k to $6k; tokenization build 20 to 40 hrs ~$3k to $6k) | $27k to $52k (2 Mac Studio ~$12k to $20k, UPS/cabinet; model evaluation and validation 40 to 80 hrs ~$6k to $12k; pen test) |
| **Monthly vendors, low / expected / high** | $930 / $1,950 / $4,180 | $1,050 / $2,050 / $4,300 (smaller cloud, same tokens, plus the appliance) | $1,200 / $2,000 / $3,500 (no cloud or tokens; adds hardware amortized over 3 yrs, backup, MDM) |
| **Labor beyond the $4k retainer, monthly** | $0 | $500 to $1,500 (appliance + tokenizer upkeep) | $2,250 to $4,500 (model upkeep, regression testing, hardware) |
| **3-year TCO incl. retainer, low / expected / high** | **~$184k / ~$226k / ~$320k** | **~$212k / ~$274k / ~$390k** | **~$295k / ~$378k / ~$484k** |
| **Uptime** | Highest | Medium (site-dependent agents) | Lowest without the spare |
| **Privacy vs AI vendor** | Full packet under BAA + zero retention | Clinical content under BAA, identifiers stay local | Nothing to an AI vendor |
| **Output quality** | Best | Best (same model) | Lower, must be proven |
| **Staff HIPAA duties** | None new | Room, log, inventory | Room, log, inventory, contingency for everything |
| **Lock-in** | Low (center's account) | Low | Lowest hardware lock-in, highest dependence on Rick |

The retainer accounts for $144k of every 3-year figure. Vendor spend alone over 3 years is about $76k (A), $94k (B), and $112k (C) at expected volume, including one-time costs.

### Recommendation

**Option A, with option B's tokenization as an add-on if the owners want it.** A is the cheapest, most reliable, and simplest for a lean staff, and it uses the strongest model, which matters most for appeals. The privacy concern is real but is handled contractually (BAA + zero data retention, US region, the center's own account). If Fernando or Luis want identifiers kept away from the AI provider, the tokenization step can run inside the cloud account instead of on a Mac mini. That gives most of B's privacy benefit without B's on-site hardware duties. Use B's on-site Mac mini only if the RIS forces a local HL7 endpoint.

**Option C is not recommended for opening.** It costs about $150k more over 3 years, carries a quality risk on the center's most important workflow, and makes the center more dependent on Rick, not less. It can be offered later as a measured pilot: run the local model side by side on synthetic packets and switch only if it matches Claude's results.

### Slide-ready comparison

| | **A. Cloud (recommended)** | **B. Hybrid** | **C. All on-site** |
|---|---|---|---|
| Where it runs | Your secure cloud account | Box in your building + your cloud | Boxes in your building |
| Patient data and AI | Sent under a HIPAA agreement, never kept or trained on | Names and IDs stay here, clinical details sent under the agreement | AI never sees it; payers still do |
| If the power goes out | Keeps working | Pauses, catches up | Stops |
| AI quality | Best available | Best available | Lower, must be proven |
| Your staff's extra duties | None | Lock the room, keep a log | Lock the room, keep a log, outage plan |
| Monthly (expected) | ~$6k incl. support | ~$7k incl. support | ~$9.4k incl. support |
| 3-year total (expected) | **~$226k** | ~$274k | ~$378k |

**Spoken line:** "Your patients' details do go to the AI company, the same way they go to your clearinghouse: under a signed HIPAA agreement, and never kept or trained on. If you'd rather names never leave, we can strip them first. Keeping the AI entirely in the building costs about $150k more over three years and gives you a weaker assistant, so I'd only try it as a test."

---

## Open items before Thursday

- Re-check the five headline price pages listed in the sourcing note.
- Ask which RIS and billing clearinghouse they are leaning toward: those two contracts can zero out items 3, 4, and 5.
- Get the RIS vendor's interface fee in writing during vendor selection.
