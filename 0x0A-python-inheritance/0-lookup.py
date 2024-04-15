#!/usr/bin/python3


"""
this script defines a function that
returns a list of attributes of an instance
"""
def lookup(obj):
    """
    Returns a list of attributes of an instance.
    """
    return dir(obj)
