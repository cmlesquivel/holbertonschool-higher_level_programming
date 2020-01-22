#!/usr/bin/python3
"""
function hat appends a string at the end of the text file
"""


def append_write(filename="", text=""):
    """function hat appends a string at the end of the text file"""

    with open(filename, 'a', encoding='utf-8') as file:
        number_lines = file.write(text)
    return number_lines
