#!/usr/bin/python3
"""
Module 2-is_same_class

Contains method is_same_class
returns True if object is exactly an instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Notes:
    use type() to get specific class

    Return:
    True if obj is exactly an instance of specified class
    """
    return type(obj) == a_class
