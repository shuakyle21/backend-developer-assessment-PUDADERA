#!/bin/sh
set -e

# Seed from test_data.json on first boot only (skipped if a volume already
# provides a DB file, so a restart never re-seeds/overwrites real data).
DB_PATH="${DATABASE_PATH:-./data.db}"
if [ ! -f "$DB_PATH" ]; then
    python scripts/seed.py
fi

exec "$@"
