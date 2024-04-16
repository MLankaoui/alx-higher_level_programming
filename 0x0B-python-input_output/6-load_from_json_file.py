#!/usr/bin/python3
"""a script that defines a function that
creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """load a JSON object from a JSON file"""
    with open(filename, 'r') as file:
        the_object = file.read()
        return json.loads(the_object)