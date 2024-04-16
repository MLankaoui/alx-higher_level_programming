#!/usr/bin/python3
"""a script that defines a function that returns
the json representation of an object"""
import json


def to_json_string(my_obj):
    """returns the json representation of an object"""
    return json.dumps(my_obj)
