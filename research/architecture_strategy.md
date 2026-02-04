# Chimera Architecture Strategy

## Agent Pattern: Hierarchical Swarm (Planner–Worker–Judge)

- **Why Hierarchical Swarm?**
  - Influencer workflows are **parallel by nature**.
  - Safety and correctness require a **Judge** node.
  - Sequential chains **do not scale socially**.
- Direct mapping to Chimera SRS:
  - Planners assign tasks
  - Workers execute
  - Judges verify and escalate

## HITL (Human-in-the-Loop) Placement

- **Placement:** After Judge, **not after Worker**
- Confidence-based escalation:
  - Low-confidence outputs trigger human review
- Humans act as **governors**, not editors

## Database Choice

- **PostgreSQL** for video metadata:
  - Relational, auditable, consistent
- Vector DB for embeddings is **future-proof**, out of scope
- Avoid NoSQL unless justified

## Golden Environment

- pyproject.toml present
- Modern tooling:
  - `uvicorn`, `ruff`, `pytest`
- MCP Sense visibly connected
