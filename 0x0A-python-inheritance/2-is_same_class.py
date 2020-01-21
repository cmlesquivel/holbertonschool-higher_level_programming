#!/usr/bin/python3
"""
documentation from the class is_same_class
"""


def is_same_class(obj, a_class):
    """"returns True if the object is exactly an instance of a_class"""
    return type(obj) is a_class
