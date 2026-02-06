.PHONY: setup test build run spec-check shell

setup:
	@echo "Installing Python dependencies..."
	python -m pip install --upgrade pip
	python -m pip install -e ".[dev]"

build:
	docker build -t project_chimera:latest .

test: build
	docker run --rm project_chimera:latest

shell: build
	docker run -it --rm project_chimera:latest /bin/bash

spec-check:
	@echo "Checking if code aligns with specs..."
	python3 scripts/spec_check.py
