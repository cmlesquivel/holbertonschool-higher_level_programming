#!/usr/bin/python3
for n in range(0, 10):
    for x in range(n+1, 10):
        print('{}{}'.format(n, x), end="")
        if n != 8:
            print(end=", ")
        else:
            print()
