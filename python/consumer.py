from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'topic5',
    bootstrap_servers=['35.201.148.193:9094'],
    group_id='topic9')

for message in consumer:
    message = message.value
    print('{}'.format(message))
