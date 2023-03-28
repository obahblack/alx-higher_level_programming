#!/usr/bin/python3
"""
Module 3-square
Defines class square with private attribute size and public attribute area
"""

class Square:
    """
    class Square that represents a square

    Args:
        size (int): size of the Square instance, defaults to 0.

    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Attributes:
            size (int): size of the Square instance, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """
        Computes the area of the Square instance.

        Returns:
            int: The area of the Square instance.
        """
        return (self.__size)**2
