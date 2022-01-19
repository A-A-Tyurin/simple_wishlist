[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat-square&logo=Flask)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/-MySQL-464646?style=flat-square&logo=MySQL)](https://mysql.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat-square&logo=SQLAlchemy)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat-square&logo=Pydantic)](https://pydantic-docs.helpmanual.io/)

## Проект

Небольшое CRUD API для приложения "вишлист". Позволяет создавать, обновлять и удалять записи с параметрами: название, ссылка, цена, примечание.

## Запуск проекта в dev-режиме
 - Клонировать репозиторий:
```
git clone https://github.com/A-A-Tyurin/simple_wishlist
```
 - Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
 - Установить зависимости:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- По образцу .env.template создайте свой файл переменных окружения
- Запустите сервер MySQL
- Создайте базу данных
```
docker exec -it <MySQL container name> bash
```
```
mysql --password
```
```
CREATE DATABASE wishlist;
```
- Для запуска dev-сервера выполните команду:
```
python3 wsgi.py
```

## MySQL

В качестве СУБД проект использует MySQL.
- Сервер MySQL может быть установлен локально, следуя инструкции
https://dev.mysql.com/doc/refman/8.0/en/installing.html
- Или через Docker
```
docker pull mysql
```
```
docker run -e MYSQL_ROOT_PASSWORD=<your rassword> -p 3306:3306 -d mysql
```
