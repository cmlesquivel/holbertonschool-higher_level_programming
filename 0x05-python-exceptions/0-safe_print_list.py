#!/usr/bin/python3
def safe_print_list(my_list=[], lim=0):
    acumulador = 0
    try:
        for i in range(0, lim):
            print(my_list[i], end="")
            acumulador += 1
        print("")
        return acumulador
    except:
        print("")
        return acumulador
