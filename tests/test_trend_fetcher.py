from skills.skill_fetch_trends import fetch_trends_mock

REQUIRED_TREND_KEYS = {
    "trend_id",
    "platform",
    "topic",
    "velocity_score",
    "timestamp",
    "source_url",
    "raw_payload",
}

def test_trend_data_structure():
    trends = fetch_trends_mock()
    for trend in trends:
        assert set(trend.keys()) == REQUIRED_TREND_KEYS, (
            f"Trend object missing keys: {REQUIRED_TREND_KEYS - set(trend.keys())}"
        )
