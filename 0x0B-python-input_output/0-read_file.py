#!/usr/bin/python3


"""a python scripts that defines a function that read content
from a file and prints its content to stdout
"""


def read_file(filename=""):

    """read a file with utf-8 encoding"""

    with open(filename, "r", encoding='utf-8') as file:

        """stocking the content of the file in content
        variable"""

        content = file.read()

    """printing content"""

    print(content)

    """closing the file even though it is closed automatically
    when whe used (with)"""

    file.close()
