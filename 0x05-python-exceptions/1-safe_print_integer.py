#!/usr/bin/python3
def safe_print_integer(value):
    is_integer = False
    try:
        print('{:d}'.format(value))
        return not is_integer
    except:
        return is_integer
