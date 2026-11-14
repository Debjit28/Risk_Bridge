# Questions

Keep unresolved questions concise. Add a date or context when it helps.

## 2026-11-10: Risk Calculation Methodology

- **Context:** The project requires a "cyber risk" component, but numerical scoring often feels arbitrary.
- **Current hypothesis:** Use a Qualitative Matrix (NIST 800-30 style) or a Rule-based gap system rather than arbitrary quantitative weights.
- **Alternatives still being considered:** Qualitative Matrix (5x5) vs. Rule-based "Elevated Risk" for critical gaps.
- **Evidence or research needed:** Look into NIST SP 800-30 and how it defines Likelihood/Impact.
- **Status:** unresolved

## 2026-11-13: Multi-Framework Evidence Reuse

- **Context:** A single piece of evidence (e.g., "MFA is enabled") often satisfies requirements in multiple frameworks (NIST, ISO, SOC2).
- **Current hypothesis:** Use a Many-to-Many database relationship between `Evidence` and `Controls` so that 1 Evidence -> N Controls.
- **Status:** unresolved

## 2026-11-13: Cloud Ingestion (AWS/Azure)

- **Context:** How to conveniently connect to cloud providers for automated checks.
- **Current hypothesis:** Use Read-Only IAM roles/API keys to "poll" for infrastructure state (e.g., checking S3 bucket permissions).
- **Evidence or research needed:** Research the `boto3` library for AWS state checks.
- **Status:** unresolved
