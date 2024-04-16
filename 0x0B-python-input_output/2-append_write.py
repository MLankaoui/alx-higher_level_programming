#!/usr/bin/python3


"""a script in python that defines a function the append some text into a text file and return the number of characters written"""


def append_write(filename="", text=""):
    """append content from text into filename and return number of characters written"""
    with open(filename,"a", encoding="utf-8") as f:
        """wite returns the number of characters written"""
        return f.write(text)