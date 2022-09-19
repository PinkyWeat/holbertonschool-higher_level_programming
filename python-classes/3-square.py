#!/usr/bin/python3
"""Square Class
Empty class Square + attribute size.
"""


class Square:
    """A class
    a square
"""
    def __init__(self, size=0):
        """__init__
        The __init__ method inlitialize the value
        Attributes:
            size (int): the size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area
        calculates area of a square
        """
        area = self.__size * self.__size
        return area
