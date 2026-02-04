# Worker Agent

## Purpose
Execute tasks assigned by the Planner agent according to specifications, and return structured results for Judge evaluation.

## Input Schema
{
  "task_id": "string",
  "instructions": "string",
  "parameters": "object"
}

## Output Schema
{
  "task_id": "string",
  "result": "object",
  "status": "completed | failed | degraded",
  "confidence_score": "float (0-1)",
  "timestamp": "iso-8601"
}

## Failure Conditions
- Task instructions missing or invalid → status: failed
- Execution error → status: failed, confidence_score: 0
- Partial execution → status: degraded, confidence_score < 0.5
