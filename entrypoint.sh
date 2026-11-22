#!/bin/bash
set -e

cd /app

echo "=== JeevanaRAG container initializing ==="

# Execute the bootstrap procedure unless explicitly bypassed
# (useful for serverless or horizontally-scaled worker instances).
if [ "${SKIP_BOOTSTRAP:-0}" != "1" ]; then
  python -m scripts.bootstrap
else
  echo "=== SKIP_BOOTSTRAP=1 â€” bypassing blocking bootstrap ==="
fi

# Launch the FastAPI application via uvicorn
exec uvicorn app.api.server:app \
    --host 0.0.0.0 \
    --port "${PORT:-${APP_PORT:-8000}}" \
    --log-level "${LOG_LEVEL:-info}"
