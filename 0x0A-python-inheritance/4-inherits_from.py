#!/usr/bin/python3


"""a script that creates a function that returns true if the object 
is an instance of a class that inherited (directly or indirectly) from the specified class 
otherwise False"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherits (directly or indirectly) from the specified class
    otherwise False.
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
