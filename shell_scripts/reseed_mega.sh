#!/bin/bash
rm -rf mega_api/migrations
rm database/mega.sqlite3
python3 manage.py makemigrations mega_api
python3 manage.py migrate
python3 manage.py loaddata balls
python3 manage.py loaddata mega_balls
