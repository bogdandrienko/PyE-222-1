cd ..
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
pip3 freeze > requirements.txt
sh
