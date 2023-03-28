#!/usr/bin/python3
"""
Module 4-square
Defines class Square with private size and public area
Can access and update size
"""

class Square:
    """
     class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0):
        """
        Instantiation with optimal size

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter for size

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size

        Args:
            value: sets size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the Square instance.

        Returns:
            int: The area of the Square instance.
        """
        return (self.__size)**2
