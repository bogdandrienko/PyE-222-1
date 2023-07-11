cd ..
python -m venv env
call env/scripts/activate

python manage.py makemigrations
python manage.py migrate

cmd
