###################################################################################################################################################
# virtualbox

sudo -i
sudo adduser ubuntu
su ubuntu

# TODO нужно создавать каждый раз на хостинге пользователя ubuntu

####################################################
# copy project to home/ubuntu/web
cd ~
cd ..
sudo mv home/ubuntu/web root/web

###############################################################

sudo apt-get update -y
sudo apt-get install -y nginx gunicorn wget 
sudo apt-get install -y build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install -y python3.11 python3.11-venv python3.11-dev

sudo usermod -aG ubuntu www-data
sudo ufw allow 'Nginx Full'
# sudo chown -R www-data:www-data /home/ubuntu/web/static/

cd web
python3.11 -m venv env
source env/bin/activate
python -V
pip install gunicorn
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
# http://192.168.0.120:8000/
gunicorn --bind 0.0.0.0:8000 django_settings.wsgi
# http://192.168.0.120:8000/

########################################################################################################################
GUNICORN
########################################################################################################################
# sudo rm /etc/systemd/system/gunicorn.socket
sudo nano /etc/systemd/system/gunicorn.socket
<file>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</file>

# sudo rm /etc/systemd/system/gunicorn.service
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
ExecStart=/home/ubuntu/web/env/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock django_settings.wsgi:application
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

########################################################################################################################
NGINX
########################################################################################################################

# sudo rm /etc/nginx/sites-available/web-http.conf
# sudo rm /etc/nginx/sites-enabled/web-http.conf
sudo nano /etc/nginx/sites-available/web-http.conf
<file>
server {
listen 80;
listen [::]:80;

server_name 192.168.0.120;

root /home/ubuntu/web;

location /static/ {
    alias /home/ubuntu/web/static/;

    expires max;
}

location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    # include proxy_params;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
</file>

sudo ln -s /etc/nginx/sites-available/web-http.conf /etc/nginx/sites-enabled/web-http.conf
sudo service nginx start
sudo systemctl reload nginx.service
sudo systemctl restart nginx
sudo systemctl status nginx.service
# http://192.168.0.120:80/







