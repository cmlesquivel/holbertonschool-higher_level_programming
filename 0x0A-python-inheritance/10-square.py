#!/usr/bin/python3
"""
documentation from the class BaseGeometry
"""


class BaseGeometry():
    """"BaseGeometry class emply """

    def area(self):
        """"Public instance method that raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """" method that  set name and value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """"Rectangle class  that inherits BaseGeometry"""

    def __init__(self, width, height):
        """" method constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """" define method area, return area of Rectangle """
        return self.__height * self.__width

    def __str__(self):
        """"return description of Rectangle """
        return '[Rectangle] {}/{}'.format(self.__height, self.__width)


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
