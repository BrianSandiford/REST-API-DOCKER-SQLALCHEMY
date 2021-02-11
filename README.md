# my app
Rest Api created in flask running in docker container
PostgresSQL in another container
Docker compose used to build and run both containers

#Running application

To build Docker containers with docker-compose:
docker-compose build 

To run containers:
docker-compose up

You can send HTTP requests to your Flask server on publicip:5000, you can either use a REST client like Postman or Insomnia. You can also use cURL on the cli.

curl -XPOST -H "Content-type: application/json" -d \
'{"name": "catty mcCatFace", "price": 5000, "breed": "bengal"}' \
'publicip:5000/add'

curl -X PATCH  -H "Content-type: application/json" -d \
 '{"name": "catty mcCatFace", "price": 9000, "breed": "bengal"}' \
0 'publicip:5000/edit/1'


