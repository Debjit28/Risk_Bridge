# Concepts

Record durable understanding, not every definition encountered.

## 2026-11-10: The Compliance "Three-Ingredient" Model

- **Learner's explanation:** A compliance platform is basically a system that checks if we are following rules and shows the gaps.
- **Corrected understanding:** It's the intersection of **Rules** (Frameworks like NIST/ISO), **Evidence** (Data like Wazuh logs), and **Gaps** (the difference between the two).
- **Example:** Rule: "Laptops encrypted". Evidence: "Disk encryption: off". Gap: 17 laptops identified as non-compliant.
- **Related concepts:** GRC (Governance, Risk, Compliance), Audit readiness.

## 2026-11-14: Backend Domains and Data Flow
- **Learner's explanation:** The backend needs specific domains like Auth, Assets, Ingestion, Compliance, Intelligence, and Reporting to function.
- **Corrected understanding:** A GRC platform isn't just one big script; it's a series of domains where the core separation is between **Technical Security Alerts** (raw data) and **Compliance Findings** (the regulatory meaning). The "Intelligence" domain acts as the RAG-based bridge between these two.
- **Example:** "Multiple failed logins" (Technical Alert) is processed to determine a "Failure to meet NIST AC-7" (Compliance Finding).
- **Related concepts:** Domain-Driven Design (DDD), Separation of concerns.
