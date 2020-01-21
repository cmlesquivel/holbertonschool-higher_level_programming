#!/usr/bin/python3
"""
function that reads a text file
"""


def write_file(filename="", text=""):
    """function that reads a text file"""

    with open(filename, 'w', encoding='utf-8') as file:
        number_lines = file.write(text)
    return number_lines
