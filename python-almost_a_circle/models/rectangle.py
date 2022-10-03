#!/usr/bin/python3
"""Python Interpreter"""
from models.base import Base


class Rectangle(Base):
    """new class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """new init"""
        self.__width = self.errors(width, "width")
        self.__height = self.errors(height, "height")
        self.__x = self.errors(x, "x")
        self.__y = self.errors(y, "y")
        super().__init__(id)

    def __str__(self):
        """prints"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__width}/{self.__height}"

    @property
    def width(self, width):
        """width of Rectangle"""
        self.__width = width
        return self.__width

    @width.getter
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.errors(width, "width")
        self.__width = width
        return self.__width

    @property
    def height(self, height):
        """height of Rectangle"""
        self.__height = height
        return self.__height

    @height.getter
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.errors(height, "height")
        self.__height = height
        return self.__height

    @property
    def x(self, x):
        """x of Rectangle"""
        self.__x = x
        return self.__x

    @x.getter
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """height setter"""
        self.errors(x, "x")
        self.__x = x
        return self.__x

    @property
    def y(self, y):
        """y of Rectangle"""
        self.__y = y
        return self.__y

    @y.getter
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """height setter"""
        self.errors(y, "y")
        self.__y = y
        return self.__y

    def errors(self, value, name):
        """raises the correct error"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and name in ("width", "height"):
            raise ValueError(f"{name} must be > 0")
        if value < 0 and name in ("x", "y"):
            raise ValueError(f"{name} must be >= 0")
        return value

    def area(self):
        """calcs area of Rectanglee"""
        return self.__height * self.__width

    def display(self):
        """displays the Rectangle using #"""
        for whys in range(self.__y):
            print()
        for n in range(self.__height):
            for ex in range(self.__x):
                print(" ", end="")
            for more in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update arguments"""
        length = len(args)
        if (length > 0):
            self.id = args[0]
            if length > 1:
                self.__width = args[1]
            if length > 2:
                self.__height = args[2]
            if length > 3:
                self.__x = args[3]
            if length > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """returns the dictonary rep"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
         'x': self.x, 'y': self.y}
