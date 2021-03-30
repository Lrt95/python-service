"""Module Main

"""

import sys
import argparse


def usage_line_command(message="Usage : python3 main.py [*.yml or *.yaml]"):
    print(message)


def parsing_arg(argv):
    if len(argv) == 2:
        if ((argv[1].find(".yml") == len(argv[1]) - 4) | (argv[1].find(".yaml") == len(argv[1]) - 5)):
            parser = argparse.ArgumentParser()
            parser.add_argument('file')
            args = parser.parse_args()
            print(args)
        else:
            usage_line_command()
    else:
        usage_line_command()


def main():
    parsing_arg(sys.argv)


if __name__ == '__main__':
    main()
