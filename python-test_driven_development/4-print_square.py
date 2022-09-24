#!/usr/bin/python3
"""function prints a square with #"""


def print_square(size):
    """border cases first"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        for cols in range(size):
            print("#", end='' if cols != size - 1 else '\n')
