MARVEL'S APPLICATION AVIDITY

PREREQUISITES

- YOU NEED TO HAVE THE DOCKER INSTALLED
- YOU NEED TO HAVE DOCKER COMPOSE INSTALLED

START APPLICATION

RUN THE COMMAND docker-compose build
RUN THE COMMAND docker-compose up -d

TO ADD AN CHARACTER

1I this case the command populatecomics use the parameter to find the character in the Marvel's endpoint

docker exec -it avidity_repository_web_1 python manage.py populatecomics Thor


acess the follow link http://127.0.0.1:8000/

docker exec -it mongodb bash
mongo --host 127.0.0.1 --port 27017 --username admin --password admin

