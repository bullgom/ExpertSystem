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
    machine = Machine(rules_file, initial_file)
    machine.start()


if __name__ == '__main__':
    main()
