#!/usr/bin/python3
"""Python Interpreter"""


class Base:
    """new class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """new initialization"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = Base.__nb_objects
