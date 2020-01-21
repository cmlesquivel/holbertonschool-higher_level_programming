#!/usr/bin/python3
"""
documentation from the class inherits_from
"""


def inherits_from(obj, a_class):
    """"returns True if the object is an instance of a class that inherited"""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
