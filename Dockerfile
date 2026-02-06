# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -e ".[dev]"

# Set default command
CMD ["pytest", "--maxfail=1", "--disable-warnings", "tests/"]
