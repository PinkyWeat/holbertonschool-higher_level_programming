#!/usr/bin/python3
"""Module"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Obj to text file, using JSON rep"""
    with open(filename, 'w') as tempFile:
        tempFile.write(json.dumps(my_obj))
