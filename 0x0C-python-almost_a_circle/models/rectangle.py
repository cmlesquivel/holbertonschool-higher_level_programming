#!usr/bin/python3
"""Rectangle module"""
from models.base import Base


def int_required_under_equals_zero(f):
    """Function that check the value is int and  is not under o equal 0"""
    def wrapper(self, value):
        """Define wrapper function"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(f.__name__))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(f.__name__))
        return f(self, value)
    return wrapper


def int_required_under_zero(f):
    """Function that check the value is int and  is not under 0"""
    def wrapper(self, value):
        """Define wrapper function"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(f.__name__))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(f.__name__))
        return f(self, value)
    return wrapper


class Rectangle(Base):
    """Define Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Define constructor of object class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Method that return the attribute width """
        return self.__width

    @width.setter
    @int_required_under_equals_zero
    def width(self, value):
        """Method that set the attribute width"""
        self.__width = value

    @property
    def height(self):
        """Method that return the attribute height"""
        return self.__height

    @height.setter
    @int_required_under_equals_zero
    def height(self, value):
        """Method that set the attribute height"""
        self.__height = value

    @property
    def x(self):
        """Method that return the attribute x"""
        return self.__x

    @x.setter
    @int_required_under_zero
    def x(self, value):
        """Method that set the attribute x"""
        self.__x = value

    @property
    def y(self):
        """Method that return the attribute y"""
        return self.__y

    @y.setter
    @int_required_under_zero
    def y(self, value):
        """Method that set the attribute y"""
        self.__y = value

    def area(self):
        """Method that returns the area value of the Rectangle"""
        area = self.__width * self.__height
        return area

    def display(self):
        """Method that prints the Rectangle with the character #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(end=' ')
            for x in range(self.__width):
                print ('#', end='')
            print()

    def __str__(self):
        """overriding the __str__ method"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update the attributes"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if not len(args) == 0:
            for x in range(len(args)):
                setattr(self, attributes[x], args[x])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        with_ = self.__width
        height_ = self.__height
        id_ = self.id
        y_ = self.__y
        x_ = self.__x

        return {'x': x_, 'y': y_, 'id': id_, 'height': height_, 'width': with_}
