#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    contador = 0
    if my_list != ():
        my_list.sort()

        temp = my_list[0]
        new_list.append(temp)

        for i in my_list:
            if temp == i:
                pass
            else:
                new_list.append(i)
                temp = i
        for x in new_list:
            contador = contador + x
    return contador
