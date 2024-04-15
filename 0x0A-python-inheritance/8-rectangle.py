#!/usr/bin/python3


"""Base Geomety class for Geometries"""


class BaseGeometry:
    """a method that raise an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    """a method that checks if the value is an integer and greater than 0"""    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        

"""Rectangle class for drawing a rectangle"""


class Rectangle(BaseGeometry):
    """initializes a new Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        
