from skills.skill_fetch_trends import fetch_trends_mock, OUTPUT_SCHEMA

expected_keys = set(OUTPUT_SCHEMA.keys())

def test_trend_data_structure():
    trends = fetch_trends_mock()
    for trend in trends:
        assert set(trend.keys()) == expected_keys, (
            f"Trend object missing keys: {expected_keys - set(trend.keys())}"
        )
