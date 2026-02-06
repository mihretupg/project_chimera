# Chimera Agent Skills

This directory defines the core runtime capabilities ("Skills") for Chimera Agents.
Each skill is a self-contained module with clearly defined input/output contracts.

## Available Skills
- `skill_advertiser`: Publish agent capability metadata to the network.
- `skill_fetch_trends`: Fetch and normalize trending topics.
- `skill_generate_caption`: Generate platform-specific captions.
- `skill_judge`: Evaluate worker outputs and route to HITL.
- `skill_publish_content`: Publish text/media to social platforms.
- `skill_worker`: Execute tasks and return structured results.
