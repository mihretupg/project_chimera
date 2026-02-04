import pytest

# Placeholder for trend fetcher API structure (per technical.md)
expected_keys = ["trend_id", "title", "category", "timestamp", "relevance_score"]

def fetch_trends_mock():
    """
    Mock function to simulate trend fetching.
    This should eventually call the TrendFetcher agent API.
    """
    return [{"trend_id": 1, "title": "AI revolution"}]  # intentionally incomplete

def test_trend_data_structure():
    trends = fetch_trends_mock()
    for trend in trends:
        # Failing test: missing keys will cause assertion to fail
        assert all(key in trend for key in expected_keys), \
            f"Trend object missing keys: {set(expected_keys) - set(trend.keys())}"
