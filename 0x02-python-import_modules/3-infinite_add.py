#!/usr/bin/python3
from add_0 import add
import sys

if __name__ == "__main__":
    suma = 0

    if len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            suma = suma + int(sys.argv[i])
        print('{}'.format(suma))
    else:
        print(0)
