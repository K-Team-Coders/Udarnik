from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from loguru import logger
import datetime
import uvicorn
import psycopg2
import os
import random

# Подгрузка ваших кредов для БД
load_dotenv("./DB.env")
IP = os.getenv('IP')
USER = os.getenv('USER')
PORT = os.getenv('PORT')
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
        host=IP,
        port=PORT
    )
    print('Соединение установлено!')
except Exception as e:
    logger.error(e)

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

    last_time = data[len(data)-3]
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
            values.append('NaN')

    # Цвета для алармов и ворнигов
    colors = []

    # Подшипники 9
    for index in range(21):
        current = values[0 + (index * 5)] 
        alarm_max = values[1 + (index * 5)]
        alarm_min = values[2 + (index * 5)]
        warning_max = values[3 + (index * 5)]
        warning_min = values[4 + (index * 5)]

        if type(current) is not type(3.14) or type(alarm_max) is not type(3.14) or type(alarm_min) is not type(3.14) or type(warning_max) is not type(3.14) or type(warning_min) is not type(3.14):
            # print(warning_min, current, warning_max, 'Undefined')
            colors.append('#540880')
            colors.append('#AF89C4')
        elif current < warning_max and current > warning_min:
            # print(warning_min, current, warning_max, 'OK')
            colors.append('#EFEFEF')
            colors.append('#414F4F')
        elif (current >= warning_max and current < alarm_max):
            # print(warning_max, current, alarm_max, 'WARNING')
            colors.append("#FEF1DB")
            colors.append("#F69112")
        elif (current >= alarm_max):
            # print(alarm_min, current, alarm_max, 'ALARM')
            colors.append('#FCDBCB')
            colors.append('#AA1700')
        else:
            colors.append('#EFEFEF')
            colors.append('#414F4F')

    # Для 1го ПШ
    if "#FCDBCB" in colors[:8]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[:8]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 2ой ПШ
    if "#FCDBCB" in colors[8:16]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[8:16]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 3ой ПШ
    if "#FCDBCB" in colors[16:18]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[16:18]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 4ой ПШ
    if "#FCDBCB" in colors[18:20]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[18:20]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 5ой ПШ
    if "#FCDBCB" in colors[20:22]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[20:22]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 6ой ПШ
    if "#FCDBCB" in colors[22:24]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[22:24]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 7ой ПШ
    if "#FCDBCB" in colors[24:32]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[24:32]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 8ой ПШ
    if "#FCDBCB" in colors[32:40]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[32:40]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    # Для 9ой ПШ
    if "#FCDBCB" in colors[40:42]:
        # print('RED')
        colors.append('#FCDBCB')
        colors.append('#AA1700')
    elif "#FEF1DB" in colors[40:42]:
        # print('Warning')
        colors.append("#FEF1DB")
        colors.append("#F69112")
    else:
        # print('OK')
        colors.append('#EFEFEF')
        colors.append('#414F4F')

    return {
        'values': values,
        'colors': colors,
        'time': last_time
    }

@app.get('/lastGraphEX1/')
def get_item():
    # Отслеживаемые имена для 1го Эксгаустера
    names = [
        'SM_Exgauster[2:27]', 
        'SM_Exgauster[2:2]', 
        'SM_Exgauster[2:0]', 
        'SM_Exgauster[2:1]',
        'SM_Exgauster[2:5]', 
        'SM_Exgauster[2:28]', 
        'SM_Exgauster[2:3]', 
        'SM_Exgauster[2:4]', 
        'SM_Exgauster[2:29]', 
        'SM_Exgauster[2:30]', 
        'SM_Exgauster[2:31]', 
        'SM_Exgauster[2:32]', 
        'SM_Exgauster[2:33]', 
        'SM_Exgauster[2:8]', 
        'SM_Exgauster[2:6]', 
        'SM_Exgauster[2:7]', 
        'SM_Exgauster[2:34]', 
        'SM_Exgauster[2:11]', 
        'SM_Exgauster[2:9]', 
        'SM_Exgauster[2:10]', 
        'SM_Exgauster[2:35]'
    ]

    cur = connection.cursor()
    cur.execute("""SELECT DISTINCT "Kafka".date FROM "Kafka" ORDER BY "Kafka".date ASC""")
    data=cur.fetchall()
    last_time = data[len(data)-2]

    times = []
    for index in range(1,21):
        times.append(last_time[0] - datetime.timedelta(minutes=index))
    times.reverse()

    datasets = []

    for name in names:
        value = []

        for time in times:
            cur.execute(f"""SELECT * FROM "Kafka" WHERE "Kafka".name = '{name}' AND "Kafka".date = '{time}' """)
            data=cur.fetchall()
            for subdata in data:
                value.append(subdata[2])

        randomint = random.randrange(1,9)
        datasets.append({
            "label": name,
            "data": value,
            'backgroundColor':f"#F{randomint}F{randomint}F{randomint}"
        })

    return {
        "times": times,
        "datasets": datasets
    }

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.0.156", port=8079)