sudo docker-compose ps  # список
sudo docker-compose build  # собрать
sudo docker-compose up  # поднять собранный
sudo docker-compose up -d  # поднять в фоновом режиме
sudo docker-compose down  # опустить
sudo docker-compose up -d --build  # собрать и поднять в фоновом режиме

docker-compose run app sh -c "django-admin startproject django_settings ."
redis-cli -h 127.0.0.1 -p 6380
