#!/usr/bin/python3
"""
Module - 10-student.py
Defines a student class
"""


class Student():
    """
    Initializes class
    Defines first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """Initailizes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
