#Загрузить картинку питоном.
import requests

p = requests.get('https://upload.wikimedia.org/wikipedia/commons/a/a2/Python_royal_35.JPG')
with open("img.jpg", "wb") as f:
    f.write(p.content)
