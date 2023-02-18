from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from loguru import logger
import uvicorn
import psycopg2
import os
import random

# Подгрузка ваших кредов для БД
load_dotenv("./DB.env")
IP = os.getenv('IP')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connection = 0
try:
    connection = psycopg2.connect(
        dbname='test', 
        user=USER,
        password=PASSWORD, 
        host=IP
    )
    print('Соединение установлено!')
except Exception as e:
    print(e)

@app.get('/lastMnemonicEX1/')
def get_item():
    EX1_LIST = [
        "SM_Exgauster[2:27]",
        "SM_Exgauster[2:65]",
        "SM_Exgauster[2:74]",
        "SM_Exgauster[2:83]",
        "SM_Exgauster[2:92]",
        "SM_Exgauster[2:2]",
        "SM_Exgauster[2:139]",
        "SM_Exgauster[2:151]",
        "SM_Exgauster[2:163]",
        "SM_Exgauster[2:175]",
        "SM_Exgauster[2:0]",
        "SM_Exgauster[2:137]",
        "SM_Exgauster[2:149]",
        "SM_Exgauster[2:161]",
        "SM_Exgauster[2:173]",
        "SM_Exgauster[2:1]",
        "SM_Exgauster[2:138]",
        "SM_Exgauster[2:150]",
        "SM_Exgauster[2:162]",
        "SM_Exgauster[2:174]",
        "SM_Exgauster[2:28]",
        "SM_Exgauster[2:66]",
        "SM_Exgauster[2:75]",
        "SM_Exgauster[2:84]",
        "SM_Exgauster[2:93]",
        "SM_Exgauster[2:5]",
        "SM_Exgauster[2:142]",
        "SM_Exgauster[2:154]",
        "SM_Exgauster[2:166]",
        "SM_Exgauster[2:178]",
        "SM_Exgauster[2:3]",
        "SM_Exgauster[2:140]",
        "SM_Exgauster[2:152]",
        "SM_Exgauster[2:164]",
        "SM_Exgauster[2:176]",
        "SM_Exgauster[2:4]",
        "SM_Exgauster[2:141]",
        "SM_Exgauster[2:153]",
        "SM_Exgauster[2:165]",
        "SM_Exgauster[2:177]",
        "SM_Exgauster[2:29]",
        "SM_Exgauster[2:67]",
        "SM_Exgauster[2:76]",
        "SM_Exgauster[2:85]",
        "SM_Exgauster[2:94]",
        "SM_Exgauster[2:30]",
        "SM_Exgauster[2:68]",
        "SM_Exgauster[2:77]",
        "SM_Exgauster[2:86]",
        "SM_Exgauster[2:95]",
        "SM_Exgauster[2:31]",
        "SM_Exgauster[2:69]",
        "SM_Exgauster[2:78]",
        "SM_Exgauster[2:87]",
        "SM_Exgauster[2:96]",
        "SM_Exgauster[2:32]",
        "SM_Exgauster[2:70]",
        "SM_Exgauster[2:79]",
        "SM_Exgauster[2:88]",
        "SM_Exgauster[2:97]",
        "SM_Exgauster[2:33]",
        "SM_Exgauster[2:71]",
        "SM_Exgauster[2:80]",
        "SM_Exgauster[2:89]",
        "SM_Exgauster[2:98]",
        "SM_Exgauster[2:8]",
        "SM_Exgauster[2:145]",
        "SM_Exgauster[2:157]",
        "SM_Exgauster[2:169]",
        "SM_Exgauster[2:181]",
        "SM_Exgauster[2:6]",
        "SM_Exgauster[2:143]",
        "SM_Exgauster[2:155]",
        "SM_Exgauster[2:167]",
        "SM_Exgauster[2:179]",
        "SM_Exgauster[2:7]",
        "SM_Exgauster[2:144]",
        "SM_Exgauster[2:156]",
        "SM_Exgauster[2:168]",
        "SM_Exgauster[2:180]",
        "SM_Exgauster[2:34]",
        "SM_Exgauster[2:72]",
        "SM_Exgauster[2:81]",
        "SM_Exgauster[2:90]",
        "SM_Exgauster[2:99]",
        "SM_Exgauster[2:11]",
        "SM_Exgauster[2:148]",
        "SM_Exgauster[2:160]",
        "SM_Exgauster[2:172]",
        "SM_Exgauster[2:184]",
        "SM_Exgauster[2:9]",
        "SM_Exgauster[2:146]",
        "SM_Exgauster[2:158]",
        "SM_Exgauster[2:170]",
        "SM_Exgauster[2:182]",
        "SM_Exgauster[2:10]",
        "SM_Exgauster[2:147]",
        "SM_Exgauster[2:159]",
        "SM_Exgauster[2:171]",
        "SM_Exgauster[2:183]",
        "SM_Exgauster[2:35]",
        "SM_Exgauster[2:73]",
        "SM_Exgauster[2:82]",
        "SM_Exgauster[2:91]",
        "SM_Exgauster[2:100]",
        "SM_Exgauster[2:42]",
        "SM_Exgauster[2:41]",
        "SM_Exgauster[2:37]",
        "SM_Exgauster[2:36]",
        "SM_Exgauster[2:24]",
        "SM_Exgauster[2:61]",
        "SM_Exgauster[4.1]",
        "SM_Exgauster[4.2]",
        "SM_Exgauster[4:6]",
        "SM_Exgauster[4:2]",
        "SM_Exgauster[4:4]",
        "SM_Exgauster[4:3]",
        "SM_Exgauster[4:5]",
        "SM_Exgauster[4:0]",
        "SM_Exgauster[4:1]",
        "SM_Exgauster[2.0]",
    ]
    cur = connection.cursor()
    cur.execute("""SELECT DISTINCT "Kafka".date FROM "Kafka" ORDER BY "Kafka".date ASC""")
    data=cur.fetchall()


    randomint = random.randrange(1,4)
    last_time = data[len(data)-randomint]
    cur.execute(f"""SELECT * FROM "Kafka" WHERE "Kafka".date = '{last_time[0]}' """)
    data=cur.fetchall()

    values = []
    for EX in EX1_LIST:
        filled = False
        for subdata in data:
            if subdata[1] == EX:
                if len(str(subdata[2])) > 4:
                    values.append(float(str(subdata[2])[:4]))
                else:
                    values.append(subdata[2])
                filled = True
        if not filled:
            values.append(0.0)

    # Цвета для алармов и ворнигов
    colors = []

    # Подшипники 9
    for index in range(9):
        current = values[0 + (index * 5)]
        alarm_max = values[1 + (index * 5)]
        alarm_min = values[2 + (index * 5)]
        warning_max = values[3 + (index * 5)]
        warning_min = values[4 + (index * 5)]

        if current < warning_max and current > warning_min:
            colors.append('#EFEFEF')
            colors.append('#414F4F')
        elif (current > warning_max and current < alarm_max) or (current < warning_min and current > alarm_min):
            colors.append("#FEF1DB")
            colors.append("#F69112")
        elif (current > alarm_max or current < alarm_min):
            colors.append('#FCDBCB')
            colors.append('#AA1700')
        else:
            colors.append('#EFEFEF')
            colors.append('#414F4F')

    return {
        'values': values,
        'colors': colors
    }

@app.get('/{id}')
def get_item(id:int):
    return {}

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.0.156", port=8079)