#!/bin/bash
set -e

cd /code/MapsApi/

python manage.py collectstatic --no-input

if [ ! -f "/data/db.sqlite3" ]; then
    python manage.py migrate
    python manage.py createsuperuser --no-input --first_name=Admin --last_name=User --email=chicommons@chicommons.com --password=password
    python manage.py loaddata 'apps/directory/fixtures/seed_data.yaml'
fi

python manage.py runserver 0.0.0.0:8000