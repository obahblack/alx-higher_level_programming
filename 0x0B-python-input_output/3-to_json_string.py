#!/usr/bin/python3
"""
A function that returns the JSON representation
of an object(string)
"""


import json

def to_json_string(my_obj):
    """Return the JSON representation of an object"""
    return json.dumps(my_obj)
