#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    new_list.insert(search-1, replace)
    new_list.pop(search+1)
    return new_list
