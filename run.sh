#!/bin/fish
env/bin/activate.sh
xdg-open http:localhost:8000
python manage.py runserver