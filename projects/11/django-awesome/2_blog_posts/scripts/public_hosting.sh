###################################################################################################################################################
# https://oblako.kz/

# зарегистироваться на хостинге и пополнить баланс
# купить linux-сервер (ubuntu 20.04 LTS) + нужная мощность
# Создали репозиторий на гитхабе
# подключились по ssh

# 20:48:30
# 21:00:00

sudo apt-get update -y
sudo apt-get install -y curl git nginx gunicorn wget build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install -y python3.11 python3.11-venv python3.11-dev

# доступ на чтение файлов
sudo usermod -aG root www-data
# доступ к интернету
sudo ufw allow 'Nginx Full'

cd ~
mkdir rest_api && cd rest_api
python3.11 -m venv env
source env/bin/activate
python -V
pip install django gunicorn
django-admin startproject django_settings .
django-admin startapp django_app
nano django_settings/settings.py
python manage.py runserver 0.0.0.0:8000
ip a
# 188.94.156.135:8000
gunicorn --bind 0.0.0.0:8000 django_settings.wsgi

deactivate
cd ~

# копирует репозиторий в эту папку
git clone https://github.com/bogdandrienko/django_server.git


# удаляет папку с файлами
rm -r web

# переименовывание
mv django_server web

# полный путь к текущей директории
pwd

# позволяет посмотреть активные процессы и нагрузку на ОС
htop

cd web
python3.11 -m venv env
source env/bin/activate
python -V
pip install gunicorn
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
# 188.94.156.135:8000
gunicorn --bind 0.0.0.0:8000 django_settings.wsgi

###########################
# GUNICORN
sudo nano /etc/systemd/system/gunicorn.socket
<file>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</file>

sudo nano /etc/systemd/system/gunicorn.service
<file>
[Unit]
Description=Gunicorn for the Django project
Requires=gunicorn.socket
After=network.target

[Service]
Type=notify
User=root
Group=www-data

RuntimeDirectory=gunicorn
WorkingDirectory=/root/web
ExecStart=/root/web/env/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock django_settings.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
</file>

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable --now gunicorn.service
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl status gunicorn.service
#sudo systemctl disable gunicorn
#sudo systemctl stop gunicorn

#################################
NGINX
#####

sudo nano /etc/nginx/sites-available/web-http.conf
<file>
server {
listen 80;
listen [::]:80;

server_name 188.94.156.135;

root /root/web;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /root/web/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /root/web/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /root/web/static/;

    expires max;
}

location /media/ {
    alias /root/web/static/media/;

    expires max;
}

location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
</file>

sudo ln -s /etc/nginx/sites-available/web-http.conf /etc/nginx/sites-enabled/web-http.conf
sudo nginx -t
sudo service nginx start
sudo systemctl reload nginx.service
sudo systemctl status nginx.service
# http://188.94.156.135:80/
