# Udarnik ![Логотип проекта](/frontend/Udarnik.png)

Доброго времени суток, всем кто это читает, вашему вниманию представляется распредленная система сбора и обработки сигналов экгаустеров агломерационой машины под кодовым названием  **Ударник**

# Установка

Скачайте репозиторий из
*GitHub: https://github.com/K-Team-Coders/Udarnik*

# Запуск приложения через Docker (В разработке)

ДЛЯ РАБОТЫ НЕОБХОДИМО ИСПОЛЬЗОВАНИЕ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ ДЛЯ РАБОТЫ PostgreSQL, FastAPI, python-kafka

Откройте терминал в корне проекта, пропишите команду `docker-compose up -d`

Через некоторое время можно зайти в браузер по адресу *http://localhost:8080/*

# Запуск приложения вручную

Для универсальной работы приложения, были использованы возможности библиотеки **dotenv**

В корне проекта необходимо создать файл DB.env

Пример оформления:

`IP="192.168.0.131"  
USER="temio"  
PASSWORD="temio"  
PORT="5433"  
RUN_IP="192.168.0.156"  
RUN_PORT="8079`

IP, User, Password, Port - Для подключения к PostgreSQL

Run_IP, Run_PORT - Для запуска FastAPI

#### Backend

Откройте терминал в папке ***backend***, выполните команды:

`python -m venv venv`

`venv\Scripts\activate`

`pip install -r requirements.txt`

Вы создали виртуальное окружение и загрузили необходимые библиотеки, теперь можно запустить backend-часть этого проекта

В папке backend, выполнить

`python backendFastApi.py runserver`

#### Frontend

Откройте терминал в папке ***frontend***, выполните команды:

`npm install`

`npm run serve`

После этого frontend-часть этого проекта будет доступна либо на http://localhost:8080/, либо на http://localhost:8081/

#### Database

Установите PostgreSQL v.=14

В pg_hba.conf при необходимости можно задать адреса, с которых аналитики будут брать данные, а также адреса по которым будут обращаться машины с поднятыми инстансами python-kafka, если, вы будете расширяться.

### Математическая составляющая проекта и почему это работает.

Так как данные поступают из Apache Kafka непрерывно, для их оптимального хранения и обработки было принято решение декомпозировать отношения в 4ю нормальную форму. Отношения, находящиеся в **4НФ** для данной задачи имеют вид:
**ID(Int, PK), Name(Text), Value(Double), Data(Timestamp without time zone)**.

Для реализации этого в PostgreSQL необходимо создать базу данных с одним отношением и четыремя атрибутами соотвественно.

Использование 4НФ позволяет получить преимущество в скорости вычислений для любых преобразований данных. То есть если нас интересует аналитика по одному конкретному сенсору, то мы делаем выборку с заранее заданным **Name.**
Если нас интересует анализ временных рядов, то мы осуществляем выборку по времени сообщения из Kafka.
И так далее.

### Задача предсказания времени поломки

В ходе выполнения работы по поиску метода, были получены следующие результаты:.

## API

Весь API представлен в файле **backendFastApi.py**.

GET-запросы по адресам:

1) *http://RUN_IP:RUN_PORT/lastMnemonicEX1/*
2) *http://RUN_IP_RUN_PORT/lastGraphEX1/*

Приложение можно использовать в любых проектах, достаточно пробросить API к нужным вычислениям.
