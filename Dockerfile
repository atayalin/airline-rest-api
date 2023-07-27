from python:3.9-alpine

env PYTHONUNBUFFERED 1

workdir /rest_airline_app

run apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers mariadb-dev python3-dev

copy requirements.txt /rest_airline_app/requirements.txt

run pip install -r requirements.txt

copy . /rest_airline_app

expose 8000

cmd [ "/bin/sh", "run.sh" ]
