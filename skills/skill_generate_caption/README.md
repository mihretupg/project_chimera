# Generate Caption Skill

## Purpose
Create platform-specific text captions that follow the agent persona voice and campaign context.

## Input Schema
{
  "persona_id": "string",
  "context_text": "string",
  "platform": "twitter | instagram | threads | tiktok"
}

## Output Schema
{
  "caption": "string",
  "hashtags": ["string"],
  "confidence_score": "float (0-1)"
}

## Failure Conditions
- Missing persona context
- Empty context_text
- Unsupported platform
