#!/usr/bin/python3
import json


def load_from_json_file(filename):
        """function that writes an Object to a text file,using a JSON repres"""
        with open(filename, 'r') as file:
                my_object = json.load(file)
        return my_object
