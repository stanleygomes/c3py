# Alpine Linux v3.11.2 - https://alpinelinux.org
FROM python:3.7-alpine

# install some OS packages
RUN apk --no-cache add bash bash-completion

# create app folder
RUN mkdir /app

# copy python dependencies files to container root app folder
COPY requirements.txt /app

# set path to app's folder
WORKDIR /app

# install dependencies for python
RUN pip3 install -r requirements.txt

# port to run application
EXPOSE 8000

# start server
CMD ["python3", "src/manage.py", "runserver", "0.0.0.0:8000"]
