#!/usr/bin/python3
"""
Module - contains class Base

Contains private __nb_object
"""


class Base():
    """
    Defines class - Base
    Class Attributes:
       __nd_objects
    Methods:
       __init__(self, id= none)
    Static Methods:
       to_json_string(list_dictionaries)   from_json_string(json_string)
    Class Methods:
       save_to_file(cls, list_objs)    save_to_file_cvs(cls, list_objs)
       load_from_file(cls)     load_from_file_csv(cls)
       create(cls, **dictionary)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """"
        Initialize id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
