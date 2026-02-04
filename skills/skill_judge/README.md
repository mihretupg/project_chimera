# Judge

## Purpose
Evaluate worker agent outputs and escalate low-confidence results to HITL humans for governance and safety.

## Input Schema
{
  "task_id": "string",
  "worker_output": "object",
  "confidence_score": "float (0-1)"
}

## Output Schema
{
  "decision": "approve | escalate",
  "reason": "string",
  "timestamp": "iso-8601"
}

## Failure Conditions
- Missing worker output → decision: escalate
- Confidence score < 0 or > 1 → decision: escalate
- Unable to contact HITL → log escalation and mark task as pending
