[![CodeFactor](https://www.codefactor.io/repository/github/stanleygomes/c3py/badge)](https://www.codefactor.io/repository/github/stanleygomes/c3py)

# C3PY

Excuse me, sir.

The main goal of **C3PY** is to set patterns to be easily implemented on Python projects. We want to make easy to quick start a Python enviroment with the basic resources every project could have. Check out the patterns we defined this document bellow.

*It was inspired by [Nodevader](https://github.com/stanleygomes/nodevader)*.

<p  align="center" style="padding:15px 0;">
	<img src="https://i.imgur.com/vIPoseD.png" width="400px" />
  <br />
  Icon by <a href="https://dribbble.com/creativeflip" target="_blank">Filipe Carvalho</a>
</p>

## Startup

Step by step to get this up and running

### Clone repo and go to project folder

```
git clone https://github.com/c3py/c3py.git && cd c3py
```

### Install dependencies

```bash

```

### Start server

```bash


```

Via docker-compose (start database, run migrations and start server)

```bash
docker-compose up
```

To test it on the browser, simply go to: `http://localhost:8000`

## Git flow

To file a new a feature

- create a branch from `master` branch. Use the pattern: `feature/description`
- file a pull request on `master` branch
- since your PR is aproved, it will be merged to `master` branch
- in a moment in time we'll create a release, using the pattern: `release/vX.X.X`

## Patterns

These are some of patterns definitions to help us to keep a default arquitecture.

- Package manager: [PyPI](https://pypi.org/), sure
- Python version: [v3.8.x](https://www.python.org/downloads)
- Python Framework: [Django](https://www.djangoproject.com) framework
- Python server: 
- Linter: 
- Database: 
- Migrations: Run on a container described in docker-compose file: [image](https://hub.docker.com) image
- i18n: 
- Date and time: 
- Test: 
- Logs: 
- Http Request: 
- Authentication: 
- SMTP email: 
- Docker compose and dockerfile attached running migrations e starting database and python server

## Project structure

Basic folder structure

- **src/config**: App config (some of these are inherited from .env file), constants, configuration and i18n
- **src/api**: Endpoints and business logic
- **src/static**: Images, styles, fonts and other files that can be served
- **src/middlewares**: Middlewares for routes
- **src/routes**: Routes, :]
- **src/templates**: mustache interpreted files
- **src/test**: Mocha and chai unity tests
- **src/utils**: Utilities and modules superior layer implementations
