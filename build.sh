#!/usr/bin/env bash
#Exit on error
set -o errexit

# Modify this line as needed for your packege manager (pip,poetry,etc.)
pip install -r requirements.txt

# collectstatic might fail if settings not configured; keep safe with exit on error
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
