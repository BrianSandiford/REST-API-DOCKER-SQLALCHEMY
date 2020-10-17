FROM python:3.6-alpine 

EXPOSE 8080
WORKDIR /app


ENV POSTGRES_USER="" POSTGRES_PASSWORD="" POSTGRES_HOST=postgres POSTGRES_PORT=5432 POSTGRES_DB=""

COPY requirements.txt .
COPY database.env .

RUN export $(xargs < database.env)

# Installing client libraries and any other package you need
RUN apk update && apk add libpq

# Installing build dependencies
# For python3 you need to add python3-dev *please upvote the comment
# of @its30 below if you use this*
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

# Installing and build python module
RUN pip install psycopg2

RUN pip install -r requirements.txt
# Delete build dependencies
RUN apk del .build-deps
COPY entrypoint.sh .
COPY src/ .

RUN export FLASK_APP=src/example/app.py
#COPY entrypoint.sh .
RUN chmod u+x entrypoint.sh

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0 -p 5000
#CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m start.py runserver -d --host 0.0.0.0
##CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait app.py
CMD ["/bin/sh", "entrypoint.sh"]
#ENTRYPOINT ["entrypoint.sh"]
#CMD [ "python","start.py"]

