#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length_list = len(my_list) - 1
    copy_list = my_list[:]
    if idx > length_list or idx < 0:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
