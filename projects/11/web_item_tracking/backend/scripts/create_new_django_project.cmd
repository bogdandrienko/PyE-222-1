cd ..
python -m venv env
call env/scripts/activate


pip install -r requirements.txt
pip install Django
pip freeze > requirements.txt
django-admin startproject django_settings .
django-admin startapp django_app
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000


cmd
