#!/usr/bin/python3
"""
Module contains class Rectangle

Inherits from Base;
Inits superclass' id
Contains private width, height, x, y
Contains public method area
Displays rectangle using #'s
Print [Rectangle] (<id>) <x>/<y> - <width>/<height>
Updates attributes: arg1=id, arg2= width, arg3=height, arg4=x, arg5=y
Returns dictionary representation of attributes
"""


from models.base import Base


class Rectangle(Base):
    """
    Defines class Rectangle; inherits from class Basee
    Inherited Attributes:
       id
    Class Attributes:
       __width          __height
       __x              __y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The value to set the width to.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): is set to height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the X(horizontal position of the rectangle)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the horizontal position of the rectangle.

        Args:
            value (int): the value to set
        """
        if type(value) is not int:
            raise TypeError("x must be an iAOAnteger")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the Y(vertical position of the rectangle)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the vertical position of the rectangle

        Args:
            value (int): the value to set
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def display(self):
        """
        Method to display rectangle in #
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self__x + "#" * self.__width)

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}}/{:d}".format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Method to update the attributes of the rectangle
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height =arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation """
        
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
