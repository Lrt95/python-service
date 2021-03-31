import pika
import time
import json

def callback(ch, method, properties, body):
    print(json.loads(body))


def sender():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='logs', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume('logs', callback, auto_ack=True)

    #  ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.start_consuming()

if __name__ == '__main__':
    sender()