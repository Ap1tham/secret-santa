#!/bin/bash
set -e

# Create venv if not exists
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python -m venv .venv
fi

# Activate venv (Windows Git Bash path)
echo "Activating virtual environment..."
source .venv/Scripts/activate

# Install dependencies
echo "Installing dependencies..."
pip install --quiet -r requirements.txt

# Run the Secret Santa script
echo "Running Secret Santa..."
python src/main.py
