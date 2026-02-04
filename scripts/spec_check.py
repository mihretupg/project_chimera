#!/usr/bin/env python3
"""
spec_check.py
Verifies if the essential project files defined in specs/ exist in the codebase.
"""

import os
import sys

# List of required specs
REQUIRED_SPECS = [
    "specs/_meta.md",
    "specs/functional.md",
    "specs/technical.md",
]

# Optional
OPTIONAL_SPECS = [
    "specs/openclaw_integration.md",
]

def main():
    missing_required = [f for f in REQUIRED_SPECS if not os.path.exists(f)]
    missing_optional = [f for f in OPTIONAL_SPECS if not os.path.exists(f)]

    if missing_required:
        print("❌ Missing required specs:")
        for f in missing_required:
            print(f" - {f}")
    else:
        print("✅ All required specs are present.")

    if missing_optional:
        print("⚠️ Missing optional specs:")
        for f in missing_optional:
            print(f" - {f}")
    else:
        print("✅ All optional specs are present.")

    if missing_required:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
