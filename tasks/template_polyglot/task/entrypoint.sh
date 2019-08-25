#!/usr/bin/env sh
exec gunicorn \
    --bind "${HOST:-0.0.0.0}:${PORT:-8000}" \
    --user 1001 --group 1001 \
    app:app
