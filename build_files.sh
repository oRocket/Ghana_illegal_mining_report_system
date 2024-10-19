#!/bin/bash

echo "Installing dependencies..."
pip install --upgrade pip  # Ensure the latest version of pip
pip install -r requirements.txt || exit 1

echo "Running migrations..."
python3.9 manage.py migrate || exit 1

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput || exit 1

echo "Build completed."
