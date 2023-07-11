@echo off

rem Set the path to your virtual environment.
set "VIRTUAL_ENV=C:\xampp\htdocs\04_Python\django-pos"

rem Set the path to your Django project.
set "PROJECT_DIR=C:\xampp\htdocs\04_Python\django-pos"

rem Activate the virtual environment.
call "%VIRTUAL_ENV%\venv\Scripts\activate.bat"

rem Start Django.
cd "%PROJECT_DIR%"
python manage.py runserver