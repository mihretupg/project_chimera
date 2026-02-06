"""Skill: Publish Content - post text/media to a social platform."""

INPUT_SCHEMA = {
    "platform": "twitter | instagram | threads | tiktok",
    "text_content": "string",
    "media_urls": ["string"],
    "disclosure_level": "automated | assisted | none",
}

OUTPUT_SCHEMA = {
    "status": "success | failure",
    "post_id": "string",
    "timestamp": "iso-8601",
}
