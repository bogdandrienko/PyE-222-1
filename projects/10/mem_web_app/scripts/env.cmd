cd ..
python -m venv env
call env/scripts/activate
pip install -r requirements.txt
pip install Django Pillow black[d] pylint
pip freeze > requirements.txt
cmd
