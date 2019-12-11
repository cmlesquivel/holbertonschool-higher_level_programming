#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        cod_ascii = ord(str[n])

        if cod_ascii > 96 and cod_ascii < 123:
            off_set = -32
        else:
            off_set = 0
        print('{:c}'.format(cod_ascii + off_set), end="")
    print()
