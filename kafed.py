from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'zsmk-9433-dev-01',
    bootstrap_servers='rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9092',
    security_protocol="SASL_SSL",
    api_version=(0,11,5),
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_username='9433_reader',
    sasl_plain_password='eUIpgWu0PWTJaTrjhjQD3.hoyhntiK')

print("ready")

for msg in consumer:
    print(msg.key.decode("utf-8") + ":" + msg.value.decode("utf-8"))