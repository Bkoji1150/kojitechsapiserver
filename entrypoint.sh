#!/bin/bash

set -e

APP_HOST=${PORT:-9000}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"kojitechs@gmail.com"}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-"kojitechsadmin"}
DJANGO_SUPERUSER_LAST_NAME=${DJANGO_SUPERUSER_LAST_NAME:-"admin"}

python manage.py collectstatic --noinput
python manage.py wait_for_db 
python manage.py makemigrations --noinput
python manage.py migrate 

python manage.py createsuperuser --email $SUPERUSER_EMAIL --username $DJANGO_SUPERUSER_USERNAME --noinput || true

uwsgi --socket :${APP_HOST} --workers 4 --master --enable-threads --module app.wsgi

