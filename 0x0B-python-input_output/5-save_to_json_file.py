#!/usr/bin/python3
"""a script that defines a function that writes an
Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """save the JSON representation"""
    with open(filename, "w", encoding="utf-8") as file:
        string_obj = json.dumps(my_obj)
        file.write(string_obj)
