#!/usr/bin/python3
def remove_char_at(str, x):
    new_str = ""

    for n in range(len(str)):
        if n == x:
            continue
        new_str = new_str + str[n]
    return new_str
