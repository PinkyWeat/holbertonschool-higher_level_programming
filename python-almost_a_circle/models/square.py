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
            self.id = args[0]
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
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
