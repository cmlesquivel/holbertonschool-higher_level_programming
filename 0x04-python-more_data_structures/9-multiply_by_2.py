#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dir_new = {}
    for clave, valor in sorted(a_dictionary.items()):
        dir_new[clave] = valor*2
    return dir_new
