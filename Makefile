.PHONY: setup test build run spec-check shell

setup:
	@echo "Installing Python dependencies..."
	poetry install

build:
	docker build -t project_chimera:latest .

test: build
	docker run --rm project_chimera:latest

shell: build
	docker run -it --rm project_chimera:latest /bin/bash

spec-check:
	@echo "Checking if code aligns with specs..."
	python3 scripts/spec_check.py
