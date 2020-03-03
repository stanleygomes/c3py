# Alpine Linux v3.11.2 - https://alpinelinux.org
FROM python:3.7-alpine

# install some OS packages
RUN apk --no-cache add bash bash-completion

# install gcc
RUN apk add build-base

# create app folder
RUN mkdir /app

# copy python dependencies files to container root app folder
COPY requirements.txt /app

# set path to app's folder
WORKDIR /app

# config venv inside repo
RUN python3 -m venv venv && \
  source venv/bin/activate

# install dependencies for python
RUN pip3 install -r requirements.txt

# port to run application
EXPOSE 8000

# start server
CMD ["python3", "src/app.py"]
