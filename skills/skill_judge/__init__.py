"""Skill: Judge - validate worker outputs and route to HITL."""

INPUT_SCHEMA = {
    "task_id": "string",
    "worker_output": "object",
    "confidence_score": "float (0-1)",
}

OUTPUT_SCHEMA = {
    "decision": "approve | escalate",
    "reason": "string",
    "timestamp": "iso-8601",
}
