#!/usr/bin/python3
class Square:
    """empty class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
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
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print('{}'.format(' '), end='')
                for x in range(self.__size):
                    print('{}'.format('#'), end="")
                print()

    @property
    def position(self):
        """method that returns the atribute position"""
        return self.__size

    @position.setter
    def position(self, value):
        """method that define the atribute position"""

        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
