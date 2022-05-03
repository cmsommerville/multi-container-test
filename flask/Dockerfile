# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# copy project
COPY . /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
