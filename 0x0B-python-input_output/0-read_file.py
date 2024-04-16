#!/usr/bin/python3
"""a python scripts that defines a function that read content
from a file and prints its content to stdout
"""


def read_file(filename=""):
    """read a file with utf-8 encoding and prints its content to stdout"""
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")

