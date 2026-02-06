from skills import (
    skill_advertiser,
    skill_fetch_trends,
    skill_generate_caption,
    skill_judge,
    skill_publish_content,
    skill_worker,
)

SKILL_INPUTS = {
    skill_advertiser: {"agent_id", "capabilities", "availability", "reputation_score"},
    skill_fetch_trends: set(),
    skill_generate_caption: {"persona_id", "context_text", "platform"},
    skill_judge: {"task_id", "worker_output", "confidence_score"},
    skill_publish_content: {"platform", "text_content", "media_urls", "disclosure_level"},
    skill_worker: {"task_id", "instructions", "parameters"},
}

SKILL_OUTPUTS = {
    skill_advertiser: {"status", "timestamp", "error_message"},
    skill_fetch_trends: {"trend_id", "platform", "topic", "velocity_score", "timestamp"},
    skill_generate_caption: {"caption", "hashtags", "confidence_score"},
    skill_judge: {"decision", "reason", "timestamp"},
    skill_publish_content: {"status", "post_id", "timestamp"},
    skill_worker: {"task_id", "result", "status", "confidence_score", "timestamp"},
}


def test_skill_input_schemas():
    for module, expected_keys in SKILL_INPUTS.items():
        assert hasattr(module, "INPUT_SCHEMA"), f"{module.__name__} missing INPUT_SCHEMA"
        assert set(module.INPUT_SCHEMA.keys()) == expected_keys


def test_skill_output_schemas():
    for module, expected_keys in SKILL_OUTPUTS.items():
        assert hasattr(module, "OUTPUT_SCHEMA"), f"{module.__name__} missing OUTPUT_SCHEMA"
        assert set(module.OUTPUT_SCHEMA.keys()) == expected_keys
