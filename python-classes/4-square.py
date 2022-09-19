#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """a Square"""

    def __init__(self, size=0):
        """New Square instance
        size (int): size of new square"""
        self.__size = size

    @property
    def size(self):
        """Get or set size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the Square area"""
        return self.__size ** 2
