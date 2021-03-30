"""Module Main

"""

import sys
import argparse


def usage_line_command(message="Usage : python3 main.py [*.yml or *.yaml]"):
    print(message)


def parsing_arg(argv):
    list_config_file = []
    if len(argv) == 2:
        if ((argv[1].find(".yml") == len(argv[1]) - 4) | (argv[1].find(".yaml") == len(argv[1]) - 5)):
            if len(argv[1].split(".")) == 2:
                parser = argparse.ArgumentParser()
                parser.add_argument('file', type=argparse.FileType('r'))
                args = parser.parse_args()
                for line in args.file.readlines():
                    list_config_file.append(line[:len(line) - 1]);
            else:
                usage_line_command()
        else:
            usage_line_command()
    else:
        usage_line_command()
    return  list_config_file


def main():
    list_config_file = parsing_arg(sys.argv)
    if len(list_config_file) > 0 :
        print(list_config_file)


if __name__ == '__main__':
    main()
