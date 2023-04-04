#!/usr/bin/python3
"""
Module 3-rectangle
Contains class Rectangle with private attribute width and height,
Public area and perimeter methods, and allows printing #'s
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter returns new value for width """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter return a new value for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height = value

    def area(self):
        """
        Calculates and return area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        calculates and returns the perimeter of thr rectangle
        """
        if width == 0 or height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.__height):
                rectangle += "#" * self.__width + "\n"
                return rectangle.rstrip()
