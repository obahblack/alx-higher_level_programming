#!/usr/bin/python3
"""
module 2-square
Define class with private attribute and raise error msgs
"""
class Square:
    """
    class Square defination
    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
        __size(int): size of a side of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
