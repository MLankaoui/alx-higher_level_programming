#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')

        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        for i in range(self.__y):
            print()  # Print empty lines for vertical indentation
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        return "[REACTANGLE] ({}) {}/{} - {} / {}".format(self.id, self.__x , self.__y, self.__width, self.__height)
            
    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            list_attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    
