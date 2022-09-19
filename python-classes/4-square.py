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
        self.size = size

    def size(self):
        """size
        get the size
        """
        return self.__size

    def size(self, value):
        """size
        sets the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area
        calculates area of a square
        """
        area = self.__size ** 2
        return area
