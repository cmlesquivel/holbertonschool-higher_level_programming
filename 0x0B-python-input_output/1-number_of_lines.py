#!/usr/bin/python3
"""
function that reads a text file
"""


def number_of_lines(filename=""):
    """function that reads a text file"""
    number_line = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            number_line += 1
        return number_line
