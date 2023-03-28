#!/usr/bin/python3
class Square:
    """
    Square class that represents a square
    """
    def __init__(self, size=0):
        """
        Instantiation with optimal size
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size
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
