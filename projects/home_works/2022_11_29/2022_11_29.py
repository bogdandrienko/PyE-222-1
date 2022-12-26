import requests

# TODO windows:
# pip install env
# python -m venv env
# call env/Scripts/activate.bat
# pip install requests
# pip freeze > requirements.txt

# TODO linux:
# sudo apt-get update -y
# sudo apt-get install python3-dev python3-pip python3-venv
# python3 -m venv env
# source env/bin/activate
# pip install requests
# pip freeze > requirements.txt

url = "https://picsum.photos/320/240/"
response = requests.get(url=url)

with open("new.jpg", mode="wb") as f:
    f.write(response.content)
