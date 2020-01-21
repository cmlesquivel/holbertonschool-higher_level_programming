#!/usr/bin/python3
"""
function that reads a text file
"""


def read_lines(filename="", nb_lines=0):
    """function that reads a text file"""
    number_line = 0
    counter = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            number_line += 1

    if nb_lines <= 0 or nb_lines > number_line:
        nb_lines = number_line

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            counter += 1
            print(line, end='')
            if counter == nb_lines:
                break
