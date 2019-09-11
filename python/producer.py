from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['35.201.148.193:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number': e}
    future = producer.send('topic6', value=data)
    future.get(timeout=10)
    print(f"{future.value}")
    sleep(5)
