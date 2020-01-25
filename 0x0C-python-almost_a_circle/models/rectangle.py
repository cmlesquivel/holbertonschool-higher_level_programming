#!usr/bin/python3
from models.base import Base
from functools import wraps

def _int_required(f):
    @wraps(f)
    def wrapper(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(f.__name__))
        return f(self, value)
    return wrapper

class Rectangle(Base):
    """Define Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Define constructor of object class"""
        super().__init__(id)
        self.width = width
        self.heigth = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    @_int_required
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    @_int_required
    def height(self, value):
        self.__height = value


    @property
    def x(self):
        return self.__x

    @x.setter
    @_int_required
    def x(self, value):
        self.__x = value


    @property
    def y(self):
        return self.__y

    @y.setter
    @_int_required
    def y(self, value):
        self.__y = value
