#
# Utils/trace.py
# ExpertSystem
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with MIT
#

from datetime import datetime

from Utils.settings import debug


def trace(format_str: str, *args, output=None):
    """This function provides debug output. You can easily disable
    it by assigning False to enable_debug above.
    :raises: ValueError, if amount of passed arguments doesn't
             match the amount of placeholders. (In debugging mode)
    :param format_str: format string
    :param args: values to put into string
    :param output: writing location
    """
    if not debug:
        return

    if format_str.count('{}') != len(args):
        raise ValueError

    fmt = "[{}] Message: ".format(datetime.now().time()) \
          + format_str

    log_line = fmt.format(*args)

    if output is None:
        print(log_line)
    else:
        with open(output, 'a') as out:
            out.write(log_line)
