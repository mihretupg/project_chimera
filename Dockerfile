# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (use poetry if available)
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi || echo "Poetry install skipped (dev mode)"

# Copy project files
COPY . /app

# Set default command
CMD ["pytest", "--maxfail=1", "--disable-warnings", "tests/"]
