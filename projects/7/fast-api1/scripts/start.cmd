cd ..
python -m venv env
call env/scripts/activate
pip install -r requirements.txt
pip install fastapi "uvicorn[standard]" Jinja2
pip freeze > requirements.txt
uvicorn main:app --reload --host=0.0.0.0 --port=8000
cmd
