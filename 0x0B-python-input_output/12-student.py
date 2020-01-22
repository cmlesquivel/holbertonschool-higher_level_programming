#!/usr/bin/python3


class Student:
    """Define class student"""
    def __init__(self, first_name, last_name, age):
        """Method constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation"""
        my_dict = self.__dict__
        i = 0
        newDict = {}

        if attrs is None:
            return my_dict

        for key, value in my_dict.items():
            for item in attrs:
                if item == key:
                    newDict[key] = value
        return newDict
