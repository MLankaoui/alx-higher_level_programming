#!/usr/bin/python3
"""make Square class"""


class Square:
    """Square class for square"""
    def __init__(self, size=0):
        
        if size >= 0 and size <= 9:
            self.__size = size
        else:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        

