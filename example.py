#
# example.py
# ExpertSystem
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with MIT
#

from ExpertSystem.Machine import Machine
from Utils.settings import initial_file, rules_file


def main():
    try:
        machine = Machine(rules_file, initial_file)
        machine.start()
    except RuntimeError as error:
        print(error)
    except ValueError as error:
        print(error)


if __name__ == '__main__':
    main()
