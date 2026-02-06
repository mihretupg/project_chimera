from skills import (
    skill_advertiser,
    skill_fetch_trends,
    skill_generate_caption,
    skill_judge,
    skill_publish_content,
    skill_worker,
)

SKILL_INPUTS = {
    skill_advertiser: {
        "request_id",
        "trace_id",
        "timestamp",
        "agent_id",
        "capabilities",
        "availability",
        "reputation_score",
    },
    skill_fetch_trends: {"request_id", "trace_id", "timestamp", "platforms", "max_results", "since_ts", "locale"},
    skill_generate_caption: {
        "request_id",
        "trace_id",
        "timestamp",
        "persona_id",
        "context_text",
        "platform",
    },
    skill_judge: {
        "request_id",
        "trace_id",
        "timestamp",
        "task_id",
        "worker_output",
        "confidence_score",
    },
    skill_publish_content: {
        "request_id",
        "trace_id",
        "timestamp",
        "platform",
        "text_content",
        "media_urls",
        "disclosure_level",
    },
    skill_worker: {
        "request_id",
        "trace_id",
        "timestamp",
        "task_id",
        "instructions",
        "parameters",
    },
}

SKILL_OUTPUTS = {
    skill_advertiser: {"status", "request_id", "trace_id", "timestamp", "error_message", "error"},
    skill_fetch_trends: {"status", "request_id", "trace_id", "timestamp", "trends", "error"},
    skill_generate_caption: {
        "status",
        "request_id",
        "trace_id",
        "timestamp",
        "caption",
        "hashtags",
        "confidence_score",
        "error",
    },
    skill_judge: {
        "status",
        "request_id",
        "trace_id",
        "timestamp",
        "decision",
        "reason",
        "escalation_required",
        "error",
    },
    skill_publish_content: {
        "status",
        "request_id",
        "trace_id",
        "timestamp",
        "post_id",
        "platform_post_url",
        "error",
    },
    skill_worker: {
        "status",
        "request_id",
        "trace_id",
        "timestamp",
        "task_id",
        "result",
        "confidence_score",
        "error",
    },
}


def test_skill_input_schemas():
    for module, expected_keys in SKILL_INPUTS.items():
        assert hasattr(module, "INPUT_SCHEMA"), f"{module.__name__} missing INPUT_SCHEMA"
        assert set(module.INPUT_SCHEMA.keys()) == expected_keys


def test_skill_output_schemas():
    for module, expected_keys in SKILL_OUTPUTS.items():
        assert hasattr(module, "OUTPUT_SCHEMA"), f"{module.__name__} missing OUTPUT_SCHEMA"
        assert set(module.OUTPUT_SCHEMA.keys()) == expected_keys
