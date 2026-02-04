# Project Chimera Makefile

.PHONY: setup test build run

# Install dependencies locally (optional)
setup:
	@echo "Installing Python dependencies..."
	poetry install

# Build Docker image
build:
	docker build -t project_chimera:latest .

# Run tests in Docker container (failing by design)
test: build
	docker run --rm project_chimera:latest

# Run interactive shell in container
shell: build
	docker run -it --rm project_chimera:latest /bin/bash
