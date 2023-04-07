Set-ExecutionPolicy Unrestricted -Scope Process
.\/.venv/Scripts/Activate.ps1
python questionbank/manage.py runserver

python questionbank/manage.py makemigrations
python questionbank/manage.py migrate
