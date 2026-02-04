# Project Chimera - Technical Specifications

## API Contracts

### Agent Task API
**Request:**
```json
{
  "task_id": "uuid-v4",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "required_resources": ["mcp://twitter/mentions/123"]
  },
  "assigned_worker_id": "string"
}
