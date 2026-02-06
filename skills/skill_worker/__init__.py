"""Skill: Worker - execute a single task and return structured results."""

INPUT_SCHEMA = {
    "task_id": "string",
    "instructions": "string",
    "parameters": "object",
}

OUTPUT_SCHEMA = {
    "task_id": "string",
    "result": "object",
    "status": "completed | failed | degraded",
    "confidence_score": "float (0-1)",
    "timestamp": "iso-8601",
}
