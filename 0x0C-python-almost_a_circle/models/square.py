#!/usr/bin/python3
from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y,id)
        self.size = size;

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

