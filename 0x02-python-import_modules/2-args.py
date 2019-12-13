#!/usr/bin/python3
from add_0 import add
import sys
if __name__ == "__main__":
    if len(sys.argv) > 2:
        print('{} arguments:'.format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, sys.argv[i]))
    elif len(sys.argv) == 2:
        print('1 argument:')
        print('1: {}'.format(sys.argv[1]))
    else:
        print('0 arguments.')
