# Foodgram - Grocery Assistant

The project is available at: [http://yp.hopto.org](http://yp.hopto.org)


![example workflow](https://github.com/Kinin812/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)  

## Technology stack

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Project description

Foodgram is a resource for publishing recipes.  
Users can create their own recipes, read other users' recipes, subscribe to interesting authors, add the best recipes to favorites, and create a shopping list and download it in pdf format.

## Launch using CI/CD

Install docker, docker-compose on Yandex.Cloud VM server:
```bash
ssh username@ip
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Create a folder infra:
```bash
mkdir infra
```
- Move docker-compose.yml and default.conf files to server.

```bash
scp docker-compose.yml username@server_ip:/home/<username>/
scp default.conf <username>@<server_ip>:/home/<username>/
```
- Create an .env file in the infra directory:

```bash
touch .env
```
- Fill in the .env secrets of the repository settings

```python
DB_ENGINE='django.db.backends.postgresql'
DB_NAME=YOUR_DB_NAME
POSTGRES_USER=YOUR_POSTGRES_USER
POSTGRES_PASSWORD=YOR_POSTGRES_PASSWORD
DB_HOST=db
DB_PORT='5432'
SECRET_KEY=YOUR_SECRET_KEY
ALLOWED_HOSTS=YOUR_ALLOWED_HOSTS
```

Copy the docker-compose.yml, default.conf settings from the infra folder to the server.

## Running a project via Docker
- In the infra folder run the command to build the container:
```bash
sudo docker-compose up -d
```

To access the container run the following commands:

```bash
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate --noinput 
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

Additionally you can fill the DB with ingredients and tags:

```bash
sudo docker-compose exec backend python manage.py load_tags
sudo docker-compose exec backend python manage.py load_ingrs
```

## Running a project in dev mode

- Install and activate virtual environment

```bash
source /venv/bin/activated
```

- Install dependencies from requirements.txt file

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Run migrations:

```bash
python manage.py migrate
```

- In the folder with the manage.py file run the command:
```bash
python manage.py runserver
```

### API documentation available after launch
```url
http://127.0.0.1/api/docs/
```

---

### Authors
[Kinin812](https://github.com/Kinin812) - Backend and deployment for Foodgram service.  
[Яндекс.Практикум](https://github.com/yandex-praktikum) Frontend for Foodgram service.
