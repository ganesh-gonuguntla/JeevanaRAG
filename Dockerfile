FROM python:3.11-slim

LABEL maintainer="JeevanaRAG Team"
LABEL description="Graph-powered medication safety assistant for Indian elderly patients"

# Suppress .pyc generation and ensure unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

# Install OS-level build dependencies required by imaging and data libraries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libjpeg62-turbo-dev \
        zlib1g-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages from pinned requirements
COPY requirements.txt .
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt

# Copy application source tree
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x entrypoint.sh

EXPOSE 8000

# Periodic health probe against the /ping endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD sh -c 'curl -fsS "http://localhost:${PORT:-8000}/ping" || exit 1'

ENTRYPOINT ["/app/entrypoint.sh"]
