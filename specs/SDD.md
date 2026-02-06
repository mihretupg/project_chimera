# Software Design Document (SDD) - Project Chimera

## 1. Overview
This document defines the software design for Project Chimera, an autonomous influencer network. It translates the SRS into concrete architecture, components, data flows, interfaces, and implementation decisions. It supersedes informal design notes and is the reference for engineering execution.

## 2. Goals and Non-Goals
### 2.1 Goals
- Implement the Planner-Worker-Judge (FastRender) swarm pattern.
- Use Model Context Protocol (MCP) for all external integrations.
- Provide multi-tiered memory (Redis + Weaviate) with persona management.
- Enable Human-in-the-Loop (HITL) governance based on confidence and sensitivity.
- Support agentic commerce via Coinbase AgentKit with budget guardrails.
- Scale to at least 1,000 concurrent agents with sub-10s high-priority latency.

### 2.2 Non-Goals
- Building a full social media UI for external audiences.
- Manual content creation workflows.
- Custom, platform-specific API logic inside core agents (all integrations via MCP).

## 3. System Context
### 3.1 Actors
- Network Operators: define goals and monitor fleet.
- Human Reviewers: approve/reject flagged content.
- Developers/Architects: extend MCP servers and agent behaviors.

### 3.2 External Systems
- Social platforms (Twitter/X, Instagram, TikTok, Threads) via MCP servers.
- Weaviate for semantic memory.
- Redis for episodic memory and queues.
- PostgreSQL for operational state and logs.
- Coinbase AgentKit for wallets and transactions.
- LLM providers for reasoning, judging, and vision validation.

## 4. Architecture
### 4.1 Logical View
- Orchestrator (Hub): global state, configuration, dashboard, multi-tenant management.
- Agent Swarm (Spokes): Planner, Worker, Judge services.
- MCP Host: client layer for tools/resources/prompts.
- MCP Servers: external integrations (social, memory, commerce, media generation).

### 4.2 Component Diagram (Text)
- Orchestrator
  - Campaign Service
  - Agent Registry
  - Global State Store
  - Dashboard API
- Swarm Services
  - Planner Service
  - Worker Pool
  - Judge Service
- Data Services
  - Redis (TaskQueue, ReviewQueue, Episodic Memory)
  - Weaviate (Semantic Memory)
  - PostgreSQL (Campaigns, Tenants, Logs)
- MCP Layer
  - MCP Client Runtime
  - MCP Servers: Social, Memory, Media, Commerce

### 4.3 Deployment View
- Kubernetes for all services with autoscaling.
- Each role deployed as separate service with independent scaling.
- MCP servers deployed as sidecars or standalone services depending on latency and isolation requirements.

## 5. Key Design Decisions
1. **MCP-only External Integration:** No direct API calls from agent logic.
2. **Planner-Worker-Judge Separation:** Each is stateless with explicit queues.
3. **OCC in Judge:** Validate state_version on commits.
4. **SOUL.md Persona:** Version-controlled, parsed at runtime.
5. **Confidence-Based HITL:** Route outcomes based on confidence and sensitivity.
6. **Budget Guardrails:** Daily spend caps enforced via Redis and CFO Judge.

## 6. Data Design
### 6.1 Core Schemas
#### Agent Task
```json
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "required_resources": ["mcp://twitter/mentions/123", "mcp://memory/recent"]
  },
  "assigned_worker_id": "string",
  "created_at": "timestamp",
  "status": "pending | in_progress | review | complete"
}
```

#### Task Result
```json
{
  "task_id": "uuid-v4-string",
  "status": "success | failed",
  "output": "string | url | json",
  "confidence_score": 0.0,
  "reasoning_trace": "string",
  "created_at": "timestamp"
}
```

### 6.2 Persona Model
- Stored in `SOUL.md` with YAML frontmatter.
- Parsed into `AgentPersona` (Pydantic).
- Backstory in markdown body.

### 6.3 Memory
- Episodic memory: Redis, TTL = 1 hour.
- Semantic memory: Weaviate, store summaries and long-term interactions.

## 7. Service Design
### 7.1 Planner Service
Responsibilities:
- Read campaign goals and global state.
- Decompose goals into tasks.
- Push tasks into `task_queue` (Redis).

Key APIs:
- `POST /planner/plan` -> generates tasks for a campaign.

### 7.2 Worker Service
Responsibilities:
- Pull tasks from `task_queue`.
- Execute via MCP tools.
- Push results to `review_queue`.

Key APIs:
- `POST /worker/execute` -> run a single task.

### 7.3 Judge Service
Responsibilities:
- Pull results from `review_queue`.
- Validate output vs acceptance criteria.
- Apply HITL routing.
- Commit to global state if approved.

Key APIs:
- `POST /judge/review` -> review result.

## 8. MCP Integration
### 8.1 MCP Client
- Connects to MCP servers via stdio/SSE.
- Provides `call_tool` and `read_resource` methods.

### 8.2 MCP Servers
Required servers:
- `mcp-server-twitter`
- `mcp-server-weaviate`
- `mcp-server-coinbase`
- `mcp-server-ideogram` or `mcp-server-midjourney`
- `mcp-server-runway` or `mcp-server-luma`

## 9. HITL Governance
Rules:
- Confidence > 0.90: auto-approve.
- 0.70 - 0.90: async approval queue.
- < 0.70: reject/retry.
- Sensitive topic detection overrides confidence and forces HITL.

## 10. Commerce Design
- Each agent gets a non-custodial wallet via Coinbase AgentKit.
- Transactions require CFO Judge approval.
- Daily spend enforced in Redis (`daily_spend` key).

## 11. Security and Compliance
- Secrets stored in Vault or AWS Secrets Manager.
- Wallet keys injected at runtime only.
- Audit logs for all actions and transactions.
- AI content disclosure flags enabled on all platforms.

## 12. Observability
- Centralized logging (structured JSON logs).
- Metrics: task latency, error rates, queue depth.
- Tracing: task_id propagated across services.

## 13. Implementation Phases
### Phase 1: Core Swarm
- Planner, Worker, Judge services.
- Redis queues and schemas.

### Phase 2: MCP Integration
- MCP client runtime.
- Memory and social MCP servers.

### Phase 3: Agentic Commerce
- Coinbase AgentKit integration.
- Budget guardrails and CFO Judge.

### Phase 4: HITL UI
- React Review Queue dashboard.

## 14. Open Questions
- Final LLM provider selection for reasoning/judging.
- Deployment target (AWS vs GCP) decision.
- Specific SLAs for high-priority tasks per tenant.

