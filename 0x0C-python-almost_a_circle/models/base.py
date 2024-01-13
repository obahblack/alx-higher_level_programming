#!/usr/bin/python3
"""
Module - contains class Base

Contains private __nb_object
"""


import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string representation of list dict """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json string of all instances into file """
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return instance with attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns list of instances """
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                l.append(cls.create(**instances[i]))
        except:
            pass
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])
    
    @classmethod
    def load_from_file_csv(cls):
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]), "width": int(row[1]), "height": int(row[2]), "x": int(row[3]), "y": int(row[4])}
                    if cls.__name__ == "Square":
                        dic = {"id": int(row[0]), "size": int(row[1]), "x": int(row[2]), "y": int(row[3])}
                        o = cls.create(**dic)
                        objs.append(o)
        return objs