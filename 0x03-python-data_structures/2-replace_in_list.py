#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length_list = len(my_list) - 1
    if idx > length_list or idx < 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
