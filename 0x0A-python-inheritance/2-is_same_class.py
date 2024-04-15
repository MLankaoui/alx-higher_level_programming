#!/usr/bin/python3


"""
this script defines a function that return true
if th object is an instance of the given class and
false otherwise
"""


def is_same_class(obj, a_class):

    """return true if obj is an instance of the given class
    false otherwise"""
    return True if type(obj) is a_class else False