#!/usr/bin/python3
"""
module 4-rectangle
Contains class Rectangle with private attribute width and height,
public area and perimeter methods, and allows printing #'s and repo() & eval()
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
    width (int): width
    height (int): height

    Functions:
    __init__(self, width, height)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    area(self)
    perimeter(self)
    __str__(self)
    __repr__(self)
    """
    def __init__(self, width=0, height=0):
        """ Initailizing Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter to get value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter to get value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculates and return the area of the shape """
        return (self.__width * self.__height)

    def perimeter(self):
        """ calulates the perimeter of the shape """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
    
    def __str__(self):
        """ Prints rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = ""
        for i in range(self.__height):
            row = "#" * self.__width
            pic += row + "\n"
        return pic

    def __repr__(self):
        """ string representation to create new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
