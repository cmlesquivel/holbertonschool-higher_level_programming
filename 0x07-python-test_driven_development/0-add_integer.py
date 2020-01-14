#!/usr/bin/python3

"""
This is a module for the test the functions
add_integer function add
"""


def add_integer(a, b=98):

    """function that adds 2 integers

Args:
    a(int o float): first number
    b(int o float): second number
Returns:
    Returns the add the two numbers
Raises:
    TypeError: if a or b are not numbers
"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
