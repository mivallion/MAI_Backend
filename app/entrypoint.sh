#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting Postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "Postgres launched"
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

exec "$@"
