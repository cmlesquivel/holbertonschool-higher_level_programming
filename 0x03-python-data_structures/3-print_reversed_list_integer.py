#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        length_list = len(my_list) - 1
        for i in range(length_list, -1, -1):
            print('{:d}'.format(my_list[i]))
