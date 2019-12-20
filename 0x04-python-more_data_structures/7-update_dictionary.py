#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        dir_2 = {key: value}
        a_dictionary.update(dir_2)
    else:
        a_dictionary[key] = value

    return a_dictionary
