#!/usr/bin/env python3
# @script   producer.py
# @author   Anthony Vilarim Caliani
# @contact  github.com/avcaliani
#
# @description
# Kafka Producer.
#
# @usage
# ./producer.py
import json
import random
from datetime import datetime
from time import sleep
from kafka import KafkaProducer

# Kafka
KAFKA_TOPIC = 'sales-topic'
KAFKA_SERVERS = ['localhost:9092']

# Mock
MOCK_USERS = ['anthony', 'john', 'mia', 'rachel', '#fake_user']
MOCK_PRODUCTS = [
    ('apple', 1.0), ('cherry', .05), ('lemon', .65),
    ('mango', 1.5), ('orange', 0.99), ('raspberry', .1)
]


def get_message():
    user = random.choice(MOCK_USERS)
    product = random.choice(MOCK_PRODUCTS)
    quantity = random.randint(1, 20)
    return {
        'user': user,
        'product': {
            'name': product[0],
            'price': product[1]
        },
        'quantity': quantity,
        'total': quantity * product[1],
        'created_at': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'source': 'python-mock'
    }


if __name__ == '__main__':
    print('KAFKA PRODUCER 😴\nPress Ctrl+c to stop!')
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    try:
        while True:
            msg = get_message()
            producer.send(KAFKA_TOPIC, msg)
            print(f'Message sent! Content: {msg}')
            sleep(1)
    except (KeyboardInterrupt, SystemExit):
        producer.close()
        print('Bye bye!')
