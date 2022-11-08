FROM python:3.7-alpine

RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories \ 
       && apk update
RUN apk add --no-cache --upgrade bash
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

COPY ./email_test /app
WORKDIR /app