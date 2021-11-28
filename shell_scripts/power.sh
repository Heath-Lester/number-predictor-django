#!/bin/bash
rm -rf power_api/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations power_api
python3 manage.py migrate power_api
# python3 manage.py loaddata users
