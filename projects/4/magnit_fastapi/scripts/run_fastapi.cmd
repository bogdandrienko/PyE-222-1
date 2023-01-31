cd ..
call env/Scripts/activate.bat
uvicorn main:app --reload --host=0.0.0.0 --port=8000
cmd