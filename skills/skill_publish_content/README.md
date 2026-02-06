# Publish Content Skill

## Purpose
Publish text and media to a supported social platform via MCP tooling.

## Input Schema
{
  "platform": "twitter | instagram | threads | tiktok",
  "text_content": "string",
  "media_urls": ["string"],
  "disclosure_level": "automated | assisted | none"
}

## Output Schema
{
  "status": "success | failure",
  "post_id": "string",
  "timestamp": "iso-8601"
}

## Failure Conditions
- Missing text_content
- Media upload failure
- Platform API error
