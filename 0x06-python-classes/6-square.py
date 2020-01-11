#!/usr/bin/python3
class Square:
    """empty class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

        if type(position) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

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
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print('{}'.format(' '), end="")
            for x in range(self.__size):
                print('{}'.format('#'), end='')
            print()

    @property
    def position(self):
        """method that returns the atribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """method that define the atribute position"""

        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value
