# pull official base image
FROM python:3.8.15-alpine

RUN apk update && apk add python3-dev gcc libc-dev
# add bash in container alpine - for WZ
RUN apk add --no-cache bash

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./backend /app/backend
ADD ./docker /app/docker

RUN chmod +x /app/docker/backend/server-entrypoint.sh
RUN chmod +x /app/docker/backend/worker-entrypoint.sh
