""" Module cliArgparser

Created by Marine Bijon
Python Docstring
"""

import argparse
import yaml
import sys


def cli_parse():
    """Function main

    :return: nothing stop the program if problem
    """
    if len(sys.argv) == 2:
        name_file = parsing_arg(sys.argv)
        if len(name_file) > 0:
            config = parsing_yaml(name_file)
            if (len(config)) == 0:
                usage_line_command("Error .yaml configuration in this file")
                usage_line_command("cpu: value\n"
                                   "memory: value\n"
                                   "sensor: value\n"
                                   "disk: value\n"
                                   "net: value\n"
                                   "agent: value")
            return config


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
        usage_line_command("cpu: value\nmemory: value\nsensor: value\ndisk: value\nnet: value\nagent: value")
        return

    dict_configuration = {}
    for key, value in yaml_content.items():
        if key == "cpu" or key == "memory" or key == "sensor" or key == "disk" or key == "net":
            if int(value) > 0:
                dict_configuration[key] = int(value)
        if key == "agent":
            dict_configuration[key] = str(value)
    return dict_configuration
