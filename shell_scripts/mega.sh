#!/bin/bash
rm -rf mega_api/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations mega_api
python3 manage.py migrate mega_api
python3 manage.py loaddata numbers
python3 manage.py loaddata winning_drawings
