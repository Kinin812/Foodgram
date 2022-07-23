# Foodgram - Продуктовый помощник

Проект доступен по адресу: [http://yp.hopto.org](http://yp.hopto.org)

[Админка](http://yp.hopto.org/admin)   
admin: admin_food  
test: test_food
---


![example workflow](https://github.com/Kinin812/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)  

## Стек технологий

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Описание проекта

Foodgram это ресурс для публикации рецептов.  
Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в pdf формате

## Запуск с использованием CI/CD

Установить docker, docker-compose на сервере ВМ Yandex.Cloud:
```bash
ssh username@ip
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Создайте папку infra:
```bash
mkdir infra
```
- Перенести файлы docker-compose.yml и default.conf на сервер.

```bash
scp docker-compose.yml username@server_ip:/home/<username>/
scp default.conf <username>@<server_ip>:/home/<username>/
```
- Создайте файл .env в дериктории infra:

```bash
touch .env
```
- Заполнить в настройках репозитория секреты .env

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

Скопировать на сервер настройки docker-compose.yml, default.conf из папки infra.

## Запуск проекта через Docker
- В папке infra выполнить команду, что бы собрать контейнер:
```bash
sudo docker-compose up -d
```

Для доступа к контейнеру выполните следующие команды:

```bash
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate --noinput 
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

Дополнительно можно наполнить DB ингредиентами и тэгами:

```bash
sudo docker-compose exec backend python manage.py load_tags
sudo docker-compose exec backend python manage.py load_ingrs
```

## Запуск проекта в dev-режиме

- Установить и активировать виртуальное окружение

```bash
source /venv/bin/activated
```

- Установить зависимости из файла requirements.txt

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Выполнить миграции:

```bash
python manage.py migrate
```

- В папке с файлом manage.py выполнить команду:
```bash
python manage.py runserver
```

### Документация к API доступна после запуска
```url
http://127.0.0.1/api/docs/
```

---

### Авторы
[Калмыков К.В.](https://github.com/Kinin812) - Python разработчик. Разработал бэкенд и деплой для сервиса Foodgram.  
[Яндекс.Практикум](https://github.com/yandex-praktikum) Фронтенд для сервиса Foodgram.