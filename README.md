[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![SQLite3](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=SQLite)](https://www.sqlite.org/)
[![unittest](https://img.shields.io/badge/-unittest-464646?style=flat-square&logo=unittest)](https://docs.python.org/3/library/unittest.html)

## Проект

Небольшое CRUD API для вишлист. Позволяет создать, обновлять и удалять записи с параметрами: название, ссылка, цена, примечание.

## Запуск проекта в dev-режиме
 - Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/A-A-Tyurin/simple_wishlist
```
```
cd yatube_api
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
