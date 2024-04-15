#!/usr/bin/python3


"""this script defines a function that returns true
if the object is an instance of the given class, or 
if the object is an instance of a class that inherited from
otherwise False."""


def is_kind_of_class(obj, a_class):
    """Returns True if
    the object is an instance of the given class, or
    a class that inherits from another one otherwise False."""
    
    if isinstance(obj, a_class):
        return True
    else:
        return False
