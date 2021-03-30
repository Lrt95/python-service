""" Module name

Created by Antony Correia
Python Docstring
"""

from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler

from db.databaseInflux import read_data, write_data
from argParsing import cliArgParsing
from dataSysteme.Getdatasystem import GetDataSystem

scheduler = BackgroundScheduler()
data_system = GetDataSystem()


def cpu(hardware, agent):
    write_data(data_system.create_dictionary_cpu(), hardware, "agent" + str(agent))


def disk(hardware, agent):
    print("hello")
    # print(hardware + " agent: " + str(agent))
    # print(data_system.create_dictionary_disk())
    # write_data(hardware, data_system.create_dictionary_disk(), "agent: " + str(agent))


def memory(hardware, agent):
    write_data(data_system.create_dictionary_memory(), hardware, "agent" + str(agent))


def net(hardware, agent):
    print("hello")
    # print(hardware + " agent: " + str(agent))
    # print(data_system.create_dictionary_net())
    # write_data(hardware, data_system.create_dictionary_net(), "agent: " + str(agent))


def sensor(hardware, agent):
    print("hello")
    # print(hardware + " agent: " + str(agent))
    # print(data_system.create_dictionary_sensors())
    # write_data(hardware, data_system.create_dictionary_sensors(), "agent: " + str(agent))


def create_job_scheduler(agent, config):
    """ Function create job scheduler
        add job with config yaml
    :param agent: int of index agent
    :param config: config.yaml
    """
    function_hardware = {
        "cpu": cpu,
        "disk": disk,
        "memory": memory,
        "net": net,
        "sensor": sensor
    }

    for hardware, value in config.items():
        if hardware != "agent":
            scheduler.add_job(function_hardware[hardware], 'interval', args=[hardware, agent], seconds=value)
    print('Press Ctrl + C to exit')


if __name__ == '__main__':
    dict_configuration = cliArgParsing.cli_parse()
    if dict_configuration:
        for agent in range(dict_configuration["agent"]):
            print(agent)
            create_job_scheduler(agent, dict_configuration)

    scheduler.start()
    try:
        while True:
            time.sleep(10)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
