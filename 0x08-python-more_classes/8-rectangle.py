#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """empty class Rectangle that defines a square"""

    number_of_instances = 0
    print_symbol = '#'

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
            type(self).number_of_instances += 1

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

    def area(self):
        """method that returns rectangle area"""
        return self.__height*self.__width

    def perimeter(self):
        """method that returns rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            perimeter = self.__height*2 + self.__width*2
            return perimeter

    def __str__(self):
        """class Rectangle that defines a rectangle"""
        character = ''
        if self.__height == 0 or self.__width == 0:
            return character

        for x in range(self.__height):
            character += str(self.print_symbol)*self.__width
            if x < self.__height-1:
                character += '\n'
        return character

    def __repr__(self):
        """return a string of rectangle to able to recreate a new instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
