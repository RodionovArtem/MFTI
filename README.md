![Project logo](image/logo.png)


# Парсер сайта ЦУМ

![Python](https://img.shields.io/badge/Python_3.10-blue?logo=python&logoColor=yellow)
![SQLite](https://img.shields.io/badge/SQLite-purple?logo=SQLite&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker-grey?logo=Docker&logoColor=blue)
![DockerCompose](https://img.shields.io/badge/DockerCompose-blue)
![Static Badge](https://img.shields.io/badge/FastAPI-black?logo=FastAPI)

Парсер предназначен для сбора информации о товарах, отсортированных по новым поступлениям, на сайте одежды ЦУМ. Это позволит пользователю в любой момент посмотреть, какие товары недавно поступили, таким образом он сможет быстро скупать их

###### Информация, которая будет парситься с этого сайта:
    -Бренд и тип товара
    -Цена товара
    -Описание товара(страна производителя, материал и тд.)
    -Ссылка на товар


###### Структура проекта
    │
    ├── backend
    │ └── run_server.py
    │
    ├── database
    │ └── db_create.py
    │
    ├── main.py
    └── parser.py


### Установка и настройка
###### Клонируем репозиторий:
    git clone https://github.com/RodionovArtem/MFTI.git

###### Переходим в директорию проекта
    cd MFTI

###### Сборка и запуск контейнеров Docker
    docker-compose up —build


##### Ссылка, с которой работает парсер:
    https://www.tsum.ru/catalog/odezhda-2409/?sort=date

