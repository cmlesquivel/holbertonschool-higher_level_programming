#!/usr/bin/python3
is_mayus = 0
for x in range(122, 96, -1):
    print('{:c}'.format(x + is_mayus), end='')
    if is_mayus == 0:
        is_mayus = -32
    else:
        is_mayus = 0
