#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search > len(my_list) or search < 1:
        return None
    else:
        new_list = my_list[:]
        new_list[search-1] = replace
    return new_list
