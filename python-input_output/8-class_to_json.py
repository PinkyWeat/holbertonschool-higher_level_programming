#!/usr/bin/python3
"""Module"""


def class_to_json(obj):
    """returns dict description with smple data structure for JSON obj"""
    return obj.__dict__
