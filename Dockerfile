FROM python:3.9.6-alpine

##dont generate pyc files
ENV PYTHONDONTWRITEBYTECODE 1
##message log dont stand in buffer
ENV PYTHONUNBUFFERED 1


RUN apk add --no-cache g++ snappy-dev && \
    pip install --no-cache-dir --ignore-installed python-snappy

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /container
WORKDIR /container
COPY . /container
