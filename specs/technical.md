# Project Chimera Technical Specifications

## Example Payload: Trend Data
{
  "trend_id": "string",
  "platform": "twitter | tiktok | instagram",
  "topic": "string",
  "velocity_score": "float (0-1)",
  "timestamp": "iso-8601"
}

## Failure Modes
- Missing or malformed payload → agent raises `ValidationError`
- Unreachable platform → agent marks trend as `degraded`
- Low-confidence scoring → escalate to Judge → HITL escalation
