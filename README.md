<h1>MARVEL'S APPLICATION AVIDITY<h1>

<h3>PREREQUISITES<h3>

- YOU NEED TO HAVE THE DOCKER INSTALLED
- YOU NEED TO HAVE DOCKER COMPOSE INSTALLED

<h3>START APPLICATION</h3>

RUN THE COMMAND docker-compose build
RUN THE COMMAND docker-compose up -d

<h3>TO ADD AN CHARACTER</h3>

1I this case the command populatecomics use the parameter to find the character in the Marvel's endpoint

example:

    docker exec -it avidity_repository_web_1 python manage.py populatecomics Thor

The command bellow will search for a character and persist in the database.

Adding Hulk's character

docker exec -it avidity_repository_web_1 python manage.py populatecomics Hulk

<b>command format</b>

docker exec -it avidity_repository_web_1 python manage.py populatecomics <character's name>

The command populatecomicas is a command to populate the database with the marvel's character.

Access the follow link: http://127.0.0.1:8080/

docker exec -it mongodb bash

mongo --host 127.0.0.1 --port 27017 --username admin --password admin


