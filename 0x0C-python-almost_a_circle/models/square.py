#!/usr/bin/python3
from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y,id)
        self.size = size;

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
    
    @property
    def size(self):
        return self.width    
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attritbutes = ["id", "size", "x", "y"]
        if args != None and len(args) != 0:
            for i in range(len(args)):   
                setattr(self, attritbutes[i], args[i])

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
       


