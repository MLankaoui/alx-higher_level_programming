#!/usr/bin/python3


"""a script in python that defines a function the write some text
into a text file and return the number of characters written"""


def write_file(filename="", text=""):
    """overwrite content from text into filename and return number
    of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        """wite returns the number of characters written"""
        return f.write(text)
