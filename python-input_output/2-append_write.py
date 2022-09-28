#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)"""
    with open(filename, 'a')as tempFile:
        return tempFile.write(text)
