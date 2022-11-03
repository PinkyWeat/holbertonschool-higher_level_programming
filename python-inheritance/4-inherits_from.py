#!/usr/bin/python3
"""Module"""


def inherits_from(obj, a_class):
    """True if obj is instance of a class that inherited
    directly or indirectly from the specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
