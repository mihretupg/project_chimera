"""Skill: Fetch Trends - normalize trending topics."""

from datetime import datetime, timezone

INPUT_SCHEMA = {}

OUTPUT_SCHEMA = {
    "trend_id": "string",
    "platform": "twitter | tiktok | instagram",
    "topic": "string",
    "velocity_score": "float (0-1)",
    "timestamp": "iso-8601",
}


def fetch_trends_mock():
    """Return a single mock trend entry conforming to the output schema."""
    return [
        {
            "trend_id": "trend-001",
            "platform": "twitter",
            "topic": "AI revolution",
            "velocity_score": 0.92,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    ]
