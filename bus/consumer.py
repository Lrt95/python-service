import pika
import json

from db.databaseInflux import write_data


def callback(ch, method, properties, body):
    """Function callback call when received message

    :param ch:
    :param method:
    :param properties:
    :param body: message received
    """
    dict_message = (json.loads(body))
    print(f' [*] Job Received: {dict_message["hardware"]} - Agent: {dict_message["agent"]}')
    write_data(dict_message["message"], dict_message["hardware"], dict_message["agent"])


def consumer():
    """Function consumer received message in queue

    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='logs', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume('logs', callback, auto_ack=True)

    #  ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.start_consuming()


if __name__ == '__main__':
    consumer()
