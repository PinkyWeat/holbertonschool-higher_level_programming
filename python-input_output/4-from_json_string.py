#!/usr/bin/python3
"""Module"""
import json


def from_json_string(my_str):
    """returns obj represented by JSON string"""
    return json.loads(my_str)
