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
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        self.name = name
        self.value = value
