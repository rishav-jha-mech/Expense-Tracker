@echo off
call env\Scripts\activate.bat
start "" "http:localhost:8000"
python manage.py runserver