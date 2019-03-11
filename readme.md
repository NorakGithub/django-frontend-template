# Django + Frontend Template
Template for starting backend with Django and frontend with any choices of your.

## Recommended Technology
- Python 3.6
- Postgres 10

## When should you use this template?
- When you surely know that you are choosing Django for your API Backend.

## The Goal of This Template
- Allow you to choose which frontend technology you want.
- Allow backend to able to develop using PyEnv or Docker Compose.

## Backend Guides
#### Starting with PyEnv
- Install PyEnv from [here](https://github.com/pyenv/pyenv#homebrew-on-macos), I recommend using brew if you are on Mac.
- Install VirtualEnv from [here](https://github.com/pyenv/pyenv-virtualenv).
- Install Python and Virtual Environment for your project:
```
> pyenv install 3.6.7
> pyenv virtualenv 3.6.8 your-project-name
```
- Change database name in `backend/config/settings/databases.py` by rename `ChangeDBName` to your database name.
- Change directory to backend, make this directory to be your backend interpreter, install dependencies and runserver, make sure Postgres is up and running.
```
> cd backend
> pyenv local your-project-name
> pip install -r requirements.txt
> python manage.py runserver
```

#### Start with Docker Compose
- Follow instruction to install [Docker](https://docs.docker.com/docker-for-mac/)
- Install Docker Compose [here](https://docs.docker.com/compose/install/), I recommend using `pip`.
```
> pip install docker-compose
```
- Build docker image for backend
```
> docker-compose build django
```
- Change database in `.env` and `docker-compose.yml` by replace `ChangeDBName` to your Postgres Database Name
- Now we can start our project with already written script
```
> ./project_start.sh
```
