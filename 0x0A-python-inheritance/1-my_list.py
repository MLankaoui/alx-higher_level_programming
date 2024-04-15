#!/usr/bin/python3


"""script that creates a class that inherits from list"""


class MyList(list):
    """a public method that prints a list in ascending order"""
    def print_sorted(self):
        print(sorted(self))