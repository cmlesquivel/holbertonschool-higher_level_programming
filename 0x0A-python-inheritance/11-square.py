#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""
documentation from the class BaseGeometry
"""


class Square(Rectangle):
    """"Square class  that inherits Rectangle"""

    def __init__(self, size):
        """" method constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """" define method area, return area of Square """
        return self.__size ** 2

    def __str__(self):
        """"return description of Square """
        return '[Square] {}/{}'.format(self.__size, self.__size)
