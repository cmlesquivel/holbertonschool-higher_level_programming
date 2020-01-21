#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print('{}'.format(line), end='')
