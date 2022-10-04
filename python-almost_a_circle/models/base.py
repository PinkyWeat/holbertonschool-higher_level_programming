#!/usr/bin/python3
"""Python Interpreter"""
import json


class Base:
    """new class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """new initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """formats to JSON for sharing data"""
        if list_dictionaries is None:
            return "[]"
        else:
            jeison = json.dumps(list_dictionaries)
        return jeison
