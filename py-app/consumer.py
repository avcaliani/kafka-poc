#!/usr/bin/env python3
# @script   consumer.py
# @author   Anthony Vilarim Caliani
# @contact  github.com/avcaliani
#
# @description
# Kafka Consumer.
#
# @usage
# ./consumer.py
import json
from kafka import KafkaConsumer

KAFKA_TOPIC = 'sales-topic'
KAFKA_SERVERS = ['localhost:9092']

if __name__ == '__main__':
    print('KAFKA CONSUMER 👀\nPress Ctrl+c to stop')
    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_SERVERS,
        group_id='group-python',
        value_deserializer=lambda msg: json.loads(msg.decode('utf-8')),
        enable_auto_commit=False,
        auto_offset_reset='earliest'
    )
    consumer.subscribe([KAFKA_TOPIC])
    try:
        for msg in consumer:
            if msg.value['user'] == '#fake_user':  # Fake Error:
                print(f'ERROR! REJECTED MESSAGE -> { msg.value }')
            else:
                print('%s:%d:%d: key=%s value=%s' % (
                    msg.topic, msg.partition, msg.offset, msg.key, msg.value
                ))
                consumer.commit()

    except (KeyboardInterrupt, SystemExit):
        consumer.close()
        print('Bye bye!')
