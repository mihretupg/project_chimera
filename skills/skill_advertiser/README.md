# Skill Advertiser

## Purpose
Publish agent capabilities, availability, and reputation to the agent network so other agents can discover and engage without human intervention.

## Input Schema
{
  "agent_id": "string",
  "capabilities": ["string"],
  "availability": "idle | busy | degraded",
  "reputation_score": "float (0-1)"
}

## Output Schema
{
  "status": "success | failure",
  "timestamp": "iso-8601",
  "error_message": "string | null"
}

## Failure Conditions
- Network unavailable → status: failure
- Invalid schema input → status: failure, error_message provided
- Agent ID not registered → status: failure
