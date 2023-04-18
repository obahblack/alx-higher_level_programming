#!/usr/bin/python3
"""
Module contains class Square

Inherits from Rectangle;
Inits superclass' id, width (as size), height (as size), x, y
Contains public attribute size
Prints [Square] (<id>) <x>/<y> - <size>
Updates attributes: arg1=id, arg2=size, arg3=x, arg4=y
Returns dictionary representation of attributes
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines the class Square which inherits from Rectangle
    Inherited Attributes:
    id
    __weight       __height
    __x            __y
    Class Attributes:
       size
    Inherited Methods:
       Base.init(self, id=None)
       Rectangle.init(self, width, height, x=0, y=0, id=None)
       update(self, *args, **kwargs)
       width(self)      width(self, value)
       height(self)     height(self, value)
       x(self)          x(self, value)
       y(self)          y(self, value)
       area(self)       display(self)
    Methods:
       __str__
       __init__(self, size, x=0, y=0, id=None)
       update(self, *args, **kwargs)
       size(self)        size(self, value)
       to_dictionary(self)
    """


    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the value size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Method to update the attributes of the Square instance
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns a dictionary representation of a Square """

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
