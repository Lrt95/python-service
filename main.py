
"""Module Main

"""

import sys
import argparse
import yaml


def usage_line_command(message="Usage : python3 main.py [*.yml or *.yaml]"):
    """Function usage_line_command

    :param message: print message error of the parsing file or parsing command line
    """
    print(message)


def parsing_arg(argv):
    """Function parsing_argv

    :param argv: arguments of the command line
    :return: the name of the file
    """
    if len(argv) == 2:
        if (argv[1].find(".yml") == len(argv[1]) - 4) or (argv[1].find(".yaml") == len(argv[1]) - 5):
            if len(argv[1].split(".")) == 2:
                parser = argparse.ArgumentParser()
                parser.add_argument('file', type=argparse.FileType('r'))
                args = parser.parse_args()
                return args.file.name
            else:
                usage_line_command()
        else:
            usage_line_command()
    else:
        usage_line_command()


def parsing_yaml(name_file):
    """Function parsing_yaml

    :param name_file: name of the file to parse
    :return: dict with the value find in file.yaml
    """
    yaml_file = open(name_file, 'r')
    try:
        yaml_content = yaml.safe_load(yaml_file)
    except yaml.YAMLError as exc:
        usage_line_command("Error .yaml configuration in this file")
        usage_line_command("cpu: value\nmemory: value\nsensor: value\ndisk: value\nnet: value")
        return

    dict_configuration = {}
    for key, value in yaml_content.items():
        if key == "cpu" or key == "memory" or key == "sensor" or key == "disk" or key == "net":
            if int(value) > 0:
                dict_configuration[key] = int(value)
    return dict_configuration


def main():
    """Function main

    :return: nothing stop the program if problem
    """
    name_file = parsing_arg(sys.argv)
    if len(name_file) > 0:
        dict_configuration = parsing_yaml(name_file)
        if (len(dict_configuration)) == 0:
            usage_line_command("Error .yaml configuration in this file")
            usage_line_command("cpu: value\nmemory: value\nsensor: value\ndisk: value\nnet: value")
            return
        print(dict_configuration)


if __name__ == '__main__':
    main()

""" Module name

Created by Antony Correia
Python Docstring
"""

from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler

from db.databaseInflux import DatabaseInflux

interval_schedule = 3


def launch_task():
    """Function launch task
        For lunch task to schedule
    """
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(launch_task, 'interval', seconds=interval_schedule)
    scheduler.start()
    print('Press Ctrl + C to exit')
    db = DatabaseInflux("agent1")
    db.write_data({"disk_partitions": 234.25, "disk_io_counters": 254}, "disk")
    print(db.read_data("disk"))
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

