#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    contador = 0

    for i in new_list:
        contador = contador + i

    return contador
