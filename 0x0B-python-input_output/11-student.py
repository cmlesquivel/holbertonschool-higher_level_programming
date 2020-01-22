#!/usr/bin/python3


class Student:
    """Define class student"""
    def __init__(self, first_name, last_name, age):
        """Method constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation"""
        return self.__dict__
