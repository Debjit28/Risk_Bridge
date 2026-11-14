# Mistakes

Record meaningful bugs or recurring misconceptions. Preserve the original reasoning.

## 2026-11-10: Building before Planning (The "Stack-First" Trap)

- **Problem:** Attempting to finalize a technology stack (FastAPI, Next.js, etc.) before the core problem or data model was defined.
- **Mistake:** Assuming the stack is the starting point for a design.
- **Original mental model:** "I need to know my stack to start building the project."
- **Correct mental model:** Requirements and the domain problem (how to map Wazuh events to controls) dictate the architecture, which then informs the stack.
- **Category:** Design Methodology
- **Prevention:** Always define the "decision the platform makes" and the "primary output" before committing to a framework.
- **Follow-up exercise:** Defend the choice of PostgreSQL/pgvector specifically in the context of the RAG requirements.

## 2026-11-14: Treating Alerts as Compliance Findings
- **Problem:** Equating raw security logs directly with compliance findings.
- **Mistake:** Assuming that an alert from a SIEM automatically translates to a compliance status without intermediate reasoning.
- **Original mental model:** "Wazuh log is the compliance finding."
- **Correct mental model:** Logs are *Evidence*; Compliance Findings are *interpretations* of evidence against specific controls. They must be kept distinct in the architecture to allow for human review and audit trails.
- **Category:** Architecture / Logic
- **Prevention:** Always distinguish between the "Technical Finding" domain and the "Compliance Mapping" domain.
