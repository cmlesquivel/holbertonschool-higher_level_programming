#!/usr/bin/python3
import json


def class_to_json(obj):
    """
    A function takes in a custom object and returns a dictionary
    representation of the object.This dict representation includes
    meta data such as the object's module and class names.
    """

    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    obj_dict.update(obj.__dict__)

    return obj_dict
