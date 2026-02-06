"""Skill: Generate Caption - create platform-specific text captions."""

INPUT_SCHEMA = {
    "persona_id": "string",
    "context_text": "string",
    "platform": "twitter | instagram | threads | tiktok",
}

OUTPUT_SCHEMA = {
    "caption": "string",
    "hashtags": ["string"],
    "confidence_score": "float (0-1)",
}
