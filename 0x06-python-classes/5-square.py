#!/usr/bin/python3
class Square:
    """empty class Square that defines a square"""
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """method that returns the current square area"""
        return self.__size**2

    @property
    def size(self):
        """method that returns the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """method that define the size of square"""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print('{}'.format('#'), end="")
                print()
