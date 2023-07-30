# зарегистироваться на хостинге
# купить linux-сервер (ubuntu 22.04 LTS)
#

sudo apt-get update -y && sudo apt update -y
sudo apt-get install -y python3-dev python3-pip python3-venv

cd ~
mkdir web && cd web
python3 -m venv env
source env/bin/activate
pip3 install Django
django-admin startproject settings .
django-admin startapp app
python manage.py runserver 0.0.0.0:8000

###################################################

sudo apt-get install -y build-essential libpq-dev unixodbc-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev
sudo apt-get install -y git nginx curl wget htop gunicorn postgresql postgresql-contrib redis
sudo snap install --classic certbot

sudo usermod -aG ubuntu www-data

###########################
# POSTGRESQL

sudo passwd postgres
sudo -i -u postgres
psql postgres
CREATE USER django_usr WITH PASSWORD 'Qwerty!1234$';
CREATE DATABASE django_db OWNER django_usr;
ALTER ROLE django_usr SET client_encoding TO 'utf8';
ALTER ROLE django_usr SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django_db TO django_usr;
\q

psql django_db
\d
\l

\q
exit

sudo systemctl stop postgresql
sudo systemctl status postgresql
sudo systemctl restart postgresql
sudo systemctl status postgresql

psql django_db
\c postgres
\c django_db

CREATE TABLE zarplata (id serial PRIMARY KEY, username VARCHAR ( 50 ) UNIQUE NOT NULL, salary INT);

\d
select * from zarplata;
insert into zarplata (username, salary) VALUES ('Bogdan', '60000'), ('Alice', '80000');
select * from zarplata;
\q
exit

###########################
# REDIS

redis-cli
ping
exit


###########################
# ...


sudo rm -r web1


python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python manage.py runserver 0.0.0.0:8000

gunicorn --bind 0.0.0.0:8000 django_setttings.wsgi

###########################
# GUNICORN

pwd

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

User=ubuntu
Group=www-data

RuntimeDirectory=gunicorn
WorkingDirectory=/home/ubuntu/web
ExecStart=/home/ubuntu/web/env/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock django_setttings.wsgi:application
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

#################################
NGINX
#####

sudo nano /etc/nginx/sites-available/bogdandrienko-http.conf
<file>
server {
listen 80;
listen [::]:80;

server_name bogdandrienko.site www.bogdandrienko.site 195.49.210.79;

root /home/ubuntu/web;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /home/ubuntu/web/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /home/ubuntu/web/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /home/ubuntu/web/static/;

    expires max;
}

location /media/ {
    alias /home/ubuntu/web/static/media/;

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

sudo ln -s /etc/nginx/sites-available/bogdandrienko-http.conf /etc/nginx/sites-enabled/bogdandrienko-http.conf

sudo ufw allow 'Nginx Full'
sudo service nginx start
sudo systemctl status nginx.service
sudo systemctl reload nginx.service

python manage.py collectstatic --noinput
pip install redis psycopg2-binary
pip freeze > requirements.txt

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',
        'USER': 'django_usr',
        'PASSWORD': 'Qwerty!1234$',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

python manage.py makemigrations
python manage.py migrate
python manage.py check --database default
python manage.py createsuperuser --username admin --email bogdandrienko@gmail.com

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "database": {  # экономия ОЗУ == для тяжёлых и не особо нужных
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache_table",
        "TIMEOUT": "120",
        "OPTIONS": {
            "MAX_ENTIES": 200,
        },
    },
    "ram_cache": {  # дорого для ОЗУ == для нужных данных
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "django_ram_cache_table",
    },
}
python manage.py createcachetable