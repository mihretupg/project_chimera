# Project Chimera

Project Chimera is an Autonomous Influencer Network prototype. This repository contains the baseline environment, specifications, and scaffolding needed to build and validate the system described in the SRS/SDD.

## What's Included

- `specs/`: SRS, SDD, and supporting specifications
- `skills/`: Skill contracts and Python module stubs
- `tests/`: Baseline tests for skill schemas and trend fetcher
- `scripts/`: Spec validation helpers
- `Dockerfile`, `Makefile`: Build and test automation
- `.github/workflows/`: CI checks for repository structure

## Prerequisites

- Python 3.10+ (local development)
- Docker (for container builds)
- Make (optional, for `make build`)

## Quick Start (Local)

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
```

## Docker Build

```bash
docker build -t project_chimera:latest .
```

## Spec Checks

```bash
python scripts/spec_check.py
```

## MCP Sense (Optional)

If you are connecting to Tenx MCP Sense, ensure `mcp_config.json` exists with the correct headers:

```json
{
  "servers": {
    "tenxfeedbackanalytics": {
      "url": "https://mcppulse.10academy.org/proxy",
      "type": "http",
      "headers": {
        "X-Device": "windows",
        "X-Coding-Tool": "vscode"
      }
    }
  },
  "inputs": []
}
```

Start MCP Sense:
```bash

mcp-sense --config mcp_config.json
```

Confirm the connection in logs.

## Repository Readiness

The repository includes the required structure for submission:
- `specs/`, `tests/`, `skills/`
- `Dockerfile`, `Makefile`
- `.github/workflows/`

See `SPEC_CHECKLIST.md` for a concise validation checklist.

