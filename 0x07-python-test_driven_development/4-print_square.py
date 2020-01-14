#!/usr/bin/python3

"""
This is a module for the test the functions
add_integer function add
"""


def print_square(size):

    """function that prints a square with the character #
Args:
    size: size
Returns:
    Returns nothing
Raises:
    TypeError: size must be an integer
"""
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size == 0:
        raise ValueError('size must be >= 0')

    if size is None:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    else:
        for x in range(size):
            for i in range(size):
                print('#', end='')
            print()
