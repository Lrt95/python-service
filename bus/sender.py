"""Module sender.py

"""

import pika
import json


def sender(message, hardware, agent):
    """ Function sender of data bus

    :param message: message send with all informations
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='logs', durable=True)

    dict_agent = {"agent": agent, "hardware": hardware, "message": message()}
    print(f'Job send: {hardware} - Agent: {agent}')

    channel.basic_publish(exchange='', routing_key='logs', body=json.dumps(dict_agent),
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))

    connection.close()
