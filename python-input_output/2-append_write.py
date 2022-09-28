#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)"""
    with open(filename, 'a') as tempFile:
        return tempFile.write(text)
