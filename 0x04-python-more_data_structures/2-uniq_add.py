#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    contador = 0
    for i in my_list:
        if my_list.count(i) == 1:
            new_list.append(i)
    for x in new_list:
        contador = contador + x
    return contador
