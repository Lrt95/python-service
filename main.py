""" Module name

Created by Antony Correia
Python Docstring
"""

import time

from apscheduler.schedulers.background import BackgroundScheduler

# from db.databaseInflux import write_data
from argParsing import cliArgParsing
from dataSysteme.Getdatasystem import GetDataSystem
from bus.sender import sender

scheduler = BackgroundScheduler()
data_system = GetDataSystem()


def send_producer(hardware, agent, create_dict):
    """ Function send_producer
        Send info system to producer
    :param create_dict: dict of data system
    :param hardware: String of name hardware
    :param agent: String of name agent
    """
    sender(create_dict, hardware, agent)


def create_job_scheduler(agent, config):
    """ Function create job scheduler
        add job with config yaml
    :param agent: int of index agent
    :param config: config.yaml
    """
    function_hardware = {
        "cpu": data_system.create_dictionary_cpu,
        "disk": data_system.create_dictionary_disk,
        "memory": data_system.create_dictionary_memory,
        "net": data_system.create_dictionary_net,
        "sensor": data_system.create_dictionary_sensors
    }

    for hardware, value in config.items():
        if hardware != "agent":
            scheduler.add_job(send_producer, 'interval', args=[hardware, agent, function_hardware[hardware]],
                              max_instances=10,
                              seconds=value)


if __name__ == '__main__':
    dict_configuration = cliArgParsing.cli_parse()
    if dict_configuration:
        print('Press Ctrl + C to exit')
        for agent in range(dict_configuration["agent"]):
            create_job_scheduler(agent, dict_configuration)

    scheduler.start()
    try:
        while True:
            time.sleep(10)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
