from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['35.201.148.193:2181'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number': e}
    producer.send('test', value=data)
    sleep(5)
