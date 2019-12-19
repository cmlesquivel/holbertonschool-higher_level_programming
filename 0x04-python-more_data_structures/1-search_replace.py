#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    if search > len(my_list) or search < 1:
        return new_list
    else:
        new_list[search-1] = replace
    return new_list
