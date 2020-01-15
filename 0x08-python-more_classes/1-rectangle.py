#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """empty class Rectangle that defines a square"""
    def __init__(self, width=0, height=0):

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """method that returns the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """method that define the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """method that returns the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """method that define the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
