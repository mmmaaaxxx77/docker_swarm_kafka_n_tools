from kafka import KafkaConsumer, TopicPartition
import json

consumer = KafkaConsumer(
    'topic1',
    bootstrap_servers=['104.199.243.52:9094'],
    group_id='topic1',
    auto_offset_reset='earliest')

# consumer.seek(TopicPartition(topic='topic1', partition=0), 0)
# consumer.seek(TopicPartition(topic='topic1', partition=1), 0)
# consumer.seek(TopicPartition(topic='topic1', partition=2), 0)
for message in consumer:
    # message = message.value
    print(f'{json.loads(message.value)} --- {message}')
