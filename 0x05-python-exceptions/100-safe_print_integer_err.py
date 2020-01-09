#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_integer = True
    try:
        print('{:d}'.format(value))
        return is_integer
    except ValueError as err:
        print("Exception {}".format(err), file=sys.stderr)
        return not is_integer
