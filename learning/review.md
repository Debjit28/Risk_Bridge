# Review

Keep short retrieval prompts or review metadata for meaningful topics.

## 2026-11-14: Backend Map & Architectural Domain Definition

- **What we worked on:** Designed the backend architecture map (Phase 1) and defined core domains.
- **Major conclusions:** The backend will be organized into 6 core domains: Auth/Org, Assets, Ingestion, Compliance, Intelligence, and Reporting. 
- **Decisions made:**
    - Confirmed the distinction between Technical Alerts and Compliance Findings.
    - Confirmed MVP scope excludes "Threat Intelligence" for now to focus on core Compliance mapping.
    - Architecture uses a Pipeline flow: Ingestion -> Normalization -> RAG Intelligence -> Persistent Storage -> Dashboard.
- **Reasoning behind decisions:** Separating technical evidence from compliance findings is required for auditability and explainability.
- **Unresolved issues:** Threat Intelligence inclusion, database schema finalization, and remediation UI workflows.
- **Stopping point:** Backend domains defined, architecture conceptualized, readiness for Phase 2 (API Map) and Phase 3 (Data Model).
- **Recommended starting point for next session:** Design the API Map (endpoints) for the "Ingestion" and "Compliance" domains.

## 2026-11-13: Defining the "Open Source Vanta Alternative"

- **What we worked on:** Refined the project goal from a general GRC platform to a "Modern/Continuous GRC" tool (like an open-source Vanta).
- **Major conclusions:** 
    - The platform should handle **Regulatory Sovereignty** by allowing regional/industry profiles.
    - Focus on **Actionable Intelligence** (Remediation steps for non-technical users).
    - Use **Continuous Polling** for cloud/SIEM state instead of static manual entry.
- **Decisions made:**
    - Use **REST APIs** (FastAPI) for ingestion.
    - Implement **Read-Only Cloud Connectors** (AWS/Azure) for evidence collection.
    - Use **Docker Compose** for portability and environment consistency.
- **Alternatives considered:** Manual data entry GRC vs. Automated Continuous GRC.
- **Reasoning behind decisions:** Automation provides "Evidence-based" compliance which is harder to fake and more valuable to businesses than manual spreadsheets.
- **Important tradeoffs discovered:** Automating remediation (fixing things) is too risky for production; focus should be on **Automated Detection** and **Manual Human-in-the-loop Sign-off**.
- **Unresolved issues:** Database schema for many-to-many evidence reuse, implementation of the "Polling" loops, UI design for non-technical remediation.
- **Stopping point:** Core product vision and feature set finalized.
- **Recommended starting point for next session:** Design the **Database Schema** (ER Diagram logic) for Frameworks, Controls, Evidence, and Assets.
