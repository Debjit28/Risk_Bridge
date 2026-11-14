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

## 2026-11-13: AI Training vs. RAG Misconception

- **Problem:** Thinking that "adding AI" meant training a custom machine learning model from scratch.
- **Mistake:** Confusing **Model Training** (creating the brain) with **RAG/Inference** (giving the brain a textbook).
- **Original mental model:** "I have to train an AI model to understand security."
- **Correct mental model:** Use a pre-trained LLM (via OpenRouter/Ollama) and provide it with specific context (NIST/ISO text) at query time. This is faster, cheaper, and more accurate for compliance mapping.
- **Category:** AI Architecture
- **Prevention:** Distinguish between learning a language (Training) and looking up facts (RAG).

## 2026-11-13: The "Static Audit" Assumption

- **Problem:** Initially viewing GRC as just a dashboard or a "one-time" report.
- **Mistake:** Underestimating the value of **Continuous Monitoring**.
- **Original mental model:** "It's just a GRC platform, that's it."
- **Correct mental model:** Modern GRC is a "living" system that acts as an "Open Source Vanta Alternative," providing continuous evidence collection rather than static annual audits.
- **Category:** Product Strategy
