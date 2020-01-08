#!/usr/bin/python3
def safe_print_list_integers(my_list=[], lim=0):
    acumulador = 0
    for i in range(0, lim):
        try:
            print('{:d}'.format(my_list[i]), end="")
            acumulador += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return acumulador
