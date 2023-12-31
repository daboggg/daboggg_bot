# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/daboggg_bot

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
ADD ./requirements.txt .
RUN pip install -r requirements.txt

 #copy project
COPY . .
