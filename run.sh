#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "=========================================================="
echo "    PROJECT AURORA: CROP PATHOLOGY ENGINE (UZBEKISTAN)    "
echo "=========================================================="

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

# Initialize .env from .env.example if missing
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    echo "Creating .env from .env.example template..."
    cp .env.example .env
fi

# Generate sample assets if not present
if [ ! -f "aurora/samples/cotton_bacterial_blight.jpg" ]; then
    echo "Generating sample field assets..."
    python3 aurora/samples_generator.py
fi

PORT="${PORT:-8000}"
HOST="${HOST:-0.0.0.0}"

echo "Starting Project Aurora on http://${HOST}:${PORT}..."
exec python3 main.py --host "$HOST" --port "$PORT" --reload
