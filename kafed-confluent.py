from confluent_kafka import Consumer
from dotenv import load_dotenv
from loguru import logger
import psycopg2
import os
import json

# Подгрузка ваших кредов для БД
load_dotenv("./DB.env")
IP = os.getenv('IP')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

def error_callback(err):
    print('Something went wrong: {}'.format(err))

# Параметры для Kafka
params = {
    'bootstrap.servers': 'rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091',
    'security.protocol': 'SASL_SSL',
    'ssl.ca.location': './CA.txt',
    'sasl.mechanism': 'SCRAM-SHA-512',
    'sasl.username': '9433_reader',
    'sasl.password': 'eUIpgWu0PWTJaTrjhjQD3.hoyhntiK',
    'group.id': 'MozhaykaTeam',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False,
    'error_cb': error_callback,
    'debug': 'all',
}

# Подрубаем коннектор Кафки
c = Consumer(params)
c.subscribe(['zsmk-9433-dev-01'])

# Подключение к PostgreSQL
connection = psycopg2.connect(
    database='test',
    user=USER,
    password=PASSWORD,
    host=IP,
    port='5432'
)
cursor = connection.cursor()

# Сбор данных с Kafka
while True:
    msg = c.poll(timeout=3.0)
    if msg:
        message = msg.value().decode()
        try:
            message = json.loads(message.replace('\\', ''))
            moment = message['moment']
            moment.replace('T', ' ')

            keys = list(message.keys())
            for key in keys[1:]:
                try:
                    cursor.execute(f""" INSERT INTO "Kafka" VALUES ('{key}', '{message[key]}', '{moment}') """)
                    connection.commit()
                except Exception as e:
                    logger.error(f"""'{key}', '{message[key]}', '{moment}'""")

        except Exception as e:
            logger.debug(e)