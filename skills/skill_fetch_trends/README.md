# Trend Fetcher Skill

## Purpose
Fetch trending topics from supported platforms and normalize the data for downstream agents.

## Input Schema
- None (agent-triggered)

## Output Schema
{
  "trend_id": "string",
  "platform": "twitter | tiktok | instagram",
  "topic": "string",
  "velocity_score": "float (0-1)",
  "timestamp": "iso-8601"
}

## Failure Conditions
- Network unreachable
- Malformed response
- API rate-limited
