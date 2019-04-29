#!/bin/bash


pip install -r requirements.txt
#pip install pur
#pip install --upgrade -r requirements.txt

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

echo "Ждем 30 секунд запуска БД"
# ждем пока БД загрузится
sleep 30
python manage.py migrate

echo "Starting server"
python manage.py runserver 0.0.0.0:8000