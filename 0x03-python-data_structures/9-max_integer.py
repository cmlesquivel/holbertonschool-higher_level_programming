#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        copy_list = my_list[:]
        copy_list.sort()
        return copy_list[-1]
