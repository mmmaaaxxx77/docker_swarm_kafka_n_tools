import json
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['104.199.243.52:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number': f"{e}", "msg": f"這是{e}"}
    print(data)
    future = producer.send('topic3', value=data)
    future.get(timeout=10)
    print(f"{future.value}")
    sleep(1)
