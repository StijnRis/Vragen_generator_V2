Set-ExecutionPolicy Unrestricted -Scope Process
.\/.venv/Scripts/Activate.ps1
python manage.py runserver

python questionbank/manage.py makemigrations
python questionbank/manage.py migrate
