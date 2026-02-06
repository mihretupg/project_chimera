"""Skill: Advertiser - publishes agent capability metadata."""

INPUT_SCHEMA = {
    "agent_id": "string",
    "capabilities": ["string"],
    "availability": "idle | busy | degraded",
    "reputation_score": "float (0-1)",
}

OUTPUT_SCHEMA = {
    "status": "success | failure",
    "timestamp": "iso-8601",
    "error_message": "string | null",
}
