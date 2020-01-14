#!/usr/bin/python3

"""
This is a module for the test the functions
add_integer function add
"""


def say_my_name(first_name, last_name=""):

    """function that prints My name is <first name> <last name>
Args:
    first_name: first_name
    last_name: last_name
Returns:
    Returns nothing
Raises:
    TypeError: first_name must be a string
"""
    if first_name is None:
        raise TypeError('first_name must be a string')

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
