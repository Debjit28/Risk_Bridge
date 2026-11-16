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

## 2026-11-16: Docker Networking and Environment Variables
- **Problem:** Docker build failing because the project structure wasn't detected correctly, and Postgres failing to initialize because environment variables were missing.
- **Mistake:** Assuming the container environment automatically shares credentials/configs without explicit definition, and not structuring the Dockerfile to support local development workflows (like `uv sync` needing the package to be installed).
- **Original mental model:** "Docker just needs `docker-compose.yml` to work; credentials can be handled later."
- **Correct mental model:** Containers are isolated; environment variables must be injected, and the build context must be configured to allow the language package manager (in this case `uv`) to find the project source code.
- **Category:** Infrastructure
- **Prevention:** Always include an `.env.example` file and configure Docker `depends_on` with `service_healthy`.
