#!/usr/bin/python3
"""Python Interpreter"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """new class"""

    def __init__(self, size, x=0, y=0, id=None):
        """new init Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] {self.x}/{self.y} - {self.__width}"

    @property
    def size(self):
        """New property"""
        return self.width

    @size.setter
    def size(self, value):
        """Set private size attribute"""
        self.__width = value
        self.__height = value
