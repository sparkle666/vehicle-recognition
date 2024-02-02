#!/bin/bash
set -e

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start Gunicorn
exec gunicorn --bind :8000 --workers 2 django_project.wsgi
