#!/usr/bin/env bash
exec php \
    -S "${HOST:-0.0.0.0}:${PORT:-8000}" \
    -t /opt/app/ \
    /opt/app/index.php
