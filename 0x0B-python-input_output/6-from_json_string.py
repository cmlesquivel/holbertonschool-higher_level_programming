#!/usr/bin/python3
import json


def from_json_string(my_str):
    """function that returns an object Python represented by a JSON """
    return json.loads(my_str)
