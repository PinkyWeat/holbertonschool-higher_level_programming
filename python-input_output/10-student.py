#!/usr/bin/python3
"""Module"""


from re import L


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """initialize new instance Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary version of students"""
        if isinstance(attrs, str):
            for x in dict.items():
                print(x[0])
        return self.__dict__
