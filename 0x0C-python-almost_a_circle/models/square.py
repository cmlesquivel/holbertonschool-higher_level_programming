#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Rectangle Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Define constructor of object class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method"""
        return '[Square] ({}) {}/{} - {}'.\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Method that return the attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """Method that set the attribute size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributes"""
        attributes = ['id', 'size', 'x', 'y']
        if not len(args) == 0:
            for x in range(len(args)):
                setattr(self, attributes[x], args[x])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
