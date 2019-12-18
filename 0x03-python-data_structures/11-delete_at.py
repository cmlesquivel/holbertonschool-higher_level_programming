#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lenght_list = len(my_list)
    new_list = my_list
    if idx > lenght_list - 1 or idx < 0:
        return new_list
    else:
        del new_list[idx]
        return new_list
