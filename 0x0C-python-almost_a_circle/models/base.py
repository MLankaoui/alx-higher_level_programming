#!/usr/bin/python3
"""class base to create other instances"""



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
