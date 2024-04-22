#!/usr/bin/python3
"""class base to create other instances"""
import json


class Base:
    """private class attribute"""
    __nb_object = 0

    """a class constructor that has two parameters"""
    def __init__(self, id=None):
        """if id is not none we assign the true value
        else if it is not none we increment the nb_object and assign
        it to the id
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        string = cls.to_json_string(list_dicts)

        with open(filename, "w") as file:
            file.write(string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"

        else:
            return json.loads(json_string)
