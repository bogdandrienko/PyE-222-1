sudo docker ps      # список

sudo docker-compose build   # собрать
sudo docker-compose up      # поднять собранный
sudo docker-compose down    # опустить

sudo docker-compose up --build   # поднять в фоновом режиме со сборкой
sudo docker-compose up -d --build  # собрать и поднять в фоновом режиме

sudo docker-compose run web sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser"

# docker
sudo apt update -y
sudo apt install -y docker-compose
# docker

# redis
sudo apt update -y
redis-cli -h 127.0.0.1 -p 6379
ping # PONG
exit
# redis

# postgresql
sudo apt update -y
sudo apt-get install -y postgresql-client
psql -U ubuntu -p 5432 -d postgres
# postgresql

