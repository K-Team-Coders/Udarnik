from confluent_kafka import Consumer

def error_callback(err):
    print('Something went wrong: {}'.format(err))

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

c = Consumer(params)
c.subscribe(['zsmk-9433-dev-01'])
with open('data.txt', 'w') as f:
    while True:
        msg = c.poll(timeout=3.0)
        if msg:
            val = msg.value().decode()
            f.write(val)
            f.write('\n\n')