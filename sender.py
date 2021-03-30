"""Module sender.py

"""

import pika
import json


def sender(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    print(connection)
    channel = connection.channel()
    channel.queue_declare(queue='logs', durable=True)

    channel.basic_publish(exchange='', routing_key='logs', body=json.dumps(message),
                          properties=pika.BasicProperties(
                            delivery_mode=2
                        ))
    print(f" [x] Sent {message}")
    connection.close()


def main():
    sender({"id": "test", "toto": "titi"})


if __name__ == '__main__':
    main()
