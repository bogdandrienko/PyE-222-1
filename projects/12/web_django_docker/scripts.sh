# install
# create VM
# change NET + dvd

sudo apt update -y
sudo apt install -y openssh-server
ip a
sudo apt install -y docker-compose
# install



sudo docker ps      # список

sudo docker-compose build   # собрать
sudo docker-compose up      # поднять собранный
sudo docker-compose down    # опустить

sudo docker stop 2579298976d6febd1b7c7cddd8069aedc93f106ef9752a21d65a59482e9d5dbc  # остановка контейнера

sudo docker-compose up --build   # поднять со сборкой
sudo docker-compose up -d --build  # собрать и поднять в фоновом режиме

sudo docker-compose run web sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser"

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

