#!/usr/bin/python3
"""Python Interpreter"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """new class"""

    def __init__(self, size, x=0, y=0, id=None):
        """new init Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints info of Square"""
        return f"[Square] ({self.id}) " \
            f"{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """New property"""
        return self.width

    @size.getter
    def size(self):
        """sets size"""
        return self.size

    @size.setter
    def size(self, value):
        """Set private size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates Square data"""
        if len(args) >= 1:
            for num, arguments in enumerate(args):
                if num == 0:
                    self.id = arguments
                if num == 1:
                    self.size = arguments
                if num == 2:
                    self.x = arguments
                if num == 3:
                    self.y = arguments
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
