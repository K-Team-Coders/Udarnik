import psycopg2
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
import pandas as pd
from datetime import datetime
import uvicorn
import psycopg2
import os
import random
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from urllib.parse import urlparse
from urllib.parse import parse_qs
app = FastAPI()
exgauster_5 = ['SM_Exgauster[3:27]',
'SM_Exgauster[3:63]',
'SM_Exgauster[3:72]',
'SM_Exgauster[3:81]',
'SM_Exgauster[3:90]',
'SM_Exgauster[3:2]',
'SM_Exgauster[3:137]',
'SM_Exgauster[3:149]',
'SM_Exgauster[3:161]',
'SM_Exgauster[3:173]',
'SM_Exgauster[3:0]',
'SM_Exgauster[3:135]',
'SM_Exgauster[3:147]',
'SM_Exgauster[3:159]',
'SM_Exgauster[3:171]',
'SM_Exgauster[3:1]',
'SM_Exgauster[3:136]',
'SM_Exgauster[3:148]',
'SM_Exgauster[3:160]',
'SM_Exgauster[3:172]',
'SM_Exgauster[3:28]',
'SM_Exgauster[3:64]',
'SM_Exgauster[3:73]',
'SM_Exgauster[3:82]',
'SM_Exgauster[3:91]',
'SM_Exgauster[3:5]',
'SM_Exgauster[3:140]',
'SM_Exgauster[3:152]',
'SM_Exgauster[3:164]',
'SM_Exgauster[3:176',
'SM_Exgauster[3:3]',
'SM_Exgauster[3:138]',
'SM_Exgauster[3:150]',
'SM_Exgauster[3:162]',
'SM_Exgauster[3:174]',
'SM_Exgauster[3:4]',
'SM_Exgauster[3:139]',
'SM_Exgauster[3:151]',
'SM_Exgauster[3:163]',
'SM_Exgauster[3:175]',
'SM_Exgauster[3:29]',
'SM_Exgauster[3:65]',
'SM_Exgauster[3:74]',
'SM_Exgauster[3:83]',
'SM_Exgauster[3:92]',
'SM_Exgauster[3:30]',
'SM_Exgauster[3:66]',
'SM_Exgauster[3:75]',
'SM_Exgauster[3:84]',
'SM_Exgauster[3:93]',
'SM_Exgauster[3:31]',
'SM_Exgauster[3:67]',
'SM_Exgauster[3:76]',
'SM_Exgauster[3:85]',
'SM_Exgauster[3:94]',
'SM_Exgauster[3:32]',
'SM_Exgauster[3:68]',
'SM_Exgauster[3:77]',
'SM_Exgauster[3:86]',
'SM_Exgauster[3:95]',
'SM_Exgauster[3:33]',
'SM_Exgauster[3:69]',
'SM_Exgauster[3:78]',
'SM_Exgauster[3:87]',
'SM_Exgauster[3:96]',
'SM_Exgauster[3:8]',
'SM_Exgauster[3:143]',
'SM_Exgauster[3:155]',
'SM_Exgauster[3:167]',
'SM_Exgauster[3:179]',
'SM_Exgauster[3:6]',
'SM_Exgauster[3:141]',
'SM_Exgauster[3:153]',
'SM_Exgauster[3:165]',
'SM_Exgauster[3:177]',
'SM_Exgauster[3:7]',
'SM_Exgauster[3:142]',
'SM_Exgauster[3:154]',
'SM_Exgauster[3:166]',
'SM_Exgauster[3:178]',
'SM_Exgauster[3:34]',
'SM_Exgauster[3:70]',
'SM_Exgauster[3:79]',
'SM_Exgauster[3:88]',
'SM_Exgauster[3:97]',
'SM_Exgauster[3:11]',
'SM_Exgauster[3:146]',
'SM_Exgauster[3:158]',
'SM_Exgauster[3:170]',
'SM_Exgauster[3:182]',
'SM_Exgauster[3:9]',
'SM_Exgauster[3:144]',
'SM_Exgauster[3:156]',
'SM_Exgauster[3:168]',
'SM_Exgauster[3:180]',
'SM_Exgauster[3:10]',
'SM_Exgauster[3:145]',
'SM_Exgauster[3:157]',
'SM_Exgauster[3:169]',
'SM_Exgauster[3:181]',
'SM_Exgauster[3:35]',
'SM_Exgauster[3:71]',
'SM_Exgauster[3:80]',
'SM_Exgauster[3:89]',
'SM_Exgauster[3:98]',
'SM_Exgauster[3:42]',
'SM_Exgauster[3:41]',
'SM_Exgauster[3:37]',
'SM_Exgauster[3:36]',
'SM_Exgauster[3:24]',
'SM_Exgauster[3:61]',
'SM_Exgauster[5.1]',
'SM_Exgauster[5.2]',
'SM_Exgauster[5:6]',
'SM_Exgauster[5:2]',
'SM_Exgauster[5:4]',
'SM_Exgauster[5:3]',
'SM_Exgauster[5:5]',
'SM_Exgauster[5:0]',
'SM_Exgauster[5:1]',
'SM_Exgauster[3.0]']


try:
    connection = psycopg2.connect(
        dbname='test', 
        user='jora', 
        password='jora', 
        host='192.168.0.156'
    )
   
    print('Соединение установлено!')
    cur = connection.cursor()
    cur.execute("""SELECT * FROM "Kafka" ORDER BY "Kafka".date ASC""")
    data=cur.fetchall()
    cur.close()
    connection.close()
except Exception as e:
    print(e)
data_used=data[:415000]



def get_norm_df(df):
    df=pd.DataFrame(data,columns=['0','name', 'value', 'date'])
    #df = df.set_index('date')
    df = df.drop(df.columns[0], axis=1)
    df =df.set_index('date')
    df.sort_index(inplace=True,ascending=True)
    return df
def take_data_for(df,exgauster):
    data_exgauster = df.loc[df['name'].isin(exgauster_5)]
    return data_exgauster
def take_param(df,param):
    return df.loc[df['name'] == param]

dis=take_param(take_data_for(get_norm_df(data),exgauster_5),'SM_Exgauster[3:24]')
dis=dis.drop(dis.columns[0], axis=1)

def split_data_and_train(dis):
    train = dis[:len(dis)//2]
    test = dis[len(dis)//2:]
    model = SARIMAX(train,order = (3, 0, 0), seasonal_order = (0, 1, 0, 12))
    result = model.fit()
    start = len(train)
    end = len(train) + len(test) - 1
    predictions = result.predict()
    return predictions,test,train

@app.get('/type/{item}/make_pred/')
async def index(item:str):
    return {'item':item,
        "pred": split_data_and_train(dis)[0],
            "test":split_data_and_train(dis)[1],
            "train":split_data_and_train(dis)[2]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5023)