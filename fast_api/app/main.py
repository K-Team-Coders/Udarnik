from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import psycopg2
data=0

try:
    connection = psycopg2.connect(
        dbname='test', 
        user='jora', 
        password='jora', 
        host='192.168.0.156'
    )
   
    print('Соединение установлено!')
    cur = connection.cursor()
    cur.execute("""SELECT * FROM "Kafka"  """)
    data=cur.fetchall()
    cur.close()
    connection.close()
except Exception as e:
    print(e)


@app.get('/database')
def get_item():
    return {'database_is':data}

@app.get('/{id}')
def get_item(id:int):
    return {'string':data[id]}
