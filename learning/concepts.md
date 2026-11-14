# Concepts

Record durable understanding, not every definition encountered.

## 2026-11-10: The Compliance "Three-Ingredient" Model

- **Learner's explanation:** A compliance platform is basically a system that checks if we are following rules and shows the gaps.
- **Corrected understanding:** It's the intersection of **Rules** (Frameworks like NIST/ISO), **Evidence** (Data like Wazuh logs), and **Gaps** (the difference between the two).
- **Example:** Rule: "Laptops encrypted". Evidence: "Disk encryption: off". Gap: 17 laptops identified as non-compliant.
- **Related concepts:** GRC (Governance, Risk, Compliance), Audit readiness.

## 2026-11-13: Regulatory Sovereignty & Industry Profiles

- **Learner's explanation:** Compliance rules change depending on which country you are in.
- **Corrected understanding:** Regulations are a matrix of **Geography** (Region/Country) and **Sector** (Industry). A global GRC platform must use data-driven rulesets (storing rules in DB, not code) to switch between frameworks like India's DPDP, EU's GDPR, or Finance's RBI rules without rewriting the application.
- **Example:** A healthcare company in the US (HIPAA) vs. a bank in India (RBI).
- **Related concepts:** Multi-tenancy, Dynamic Schema.

## 2026-11-13: Continuous GRC (Polling vs. Scanning)

- **Learner's explanation:** Continuous scanning to check for compliance issues all the time.
- **Corrected understanding:** In GRC, "scanning" often refers to **Continuous Monitoring** or **Polling for State**. Instead of active vulnerability scanning (like a hacker tool), the platform regularly queries systems (AWS APIs, local configs, SIEM logs) to verify that security controls are still active.
- **Example:** Every hour checking if AWS S3 buckets are public vs. running a network exploit scan.
- **Related concepts:** State drift, Evidence-based auditing.

## 2026-11-13: Actionable Intelligence

- **Learner's explanation:** Making the project so even if you don't know cyber you know what to do.
- **Corrected understanding:** Designing a GRC platform for non-technical stakeholders (CEOs, Auditors) by translating technical failures (e.g., "Port 22 open") into business impact and specific remediation instructions (e.g., "Close this port to satisfy NIST PR.AC-3").
- **Related concepts:** User Experience (UX) for Compliance, Remediation workflows.
