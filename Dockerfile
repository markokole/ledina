FROM python:3.8-alpine
LABEL maintainer marko

USER root

RUN apk update && apk add --no-cache build-base libffi-dev openssl-dev python3-dev krb5-dev linux-headers zeromq-dev postgresql-dev musl-dev wget unzip

RUN pip3 install psycopg2-binary Django ipython django-extensions psycopg2 jupyter

RUN mkdir /project
ADD project /project
WORKDIR "/project"
EXPOSE 8000
